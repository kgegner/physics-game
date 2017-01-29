# Transfer Game - Problem Screen Class

# Author: Kathleen Gegner
# Update: 12/3/16
# File name: problem.py

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label	 import Label
from kivy.uix.image import Image
from kivy.properties import StringProperty, NumericProperty, ListProperty, DictProperty, ObjectProperty, BooleanProperty
from kivy.app import App
from graphic import DynamicGraphicContainer, StaticGraphicContainer
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.clock import Clock
from copy import deepcopy
from consts import TOOL_INFO, PROB_INFO, FEEDBACK, COLORS

class TextPopup(Popup):
	""" 
	Class definition for content to go in pop up windows.
	Content includes text and a button.
	"""		
	def __init__(self, popup_text, popup_title, size, **kwargs):
		super(TextPopup, self).__init__(**kwargs)
		self.size_hint = size
		self.label.text = popup_text
		self.title = popup_title

class HeadingContainer(FloatLayout):
	""" 
	Class definition for header that keeps track of game progress 
	and hosts home and help buttons. 
	"""
	# Create properties to store color setting for each circle
	circle1_color = ListProperty([1, 1, 1, 1])
	circle2_color = ListProperty([1, 1, 1, 1])
	circle3_color = ListProperty([1, 1, 1, 1])
	
	# Create properties to store text for each circle
	circle1_text = StringProperty('')
	circle2_text = StringProperty('')
	circle3_text = StringProperty('')
	
	# Create property that holds what next screen should be displayed
	next_screen = DictProperty()
		
	def __init__(self, problem_num, **kwargs):
		super(HeadingContainer, self).__init__(**kwargs)
		
		# Keep track of which problem_number the user is working on
		self.problem_num = problem_num
		
		# Update circle color/text based on which problem user is working on
		# Circles keep track of player's progression 
		if problem_num == 1:
			self.circle1_color = COLORS['pink']['rgba']
			self.circle1_text = str(problem_num)
		if problem_num == 2:
			self.circle2_color = COLORS['pink']['rgba']
			self.circle1_text = ''
			self.circle2_text = str(problem_num)
		if problem_num == 3:
			self.circle3_color = COLORS['pink']['rgba']
			self.circle2_text = ''
			self.circle3_text = str(problem_num)
	
	def screen_forward(self):
		""" Set next screen to be one more than the current one. """
		if self.problem_num == 1:
			self.next_screen = {'name': 'prob2', 'direction': 'left'}
		if self.problem_num == 2:
			self.next_screen = {'name': 'prob3', 'direction': 'left'}
		if self.problem_num == 3:
			# Launch popup window to tell user they won, then go back to home screen
			popup = TextPopup(self.read_text('./questions/win.txt'), 'You did it!', (0.3, 0.5))
			popup.open()
			# Close application
			#App.get_running_app().stop()
			self.next_screen = {'name': 'home', 'direction': 'right'}
		print('Heading class\n', self.next_screen)
	
	def screen_backward(self):
		""" Set next screen to be one less than the current one. """
		if self.problem_num == 1:
			self.next_screen = {'name': 'home', 'direction': 'right'}
		if self.problem_num == 2:
			self.next_screen = {'name': 'prob1', 'direction': 'right'}
		if self.problem_num == 3:
			self.next_screen = {'name': 'prob2', 'direction': 'right'}
		print('Heading class\n', self.next_screen)
		
	def read_text(self, filename):
		with open(filename) as f:
			fileContents = f.read()
			return fileContents
		
class QuestionContainer(FloatLayout):
	""" 
	Class definition for container that host's question text 
	and question title.
	"""
	# Create properties to store question title and text
	question_title = StringProperty()
	question_text = StringProperty()
	
	def __init__(self, title, fname, **kwargs):
		super(QuestionContainer, self).__init__(**kwargs)
		self.question_title = title
		self.question_text = self.read_text(fname)
		
	def read_text(self, filename):
		with open(filename) as f:
			fileContents = f.read()
			return fileContents
			
class WorkspaceContainer(FloatLayout):
	"""
	Class definition for container that hosts the drawing area, 
	animation, animation control, and feedback agent.
	"""
	def __init__(self, **kwargs):
		super(WorkspaceContainer, self).__init__(**kwargs)

class ToolboxContainer(FloatLayout):
	"""
	Class definition for container that hosts the buttons
	to create each drawing tool. 
	"""
	def __init__(self, **kwargs):
		super(ToolboxContainer, self).__init__(**kwargs)
		
