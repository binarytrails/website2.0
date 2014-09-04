"""
Utilities powered by the magnificent me.
"""

import os, glob

def get_filenames(path, by_newest):
    	
	files = filter(os.path.isfile, glob.glob(path + "*"))
    	files.sort(key=lambda x: os.path.getmtime(x))
    
	if by_newest:
        	files.reverse()
	
	names = []
	for f in files:
		fidx = f.rfind("/") + 1
		name = f[fidx:]
		names.append(name)    

	return names
