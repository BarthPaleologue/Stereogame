from feather.material import ColorMaterial

class DefaultMaterial(ColorMaterial):
    def __init__(self):
        super().__init__(255.0 / 255.0, 192.0 / 255.0, 203.0 / 255.0)