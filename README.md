##generate_rgbd_dataset

This project is tested in ROS kinetic.

This project aims to generate **rgb images, depth images** from **Example.bag**, **images are named by their time stamp.**

#### Run

- start ROS
`roscore`
- play your bag
`rosbag play Example.bag --clock`

- another terminal
`python  genrgb.py`

- another terminal
`python  gendepth.py`

- use associate.py to associate rgb.txt and depth.txt
`python associate.py rgb.txt depth.txt > associate.txt`

#### settings
you can set your image topic and filepath in genrgb.py and gendepth.py`