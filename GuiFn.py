import cv2
import numpy as np


def overlay_image(im1, im2, x_offset, y_offset):
    '''Mutates im1, placing im2 over it at a given offset.'''
    im1[y_offset:y_offset+im2.shape[0], x_offset:x_offset+im2.shape[1]] = im2
    return im1

def overlayblend(a,b):
    a = a.astype(float) / 255
    b = b.astype(float) / 255  # make float on range 0-1

    mask = a >= 0.5  # generate boolean mask of everywhere a > 0.5
    ab = np.zeros_like(a)  # generate an output container for the blended image

    # now do the blending
    ab[~mask] = (2 * a * b)[~mask]  # 2ab everywhere a<0.5
    ab[mask] = (1 - 2 * (1 - a) * (1 - b))[mask]  # else this

    # Scale to range 0..255 and save
    x = (ab * 255).astype(np.uint8)
    return x

def readjupimgs(b,r,g,promap,width,height):
    blue = cv2.imread(b, 0)
    green = cv2.imread(r, 0)
    red = cv2.imread(g, 0)
    images = [0, 0, 0]
    images[0] = blue  # blue
    images[1] = green  # green
    images[2] = red  # red

    img = cv2.merge(images)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

    pro = cv2.imread(promap, cv2.IMREAD_UNCHANGED)
    pro = decreaseOpacity(pro,0.7)

    imgpro = overlayblend(pro, img)
    imgpro = cv2.resize(imgpro, (width, height))

    img_s = sharpen_img(imgpro)
    return img_s

def decreaseOpacity(img,Opacity):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    img = np.array(img, dtype=np.float64)
    a_channel = np.ones(img.shape, dtype=np.float64) * Opacity
    img = img * a_channel
    return img

def sharpen_img(img):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    img_s = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
    return img_s

def blendWithTransparent(background,foreground,width,height,x_offset,y_offset):

    foreground = cv2.cvtColor(foreground, cv2.COLOR_BGR2BGRA)
    background = cv2.cvtColor(background, cv2.COLOR_BGR2BGRA)

    foreground = cv2.resize(foreground, (width, height))
    array_created = np.full((background.shape[0], background.shape[1], 4), 0, dtype=np.uint8)

    foreground_over = overlay_image(array_created, foreground, x_offset, y_offset)

    # normalize alpha channels from 0-255 to 0-1
    alpha_background = background[:, :, 3] / 255.0
    alpha_foreground = foreground_over[:, :, 3] / 255.0

    # set adjusted colors
    newimg = np.zeros_like(background)
    for color in range(0, 3):
        newimg[:, :, color] = alpha_foreground * foreground_over[:, :, color] + \
                              alpha_background * background[:, :, color] * (1 - alpha_foreground)

    # set adjusted alpha and denormalize back to 0-255
    newimg[:, :, 3] = (1 - (1 - alpha_foreground) * (1 - alpha_background)) * 255

    return newimg

def shifthue(img,value):
    # extract alpha channel
    alpha = img[:,:,3]

    # extract bgr channels
    bgr = img[:,:,0:3]

    # convert to HSV
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    #h = hsv[:,:,0]
    #s = hsv[:,:,1]
    #v = hsv[:,:,2]
    h,s,v = cv2.split(hsv)

    # modify hue channel by adding difference and modulo 180
    hnew = np.mod(h + value, 180).astype(np.uint8)

    # recombine channels
    hsv_new = cv2.merge([hnew,s,v])

    # convert back to bgr
    bgr_new = cv2.cvtColor(hsv_new, cv2.COLOR_HSV2BGR)

    # put alpha back into bgr_new
    bgra = cv2.cvtColor(bgr_new, cv2.COLOR_BGR2BGRA)
    bgra[:,:,3] = alpha

    return bgra

def change_brightness(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v,value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

def contrast(img,value):
    # converting to LAB color space
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l_channel, a, b = cv2.split(lab)

    # Applying CLAHE to L-channel
    # feel free to try different values for the limit and grid size:
    clahe = cv2.createCLAHE(clipLimit=value, tileGridSize=(8, 8))
    cl = clahe.apply(l_channel)

    # merge the CLAHE enhanced L-channel with the a and b channel
    limg = cv2.merge((cl, a, b))

    # Converting image from LAB Color model to BGR color spcae
    enhanced_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    return enhanced_img

def saturation(img,value):
    # Convert from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Grab saturation channel
    saturation = hsv[..., 1]

    # Increase saturation by a given value
    saturation = cv2.add(saturation, value)

    # Clip resulting values to fit within 0 - 255 range
    np.clip(saturation, 0, 255)

    # Put back adjusted channel into the HSV image
    hsv[..., 1] = saturation

    # Convert back from HSV to BGR
    new = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return new


def apply_brightness_contrast(input_img, contrast=0):
    brightness = 0
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow

        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()

    if contrast != 0:
        f = 131 * (contrast + 127) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)
    return buf

