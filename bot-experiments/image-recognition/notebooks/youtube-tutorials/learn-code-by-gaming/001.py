# import needed libraries

import cv2 as cv
import numpy as np

haystack_tg_img = 'porings.jpg' # random image from internet of ragnarok online
needle_tg_img = 'poring.jpg'

haystack_img = cv.imread('imgs/%s'% haystack_tg_img, cv.IMREAD_UNCHANGED)
needle_img = cv.imread('imgs/%s'% needle_tg_img, cv.IMREAD_UNCHANGED)

# cv.imshow(haystack_tg_img, haystack_img);
# cv.imshow(needle_tg_img, needle_img);

result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

# cv.imshow('Result', result)
# cv.waitKey(0)
# cv.destroyAllWindows

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print('Best match top left position %s' % str(max_loc))
print('Best match confidence %s' % str(max_val))

treshhold = 0.8

if(max_val >= treshhold):
    print('needle found')

    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    cv.rectangle(haystack_img, top_left, bottom_right, color=(0,0, 255), thickness=2, lineType=cv.LINE_4)

    # cv.imshow('result',haystack_img)
    # cv.waitKey()
    # cv.destroyAllWindows

    cv.imwrite('result.jpg', haystack_img)
else:
    print('needle not found')