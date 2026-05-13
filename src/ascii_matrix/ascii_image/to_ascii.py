CHARSET = "マミムメモガギグゲゴ108965QWERTYUIOPASDFGHJKLZXCVBnmwqpdbkloivcxz+=-:. "
from PIL import Image as PILImage

def to_ascii(pil_image: PILImage.Image) -> str:
    grayscale_img = pil_image.convert('L')
    pixels        = list(grayscale_img.get_flattened_data())
    width, _      = grayscale_img.size

    ascii_chars = []
    charset_len = len(CHARSET)

    for index, pixel in enumerate(pixels):
        charset_index = int((pixel / 255.0) * (charset_len - 1))
        ascii_chars.append(CHARSET[charset_index])

        if (index + 1) % width == 0:
            ascii_chars.append("\n")

    return "".join(ascii_chars)
