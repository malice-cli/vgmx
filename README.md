# vgmx
CLI (Command Line) tool to parse and read VGM/VGZ files

## Installation
Refer to `install.bat` for windows and `install.sh` for linux

## Usage
```
vgmx.exe ./example.vgz
```
```json
{
  "IntroDuration": 82.4,
  "LoopDuration": 81.92,
  "Loop": true,
  "Gd3Tag": {
    "Title": {
      "en": "Caveman Rock",
      "jp": ""
    },
    "Game": {
      "en": "James Bond 007: The Duel",
      "jp": "００７・死闘"
    },
    "System": {
      "en": "Sega Mega Drive / Genesis",
      "jp": "セガメガドライブ"
    },
    "Composer": {
      "en": "Matt Furniss",
      "jp": ""
    },
    "ReleaseDate": "1992/11",
    "ConvAuthor": "-DJSW-",
    "Notes": ""
  },
  "Chips": [
    {
      "Name": "YM2612",
      "Type": "FM"
    },
    {
      "Name": "RF5C68",
      "Type": "PCM"
    },
    {
      "Name": "YM2203",
      "Type": "FM"
    },
    {
      "Name": "YM2608",
      "Type": "FM"
    },
    {
      "Name": "YM2610",
      "Type": "FM"
    },
    {
      "Name": "YM3812",
      "Type": "FM"
    },
    {
      "Name": "YM3526",
      "Type": "FM/PCM"
    },
    {
      "Name": "Y8950",
      "Type": "ADPCM"
    },
    {
      "Name": "YMF262",
      "Type": "FM"
    },
    {
      "Name": "YMF278B",
      "Type": "FM"
    },
    {
      "Name": "YMF271",
      "Type": "FM"
    },
    {
      "Name": "YMZ280B",
      "Type": "PCM/ADPCM"
    },
    {
      "Name": "RF5C164",
      "Type": "PCM"
    },
    {
      "Name": "PWM",
      "Type": "PWM"
    },
    {
      "Name": "AY8910",
      "Type": "PSG"
    }
  ],
  "Version": 336,
  "DataOffset": 64,
  "Rate": 60,
  "Samples": 3633771
}
```
