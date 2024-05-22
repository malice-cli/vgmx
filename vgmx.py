import sys
import struct
import gzip
import json
import os
from argparse import ArgumentParser

def read_vgm(file_path):
    with open(file_path, 'rb') as file:
        buf = file.read()
    if buf[0] == 0x1f and buf[1] == 0x8b:
        with gzip.open(file_path, 'rb') as gz_file:
            buf = gz_file.read()
    return buf

def parse_vgm(file_path):
    buf = read_vgm(file_path)
    if buf[0:4] != b'Vgm ':
        raise ValueError("The file provided has an invalid header")
    
    loop_offset = struct.unpack_from('<I', buf, 0x1C)[0]
    total_samples = struct.unpack_from('<I', buf, 0x18)[0]
    loop_samples = struct.unpack_from('<I', buf, 0x20)[0]
    
    vgm_version = struct.unpack_from('<I', buf, 0x08)[0]
    vgm_data_offset = struct.unpack_from('<I', buf, 0x34)[0] + 0x34 if struct.unpack_from('<I', buf, 0x34)[0] != 0 else 0x40
    rate = struct.unpack_from('<I', buf, 0x24)[0]
    
    intro_duration = total_samples / 44100
    loop_duration = loop_samples / 44100 if loop_offset > 0 and loop_samples > 0 else 0
    
    gd3_offset = struct.unpack_from('<I', buf, 0x14)[0] + 0x14
    gd3_tag = extract_gd3(buf, gd3_offset)
    # HELL!!!
    chips = [
        'None' if struct.unpack_from('<I', buf, 0x2C)[0] == 0 else {'Name': "YM2612", 'Type': 'FM'},
        'None' if struct.unpack_from('<I', buf, 0x30)[0] == 0 else {'Name': "YM2151", 'Type': 'FM'},
        'None' if struct.unpack_from('<I', buf, 0x38)[0] == 0 else {'Name': 'S-PCM', 'Type': 'PCM'},
        'None' if struct.unpack_from('<I', buf, 0x40)[0] == 0 else {'Name': "RF5C68", 'Type': 'PCM'},
        'None' if struct.unpack_from('<I', buf, 0x44)[0] == 0 else {'Name': "YM2203", 'Type': "FM"},
        'None' if struct.unpack_from('<I', buf, 0x48)[0] == 0 else {'Name': "YM2608", 'Type': 'FM'},
        'None' if struct.unpack_from('<I', buf, 0x4C)[0] == 0 else {'Name': "YM2610", 'Type': 'FM'},
        'None' if struct.unpack_from('<I', buf, 0x50)[0] == 0 else {'Name': "YM3812", 'Type': 'FM'},
        'None' if struct.unpack_from('<I', buf, 0x54)[0] == 0 else {'Name': "YM3526", 'Type': 'FM/PCM'},
        'None' if struct.unpack_from('<I', buf, 0x58)[0] == 0 else {'Name': "Y8950", 'Type': 'ADPCM'},
        'None' if struct.unpack_from('<I', buf, 0x5C)[0] == 0 else {'Name': "YMF262", 'Type': 'FM'},
        'None' if struct.unpack_from('<I', buf, 0x60)[0] == 0 else {'Name': "YMF278B", 'Type': 'FM'},
        'None' if struct.unpack_from('<I', buf, 0x64)[0] == 0 else {'Name': "YMF271", 'Type': 'FM'},
        'None' if struct.unpack_from('<I', buf, 0x68)[0] == 0 else {'Name': "YMZ280B", 'Type': 'PCM/ADPCM'},
        'None' if struct.unpack_from('<I', buf, 0x6C)[0] == 0 else {'Name': "RF5C164", 'Type': 'PCM'},
        'None' if struct.unpack_from('<I', buf, 0x70)[0] == 0 else {'Name': "PWM", 'Type': 'PWM'},
        'None' if struct.unpack_from('<I', buf, 0x74)[0] == 0 else {'Name': 'AY8910', 'Type': 'PSG'},
    ]
    
    chips = [chip for chip in chips if chip != 'None']
    
    return {
        'IntroDuration': round(intro_duration, 2),
        'LoopDuration': round(loop_duration, 2),
        'Loop': loop_offset != 0,
        'Gd3Tag': gd3_tag,
        'Chips': chips,
        'Version': vgm_version,
        'DataOffset': vgm_data_offset,
        'Rate': rate,
        'Samples': total_samples
    }

def extract_gd3(buffer, offset):
    magic = buffer[offset:offset + 4].decode('utf-8')
    if magic != 'Gd3 ':
        return {}
    
    gd3_data = {
        'Title': {},
        'Game': {},
        'System': {},
        'Composer': {}
    }
    current_offset = offset + 12
    
    for key in ['Title', 'Game', 'System', 'Composer']:
        gd3_data[key]['en'] = read_string(buffer, current_offset)
        current_offset += len(gd3_data[key]['en']) * 2 + 2
        gd3_data[key]['jp'] = read_string(buffer, current_offset)
        current_offset += len(gd3_data[key]['jp']) * 2 + 2
    
    gd3_data['ReleaseDate'] = read_string(buffer, current_offset)
    current_offset += len(gd3_data['ReleaseDate']) * 2 + 2
    
    gd3_data['ConvAuthor'] = read_string(buffer, current_offset)
    current_offset += len(gd3_data['ConvAuthor']) * 2 + 2
    
    gd3_data['Notes'] = read_string(buffer, current_offset)
    
    return gd3_data

def read_string(buffer, offset):
    result = ''
    while True:
        char = struct.unpack_from('<H', buffer, offset)[0]
        if char == 0:
            break
        result += chr(char)
        offset += 2
    return result

def main():
    parser = ArgumentParser(description="VGMX")
    parser.add_argument("input", help="Path to the VGM/VGZ file")
    parser.add_argument("-o", "--output", action="store_true", help="Output to a JSON file")
    
    args = parser.parse_args()
    input_file_path = args.input
    output_flag = args.output

    try:
        data = parse_vgm(input_file_path)
        
        if output_flag:
            output_file_path = os.path.splitext(input_file_path)[0] + '.json'
            with open(output_file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)  # Ensure ASCII characters are not escaped
            print(f'Output written to {output_file_path}')
        else:
            print(json.dumps(data, indent=2, ensure_ascii=False))
    except Exception as error:
        print(f'Error: {error}')
        sys.exit(1)

if __name__ == '__main__':
    main()
