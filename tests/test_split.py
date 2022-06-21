#!/usr/bin/env python
from __future__ import division
from OpenGL.GL import *
import numpy as np
import math
import pygame


#local imports
from geometry import *

with open('./shaders/interlaceVertex.glsl', 'r') as file:
    vs_dual_tx = file.read()

with open('./shaders/interlaceFragment.glsl', 'r') as file:
    fs_dual_tx = file.read()


if __name__ == "__main__":
	width, height = 1920, 1080
	pygame.init()
	pygame.display.set_mode((width, height), pygame.DOUBLEBUF|pygame.OPENGL|pygame.HWSURFACE, 0)
	pygame.display.toggle_fullscreen()

	rect = Rectangle('rect')
	rect_flip = Rectangle('rect_flip', True)

	#create matrices
	ortho_mx = ortho(-1, 1, 1, -1, -50, 50)
	ident_matrix = np.identity(4, dtype=np.float32)

	prog1 = Program(vs_dual_tx, fs_dual_tx)

	textures = [
		Texture("res/planet/planet_droite.png"),
		Texture("res/planet/planet_gauche.png"),
		Texture("res/black.jpg"),
		Texture("res/black.jpg"),
		Texture("res/black.jpg"),
		Texture("res/black.jpg"),
		Texture("res/black.jpg"),
		Texture("res/black.jpg"),
	]

	sTextures = [prog1.getUniformLocation(f"sTextures[{i}]") for i in range(8)]

	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

	glViewport(0, 0, width, height)

	running = True
	while running:

		#draw final view interleave, draw full-screen quad with all our textures
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		prog1.use(ortho_mx, ident_matrix)

		for i, texture in enumerate(textures):
			texture.activate(sTextures[i], i)

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

