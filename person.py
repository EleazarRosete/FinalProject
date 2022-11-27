class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password


class stats(user):
    def __init__(self, username, password, points, rank, finished):
        super().__init__(username, password)
        self.points = points
        self.rank = rank
        self.finished = finished
        print("\nUser Stats!"
              "\n   -   Username  : ", self.username,
              "\n   -   User Pass : ", self.password,
              "\n   -   Points    : ", self.points,
              "\n   -   Rank      : ", self.rank,
              "\n   -   Tasks Done: ")
        for x in finished:
            print("            -    : ", x)