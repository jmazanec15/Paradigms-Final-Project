class _planets_database:

    def __init__(self):
        self.planets     = {}
        self.users      = {}
        self.ratings    = {}
    
    def load_planets(self, movie_file, img_file):
        self.movies     = {}
        mvs = open(movie_file)
        for line in mvs:
            mov_arr = line.rstrip().split('::')
            self.movies[int(mov_arr[0])] = {}
            self.movies[int(mov_arr[0])]["id"] = int(mov_arr[0])          
            self.movies[int(mov_arr[0])]["title"] = mov_arr[1]
            self.movies[int(mov_arr[0])]["genre"] = mov_arr[2]
            self.movies[int(mov_arr[0])]["img"] = None
        mvs.close()
        # load in images to each movie
        imgs = open(img_file)
        for line in imgs:
            img_arr = line.rstrip().split('::')
            self.movies[int(img_arr[0])]['img'] = img_arr[2]
        imgs.close()

    def get_planet(self, mid):
        if mid in self.movies:
            return [self.movies[mid]["title"], self.movies[mid]["genre"]]
        return None

    def get_planet(self):
        movies = dict()
        for key in self.movies:
            movies[key] = self.movies[key]
        return movies

    def set_planet(self, mid, inp):
        if mid not in self.movies:
            self.movies[mid] = {}
        self.movies[mid]["title"] = inp[0]
        self.movies[mid]["genre"] = inp[1]

    def delete_planet(self, mid):
        self.movies.pop(mid, None)

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
