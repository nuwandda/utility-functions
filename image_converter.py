from PIL import Image
import argparse
import threading
import extensions


def convert_image(img, ext, out_name):
    if ext == 'png':
        img.save(out_name + '.png', 'png')
    elif ext == 'jpg':
        img.save(out_name + '.jpg', 'jpeg')
    elif ext == 'webp':
        img.save(out_name + '.webp', 'webp')

if __name__ == '__main__':
    print('Convertion started.')
    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument('-i', '--Input', help='Image to be converted', type=str, required=True)
    parser.add_argument('-t', '--Type', help='Desired image type', type=str, required=True)
    
    # Read arguments from command line
    args = parser.parse_args()
    file_extension = args.Type.lower()
    out_name = args.Input
    img = Image.open(args.Input).convert('RGB')

    # Create filename for output file
    out_name = out_name.split('.')[0]

    loading_process = threading.Thread(target=convert_image, args=(img, file_extension, out_name, ))
    loading_process.start()

    extensions.loadingAnimation(loading_process)
    loading_process.join()
    
    print('Saved in ' + out_name)

