class _planets_database:

    def __init__(self):
        self.planets = {}       #{'planet1':{'Mass':1.2,'Type':1,...},'planet2':{'Mass':1.3,'Type':0,...},...}
    
    # Load information about all planets stro database
    def load_planets(self, planet_file):
        file = open(planet_file)
        file.readline()
        for line in file:
            planet_array = line.rstrip().split(',')
            self.planets[str(planet_array[0])] = {}
            self.planets[str(planet_array[0])]['type'] = str(planet_array[1])
            self.planets[str(planet_array[0])]['mass'] = str(planet_array[2])
            self.planets[str(planet_array[0])]['radius'] = str(planet_array[3])
            self.planets[str(planet_array[0])]['period'] = str(planet_array[4])
            self.planets[str(planet_array[0])]['semiMajorAxis'] = str(planet_array[5])
            self.planets[str(planet_array[0])]['eccentricity'] = str(planet_array[6])
            self.planets[str(planet_array[0])]['periastron'] = str(planet_array[7])
            self.planets[str(planet_array[0])]['longitude'] = str(planet_array[8])
            self.planets[str(planet_array[0])]['ascendingNode'] = str(planet_array[9])
            self.planets[str(planet_array[0])]['inclination'] = str(planet_array[10])
            self.planets[str(planet_array[0])]['surfaceTemperature'] = str(planet_array[11])
            self.planets[str(planet_array[0])]['age'] = str(planet_array[12])
            self.planets[str(planet_array[0])]['discoveryMethod'] = str(planet_array[13])
            self.planets[str(planet_array[0])]['dicoveryYear'] = str(planet_array[14])
            self.planets[str(planet_array[0])]['lastUpdated'] = str(planet_array[15])
            self.planets[str(planet_array[0])]['rightAscension'] = str(planet_array[16])
            self.planets[str(planet_array[0])]['declination'] = str(planet_array[17])
            self.planets[str(planet_array[0])]['distanceFromSun'] = str(planet_array[18])
            self.planets[str(planet_array[0])]['hostStarMass'] = str(planet_array[19])
            self.planets[str(planet_array[0])]['hostStarRadius'] = str(planet_array[20])
            self.planets[str(planet_array[0])]['hostStarMetallicity'] = str(planet_array[21])
            self.planets[str(planet_array[0])]['hostStarTemperature'] = str(planet_array[22])
            self.planets[str(planet_array[0])]['hostStarAge'] = str(planet_array[23])
            self.planets[str(planet_array[0])]['listsPlanetIsOn'] = str(planet_array[24])
            self.planets[str(planet_array[0])]['visitors'] = str(0)
        file.close()

    # Get information about single planet
    def get_planet(self, pid):
        if pid in self.planets:
            self.planets[pid]['visitors'] = str(int(self.planets[pid]['visitors']) + 1)
            return {'mass':self.planets[pid]['mass'],'radius':self.planets[pid]['radius'],'period':self.planets[pid]['period'],'visitors':self.planets[pid]['visitors']}
        return None

    # Get infomation about all planets in database
    def get_planets(self):
        planets = dict()
        for key in self.planets:
            planets[key] = self.planets[key]
        return planets

    # Set information about a single planet, adds new entry if planet not present in database
    def set_planet(self, pid, inp):
        if pid not in self.planets:
            self.planets[pid] = {}
        self.planets[pid]['type'] = str(inp[0])
        self.planets[pid]['mass'] = str(inp[1])
        self.planets[pid]['radius'] = str(inp[2])
        self.planets[pid]['period'] = str(inp[3])
        self.planets[pid]['semiMajorAxis'] = str(inp[4])
        self.planets[pid]['eccentricity'] = str(inp[5])
        self.planets[pid]['periastron'] = str(inp[6])
        self.planets[pid]['longitude'] = str(inp[7])
        self.planets[pid]['ascendingNode'] = str(inp[8])
        self.planets[pid]['inclination'] = str(inp[9])
        self.planets[pid]['surfaceTemperature'] = str(inp[10])
        self.planets[pid]['age'] = str(inp[11])
        self.planets[pid]['discoveryMethod'] = str(inp[12])
        self.planets[pid]['dicoveryYear'] = str(inp[13])
        self.planets[pid]['lastUpdated'] = str(inp[14])
        self.planets[pid]['rightAscension'] = str(inp[15])
        self.planets[pid]['declination'] = str(inp[16])
        self.planets[pid]['distanceFromSun'] = str(inp[17])
        self.planets[pid]['hostStarMass'] = str(inp[18])
        self.planets[pid]['hostStarRadius'] = str(inp[19])
        self.planets[pid]['hostStarMetallicity'] = str(inp[20])
        self.planets[pid]['hostStarTemperature'] = str(inp[21])
        self.planets[pid]['hostStarAge'] = str(inp[22])
        self.planets[pid]['listsPlanetIsOn'] = str(inp[23])
        self.planets[pid]['visitors'] = str(inp[24])

    # Deletes entry for specified planet in database
    def delete_planet(self, pid):
        self.planets.pop(pid, None)

    # Deletes all entries for planets in databse
    def delete_planets(self):
        self.planets = {}