# CPE695FinalProject

## Requirments:
-Ubuntu 20.04
-ROS-Noetic
-The Simulation Enviorment

## Pre-requisites
-C++ Compiler
-Gazebo ROS Package


## Running Intructions
1. Install dependencies:

    `sudo apt install ros-noetic-navigation`

    `sudo apt install ros-noetic-turtlebot3-*`

2. Suppose you have made a catkin workspace named catkin_ws.
3. Once you are finished with all the dependencies, you can git clone this package from github into your ROS workspace and catkin_make it.

    `cd ~/catkin_ws/src`

    `git clone --recurse-submodules https://github.com/NikolaCiric7117/CPE695FinalProject.git`

    `cd ~/catkin_ws`

    `catkin_make`
4. If you installed all dependencies correctly, you shouldn’t get any errors.
5. Change the file permissions to make it executable in /src fold if required:

   `cd/navigation/scripts`

    `ls`

    `chmod +x *`
6. You can run the environment by executing

    `roslaunch navigation cafe_global_planner.launch`


   make sure to source by:

   `source /devel/setup.bash`

7. To get the stats you have to run this script in a new terminal first before step 8:

   `rosrun navigation time_take.py`

8. To commence navigation type in another terminal:

   `rosrun navigation goal_pose.py`

   once the goal has been reached type

   `^c` into the the terminal from step 7





   
