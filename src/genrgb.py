#!/usr/bin/env python

#this file is used to generate rgb images named by its record time.

#output     rgb images,  
#           rgb.txt
from __future__ import print_function

import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy
import os

yourrootpath = '/home/kadn/dataset416/rgb/'
rgbtopic = "/camera/rgb/image_raw"

class image_converter:

  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber(rgbtopic, Image,self.callback)
#    self.rootpath = '/media/kadn/DATA2/dataset/dataset416/rgbd/'
    self.rootpath = yourrootpath
    self.rgbtxtfile = 'rgb.txt'
    self.file = open(self.rootpath+self.rgbtxtfile, 'w')

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    timestr = str(data.header.stamp)
    timef = timestr[:len(timestr)-9]
    times = timestr[len(timestr)-9: len(timestr)-3]
    time = timef + '.' + times
    name = 'rgb/'+time+'.png'
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
  rospy.init_node('rgbimage_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
    ic.file.close()
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
