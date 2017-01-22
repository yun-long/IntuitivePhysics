import constants as c
import numpy as np
import os
from glob import glob
from PIL import Image
from utils import *
TRAIN_DIR_CLIPS = c.get_dir(os.path.join(c.DATA_DIR, '.Clips/'))
NUM_CLIPS = len(glob(TRAIN_DIR_CLIPS + '*'))
path = c.TRAIN_DIR_CLIPS + str(np.random.choice(NUM_CLIPS)) + '.npz'
clip = np.load(path)['arr_0'][0,:,:,1]
clip =  denormalize_frames(clip)
img = Image.fromarray(clip, 'L')
img.show()

