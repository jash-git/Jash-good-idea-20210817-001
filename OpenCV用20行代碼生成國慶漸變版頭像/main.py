
import cv2 as cv
import numpy as np


def auto_mask_demo(image):
    gq = cv.imread("D:/2.png")
    cv.imshow("input", gq)

    # 生成mask区域
    h, w, c = gq.shape
    mask = np.zeros((h, w), dtype=np.float32)
    for row in range(h):
            start = np.int(np.abs(np.sin(row * np.pi / 180) * 50))
            mask[row, start:w] = np.linspace(0, 255, w-start)
    mask = mask / 255.0
    cv.imshow("mask", mask)

    # generate icon
    dst = cv.resize(image, (w, h), interpolation=cv.INTER_CUBIC)
    result = np.zeros_like(dst)
    for row in range(h):
        for col in range(w):
            w2 = mask[row, col]
            w1 = 1.0 - w2
            b1, g1, r1 = gq[row, col]
            b2, g2, r2 = dst[row, col]
            b = b1 * w1 + b2 * w2
            g = g1 * w1 + g2 * w2
            r = r1 * w1 + r2 * w2
            result[row, col] = (np.int(b), np.int(g), np.int(r))
    cv.imshow("profile image", result)
    cv.imwrite("D:/result.png", result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    src = cv.imread("D:/1.png")
    auto_mask_demo(src)