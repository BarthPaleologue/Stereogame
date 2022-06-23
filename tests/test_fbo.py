#!/usr/bin/env python
from __future__ import division
from OpenGL.GL import *
import numpy as np
import pygame
from pygame.math import Vector3

#local imports
from geometry import *
from interlacer import Interlacer

with open('./shaders/fbo/fboVertex.glsl', 'r') as file:
    vs_tx = file.read()

with open('./shaders/fbo/fboFragment.glsl', 'r') as file:
    fs_tx = file.read()

with open('./shaders/fbo/flatFragment.glsl', 'r') as file:
    fs_flat = file.read()

if __name__ == "__main__":
	width, height = 1920, 1080
	pygame.init()
	pygame.display.set_mode((width, height), pygame.DOUBLEBUF|pygame.OPENGL|pygame.HWSURFACE, 0)
	pygame.display.toggle_fullscreen()
	
	# shapes
	rect = Rectangle('rect')
	rect.setPosition(-6, -3, 0)
	rect.setScaling(0.5, 0.5, 1)

	yellow_rect = Cube('yellow_rect')
	yellow_rect.setPosition(1, 1, -3)
	yellow_rect.setRotationY(45)

	galaxy_rect = Rectangle('galaxy_rect', True)
	galaxy_rect.setPosition(0, 0, -6)
	galaxy_rect.setScaling(8 * width / height, 8, 1)
	
	# screen
	screen = Rectangle('screen', True)

	#create matrices
	perspective_mx = perspective(45, width / height, 0.1, 100)
	model_matrix = np.identity(4, dtype=np.float32)
	ortho_mx = ortho(-1, 1, 1, -1, -50, 50)
	ident_matrix = np.identity(4, dtype=np.float32)

	eyeTarget = Vector3(0, 0, 0)

	eye_distance = 0.008

	right_eye = Vector3(-eye_distance / 2, 0, 5)
	right_view_matrix = lookat(right_eye, eyeTarget)

	left_eye = Vector3(eye_distance / 2, 0, 5)
	left_view_matrix = lookat(left_eye, eyeTarget)


	prog1 = Program(vs_tx, fs_tx)
	texture = Texture("res/Galaxy.jpg")

	prog2 = Program(vs_tx, fs_flat)

	prog3 = Program(vs_tx, fs_flat)

	interlacer = Interlacer()

	blackTex = Texture("res/black.jpg")

	fbo_width = int(width/2)
	fbo_height = int(height/2)
	
	#create fbo object
	fbo_right = FrameBuffer(fbo_width, fbo_height)
	fbo_left = FrameBuffer(fbo_width, fbo_height)

	fbos = [fbo_right, fbo_left]
	view_matrices = [right_view_matrix, left_view_matrix]
	
	def up_eye_distance(eye_distance) :
		eye_distance += 0.001
		print('UP')
		print(eye_distance)
		return eye_distance
	def down_eye_distance(eye_distance) :
		eye_distance -= 0.001
		print('DOWN')
		print(eye_distance)
		return eye_distance

	def renderView(view_matrix, index):
		glViewport(0, 0, fbo_width, fbo_height)

		glClearColor(0.0, 0.0, 0.2, 1.0)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_BLEND)

		### Position des plans dans l'espace ###

		general_mv_matrix = model_matrix.dot(view_matrix)

		mv_matrix = galaxy_rect.getMatrix().dot(general_mv_matrix)
		prog1.use(perspective_mx, mv_matrix)
		prog1.setTexture("sTexture", texture)
		galaxy_rect.draw(prog1.program)

		mv_matrix = rect.getMatrix().dot(general_mv_matrix)
		prog2.use(perspective_mx, mv_matrix)
		
		if index == 0 or index == 1:
			prog2.setVector4("color", 1.0, 0.0, 0.0, 1.0)
		elif index == 4 or index == 5:
			prog2.setVector4("color", 0.0, 1.0, 0.0, 1.0)
		else:
			prog2.setVector4("color", 0.0, 0.0, 1.0, 1.0)
		
		rect.draw(prog2.program)

		mv_matrix = yellow_rect.getMatrix().dot(general_mv_matrix)
		prog3.use(perspective_mx, mv_matrix)
		prog3.setVector4("color", 1.0, 1.0, 0.0, 1.0)
		yellow_rect.draw(prog3.program)

	time = 0.0
	x,z = 0.0, 0.0
	circleRadius = 2

	running = True
	while running:
		time += 0.01
		
		
		yellow_rect.setRotationY(45.0 + time * 50.0)

		rotationSpeed = 1
		x = math.cos(time * rotationSpeed) * circleRadius
		z = math.sin(time * rotationSpeed) * circleRadius

		yellow_rect.setPosition(x, 0, z)

		for i in range(2):
			fbos[i].bind()
			renderView(view_matrices[i], i)

		glUseProgram(0)
		#render to main video output
		glBindFramebuffer(GL_FRAMEBUFFER, 0)
		glDisable(GL_DEPTH_TEST)
		glDisable(GL_BLEND)

		glClearColor(0.0, 0.0, 0.0, 1.0)
		glViewport(0, 0, width, height)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

		### drawing on screen
		interlacer.use(ortho_mx, ident_matrix)

		interlacer.setTextureFromFBO(fbo_right, 1)
		interlacer.setTextureFromFBO(fbo_left, 0)
		interlacer.setTextureFromImage(blackTex, 2)
		interlacer.setTextureFromImage(blackTex, 3)
		interlacer.setTextureFromImage(blackTex, 4)
		interlacer.setTextureFromImage(blackTex, 5)
		interlacer.setTextureFromImage(blackTex, 6)
		interlacer.setTextureFromImage(blackTex, 7)

		screen.draw(interlacer.program)

		pygame.display.flip()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_z]:
			circleRadius += 0.05
		if keys[pygame.K_s]:
			circleRadius -= 0.05
		if keys[pygame.K_UP]:
			eye_distance = up_eye_distance(eye_distance)
		if keys[pygame.K_DOWN] :
			eye_distance = down_eye_distance(eye_distance)
		view_matrices = [lookat(Vector3(-eye_distance / 2, 0, 5), eyeTarget), lookat(Vector3(eye_distance / 2, 0, 5), eyeTarget)]
		

		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEMOTION:
				x, y = event.rel
				if any(event.buttons):
					model_matrix = model_matrix.dot(rotate(y, -1, 0, 0)).dot(rotate(x, 0, -1, 0))