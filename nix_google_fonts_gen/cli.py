import logging

from argparse import ArgumentParser
from pathlib import Path

from nix_google_fonts_gen.overlay import create_overlay


def parse_arguments():
    parser = ArgumentParser(
        description="Generate Nix package overlay from Google Fonts repository."
    )
    parser.add_argument(
        "repository", type=Path, help="Path to local Google Fonts Git repository."
    )
    parser.add_argument("overlay", type=Path, help="Path to overlay directory.")
    return parser.parse_args()


def main():
    logging.basicConfig(level=logging.INFO)
    args = parse_arguments()
    create_overlay(args.repository, args.overlay)
