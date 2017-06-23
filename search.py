# USAGE
# python search.py --index index.csv --query queries/103100.png --result-path dataset
# from __future__ import print_function
# import the necessary packages
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher
import argparse
import cv2
import numpy as np


# take picture and store it
cap = cv2.VideoCapture(1) # video capture source camera (Here webcam of laptop)
ret,frame = cap.read() # return a single frame in variable `frame`
cv2.imwrite('/Users/benson/Desktop/vacation-image-search-engine/queries/snapshot.png',frame)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())

# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))

# load the query image and describe it
query = cv2.imread(args["query"])
features = cd.describe(query)

# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)

# display the query
cv2.imshow("Query", query)

# empty a file
open("result.txt", 'w').close()

# create a file
f = open('result.txt', 'w')

# loop over the results
for (score, resultID) in results:
	# load the result image and display it
	result = cv2.imread(args["result_path"] + "/" + resultID)
	cv2.imshow("Result", result)
	cv2.waitKey(0)
	print resultID + ': ' + str(score)
	# print(resultID + ': ' + str(score), file=result.txt)
	f.write(resultID + ': ' + str(score) + '\n')


#f.close()
