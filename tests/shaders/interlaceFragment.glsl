uniform sampler2D sTexture1;
uniform sampler2D sTexture2;

varying vec2 vTexCoord;

void main() {
    int x = gl_FragCoord.x;
    int y = gl_FragCoord.y;

    // interlace r g b in each pixel

    if (int( mod(x, 2.0) ) == 1) {
        gl_FragColor = texture2D(sTexture1, vTexCoord);
    } else {
        gl_FragColor = texture2D(sTexture2, vTexCoord);
    }
}