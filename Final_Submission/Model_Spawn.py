#!/usr/bin/env python

import sys
import rospy
import rospkg

from gazebo_msgs.srv import (
    SpawnModel,
)
from geometry_msgs.msg import (
    Pose,
    Point,
)
from std_msgs.msg import (
    Header,
    Empty,
)

def load_tables(table_pose1=Pose(position=Point(x=1.1, y=0, z=0.73)),
                       table_reference_frame1="world",
                       table_pose2=Pose(position=Point(x=0.6, y=1.1, z=0.73)),
                       table_reference_frame2="world",
                       table_pose3=Pose(position=Point(x=0.6, y=-1.1, z=0.73)),
                       table_reference_frame3="world"):
    #Get models from directory
    model_path = rospkg.RosPack().get_path('baxter_sim_examples')+"/models/"
    #Load 1
    table1_xml = ''
    with open (model_path + "real_table/object.urdf", "r") as table_file:
        table1_xml=table_file.read().replace('\n', '')
    #Load 2 & 3 orientation
    table2_xml = ''
    with open (model_path + "real_table2/object.urdf", "r") as table_file:
        table2_xml=table_file.read().replace('\n', '')
    rospy.wait_for_service('/gazebo/spawn_urdf_model')

    #Spawn 1
    try:
        spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
        resp_urdf1 = spawn_urdf("table1", table1_xml, "/",
                             table_pose1, table_reference_frame1)
    except rospy.ServiceException, e:
        rospy.logerr("Spawn SDF service call failed: {0}".format(e))

    #Spawn 2
    try:
        spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
        resp_urdf2 = spawn_urdf("table2", table2_xml, "/",
                             table_pose2, table_reference_frame2)
    except rospy.ServiceException, e:
        rospy.logerr("Spawn SDF service call failed: {0}".format(e))

    #Spawn 3
    try:
        spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
        resp_urdf3 = spawn_urdf("table3", table2_xml, "/",
                             table_pose3, table_reference_frame3)
    except rospy.ServiceException, e:
        rospy.logerr("Spawn SDF service call failed: {0}".format(e))

def load_UP(block_no, block_side, block_pose_left=Pose(position=Point(x=0.1, y= 0.7, z=0.74)),
                       block_reference_frame="world",
                       block_pose_right=Pose(position=Point(x=0.1, y= -0.7, z=0.74))):
    # Get Models' Path
    model_path = rospkg.RosPack().get_path('baxter_sim_examples')+"/models/" 
    block_xml = ''
    with open (model_path + "Upright/object.urdf", "r") as block_file:
          block_xml = block_file.read().replace('\n', '')

    rospy.wait_for_service('/gazebo/spawn_urdf_model')
    #Spawn bricks on left side
    if block_side == 'l':
        try:
            spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
            resp_urdf = spawn_urdf(block_no, block_xml, "/",
                                    block_pose_left, block_reference_frame)
        except rospy.ServiceException, e:
            rospy.logerr("Spawn SDF service call failed: {0}".format(e))

    #Spawn Bricks on right side
    elif block_side == 'r':
        try:
            spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
            resp_urdf = spawn_urdf(block_no, block_xml, "/",
                                   block_pose_right, block_reference_frame)
        except rospy.ServiceException, e:
            rospy.logerr("Spawn SDF service call failed: {0}".format(e))
    else:
      print('You dingus, thats not a side!')

def load_Flat(block_no, block_side, block_pose_left=Pose(position=Point(x=0.3, y= 0.7, z=0.73)),
                       block_reference_frame="world",
                       block_pose_right=Pose(position=Point(x=0.3, y=-0.7, z=0.73))):
    # Get Models' Path
    model_path = rospkg.RosPack().get_path('baxter_sim_examples')+"/models/" 
    block_xml = ''
    with open (model_path + "Flat/object.urdf", "r") as block_file:
        block_xml = block_file.read().replace('\n', '')
    rospy.wait_for_service('/gazebo/spawn_urdf_model')

    if block_side == 'l':
      try:
          spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
          resp_urdf = spawn_urdf(('Flat %s' %block_no), block_xml, "/",
                                 block_pose_left, block_reference_frame)
      except rospy.ServiceException, e:
          rospy.logerr("Spawn SDF service call failed: {0}".format(e))

    elif block_side == 'r':
      try:
          spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
          resp_urdf2 = spawn_urdf(('Flat %s' %block_no), block_xml, "/",
                                 block_pose_right, block_reference_frame)
      except rospy.ServiceException, e:
          rospy.logerr("Spawn SDF service call failed: {0}".format(e))
    else:
      print('You dingus, thats not a side!')
