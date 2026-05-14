# Ascii Matrix

Converts images into a Matrix-style digital rain animation in the terminal. Rendered as falling ASCII characters over your image's silhouette with customizable color.

## Requirements

- Python 3.13+

## Setup

    curl -LsSf https://astral.sh/uv/install.sh | sh

    uv sync
    uv run ascii-matrix --image path/to/image.jpg --color green

## Usage

    ascii-matrix -i <path-to-image> [-c <color>]

    Options:
    - -i, --image — Path to the image file (required)
    - -c, --color — Color of the matrix effect: red, green, blue, white (default: white)

## Demo

https://github.com/user-attachments/assets/dbd8b1f1-0c27-4755-b2d9-4d0b58cf350e

