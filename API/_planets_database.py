class _planets_database:

    def __init__(self):
        self.planets = {}		#{'planet1':{'Mass':1.2,'Type':1,...},'planet2':{'Mass':1.3,'Type':0,...},...}
    
    # Load information about all planets into database
    def load_planets(self, planet_file):
        file = open(planet_file)
        for line in file:
            planet_array = line.rstrip().split(',')
            self.planets[str(planet_array[0])] = {}
            self.planets[str(planet_array[0])]['type'] = int(planet_array[1])
            self.planets[str(planet_array[0])]['mass'] = int(planet_array[2])
            self.planets[str(planet_array[0])]['radius'] = int(planet_array[3])
            self.planets[str(planet_array[0])]['period'] = int(planet_array[4])
            self.planets[str(planet_array[0])]['semiMajorAxis'] = int(planet_array[5])
            self.planets[str(planet_array[0])]['eccentricity'] = int(planet_array[6])
            self.planets[str(planet_array[0])]['periastron'] = int(planet_array[7])
            self.planets[str(planet_array[0])]['longitude'] = int(planet_array[8])
            self.planets[str(planet_array[0])]['ascendingNode'] = int(planet_array[9])
            self.planets[str(planet_array[0])]['inclination'] = int(planet_array[10])
            self.planets[str(planet_array[0])]['surfaceTemperature'] = int(planet_array[11])
            self.planets[str(planet_array[0])]['age'] = int(planet_array[12])
            self.planets[str(planet_array[0])]['discoveryMethod'] = str(planet_array[13])
            self.planets[str(planet_array[0])]['dicoveryYear'] = int(planet_array[14])
            self.planets[str(planet_array[0])]['lastUpdated'] = str(planet_array[15])
            self.planets[str(planet_array[0])]['rightAscension'] = str(planet_array[16])
            self.planets[str(planet_array[0])]['declination'] = str(planet_array[17])
            self.planets[str(planet_array[0])]['distanceFromSun'] = int(planet_array[18])
            self.planets[str(planet_array[0])]['hostStarMass'] = int(planet_array[19])
            self.planets[str(planet_array[0])]['hostStarRadius'] = int(planet_array[20])
            self.planets[str(planet_array[0])]['hostStarMetallicity'] = int(planet_array[21])
            self.planets[str(planet_array[0])]['hostStarTemperature'] = int(planet_array[22])
            self.planets[str(planet_array[0])]['hostStarAge'] = int(planet_array[23])
            self.planets[str(planet_array[0])]['listsPlanetIsOn'] = str(planet_array[24])
        file.close()

    # Get information about single planet
    def get_planet(self, pid):
        if pid in self.planets:
            return [self.planets[pid]['mass'], self.planets[pid]['radius'], self.planets[pid]['period']]
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
        self.planets[pid]['type'] = int(inp[1])
        self.planets[pid]['mass'] = int(inp[2])
        self.planets[pid]['radius'] = int(inp[3])
        self.planets[pid]['period'] = int(inp[4])
        self.planets[pid]['semiMajorAxis'] = int(inp[5])
        self.planets[pid]['eccentricity'] = int(inp[6])
        self.planets[pid]['periastron'] = int(inp[7])
        self.planets[pid]['longitude'] = int(inp[8])
        self.planets[pid]['ascendingNode'] = int(inp[9])
        self.planets[pid]['inclination'] = int(inp[10])
        self.planets[pid]['surfaceTemperature'] = int(inp[11])
        self.planets[pid]['age'] = int(inp[12])
        self.planets[pid]['discoveryMethod'] = str(inp[13])
        self.planets[pid]['dicoveryYear'] = int(inp[14])
        self.planets[pid]['lastUpdated'] = str(inp[15])
        self.planets[pid]['rightAscension'] = str(inp[16])
        self.planets[pid]['declination'] = str(inp[17])
        self.planets[pid]['distanceFromSun'] = int(inp[18])
        self.planets[pid]['hostStarMass'] = int(inp[19])
        self.planets[pid]['hostStarRadius'] = int(inp[20])
        self.planets[pid]['hostStarMetallicity'] = int(inp[21])
        self.planets[pid]['hostStarTemperature'] = int(inp[22])
        self.planets[pid]['hostStarAge'] = int(inp[23])
        self.planets[pid]['listsPlanetIsOn'] = str(inp[24])

    # Deletes entry for specified planet in database
    def delete_planet(self, pid):
        self.planets.pop(pid, None)

'''
    def load_users(self, user_file):
        self.users     = {}
        mvs = open(user_file)
        for line in mvs:
            user_arr = line.rstrip().split('::')
            self.users[int(user_arr[0])] = {}
            self.users[int(user_arr[0])]["gender"] = user_arr[1]
            self.users[int(user_arr[0])]["age"] = int(user_arr[2])
            self.users[int(user_arr[0])]["occupation"] = int(user_arr[3])
            self.users[int(user_arr[0])]["zipcode"] = user_arr[4]
            self.users[int(user_arr[0])]["id"] = int(user_arr[0])
        mvs.close()


    def get_user(self, uid):
        if uid in self.users:
            user = self.users[uid]
            return user
        return None

    def get_users(self):
        ids = dict()
        for key in self.users:
            ids[key] = self.users[key]
        return ids

    def set_user(self,uid, inp):
        if uid not in self.users:
            self.users[uid] = {}
        self.users[uid]["gender"] = inp[0]
        self.users[uid]["age"] = inp[1]
        self.users[uid]["occupation"] = inp[2]
        self.users[uid]["zipcode"] = inp[3]
        self.users[uid]["id"] = uid

    def delete_user(self, uid):
        self.users.pop(uid, None)

    def load_ratings(self, ratings_file):
        self.ratings     = {}
        mvs = open(ratings_file)
        for line in mvs:
            rating_arr = line.rstrip().split('::')
            if int(rating_arr[1]) not in self.ratings:
                self.ratings[int(rating_arr[1])] = {}
            self.ratings[int(rating_arr[1])][int(rating_arr[0])] = int(rating_arr[2])
        mvs.close()

    def get_rating(self, mid):
        if mid not in self.ratings:
            return float(0)
        r_sum = float(0)
        total = float(len(self.ratings[mid]))
        print(total)
        for r in self.ratings[mid]:
            r_sum += float(self.ratings[mid][r])

        return r_sum/total

    def get_highest_user_rating(self, uid):
        if len(self.ratings) == 0:
            return None 
        max_rating = float(0)
        max_mid = 0
        for mid in self.ratings:
            avg = self.get_rating(mid)
            if avg >= max_rating and uid not in self.ratings[mid] or max_mid == 0:
                if avg == max_rating and mid >= max_mid and max_mid != 0:
                    continue
                max_rating = avg
                max_mid = mid  
        return max_mid

    def set_user_movie_rating(self, uid, mid, rating):
        if mid in self.ratings: 
            self.ratings[mid][uid] = rating

    def get_user_movie_rating(self, uid, mid):
        if mid in self.ratings and uid in self.ratings[mid]:
            return self.ratings[mid][uid]
        return None

    def delete_all_ratings(self):
        self.ratings = {}

    def print_sorted_movies(self):
        for mov in sorted(self.movies):
            print(mov)
'''