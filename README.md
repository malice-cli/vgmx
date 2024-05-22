# vgmx
CLI (Command Line) tool to parse and read VGM/VGZ files

## Installation
Refer to `install.bat` for windows and `install.sh` for linux

## Usage
```
vgmx.exe ./example.vgz -o
```
```json
{
  "IntroDuration": 41.86,
  "LoopDuration": 41.34,
  "Loop": true,
  "Gd3Tag": {
    "Title": {
      "en": "Data Menu",
      "jp": ""
    },
    "Game": {
      "en": "F1 Circus MD",
      "jp": "\uff26\uff11\u30b5\u30fc\u30ab\u30b9\uff2d\uff24"
    },
    "System": {
      "en": "Sega Mega Drive / Genesis",
      "jp": "\u30bb\u30ac\u30e1\u30ac\u30c9\u30e9\u30a4\u30d6"
    },
    "Composer": {
      "en": "Hiroshi Ogawa",
      "jp": "\u5c0f\u5ddd \u535a\u53f8"
    },
    "ReleaseDate": "1991/12/20",
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
  "Samples": 1845959
}
```
