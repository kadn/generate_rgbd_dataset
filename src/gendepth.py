#!/usr/bin/env python

#this file is used to generate rgb images named by its record time.

#output     depth images,  
#           depth.txt
from __future__ import print_function

import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import os

yourrootpath = '/home/kadn/dataset416/rgbd/'
depthtopic = "/camera/depth/image"

class image_converter:

  def __init__(self):

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber(depthtopic,Image,self.callback)
    self.rootpath = yourrootpath
    self.rgbtxtfile = 'depth.txt'
    self.file = open(self.rootpath+self.rgbtxtfile, 'w')

  def callback(self,data):
    try:
      # print('encoding', data.encoding)
      # print(len(data.data))
      cv_image = np.fromstring(str(bytearray(data.data)), np.float32)
      cv_image = cv_image / 10.0*255.0
      cv_image = np.float32(cv_image)
      cv_image = np.reshape(cv_image, (480, 640))
    except CvBridgeError as e:
      print(e)

    timestr = str(data.header.stamp)
    timef = timestr[:len(timestr)-9]
    times = timestr[len(timestr)-9: len(timestr)-3]
    time = timef + '.' + times
    name = 'depth/'+time+'.png'
    filepath = self.rootpath + name
    cv2.imwrite(filepath, cv_image)
    self.file.write(time) 
    self.file.write('\t')
    self.file.write(name)
    self.file.write('\n')

#    cv2.imshow("Image window", cv_image)
#    cv2.waitKey(3)


def main(args):
  ic = image_converter()
  rospy.init_node('depthimage_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
    ic.file.close()
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
