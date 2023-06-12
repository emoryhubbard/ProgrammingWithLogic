# This line imports or includes the library we will need
from PIL import Image

def main():
    foreground_name = input("Enter green screen image file name (in the same folder as this program, eg. spaceshuttle.jpg): ")
    background_name = input("Enter background image file name (eg. earth.jpg): ")
    save_name = input("Enter new image file name: ")

    foreground_image = Image.open(foreground_name)
    background_image = Image.open(background_name)
    
    # This line modifies the foreground image by replacing green pixels with background pixels
    replace_background(foreground_image, background_image)
    foreground_image.show()
    foreground_image.save(save_name)

    return

def replace_background(foreground_image, background_image):
    foreground_pixels = foreground_image.load()
    background_pixels = background_image.load()
    width, height = foreground_image.size
    green = 44, 207, 64 # tested top left green screen pixel color to see it's 44, 207, 64 in spaceshuttle.jpg
    
    for row in range(height):
        for x in range(width):
            if foreground_pixels[x, row] == green or is_close(foreground_pixels[x, row]):
                foreground_pixels[x, row] = background_pixels [x, row]

    return

def is_close(pixel): # there are too many "close" greens caused by lossy jpeg compression
    r, g, b = pixel # color components of pixel to be tested
    rg, gg, bg = 44, 207, 64 # same green screen pixel color components from earlier
    red_precision = 2.5 # used trial and error to optimize these values. They work for multiple images.
    green_precision = .6
    blue_precision = 2.5
    rg = round(rg * red_precision)
    gg = round(gg * green_precision)
    bg = round(bg * blue_precision)
    
    if r <= rg and g >= gg and b <= bg:
        is_close = True
    else:
        is_close = False

    return is_close

def test():
    image_original = Image.open("spaceshuttle.jpg")
    pixels_original = image_original.load()
    width, height = image_original.size
    weird_color = (255, 0, 255)

    line_y = int(height / 2)
    line_x = 0

    while line_x <= width - 1:
        pixels_original[line_x, line_y] = weird_color
        line_x += 1
    
    image_original.show()
    image_original.save("purple_test.jpg")

    screen_green = pixels_original[0, 0]
    print(screen_green)

if __name__ == "__main__":
    main()
