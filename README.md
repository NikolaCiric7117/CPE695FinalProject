# CPE695FinalProject

## Requirements:
-Ubuntu 20.04
-ROS-Noetic
-The Simulation Enviorment

## Prerequisite:
-C++ Compiler
-Gazebo ROS Package


##  Running Instructions
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
5. Change the file permissions to make it executable in /scripts folder if required:

   `cd src/CPE695FinalProject/scripts`

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

9 To change to the path planning algorithm to the `param` folder and find the `global_planner.yaml` file. Then change the parameter to `use_dijkstra` to `true`

10. To run the simulation in empty enviroment simply comment out line 69 in the `cafe_global_planner.launch` file

11. To run the simualtion in a enviorment with only static objects comment out the line from step 10 and open the gazebo simultor and place the objects from the top toolbar whereever you would like. 





   
