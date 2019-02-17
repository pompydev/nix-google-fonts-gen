# nix-google-fonts-gen 🖋

Tool for generating Nix package overlays from Google Fonts. Generated Nix
overlays will contain individual derivations for all the fonts in Google Fonts
project.

## Usage

```
usage: nix-google-fonts-gen [-h] repository overlay

Generate Nix package overlay from Google Fonts repository.

positional arguments:
  repository  Path to local Google Fonts Git repository.
  overlay     Path to overlay directory.

optional arguments:
  -h, --help  show this help message and exit
```

## Acknowledgements

This project makes use of font protocol buffer definitions from the
[gftools](https://github.com/googlefonts/gftools) repository.
