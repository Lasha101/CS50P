import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments!")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments!")
    elif not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid file extension for input image!")
    elif not sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid file extension for shirt image!")
    elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
        sys.exit("The file extensions are the same.")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        make_image(input_file, output_file)

def make_image(input_file, output_file):
    try:
        input_image = Image.open(input_file)
        shirt = Image.open("shirt.png")
        size = shirt.size
        input_image = ImageOps.fit(input_image, size)
        input_image.paste(shirt, shirt)


        input_image.save(output_file)  # Save the resulting image
        print("Image created successfully!")

    except (FileNotFoundError, PermissionError, ValueError, UnicodeDecodeError) as e:
        sys.exit("Error: " + str(e))

if __name__ == "__main__":
    main()


