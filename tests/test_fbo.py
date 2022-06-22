#!/usr/bin/env python
from __future__ import division
from OpenGL.GL import *
import numpy as np
import math
import pygame


#local imports
from geometry import *

vs_tx = textwrap.dedent("""\
    uniform mat4 uMVMatrix;
    uniform mat4 uPMatrix;
       
    attribute vec3 aVertex;
    attribute vec2 aTexCoord;
    
    varying vec2 vTexCoord;
    
    void main(){
       vTexCoord = aTexCoord;
       gl_Position = (uPMatrix * uMVMatrix)  * vec4(aVertex, 1.0);
    }
    """)

fs_tx = textwrap.dedent("""\
    uniform sampler2D sTexture;

    varying vec2 vTexCoord;

    void main() {
	   gl_FragColor = texture2D(sTexture, vTexCoord);
    }
    """)

fs_flat = textwrap.dedent("""\
	uniform vec4 col;
    void main() {
       gl_FragColor = col;
    }
    """)

if __name__ == "__main__":
	width, height = 1920, 1080
	pygame.init()
	pygame.display.set_mode((width, height), pygame.DOUBLEBUF|pygame.OPENGL|pygame.HWSURFACE, 0)
	rect = Rectangle('rect')
	rect_flip = Rectangle('rect_flip', True)

	#create matrices
	perspective_mx = perspective(45, width/height, 0.1, 100)
	model_matrix = np.identity(4, dtype=np.float32)
	ortho_mx = ortho(-1, 1, 1, -1, -50, 50)
	ident_matrix = np.identity(4, dtype=np.float32)

	eye = pygame.math.Vector3(0, 0, 10)
	center = pygame.math.Vector3(0, 0, 0)
	view_matrix = lookat(eye, center)


	prog1 = Program(vs_tx, fs_tx)
	sTexture = prog1.getUniformLocation("sTexture")
	texture = Texture("res/Galaxy.jpg")

	prog2 = Program(vs_tx, fs_flat)
	uCol = prog2.getUniformLocation("col")


	fbo_width = int(width/2)
	fbo_height = int(height/2)
	#create fbo object
	fbo = FrameBuffer(fbo_width, fbo_height)

	running = True
	while running:
		eyemx = view_matrix
		fbo.bind()
		glViewport(0, 0, fbo_width, fbo_height)


		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_BLEND)

		mv_matrix = translate(0, 0, -4).dot(scale(2*width/height, 2, 1)).dot(model_matrix).dot(eyemx)
		prog1.use(perspective_mx, mv_matrix)
		texture.activate(sTexture)
		rect_flip.draw(prog2.program)

		mv_matrix = translate(0, 0, -2).dot(model_matrix).dot(eyemx)
		prog2.use(perspective_mx, mv_matrix)
		glUniform4f(uCol, 1, 0, 0, 1)
		rect.draw(prog2.program)


		glUseProgram(0)
		#render to main video output
		glBindFramebuffer(GL_FRAMEBUFFER, 0)
		glDisable(GL_DEPTH_TEST)
		glDisable(GL_BLEND)

		glViewport(0, 0, width, height)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		prog1.use(ortho_mx, ident_matrix)
		fbo.bind_texture(sTexture, 0)
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
