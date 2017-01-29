# Transfer Game - Graphics Class

# Author: Kathleen Gegner
# Update: 12/5/16

# File name: graphic.py

from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import DragBehavior
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.lang import Builder
from kivy.app import App


class DynamicGraphicContainer(DragBehavior, FloatLayout):	
	'''
	Class definition for graphic container widget. 
	Container composed of image and user input box.
	User input changes width of image by entering a 
	number between 0 and 100.
	'''
	
	# Create properties to store image dimensions and filename
	img_fname = StringProperty()
	img_width = NumericProperty(1)
	img_height = NumericProperty(1)
	
	# Create property to keep track of when the graphic container (tool) is selected
	#tool_selected = ObjectProperty()
	
	def __init__(self, fname, size, **kwargs):
		super(DynamicGraphicContainer, self).__init__(**kwargs)
		self.img_fname = fname
		self.size_hint = size
			
	def change_graphic_size(self):
		try:
			# If value entered in text box, update image's length
			if self.textbox.text  != '':
				if self.img_fname.split('/')[-1].split('.')[0].startswith('v'):
					# Scale height (scale by 100, so user can enter non-decimal number)
					self.img_height = float(self.textbox.text) / 100.
				else:
					# Change width (scale by 100, so user can enter non-decimal number)
					self.img_width = float(self.textbox.text) / 100.
			self.img.size_hint = (self.img_width, self.img_height)
		except ValueError:
			print('Invalid number entered.')
			
class StaticGraphicContainer(DragBehavior, FloatLayout):	
	'''
	Class definition for graphic container widget. 
	Container composed of image and user input box.
	User input changes width of image by entering a 
	number between 0 and 100.
	'''
	
	# Create properties to store image dimensions and filename
	img_fname = StringProperty()
	img_width = NumericProperty(1)
	img_height = NumericProperty(1)
	
	# Create property to keep track of when the graphic container (tool) is selected
	#tool_selected = ObjectProperty()
	
	def __init__(self, fname, size, **kwargs):
		super(StaticGraphicContainer, self).__init__(**kwargs)
		self.img_fname = fname
		self.size_hint = size
			
	
class GraphicApp(App):
	def build(self):
		return StaticGraphicContainer('./graphics/beyonce.png', (0.3, 0.3))
		#return StaticGraphicContainer('./graphics/animations/bey.gif', (0.3, 0.3))
		#return GraphicContainer('./graphics/California Coast.jpg', 0.3, 0.3)
		#return RoadContainer(0.5,0.1)
		
if __name__ == '__main__':
	GraphicApp().run()
else:
	Builder.load_file('graphic.kv')