uniform sampler2D sTexture1;
uniform sampler2D sTexture2;

varying vec2 vTexCoord;

// always positive modulus
float cmod(float a, float b) {
    return mod(mod(a, b) + b, b);
}

void main() {
    float x = (gl_FragCoord.x - 0.5);
    float y = 1080.0 - (gl_FragCoord.y - 0.5);

    //x = vTexCoord.x * 1920.0;
    //y = vTexCoord.y * 1080.0;

    int Ri = 0;
    int Gi = 0;
    int Bi = 0;

    float offset = 7.0;
    Ri = int(cmod(3.0 * (x - y) + offset, 8.0));
    Gi = int(cmod(3.0 * (x - y) + 1.0 + offset, 8.0));
    Bi = int(cmod(3.0 * (x - y) + 2.0 + offset, 8.0));

    float r = 0.0;
    float g = 0.0;
    float b = 0.0;

    r = texture2D(sTexture1, vTexCoord).r;

    // VIEW 0
    if(Ri == 0) {
        //r = texture2D(sTexture1, vTexCoord).r;
        r = 1.0;
    }
    if(Gi == 0) {
        g = 0.0;//texture2D(sTexture1, vTexCoord).g;
    }
    if(Bi == 0) {
        b = 0.0;//texture2D(sTexture1, vTexCoord).b;
    }

    // VIEW 1
    if(Ri == 1) {
        r = 0.0;//texture2D(sTexture1, vTexCoord).r;
    }
    if(Gi == 1) {
        g = 0.0;//texture2D(sTexture1, vTexCoord).g;
    }
    if(Bi == 1) {
        b = 0.0;//texture2D(sTexture1, vTexCoord).b;
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

    gl_FragColor = vec4(r, 0.0, 0.0, 1.0);
}