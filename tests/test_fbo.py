#!/usr/bin/env python
from __future__ import division
from OpenGL.GL import *
import numpy as np
import math
import pygame
from pygame.math import Vector3


#local imports
from geometry import *

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
	rect = Rectangle('rect')
	rect2 = Rectangle('rect2')
	rect_flip = Rectangle('rect_flip', True)

	#create matrices
	perspective_mx = perspective(45, width/height, 0.1, 100)
	model_matrix = np.identity(4, dtype=np.float32)
	ortho_mx = ortho(-1, 1, 1, -1, -50, 50)
	ident_matrix = np.identity(4, dtype=np.float32)

	eyeTarget = Vector3(0, 0, 0)

	right_eye = Vector3(-1, 0, 10)
	right_view_matrix = lookat(right_eye, eyeTarget)

	left_eye = Vector3(1, 0, 10)
	left_view_matrix = lookat(left_eye, eyeTarget)


	prog1 = Program(vs_tx, fs_tx)
	sTexture = prog1.getUniformLocation("sTexture")
	texture = Texture("res/Galaxy.jpg")

	prog2 = Program(vs_tx, fs_flat)

	prog3 = Program(vs_tx, fs_flat)

	fbo_width = int(width/2)
	fbo_height = int(height/2)
	
	#create fbo object
	fbo1 = FrameBuffer(fbo_width, fbo_height)

	running = True
	while running:
		fbo1.bind()
		glViewport(0, 0, fbo_width, fbo_height)


		glClearColor(0.0, 0.0, 1.0, 1.0);
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_BLEND)

		### Position des plans dans l'espace ###

		mv_matrix = translate(0, 0, -4).dot(scale(2*width/height, 2, 1)).dot(model_matrix).dot(right_view_matrix)
		prog1.use(perspective_mx, mv_matrix)
		prog1.setTexture("sTexture", texture)
		rect_flip.draw(prog1.program)

		mv_matrix = translate(0, 0, -2).dot(model_matrix).dot(right_view_matrix)
		prog2.use(perspective_mx, mv_matrix)
		prog2.setVector4("color", 1.0, 0.0, 0.0, 1.0)
		rect.draw(prog2.program)

		mv_matrix = translate(1, 1, -3).dot(model_matrix).dot(right_view_matrix)
		prog3.use(perspective_mx, mv_matrix)
		prog3.setVector4("color", 1.0, 1.0, 0.0, 1.0)
		rect2.draw(prog3.program)

		mv_matrix = translate(0, 0, -6).dot(model_matrix).dot(right_view_matrix)



		glUseProgram(0)
		#render to main video output
		glBindFramebuffer(GL_FRAMEBUFFER, 0)
		glDisable(GL_DEPTH_TEST)
		glDisable(GL_BLEND)

		glClearColor(0.0, 0.0, 0.0, 1.0)
		glViewport(0, 0, width, height)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

		prog1.use(ortho_mx, ident_matrix)
		fbo1.bind_texture(sTexture, 0)
		rect_flip.draw(prog1.program)


		pygame.display.flip()

		events = pygame.event.get()
		if len(events):
			for event in events:
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.MOUSEMOTION:
					x, y = event.rel
					if any(event.buttons):
						model_matrix = model_matrix.dot(rotate(y, -1, 0, 0)).dot(rotate(x, 0, -1, 0))
