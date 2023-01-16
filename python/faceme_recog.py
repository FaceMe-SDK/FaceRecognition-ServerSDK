import ctypes, ctypes.util
from ctypes import *
from numpy.ctypeslib import ndpointer
import sys
import os

lib_path = os.path.abspath(os.path.dirname(__file__)) + '/../bin/linux_x86_64/libfaceme_recog1.so'
recog_engine = cdll.LoadLibrary(lib_path)

fmr_version = recog_engine.fmr_version
fmr_version.argtypes = []
fmr_version.restype = ctypes.c_char_p

fmr_init = recog_engine.fmr_init
fmr_init.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
fmr_init.restype = ctypes.c_int32

fmr_extract_feature = recog_engine.fmr_extract_feature
fmr_extract_feature.argtypes = [ndpointer(ctypes.c_ubyte, flags='C_CONTIGUOUS'), ctypes.c_int32, ctypes.c_int32, ndpointer(ctypes.c_int32, flags='C_CONTIGUOUS'), ndpointer(ctypes.c_ubyte, flags='C_CONTIGUOUS'), ndpointer(ctypes.c_int32, flags='C_CONTIGUOUS')]
fmr_extract_feature.restype = ctypes.c_int

fmr_compare_feature = recog_engine.fmr_compare_feature
fmr_compare_feature.argtypes = [ndpointer(ctypes.c_ubyte, flags='C_CONTIGUOUS'), ndpointer(ctypes.c_ubyte, flags='C_CONTIGUOUS')]
fmr_compare_feature.restype = ctypes.c_double
