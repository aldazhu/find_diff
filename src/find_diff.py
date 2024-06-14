import cv2 as cv
import numpy as np


# BOX_TOP = [16, 322, 1222, 1128] # x1, y1, x2, y2
# BOX_BOTTOM = [16, 1163, 1222, 1969] # x1, y1, x2, y2
SUB_IMAGE_WIDTH = 1222 - 16
SUB_IMAGE_HEIGHT = 1128 - 322
IMAGE_1_START_Y = 323
IMAGE_2_START_Y = 1163
START_X = 16
END_X = 1222

BOX_TOP = [START_X, IMAGE_1_START_Y, END_X, IMAGE_1_START_Y + SUB_IMAGE_HEIGHT] # x1, y1, x2, y2
BOX_BOTTOM = [START_X, IMAGE_2_START_Y, END_X, IMAGE_2_START_Y + SUB_IMAGE_HEIGHT] # x1, y1, x2, y2

IMAGE_WIDTH = 1240
IMAGE_HEIGHT = 2772

MIN_RECT_AREA = 10*10



def calculate_diff(img1, img2):
    """_summary_

    Args:
        img1 (_type_): _description_
        img2 (_type_): _description_
    """
    diff = cv.absdiff(img1, img2)
    cv.namedWindow("diff", cv.WINDOW_KEEPRATIO)
    cv.imshow("diff", diff)
    return diff

def blob_detection(img):
    """输入一张CV_8UC3格式的图片，这个图片是两个图片的差值，然后进行blob检测，返回blob的外接矩形

    Args:
        img (_type_): _description_
    """
    pass
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, binary = cv.threshold(gray, 20, 255, cv.THRESH_BINARY)
    # 闭运算
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
    binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
    # 开运算
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (17, 17))

    cv.namedWindow("binary", cv.WINDOW_KEEPRATIO)
    cv.imshow("binary", binary)
    contours, _ = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    rects = []
    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)
        if w*h < MIN_RECT_AREA:
            continue
        rects.append([x, y, x+w, y+h])
    return rects

def split_image(img, box1, box2):
    """输入一张CV_8UC3格式的图片，将图片分割成两张图片

    Args:
        img (_type_): _description_
        box1 (_type_): x1, y1, x2, y2
        box2 (_type_): x1, y1, x2, y2
    """
    pass
    image1 = img[box1[1]:box1[3], box1[0]:box1[2]]
    image2 = img[box2[1]:box2[3], box2[0]:box2[2]]
    return image1, image2

def draw_rects(img, rects):
    """输入一张CV_8UC3格式的图片，和一组矩形，将矩形画在图片上

    Args:
        img (_type_): _description_
        rects (_type_): _description_
    """
    pass
    for rect in rects:
        x1, y1, x2, y2 = rect
        cv.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    return img


def find_diff(image):
    h, w, _ = image.shape
    image1, image2 = split_image(image, BOX_TOP, BOX_BOTTOM)
    diff = calculate_diff(image1, image2)
    rects = blob_detection(diff)
    view = draw_rects(image1, rects)

    cv.namedWindow("view", cv.WINDOW_KEEPRATIO)
    cv.imshow("view", view)
    
    

def demo():
    pass
    image_path = r"G:\vsproj\sample_code\find_diff\images\2.jpg"
    image = cv.imread(image_path)
    find_diff(image)

def read_image(image_path):
    """路径可以包含中文

    Args:
        image_path (_type_): _description_
    """
    pass
    image = cv.imdecode(np.fromfile(image_path, dtype=np.uint8), -1)
    return image

def run_loop():
    pass
    image_paths = {}
    while True:
        image_path = input("Please input the image path:")
        image = read_image(image_path)
        if image is None:
            print("Invalid image path")
            continue
        find_diff(image)
        key = cv.waitKey(0)
        cv.destroyAllWindows()
        if key == ord('q'):
            break

if __name__ == "__main__":
    # demo()
    run_loop()


