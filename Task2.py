class Road:
    _width = 20
    _length = 5000

    def RoadMass(self, asphalt_mass, asphalt_layer):
        result = self._length * self._width * asphalt_mass * asphalt_layer
        return result
