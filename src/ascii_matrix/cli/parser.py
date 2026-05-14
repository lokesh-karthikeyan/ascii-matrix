import argparse

def parse_args(args=None):
    parser = argparse.ArgumentParser(description="ASCII Matrix CLI")

    parser.add_argument("-i", "--image", type=str, required=True, help="Name of the image")
    parser.add_argument("-c", "--color", type=str, default="white", choices=["red", "green", "blue", "white"], help="Name of the color (Red, Green, Blue, White (Default))")

    return parser.parse_args(args)
