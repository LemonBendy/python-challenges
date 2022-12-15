from numpy import complex, array
from PIL import Image
import colorsys
width_of_the_set = 2100


def color(i):
    color_of_the_set = 255 * array(colorsys.hsv_to_rgb(i / 245.0, 0.9, 0.4))
    return tuple(color_of_the_set.astype(int))


def mandelbrot_set(x, y):
    c1 = complex(x, y)
    c2 = 0
    for n in range(1, 2000):
        if abs(c2) > 2:
            return color(n)
        c2 = c2 * c2 + c1
    return (0, 0, 0)


image = Image.new('RGB', (width_of_the_set, int(width_of_the_set / 2)))
pixels = image.load()
for x in range(image.size[0]):
    print("%.2f %%" % (x / width_of_the_set * 100.0))
    for y in range(image.size[1]):
        pixels[x, y] = mandelbrot_set((x - (0.75 * width_of_the_set)) / (width_of_the_set / 4),
                                      (y - (width_of_the_set / 4)) / (width_of_the_set / 4))
image.show()
