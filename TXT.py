import os, platform, time, sys
bit = platform.architecture()[0]
if bit == '64bit':
 import XD
elif bit == '32bit':
 import XD31
