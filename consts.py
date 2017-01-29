from kivy.utils import get_color_from_hex

# Color pallette
COLORS = {'white': {'hex': '#FFFFFF' , 'rgba': get_color_from_hex('FFFFFF')},
		  'gray': {'hex': 'E8E8E8', 'rgba': get_color_from_hex('E8E8E8')},
		  'dgray': {'hex': 'D5D5D5', 'rgba': get_color_from_hex('D5D5D5')},
		  'blue': {'hex': '5087CB', 'rgba': get_color_from_hex('5087CB')},
		  'dblue': {'hex': '3A5278', 'rgba': get_color_from_hex('3A5278')},
		  'pink': {'hex': 'FF7687', 'rgba': get_color_from_hex('FF7687')}}
		
# Font pallette
FONTS = {'open_sans': {'regular': './fonts/OpenSans-Regular.ttf',
						'semibold': './fonts/OpenSans-Semibold.ttf',
						'bold': './fonts/OpenSans-Bold.ttf'},
		 'arial': 	   {'regular': './fonts/Arial.ttf',
						'bold': './fonts/Arial Bold.ttf'}}
		

# Dictionary providing graphic's filename and size for each tool
TOOL_INFO = {'l_arrow':	{'fname': './graphics/l_arrow.png', 'size': (0.6, 0.1)},
			 'r_arrow':	{'fname': './graphics/r_arrow.png', 'size': (0.6, 0.1)},
	  		 'h_dim':	{'fname': './graphics/h_dim.png', 'size': (0.6, 0.1)},
			 'v_dim':	{'fname': './graphics/v_dim.png', 'size': (0.1, 0.6)},
			 'road': 	{'fname': './graphics/road.png', 'size': (0.75, 0.1)},
			 'lift':	{'fname': './graphics/lift.png', 'size': (0.18, 0.25)},
  	  		 'pile':	{'fname': './graphics/pile.png', 'size': (0.15, 0.17)},
			 'hill':	{'fname': './graphics/hill.png', 'size': (0.5, 0.4)},
			 'adele':   {'fname': './graphics/adele.png', 'size': (0.11, 0.21)},
	  		 'amy':		{'fname': './graphics/sled_amy.png', 'size': (0.15, 0.3)},
			 'beyonce':	{'fname': './graphics/car_bey.png', 'size': (0.17, 0.16)},
			 'jay-z':	{'fname': './graphics/jay-z.png', 'size': (0.15, 0.25)},
			 'taylor':	{'fname': './graphics/taylor.png', 'size': (0.15, 0.25)},
			 'tina':   	{'fname': './graphics/sled_tina.png', 'size': (0.15, 0.3)}}
			
# Dictionary providing path to tool button image
TOOL_BUTTON_INFO = {'l_arrow': './graphics/buttons/l_arrow.png',
			 		'r_arrow':	'./graphics/buttons/r_arrow.png', 
	  		 		'h_dim':	'./graphics/buttons/h_dim.png', 
			 		'v_dim':	'./graphics/buttons/v_dim.png',
			 		'road': 	'./graphics/buttons/road.png',
			 		'lift':		'./graphics/buttons/lift.png',
  	  		 		'pile':		'./graphics/buttons/pile.png',
			 		'hill':		'./graphics/buttons/hill.png',
			 		'adele':    './graphics/buttons/adele.png',
	  		 		'amy':		'./graphics/buttons/amy.png',
			 		'beyonce':	'./graphics/buttons/beyonce.png',
			 		'jay-z':	'./graphics/buttons/jay-z.png',
			 		'taylor':	'./graphics/buttons/taylor.png',
			 		'tina':   	'./graphics/buttons/tina.png'}

# List of dictionaries for each problem
# Provide what tools should be used and specify any settings they should have
PROB_INFO = \
	[{},
	 # Problem 1
	 {
	  'q_info': 	{'topic': 'Question 1 - 1D Motion', 'fname': './questions/question1.txt'},
	  'road': 		{},
	  'beyonce':	{'animation': [{'x': 500, 'y': 0, 't': 2}, {'x': -100, 'y': 0, 't': 0.5}]},
	  'jay-z':		{},
	  'taylor':		{},
	  'h_dim':		{'value': [15, 70]},
	  'h_dim2':		{'value': [15, 70]}
	 },
	
	 # Problem 2
	 {
	  'q_info': 	{'topic': 'Question 2 - 2D Motion (Projectiles)', 'fname': './questions/question2.txt'},
	  'lift':		{},
  	  'adele':   	{'animation': [{'x': 300, 'y': -170, 't': 1.5}]},
  	  'pile':		{},
  	  'h_dim':		{'value': [40]},
  	  'v_dim':		{'value': [24]}
	 },
	 
	 # Problem 3
	 {
	  'q_info': 	{'topic': 'Question 3 - Forces and Energy', 'fname': './questions/question3.txt'},
	  'hill':		{},
	  'tina':   	{'animation': [{'x': -425, 'y': -150, 't': 1.5}]},
	  'amy':		{'animation': [{'x': -425, 'y': -150, 't': 1.5}]},
	  'h_dim':		{'value': [48]},
	  'v_dim':		{'value': [35]}
	 }]


# Dictionary of feedback that can be issued to guide the user
FEEDBACK = {'animation': "Hmm... I need a celebrity to move. Make sure you have the correct one. \n\n#CelebritiesDoPhysics!",
			'dimension': "You should use dimension lines to express lengths, widths, and heights. \n\n#RulersAreCool",
			'celebrity': "Make sure all celebrities are accounted for. We wouldn't want them getting lost. \n\n#CelebrityProblems",
			'component': "You are missing a key component... maybe a road, a hill, a ski-lift, or pile of snow. \n\n#BoringWithoutIt",
			'value': "You've drawn the dimension lines, but the values don't look quite right. \n\n#MistakesAreStillProgress #ChanceToMakeItBetter"}


if __name__ == '__main__':
	for name, dictionary in PROB_INFO[1].items():
		if 'animation' in dictionary.keys():
			anim_object = name
	print(anim_object)
	print(TOOL_INFO['hill']['size'])
	print(COLORS['dgray']['rgba'][0]*255)
	