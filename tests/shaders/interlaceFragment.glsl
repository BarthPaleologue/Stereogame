uniform sampler2D sTexture1;
uniform sampler2D sTexture2;

varying vec2 vTexCoord;

// always positive modulus
float cmod(float a, float b) {
    return mod(mod(a, b) + b, b);
}

void main() {
    float x = gl_FragCoord.x;
    float y = (1080.0 - (gl_FragCoord.y));

    int Ri = 0;
    int Gi = 0;
    int Bi = 0;

    if(x-y > 0.0) {
        Ri = int(cmod(3.0 * abs(x - y), 8.0));
        Gi = int(cmod(3.0 * abs(x - y) + 1.0, 8.0));
        Bi = int(cmod(3.0 * abs(x - y) + 2.0, 8.0));
    } else {
        Ri = 8 - int(cmod(3.0 * abs(x - y), 8.0));
        Gi = 8 - int(cmod(3.0 * abs(x - y) + 1.0, 8.0));
        Bi = 8 - int(cmod(3.0 * abs(x - y) + 2.0, 8.0));
    }


    float r = 0.0;
    float g = 0.0;
    float b = 0.0;

    // VIEW 1
    if(Ri == 0 || Ri == 1) {
        r = texture2D(sTexture1, vTexCoord).r;
    }
    if(Gi == 0 || Gi == 1) {
        g = texture2D(sTexture1, vTexCoord).g;
    }
    if(Bi == 0 || Bi == 1) {
        b = texture2D(sTexture1, vTexCoord).b;
    }

    // VIEW 2
    if(Ri == 2 || Ri == 3) {
        r = 0.0;
    }
    if(Gi == 2 || Gi == 3) {
        g = 0.0;
    }
    if(Bi == 2 || Bi == 3) {
        b = 0.0;
    }

    // VIEW 3
    if(Ri == 4 || Ri == 5) {
        //r = texture2D(sTexture2, vTexCoord).r;
        r = 0.0;
    }
    if(Gi == 4 || Gi == 5) {
        //g = texture2D(sTexture2, vTexCoord).g;
        g = 0.0;
    }
    if(Bi == 4 || Bi == 5) {
        //b = texture2D(sTexture2, vTexCoord).b;
        b = 0.0;
    }

    // VIEW 4
    if(Ri == 6 || Ri == 7) {
        r = 0.0;
    }
    if(Gi == 6 || Gi == 7) {
        g = 0.0;
    }
    if(Bi == 6 || Bi == 7) {
        b = 0.0;
    }

    gl_FragColor = vec4(r, g, b, 1.0);
}