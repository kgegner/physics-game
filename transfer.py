from random import random

from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.properties import ListProperty, NumericProperty, ObjectProperty, StringProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SlideTransition
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import DragBehavior
from kivy.core.window import Window

from screens import *
from graphic import *

"""
Original author: Kathleen Gegner
Last modified by: Kathleen Gegner
Last modified on: 12/8/16

Animations and celebrities by: Zack Tucker, http://zacktucker.me/
Interface and tool design by: Aileen (Qiualin) Bai, http://www.aileenbai.com/
"""

class MyScreenManager(ScreenManager):
	
	def __init__(self, **kwargs):
		super(MyScreenManager, self).__init__(**kwargs)
		homeScreen = HomeScreen()
		prob1screen = ProblemScreen(1, name = 'prob1')
		prob2screen = ProblemScreen(2, name = 'prob2')
		prob3screen = ProblemScreen(3, name = 'prob3')
		self.add_widget(homeScreen)
		self.add_widget(prob1screen)
		self.add_widget(prob2screen)
		self.add_widget(prob3screen)
		homeScreen.bind(update_screen=self.update_screen_callback)
		prob1screen.bind(update_screen=self.update_screen_callback)
		prob2screen.bind(update_screen=self.update_screen_callback)
		prob3screen.bind(update_screen=self.update_screen_callback)
		
	def update_screen_callback(self, instance, value):
		""" Update the current screen being displayed. """
		self.transition = SlideTransition(direction=value['direction'])
		self.current = value['name']
		

class TransferApp(App):
	def build(self):
		Window.clearcolor = (1,1,1,1)
		Window.size = (1250, 800)
		return MyScreenManager()

if __name__ == '__main__':
	TransferApp().run()