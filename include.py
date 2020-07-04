import os
from datetime import datetime
PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
IDENTIFIER   = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

#numerical libs
import math
import numpy as np
import random
import PIL
import cv2
import matplotlib
matplotlib.use('TkAgg')
#matplotlib.use('WXAgg')
#matplotlib.use('Qt4Agg')
#matplotlib.use('Qt5Agg') #Qt4Agg
print(matplotlib.get_backend())
#print(matplotlib.__version__)

# torch libs
import torch
from torch.utils.data.dataset import Dataset
from torch.utils.data import DataLoader
from torch.utils.data.sampler import *

import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
from torch.nn.parallel.data_parallel import data_parallel

# std libs
import collections
import copy
import numbers
import inspect
import shutil
from timeit import default_timer as timer
import itertools
from collections import OrderedDict

import csv
import pandas as pd
import pickle
import glob
import sys
from distutils.dir_util import copy_tree
import time

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from skimage.transform import resize as skimage_resize

# constant #
PI  = np.pi
INF = np.inf
EPS = 1e-12

#---------------------------------------------------------------------------------
class Struct(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

#---------------------------------------------------------------------------------
def remove_comments(lines, token='#'):
    """ Generator. Strips comments and whitespace from input lines.
    """

    l = []
    for line in lines:
        s = line.split(token, 1)[0].strip()
        if s != '':
            l.append(s)
    return l

def remove(file):
    if os.path.exists(file): os.remove(file)


def empty(dir):
    if os.path.isdir(dir):
        shutil.rmtree(dir, ignore_errors=True)
    else:
        os.makedirs(dir)


# http://stackoverflow.com/questions/34950201/pycharm-print-end-r-statement-not-working
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout  #stdout
        self.file = None

    def open(self, file, mode=None):
        if mode is None: mode ='w'
        self.file = open(file, mode)

    def write(self, message, is_terminal=1, is_file=1 ):
        if '\r' in message: is_file=0

        if is_terminal == 1:
            self.terminal.write(message)
            self.terminal.flush()
            #time.sleep(1)

        if is_file == 1:
            self.file.write(message)
            self.file.flush()

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass

# io ------------------------------------
def write_list_to_file(strings, list_file):
    with open(list_file, 'w') as f:
        for s in strings:
            f.write('%s\n'%str(s))
    pass


def read_list_from_file(list_file, comment='#', func=None):
    with open(list_file) as f:
        lines  = f.readlines()

    strings=[]
    for line in lines:
        s = line.split(comment, 1)[0].strip()
        if s != '':
            strings.append(s)
    if func is not None:
        strings=[func(s) for s in strings]

    return strings

def load_pickle_file(pickle_file):
    with open(pickle_file,'rb') as f:
        x = pickle.load(f)
    return x

def save_pickle_file(pickle_file, x):
    with open(pickle_file, 'wb') as f:
        pickle.dump(x, f, pickle.HIGHEST_PROTOCOL)


def backup_project_as_zip(project_dir, zip_file):
    assert(os.path.isdir(project_dir))
    assert(os.path.isdir(os.path.dirname(zip_file)))
    shutil.make_archive(zip_file.replace('.zip',''), 'zip', project_dir)
    pass

# etc ------------------------------------
def time_to_str(t, mode='min'):
    if mode=='min':
        t  = int(t)/60
        hr = t//60
        min = t%60
        return '%2d hr %02d min'%(hr,min)
    elif mode=='sec':
        t   = int(t)
        min = t//60
        sec = t%60
        return '%2d min %02d sec'%(min,sec)
    else:
        raise NotImplementedError

def np_float32_to_uint8(x, scale=255):
    return (x*scale).astype(np.uint8)

def np_uint8_to_float32(x, scale=255):
    return (x/scale).astype(np.float32)



