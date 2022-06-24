from OpenGL.GL import *
import numpy as np
import pygame
from pygame.math import Vector3

#local imports
from feather import Texture, FrameBuffer, Scene, Screen
from feather.shapes import Rectangle, Cube, Sphere
from feather.materials import ColorMaterial, TextureMaterial
from feather.projections import *
from feather.algebra import *
from feather.camera import *
from feather.shapes.sphere import Sphere
from interlacer import Interlacer

from game import Player, Battlefield

if __name__ == "__main__":
	pygame.init()
	#width, height = 1920, 1080
	infoObject = pygame.display.Info()
	width, height = infoObject.current_w, infoObject.current_h
	pygame.display.set_mode((width, height), pygame.DOUBLEBUF|pygame.OPENGL|pygame.HWSURFACE, 0)
	#pygame.display.toggle_fullscreen()

	scene = Scene()
	
	######## DECLARATION DES SHAPES

	sphere = Sphere("sphery", False, scene)
	sphere.setScaling(0.3, 0.3, 0.3)
	sphereMat = TextureMaterial(Texture("./assets/tennis.png"))
	sphere.setMaterial(sphereMat)

	battlefield = Battlefield("battly", 7, 7, 7, scene)
	battleMat = TextureMaterial(Texture("./assets/textBattle.jpeg"))
	battlefield.setMaterial(battleMat)

	#gun = OBJsanstex("./assets/awp.obj", False, scene)
	
	rect = Rectangle('rect', False, scene)
	rect.setPosition(-6, -3, 0)
	rect.setScaling(0.5, 0.5, 1)

	rectMat = ColorMaterial(1.0, 0.0, 0.0)
	rect.setMaterial(rectMat)

	yellow_cube = Cube('yellow_cube', True, scene)
	yellow_cube.setScaling(0.5, 0.5, 0.5)
	yellow_cube.setRotationY(45)
	
	cubeMat = ColorMaterial(1.0, 1.0, 0.0)
	yellow_cube.setMaterial(cubeMat)

	galaxy_rect = Rectangle('galaxy_rect', True, scene)
	galaxy_rect.setPosition(0, 0, -6)
	galaxy_rect.setScaling(8 * width / height, 8, 1)

	galaxyMat = TextureMaterial(Texture("./assets/Galaxy.jpg"))
	galaxy_rect.setMaterial(galaxyMat)
	
	######### DECLARATION DE L'ECRAN

	screen = Screen('screen')

	######### MATRICES UTILES

	perspective_mx = perspective(45, width / height, 0.1, 100)
	model_matrix = np.identity(4, dtype=np.float32)
	ortho_mx = ortho(-1, 1, 1, -1, -50, 50)
	ident_matrix = np.identity(4, dtype=np.float32)

	######### DECLARATION DES JOUEURS

	eye_distance = 0.008
	position1 = Vector3(-5, 0, 0)
	position2 = Vector3(5, 0, 0)
	perspective_mx1 = perspective(45, width / height, 0.1, 100).dot(rotate(270 ,0 ,1 ,0))
	perspective_mx2 = perspective(45, width / height, 0.1, 100).dot(rotate(90, 0, 1, 0))
	
	player1 = Player(position1, perspective_mx1, None, position2)
	player2 = Player(position2, perspective_mx2, None, position1)
	
	
	'''eyeTarget = Vector3(0, 0, 0)
	# perspective_mx : 45 = abgleVision


	eye = Vector3(-eye_distance / 2, 0, 5)
	view_matrix = lookat(eye, eyeTarget)'''

	fbo_width = int(width/2)
	fbo_height = int(height/2)
	
	#fbo = FrameBuffer(fbo_width, fbo_height)

	######### DECLARATION DE L'ENTRELACEUR

	interlacer = Interlacer()

	######### DECLARATION DES VARIABLES DE LA BOUCLE

	getTicksLastFrame = 0.0
	x,z = 0.0, 0.0
	circleRadius = 1.7

	######### GAME LOOP

	running = True
	while running:
		time = pygame.time.get_ticks() / 1000.0
		deltaTime = time - getTicksLastFrame
		getTicksLastFrame = time

		###### UPDATE ETAT DES SHAPES
		
		yellow_cube.setRotationY(45.0 + time * 70.0)
		yellow_cube.setRotationX(80.0 * time)

		rotationSpeed = 1
		x = math.cos(time * rotationSpeed) * circleRadius
		z = math.sin(time * rotationSpeed) * circleRadius

		yellow_cube.setPosition(x, 0, z)

		###### DESSIN DES SHAPES SUR FRAMEBUFFER

		fbo = player1.getOeilGauche().getFrameBuffer()
		fbo.bind()
		glViewport(0, 0, fbo_width, fbo_height)

		view_matrix = lookat(player1.getOeilGauche().getPosition(), player1.getEye_Target())
		scene.render(perspective_mx, model_matrix, view_matrix)

		###### DESSIN DES FRAMEBUFFER SUR L'ECRAN

		glUseProgram(0)
		#render to main video output
		glBindFramebuffer(GL_FRAMEBUFFER, 0)
		glDisable(GL_DEPTH_TEST)
		glDisable(GL_BLEND)

		glClearColor(0.0, 0.0, 0.0, 1.0)
		glViewport(0, 0, width, height)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

		###### ENTRELACEMENT DES FRAMEBUFFERS
		interlacer.use(ortho_mx, ident_matrix)

		interlacer.setTextureFromFBO(fbo, 0)
		interlacer.setTextureFromFBO(fbo, 1)
		interlacer.setTextureFromFBO(fbo, 2)
		interlacer.setTextureFromFBO(fbo, 3)
		interlacer.setTextureFromFBO(fbo, 4)
		interlacer.setTextureFromFBO(fbo, 5)
		interlacer.setTextureFromFBO(fbo, 6)
		interlacer.setTextureFromFBO(fbo, 7)

		screen.draw(interlacer.program)

		pygame.display.flip() # why do we need that tho ?

		####### GESTION DES ENTREES CLAVIER

		keys = pygame.key.get_pressed()
		if keys[pygame.K_z]:
			circleRadius += 0.05
		if keys[pygame.K_s]:
			circleRadius -= 0.05

		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEMOTION:
				x, y = event.rel
				if any(event.buttons):
					model_matrix = model_matrix.dot(rotate(y, -1, 0, 0)).dot(rotate(x, 0, -1, 0))