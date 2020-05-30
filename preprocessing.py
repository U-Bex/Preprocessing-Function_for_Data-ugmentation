def random_crop(prop_lim = 0.5, zoom_range = (228, 232)):
    def randomcrop(img):
        img_h, img_w, img_ch = img.shape
        prop = np.random.rand()
        
        if prop > prop_lim:
            return img


        new_size = np.random.randint(zoom_range[0],zoom_range[1])
        
        top = np.random.randint(0, new_size - img_h)
        left = np.random.randint(0, new_size - img_w)
        img = cv2.resize(img, (new_size, new_size))

        img = img[top:top+img_h, left:left+img_w, :]

        return img
    return randomcrop

def random_erasing(prop_lim = 0.5, max_rate = 0.3, min_rate = 0.05, color = True):
    def eraser(img):
        img_h, img_w, img_ch = img.shape
        prop = np.random.rand()

        random_croper = random_crop()
        img = random_croper(img)

        if prop > prop_lim:
            return img

        while True:
            h_rate = np.random.uniform(min_rate, max_rate)
            w_rate = np.random.uniform(min_rate, max_rate)
            h = int(img_h*h_rate)
            w = int(img_w*w_rate)
            left = np.random.randint(0, img_w)
            top = np.random.randint(0, img_h)

            if left + w <= img_w and top + h <= img_h:
                break

        if color:
            noise = np.random.uniform(0, 255, (h, w, img_ch))
        else:
            noise = np.random.uniform(0, 255)

        img[top:top + h, left:left + w, :] = noise

        return img

    return eraser
