import Leap, sys, thread, time, math
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class LeapMotionListener(Leap.Listener):
		finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
		bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
		state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
		
		def on_init(self, controller):
			print "Initialized"
		
		def on_connect(self, controller):
			print "Motion Sensor Connected"
			
			controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
			controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
			controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
			controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
		
		def on_disconnect(self, controller):
			print "Motion Sensor Disconnected"
			
		def on_exit(self, controller):
			print "Exited"
			
		def on_frame(self, controller):
			frame = controller.frame()
			
			for gesture in frame.gestures():
			#CIRCLE GESTURE
				if gesture.type == Leap.Gesture.TYPE_CIRCLE:
					swept_angle = 0
					circle = CircleGesture(gesture)
					if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
						clockwiseness = "Clockwise"
					else:
						clockwiseness = "Counter-Clockwise"
					if circle.state != Leap.Gesture.STATE_START:
						swept_angle = 0
						previous = CircleGesture(controller.frame(1).gesture(circle.id))
						swept_angle = (circle.progress - previous.progress)*2*Leap.PI/2
						
					print "ID: " + str(circle.id) + " Progress: " + str(circle.progress) + " Radius: " + str(circle.radius) + " Swept Angle: " + str(swept_angle*Leap.RAD_TO_DEG) + " " + clockwiseness
			
				if gesture.type == Leap.Gesture.TYPE_SWIPE:
					swipe = SwipeGesture(gesture)
					#print "Swipe ID: " + str(swipe.id) + " State: " + self.state_names[gesture.state] + " Position: " + str(swipe.position) + " Direction: " + str(swipe.direction) + " Speed (mm/s)" + str(swipe.speed)
					swipeDir = swipe.direction
					if (swipeDir.x > 0 and math.fabs(swipeDir.x)>math.fabs(swipeDir.y)):
						print "Swiped Right"
					elif (swipeDir.x < 0 and math.fabs(swipeDir.x)>math.fabs(swipeDir.y)):
						print "Swiped Left"
					elif (swipeDir.y > 0 and math.fabs(swipeDir.x)<math.fabs(swipeDir.y)):
						print "Swiped Up"
					elif (swipeDir.y < 0 and math.fabs(swipeDir.x)<math.fabs(swipeDir.y)):
						print "Swiped Down"
			
				if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
					screenTap = ScreenTapGesture(gesture)
					print "Screen Tap ID: " + str(screenTap.id) + " State: " + self.state_names[gesture.state] + " Position: " + str(screenTap.position) + " Direction: " + str(screenTap.direction)
			
				if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
					keyTap = KeyTapGesture(gesture)
					print " Key Tap ID: " + str(keyTap.id) + " State: " + self.state_names[gesture.state] + " Position: " + str(keyTap.position) + " Direction: " + str(keyTap.direction)
			
			"""
			for tool in frame.tools:
				print "Tool ID: " + str(tool.id) + " Tip Position: " + str(tool.tip_position) + " Direction: " + str(tool.direction)
			"""
			
			#print " Frame ID: " + str(frame.id) + " Timestamp: " + str(frame.timestamp) + " # of hands: " + str(len(frame.hands)) + " # of fingers: " + str(len(frame.fingers)) + " # of tools " + str(len(frame.tools)) + " # of Gestures " + str(len(frame.gestures()))
			"""	
			for hand in frame.hands:
				handType = "Left hand" if hand.is_left else "Right hand"
				
				#print handType + " Hand ID: " + str(hand.id) + " Palm Position : "  + str(hand.palm_position)
				
				#Vectors normal and direction
				normal = hand.palm_normal
				direction = hand.direction
				
				#Roll Pitch Yaw
				#print "Pitch: " + str(direction.pitch*Leap.RAD_TO_DEG) + " Roll " + str(normal.roll*Leap.RAD_TO_DEG) + " Yaw: " + str(direction.yaw*Leap.RAD_TO_DEG)
		
				arm = hand.arm
				
				print "Arm Direction: " + str(arm.direction) 
				print "Wrist Position: " + str(arm.wrist_position) 
				print "Elbow Position: " + str(arm.elbow_position)
				time.sleep(0.1)
				
				
				for finger in hand.fingers:
					#print "Type: " + self.finger_names[finger.type] + " ID: " + str(finger.id) + " Length mm: " + str(finger.length) + " Width mm: " + str(finger.width)
		
					for b in range(0,4):
						bone = finger.bone(b)
						#print "Bone: " + self.bone_names[bone.type] + " Start: " + str(bone.prev_joint) + " End: " + str(bone.next_joint) + " Direction: " + str(bone.direction)
		
				"""
			
			
			
			
def main():
	listener = LeapMotionListener()
	controller = Leap.Controller()
	
	controller.add_listener(listener)
	
	print "Press enter to quit"
	try:
			sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		controller.remove_listener(listener)
		
if __name__ == "__main__":
	main()