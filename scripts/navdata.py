#!/usr/bin/env python
import rospy
import roslib; roslib.load_manifest('sample_ardrone')
from ardrone_autonomy.msg import Navdata

def callback(navdata):
    t = navdata.header.stamp.to_sec()
    print("received odometry message: time=%f vx=%f vy=%f z=%f yaw=%f"%(t,navdata.vx,navdata.vy,navdata.altd,navdata.rotZ))
    
if __name__ == '__main__':
    rospy.init_node('sample_node', anonymous=True)
    
    # subscribe to navdata
    rospy.Subscriber("/ardrone/navdata", Navdata, callback)
    
    rospy.spin()
    
