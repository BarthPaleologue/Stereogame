precision highp float;

uniform sampler2D sTextures[8];

varying vec2 vTexCoord;

void main() {
    // getting the screen coordinates (0,0) is the bottom left corner
    int x = int(gl_FragCoord.x - 0.5);
    int y = int(gl_FragCoord.y - 0.5);

    // The view indices for the current pixel
    int Ri = mod(3 * x + y + 7, 8.0);
    int Gi = mod(3 * x + y + 8, 8.0);
    int Bi = mod(3 * x + y + 9, 8.0);

    // setting colors according to the view indices
    //float r = texture2D(sTextures[Ri], vTexCoord).r;
    //float g = texture2D(sTextures[Gi], vTexCoord).g;
    //float b = texture2D(sTextures[Bi], vTexCoord).b;
    
    // init pixel colors to black
    float r = 0.0;
    float g = 0.0;
    float b = 0.0;

    // VIEW 0
    if(Ri == 0) {
        r = texture2D(sTextures[0], vTexCoord).r;
    }
    if(Gi == 0) {
        g = texture2D(sTextures[0], vTexCoord).g;
    }
    if(Bi == 0) {
        b = texture2D(sTextures[0], vTexCoord).b;
    }

    // VIEW 1
    if(Ri == 1) {
        r = texture2D(sTextures[1], vTexCoord).r;
    }
    if(Gi == 1) {
        g = texture2D(sTextures[1], vTexCoord).g;
    }
    if(Bi == 1) {
        b = texture2D(sTextures[1], vTexCoord).b;
    }

    // VIEW 2
    if(Ri == 2) {
        r = 0.0;
    }
    if(Gi == 2) {
        g = 0.0;
    }
    if(Bi == 2) {
        b = 0.0;
    }

    // VIEW 3
    if(Ri == 3) {
        r = 0.0;
    }
    if(Gi == 3) {
        g = 0.0;
    }
    if(Bi == 3) {
        b = 0.0;
    }

    // VIEW 4
    if(Ri == 4) {
        r = 0.0;
    }
    if(Gi == 4) {
        g = 0.0;
    }
    if(Bi == 4) {
        b = 0.0;
    }

    // VIEW 5
    if(Ri == 5) {
        r = 0.0;
    }
    if(Gi == 5) {
        g = 0.0;
    }
    if(Bi == 5) {
        b = 0.0;
    }

    // VIEW 6
    if(Ri == 6) {
        r = 0.0;
    }
    if(Gi == 6) {
        g = 0.0;
    }
    if(Bi == 6) {
        b = 0.0;
    }

    // VIEW 7
    if(Ri == 7) {
        r = 0.0;
    }
    if(Gi == 7) {
        g = 0.0;
    }
    if(Bi == 7) {
        b = 0.0;
    }

    gl_FragColor = vec4(r, g, b, 1.0);
}