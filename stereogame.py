from OpenGL.GL import *
import numpy as np
import pygame
from pygame.math import Vector3

#local imports
from feather import Texture, FrameBuffer, Scene
from feather.shapes import Rectangle, Cube
from feather.material import ColorMaterial, TextureMaterial
from feather.camera import *
from interlacer import Interlacer

if __name__ == "__main__":
	#width, height = 1920, 1080
	pygame.init()
	infoObject = pygame.display.Info()
	pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.DOUBLEBUF|pygame.OPENGL|pygame.HWSURFACE, 0)
	#pygame.display.set_mode((width, height), pygame.DOUBLEBUF|pygame.OPENGL|pygame.HWSURFACE, 0)
	#pygame.display.toggle_fullscreen()

	scene = Scene()
	
	######## DECLARATION DES SHAPES
	
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

	screen = Rectangle('screen', True)

	######### MATRICES UTILES

	perspective_mx = perspective(45, width / height, 0.1, 100)
	model_matrix = np.identity(4, dtype=np.float32)
	ortho_mx = ortho(-1, 1, 1, -1, -50, 50)
	ident_matrix = np.identity(4, dtype=np.float32)

	######### DECLARATION DES JOUEURS

	eyeTarget = Vector3(0, 0, 0)

	eye_distance = 0.008

	eye = Vector3(-eye_distance / 2, 0, 5)
	view_matrix = lookat(eye, eyeTarget)

	fbo_width = int(width/2)
	fbo_height = int(height/2)
	
	fbo = FrameBuffer(fbo_width, fbo_height)

	######### DECLARATION DE L'ENTRELACEUR

	interlacer = Interlacer()

	time = 0.0
	x,z = 0.0, 0.0
	circleRadius = 1.7

	######### GAME LOOP

	running = True
	while running:
		time += 0.01

		###### UPDATE ETAT DES SHAPES
		
		yellow_cube.setRotationY(45.0 + time * 50.0)
		yellow_cube.setRotationX(60.0 * time)

		rotationSpeed = 1
		x = math.cos(time * rotationSpeed) * circleRadius
		z = math.sin(time * rotationSpeed) * circleRadius

		yellow_cube.setPosition(x, 0, z)

		###### DESSIN DES SHAPES SUR FRAMEBUFFER

		fbo.bind()
		glViewport(0, 0, fbo_width, fbo_height)

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