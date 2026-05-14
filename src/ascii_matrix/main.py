from ascii_matrix.cli.parser import parse_args
from ascii_matrix.fs.validate_path import validate_image_path
from ascii_matrix.ascii_image.image import Image
from ascii_matrix.ascii_image.to_ascii import to_ascii
from ascii_matrix.effects.matrix import matrix
from ascii_matrix.cli.render import render

def main():
    args = parse_args()
    image_path = validate_image_path(args.image)
    image = Image(image_path).image
    ascii_art = to_ascii(image)
    frames = matrix(ascii_art, args.color)
    render(frames)

if __name__ == "__main__":
    main()
