import leap, sys, math
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class LeapMotionListener(Leap.Listener):
	def on_connect(self, controller):
			print "Motion Sensor Connected"
			
			controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
			controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
			controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
			controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
			
	def on_frame(self, controller):
			frame = controller.frame()