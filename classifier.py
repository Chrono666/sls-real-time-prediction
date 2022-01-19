import os
import sched
import time

import cv2
import numpy as np
from tensorflow import keras


def get_latest_image(dirpath, valid_extensions=('jpg', 'jpeg', 'png')):
    # get filepaths of all files and dirs in the given dir
    valid_files = [os.path.join(dirpath, filename) for filename in os.listdir(dirpath)]
    # filter out directories, no-extension, and wrong extension files
    valid_files = [f for f in valid_files if '.' in f and \
                   f.rsplit('.', 1)[-1] in valid_extensions and os.path.isfile(f)]

    if not valid_files:
        raise ValueError("No valid images in %s" % dirpath)

    # getmtime -> last modified, getatime -> last accessed
    return max(valid_files, key=os.path.getmtime)


def classify_single_image(image_path, model):
    original = cv2.imread(image_path)
    rgb = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    img = cv2.resize(rgb, (224, 224)) / 255
    image = np.array([img])
    vgg_input = keras.applications.vgg16.preprocess_input(image * 255)
    Y_prob = model.predict(vgg_input)
    keras.backend.clear_session()
    if Y_prob > 0.8:
        print('\nThe image ' + image_path + ' has no curling\n', Y_prob)
    else:
        print('\nThe image ' + image_path + ' has curling\n', Y_prob)


def scheduler(sc):
    image_path = get_latest_image('images')
    classify_single_image(image_path, keras.models.load_model('vgg16'))
    s.enter(35, 1, scheduler, (sc,))


if __name__ == '__main__':
    s = sched.scheduler(time.time, time.sleep)
    s.enter(35, 1, scheduler, (s,))
    s.run()