class HomeScreen(Screen):
	"""
	Class definition for the game's home screen. 
	The home screen displays the game's instructions.
	"""	
	# Create property to hold home welcome message
	greeting = StringProperty()
	
	# Property to store which screen should be shown next 
	update_screen = DictProperty()
	
	def __init__(self, **kwargs):
		super(HomeScreen, self).__init__(**kwargs)
		self.greeting = self.read_text('./questions/home.txt')
	
	def read_text(self, filename):
		""" Reads a file and returns the contents as a string. """
		with open(filename) as f:
			fileContents = f.read()
			return fileContents
	
	def yes_pressed(self):
		""" Function to deal with a 'yes' button being pressed. """
		# Launch a pop up and then advance to the next screen once the popup is closed
		popup = TextPopup(self.read_text('./questions/instruct_reminder.txt'), 'Quick Reminder', (0.35, 0.5))
		popup.open()
		popup.btn.bind(on_press=self.update_screen_callback)
	
	def no_pressed(self):
		""" Function to deal with a 'no' button being pressed. """
		# Close application
		App.get_running_app().stop()
	
	def update_screen_callback(self, *args):
		""" Function to set which screen should be shown next. """
		self.update_screen = {'name': 'prob1', 'direction': 'left'}


class ProblemScreen(Screen):
	"""
	Class definition for all problems in the game.
	Hosts all widgets for question text, drawing tools, 
	animation definitions, and error checking.
	
	# Keyboard code ref: https://kivy.org/docs/api-kivy.core.window.html
	"""		
	# Dictionary of widget tool objects
	tools = DictProperty()
	
	# Property to store which screen should be shown next 
	update_screen = DictProperty()
		
	# Name of graphic that will be animated
	graphic_to_animate = ListProperty()
		
	def __init__(self, question_num, **kwargs):
		super(ProblemScreen, self).__init__(**kwargs)
		
		# Save question number
		self.q_num = question_num 
		
		# Get data stored in PROB_INFO
		question_title = PROB_INFO[question_num]['q_info']['topic']
		question_text_file = PROB_INFO[question_num]['q_info']['fname']
		for name, dictionary in PROB_INFO[question_num].items():
			if 'animation' in dictionary.keys():
				self.graphic_to_animate.append(name)
		
		# Create widgets to add to problem screen
		heading = HeadingContainer(question_num)
		heading.bind(next_screen=self.update_screen_callback)
		self.add_widget(heading)
		self.add_widget(QuestionContainer(question_title, question_text_file))
		
	def playbtn_callback(self):
		""" Function called when the play/reset button has been pressed. """
		
		# Get one object to animate (if there are options) from list of graphics to animate
		anim_graphic = [graphic for graphic in self.graphic_to_animate if graphic in self.tools.keys()]
			
		# If there is a graphic to animate, make that happen 
		if anim_graphic:
				
			if self.workspace.playbtn.text == 'Play':
				# Change button text when pressed and call animation function
				if self.check_answer():
					self.play_animation(anim_graphic[0])
					self.workspace.playbtn.text =  'Reset'
			else:
				# Change button text when pressed and call animation function
				self.reset_animation(anim_graphic[0])
				self.workspace.playbtn.text = 'Play'
			
		# No object to animate yet
		else:
			popup_text = FEEDBACK['animation']
			popup = TextPopup(popup_text, 'Something is not quite right!', (0.3, 0.5))
			popup.open()
			
	def add_tool(self, toolname, width, height):
		""" Adds tool selected by user to the workspace. """
		# Make sure unique tool id
		tool_id = toolname
		if toolname in self.tools:
			tool_id = toolname + '2'
		
		# Create correct graphics object for each tool
		if toolname in ['l_arrow', 'r_arrow', 'h_dim', 'v_dim']:
			widget_to_add = DynamicGraphicContainer(TOOL_INFO[toolname]['fname'], TOOL_INFO[toolname]['size'], id=tool_id)
		else:
			widget_to_add = StaticGraphicContainer(TOOL_INFO[toolname]['fname'], TOOL_INFO[toolname]['size'], id=tool_id)
		
		# Add graphics widget to the tools dictionary and then add to screen
		self.tools[tool_id] = widget_to_add
		self.add_widget(widget_to_add)
		
	def play_animation(self, anim_graphic_name):
		""" Animates object specified in graphic_to_animate. """
		
		# Stop and clear any other animations
		Animation.cancel_all(self)
		
		# Get object to be animated from the tools dictionary
		animation_object = self.tools[anim_graphic_name]
		
		# Get starting position of object that will be animated
		self.anim_pos_start = animation_object.x, animation_object.y
		x_pos, y_pos = self.anim_pos_start[0], self.anim_pos_start[1]
		
		# Get and specify animation settings
		anim_settings = PROB_INFO[self.q_num][anim_graphic_name]['animation']
		anim = Animation(duration=0.01)	 # Use this so can add new animations in loop
		for anim_setting in anim_settings:
			x_pos = x_pos+anim_setting['x']
			y_pos = y_pos+anim_setting['y']
			anim = anim + Animation(x=x_pos, y=y_pos, duration=anim_setting['t'])
			
		# Start animation
		anim.start(animation_object)

	def reset_animation(self, anim_graphic_name):
		""" Resets the animation for object specified in graphic_to_animate. """
		try:				
			# Get object to be animated from the tools dictionary
			animation_object = self.tools[anim_graphic_name]
			
			# Stop and clear any other animations
			Animation.cancel_all(self)
				
			# Reset graphic to animate back to its original position
			anim = Animation(x=self.anim_pos_start[0], 
							 y=self.anim_pos_start[1], 
							 duration=0.25)
			anim.start(animation_object)
				
		except KeyError:
			print('Nothing to animate yet. Place a {} first!'.format(self.graphic_to_animate))
		
	def check_answer(self):
		""" Checks that the proper tools have been added and the proper lengths specified. """
		
		# Get missing tools from the workspace, if any 
		required_tools = list(PROB_INFO[self.q_num].keys())
		required_tools.remove('q_info')
		missing = [tool for tool in required_tools if tool not in self.tools]
		
		# Remove missing tool if either amy or tina is accounted for (Prob 3)
		if 'tina' in missing and 'amy' in self.tools.keys():
			missing.remove('tina')
		if 'amy' in missing and 'tina' in self.tools.keys():
			missing.remove('amy')
		
		# Set whether answer is correct or not (for now based on if all tools accounted for)
		answer_correct = False if missing else True
		
		# Loop through missing tools and specify feedback types needed based on what is missing
		feedback_to_issue = []
		for tool in missing:
			if tool in ['h_dim', 'h_dim2', 'v_dim']:
				feedback_type = 'dimension'
			if tool in ['adele', 'beyonce', 'jay-z', 'taylor']:
				feedback_type = 'celebrity'
			if tool in ['road', 'lift', 'pile', 'hill']:
				feedback_type = 'component'
			
			# Keep list of feedback that needs to be issued
			if feedback_type not in feedback_to_issue:
				feedback_to_issue.append(feedback_type)
		
		# Check if correct dimenision values have been specified
		for name, tool in self.tools.items():
			
			# Only check values of dimension tools if they are the dimension tools required for the problem
			if name in ['h_dim', 'h_dim2', 'v_dim'] and name in PROB_INFO[self.q_num].keys():
				
				# Check for correct value
				if tool.textbox.text not in str(PROB_INFO[self.q_num][name]['value']):
					answer_correct = False
					
					# Keep list of feedback that needs to be issued
					if 'value' not in feedback_to_issue:
						feedback_to_issue.append('value')

		# Issue feedback via popups
		for feedback_type in feedback_to_issue:
			popup_text = FEEDBACK[feedback_type]
			popup = TextPopup(popup_text, 'Something is not quite right!', (0.3, 0.5))
			popup.open()
			
		return answer_correct
	
	def update_screen_callback(self, instance, value):
		""" Update property holding which screen should be shown next. """
		### THIS FUNCTION NOT CALLED WHEN SWITCHING BACK AND FORTH BETWEEN SCREENS ???
		self.update_screen = value
		print('Problem class\n', value)
		

