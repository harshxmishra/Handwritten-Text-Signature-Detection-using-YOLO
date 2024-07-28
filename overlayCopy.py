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
             '22.jpg', '23.png', '24.png', '25.png', '26.png', '27.png']
    images_doc = {'1.jpg': [30, 4], '2.png': [30, 4], '3.jpg': [30, 4], '4.jpg': [30, 4], '5.jpg': [30, 17], '6.jpg': [30, 10], '7.png': [30, 9], '8.png': [31, 3], '9.png': [30, 3], '10.jpg': [31, 6], '11.jpg': [30, 4], '12.jpg': [30, 3], '13.jpg': [30, 3], '14.png': [30, 4], '15.jpeg': [32, 2], '16.jpg': [31, 3], '17.png': [30, 6], '18.png': [30, 6], '19.jpg': [31, 4], '20.png': [30, 4], '21.jpg': [31, 3], '22.jpg': [30, 5], '23.png': [30, 4], '24.png': [30, 2], '25.png': [30, 2], '26.png': [30, 5], '27.png': [30, 2]}

    index_sign = ['1.jpg', '2.png', '3.png', '4.jpg']
    images_sign = {'1.jpg': [5, 40], '2.png': [3, 10], '3.png': [5, 10], '4.jpg': [5, 10]}


    for i in range(25, 27):
        print(i)

        try:
            filename = index_doc[i]
            print(filename)

            # noBg = removeBG("C:/Users/ADITYA/Desktop/Handwritten Texts/combined", filename)
            # noBg = cv2.imread("C:/Users/ADITYA/Desktop/Handwritten Texts/combined/"+ filename)

            noBg = removeBG("C:/Users/ADITYA/Desktop/Handwritten Texts/unruled/", filename, images_doc[index_doc[i]][1])
            newImg = cv2.imread("C:/Users/ADITYA/Desktop/Handwritten Texts/canvas/depositphotos_147864957-stock-photo-natural-recycled-paper-texture-newspaper.jpg")
            noBg = zoom(noBg)
            coord_x = random.randrange(0, 150)
            coord_y = random.randrange(0, 180)
            newImg = copyToNew(newImg, noBg, coord_x, coord_y)

            signatures = []

            for j in range(random.randrange(3,4)):
                sign_ind = random.choice(index_sign)
                sign = removeBG("C:/Users/ADITYA/Desktop/Handwritten Texts/signatures/", sign_ind, images_sign[sign_ind][1])
                signatures.append([sign, 100])

            # try:
                for j in signatures:
                    coord_x = random.randrange(220, newImg.shape[1])
                    coord_y = random.randrange(340, newImg.shape[0]-100)

                    j[0] = zoom(j[0], j[1])
                    newImg = copyToNew(newImg, j[0], coord_x, coord_y)

                newImg = cv2.cvtColor(newImg, cv2.COLOR_BGR2RGB)
                saveImg(root + '/finals/' + str(images_doc[index_doc[i]][0]) + '_' + filename, newImg)
                images_doc[index_doc[i]][0] += 1

                plt.imshow(newImg)
                plt.show()


        except:
            print('i=', i)
            i -= 1



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