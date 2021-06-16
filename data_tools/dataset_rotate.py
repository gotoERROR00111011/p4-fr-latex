import cv2
import glob

from tqdm import tqdm


"""
def get_aspect_ratio_txt():
    image_paths = glob.glob('./train_dataset/images/*.jpg')

    vertical = []

    for image_path in tqdm(image_paths):
        img = cv2.imread(image_path)

        height, width, _ = img.shape
        if height > width:
            vertical.append(image_path)

    with open('vertical.txt', 'w') as f:
        for v in vertical:
            f.write(f'{v},left\n')
"""


def rotate():
    with open('./dataset_rotate.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break

            image_path, direction = line.split(',')

            image_path = image_path.replace('./', '/opt/ml/input/data/')
            image = cv2.imread(image_path)

            if direction[0] == 'r':
                image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
            elif direction[0] == 'l':
                image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

            cv2.imwrite(image_path, image)


#rotate()