class ClosingScreen(Screen):
	"""
	Class definition for the game's home screen. 
	The home screen displays the game's instructions.
	"""	
	# Create property to hold home welcome message
	greeting = StringProperty()
	
	# Property to store which screen should be shown next 
	update_screen = DictProperty()
	
	def __init__(self, **kwargs):
		super(HomeScreen, self).__init__(**kwargs)
		self.greeting = self.read_text('./questions/home.txt')
	
	def read_text(self, filename):
		""" Reads a file and returns the contents as a string. """
		with open(filename) as f:
			fileContents = f.read()
			return fileContents
	
	def yes_pressed(self):
		""" Function to deal with a 'yes' button being pressed. """
		# Launch a pop up and then advance to the next screen once the popup is closed
		popup = TextPopup(self.read_text('./questions/instruct_reminder.txt'), 'Quick Reminder', (0.4, 0.6))
		popup.open()
		popup.btn.bind(on_press=self.update_screen_callback)
	
	def no_pressed(self):
		""" Function to deal with a 'no' button being pressed. """
		# Close application
		App.get_running_app().stop()
	
	def update_screen_callback(self, *args):
		""" Function to set which screen should be shown next. """
		self.update_screen = {'name': 'prob1', 'direction': 'left'}

	
class ScreensApp(App):
	def build(self):
		Window.size = (1250, 800)
		#Window.fullscreen = True
		#return HomeScreen()
		return ProblemScreen(1)
		#return ProblemScreen(2)
		#return ProblemScreen(3)
if __name__ == '__main__':
	ScreensApp().run()
else:
	Builder.load_file('screens.kv')