uniform sampler2D sTextures[8];

varying vec2 vTexCoord;

void main() {
    // getting the screen coordinates (0,0) is the bottom left corner
    float x = gl_FragCoord.x - 0.5;
    float y = gl_FragCoord.y - 0.5;
    
    // The view indices for the current pixel
    float Ri = mod(3.0 * x + y + 7.0, 8.0);
    float Gi = mod(3.0 * x + y + 8.0, 8.0);
    float Bi = mod(3.0 * x + y + 9.0, 8.0);

    // init pixel colors to black
    float r = 0.0;
    float g = 0.0;
    float b = 0.0;

    // VIEW 0
    if(Ri == 0.0) {
        r = texture2D(sTextures[0], vTexCoord).r;
        g = texture2D(sTextures[1], vTexCoord).g;
        b = texture2D(sTextures[2], vTexCoord).b;
    }

    if(Ri == 1.0) {
        r = texture2D(sTextures[1], vTexCoord).r;
        g = texture2D(sTextures[2], vTexCoord).g;
        b = texture2D(sTextures[3], vTexCoord).b;
    }

    if(Ri == 2.0) {
        r = texture2D(sTextures[2], vTexCoord).r;
        g = texture2D(sTextures[3], vTexCoord).g;
        b = texture2D(sTextures[4], vTexCoord).b;
    }

    if(Ri == 3.0) {
        r = texture2D(sTextures[3], vTexCoord).r;
        g = texture2D(sTextures[4], vTexCoord).g;
        b = texture2D(sTextures[5], vTexCoord).b;
    }

    if(Ri == 4.0) {
        r = texture2D(sTextures[4], vTexCoord).r;
        g = texture2D(sTextures[5], vTexCoord).g;
        b = texture2D(sTextures[6], vTexCoord).b;
    }

    if(Ri == 5.0) {
        r = texture2D(sTextures[5], vTexCoord).r;
        g = texture2D(sTextures[6], vTexCoord).g;
        b = texture2D(sTextures[7], vTexCoord).b;
    }

    if(Ri == 6.0) {
        r = texture2D(sTextures[6], vTexCoord).r;
        g = texture2D(sTextures[7], vTexCoord).g;
        b = texture2D(sTextures[0], vTexCoord).b;
    }

    if(Ri == 7.0) {
        r = texture2D(sTextures[7], vTexCoord).r;
        g = texture2D(sTextures[0], vTexCoord).g;
        b = texture2D(sTextures[1], vTexCoord).b;
    }

    gl_FragColor = vec4(r, g, b, 1.0);
}