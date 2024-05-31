from rembg import remove
from PIL import Image
import sys

def byebgr (input_path, outputpath):
    original_image = Image.open(input_path)
    no_bg_image = remove(original_image)
    no_bg_image = no_bg_image.convert('RGB')
    no_bg_image.save(outputpath)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print ("Usage: byebgr <input_path> <output_path>")
        sys.exit(1)
    byebgr(sys.argv[1], sys.argv[2])

# pyinstaller --onefile --noconsole --icon .\scr\byebgr.ico .\src\byebgr.py