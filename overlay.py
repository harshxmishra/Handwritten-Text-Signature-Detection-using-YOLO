import os
import random

import cv2
import numpy as np
import matplotlib.pyplot as plt


def removeBG(root, filepath, iter):

    img = os.path.join(root, filepath)
    src = cv2.imread(img, 1)
    tmp1, tmp2, tmp3 = cv2.split(src)
    (thresh, alpha1) = cv2.threshold(tmp1, 200, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    (thresh, alpha2) = cv2.threshold(tmp2, 200, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    (thresh, alpha3) = cv2.threshold(tmp3, 120, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    rgba = [alpha1, alpha2, alpha3]
    dst = cv2.merge(rgba, 4)


    kernel = np.ones((2, 2), np.uint8)
    dst = cv2.erode(dst, kernel, iterations=iter)

    return dst

def copyToNew(newImg, img, xCoord, yCoord):

    width, height = img.shape[0], img.shape[1]
    pos_y, pos_x = yCoord, xCoord

    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i, j].any() == 0:
                newImg[pos_y+i, pos_x+j] = img[i, j]

    return newImg


def saveImg(filename, img):
    cv2.imwrite(filename, img)


def main():

    root = os.getcwd()
    index_doc = ['1.jpg', '2.png', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.png', '8.png', '9.png', '10.jpg', '11.jpg',
             '12.jpg', '13.jpg', '14.png', '15.jpeg', '16.jpg', '17.png', '18.png', '19.jpg', '20.png', '21.jpg',
             '22.jpg', '23.png', '24.png', '25.png']
    images_doc = {'1.jpg': [10, 4], '2.png': [10, 4], '3.jpg': [10, 4], '4.jpg': [4, 4], '5.jpg': [4, 17], '6.jpg': [4, 10],
              '7.png': [4, 9], '8.png': [3, 3], '9.png': [4, 3], '10.jpg': [4, 6], '11.jpg': [5, 4], '12.jpg': [4, 3],
              '13.jpg': [4, 3], '14.png': [2, 4], '15.jpeg': [2, 2], '16.jpg': [3, 3], '17.png': [2, 6],
              '18.png': [3, 6], '19.jpg': [4, 4], '20.png': [6, 4], '21.jpg': [3, 3], '22.jpg': [1, 5],
              '23.png': [4, 4], '24.png': [4, 2], '25.png': [4, 2]}
    index_sign = ['1.jpg', '2.png', '3.png', '4.jpg']
    images_sign = {'1.jpg': [5, 10], '2.png': [3, 4], '3.png': [5, 4], '4.jpg': [5, 4]}

    # for i in images:
    #     images[i][0] += 1

    for i in images_doc:
        images_doc[i][0] = 20

    for i in range(len(index_doc)):
        print(i)

    # try:
        filename = index_doc[i]

        # noBg = removeBG("C:/Users/ADITYA/Desktop/Handwritten Texts/combined", filename)
        # noBg = cv2.imread("C:/Users/ADITYA/Desktop/Handwritten Texts/combined/"+ filename)

        noBg = removeBG("C:/Users/ADITYA/Desktop/Handwritten Texts/unruled/", filename, images_doc[index_doc[i]][1])
        newImg = cv2.imread("C:/Users/ADITYA/Desktop/Handwritten Texts/canvas/istockphoto-1295201916-612x612.jpg")
        noBg = zoom(noBg)
        coord_x = random.randrange(50)
        coord_y = random.randrange(80)
        newImg = copyToNew(newImg, noBg, coord_x, coord_y)

        signatures = []
        plt.imshow(newImg)
        plt.show()
        for j in range(random.randrange(1,5)):
            sign_ind = random.choice(index_sign)
            sign = removeBG("C:/Users/ADITYA/Desktop/Handwritten Texts/signatures/", sign_ind, images_sign[sign_ind][1])
            signatures.append([sign, 150])


        for j in signatures:
            coord_x = random.randrange(100)
            coord_y = random.randrange(100)
            j[0] = zoom(j[0], j[1])
            newImg = copyToNew(newImg, j[0], coord_x, coord_y )


    # except:
        print('i=', i)
        i -= 1

    saveImg(root + '/finals/' + str(images_doc[index_doc[i]][0]) + '_' + filename, newImg)
    images_doc[index_doc[i]][0] += 1
    newImg = cv2.cvtColor(newImg, cv2.COLOR_BGR2RGB)
    plt.imshow(newImg)
    plt.show()

    # newImg = cv2.imread("C:/Users/ADITYA/Desktop/Handwritten Texts/canvas/istockphoto-174990438-170667a.jpg")
    # plt.imshow(newImg)
    # plt.show()
    print(images_doc)
def zoom(img, new_height = 250):

    new_width = None

    ori_width, ori_height = img.shape[:2]

    new_width = (new_height*ori_width)//ori_width

    resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

    return resized


if __name__ == "__main__":
    main()