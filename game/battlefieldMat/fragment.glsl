varying vec2 vTexCoord;

uniform float scaleX;
uniform float scaleY;
uniform float scaleZ;

uniform sampler2D battlefieldTexture;

void main() {
    vec3 color = texture2D(battlefieldTexture, vTexCoord).rgb;
    gl_FragColor = vec4(color, 1.0);
}