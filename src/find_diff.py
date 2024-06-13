import cv2 as cv


BOX_TOP = [16, 322, 1222, 1128] # x1, y1, x2, y2
BOX_BOTTOM = [16, 1163, 1222, 1969] # x1, y1, x2, y2
SUB_IMAGE_WIDTH = 1222 - 16
SUB_IMAGE_HEIGHT = 1128 - 322

IMAGE_WIDTH = 1240
IMAGE_HEIGHT = 2772



def calculate_diff(img1, img2):
    """_summary_

    Args:
        img1 (_type_): _description_
        img2 (_type_): _description_
    """
    diff = cv.absdiff(img1, img2)
    cv.imshow("diff", diff)
    return diff

def blob_detection(img):
    """输入一张CV_8UC3格式的图片，这个图片是两个图片的差值，然后进行blob检测，返回blob的外接矩形

    Args:
        img (_type_): _description_
    """
    pass
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    rects = []
    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)
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
    cv.imshow("view", view)
    cv.waitKey(0)
    

def main():
    pass
    image_path = r"G:\vsproj\sample_code\find_diff\images\find_diff.jpg"
    image = cv.imread(image_path)
    find_diff(image)
    



if __name__ == "__main__":
    main()


