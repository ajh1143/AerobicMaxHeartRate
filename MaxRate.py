class Runner(object):



    def __init__(self, age, illness_major, illness_minor, injury_major, injury_minor, training_experience):
        """
        :int age:
        :boolean illness_major:
        :boolean illness_minor:
        :boolean injury_major:
        :boolean injury_minor:
        :boolean training_experience:
        """
        self.baseline = 180
        self.age = age
        self.illness_major = illness_major
        self.illness_minor = illness_minor
        self.injury_major = injury_major
        self.injury_minor = injury_minor
        self.training_experience = training_experience


    def score(self):
        options = self.__dict__
        attrb_switcher = {
            'baseline': 0,
            'training_experience':self.training_exp(),
            'injury_minor': self.injury_min(),
            'injury_major': self.injury_maj(),
            'illness_minor': self.illness_min(),
            'illness_major': self.illness_maj(),
            'age': -self.age
        }
        for k in options:
            attrb_switcher[k]
        print(attrb_switcher)
        total_score = sum(attrb_switcher.values())
        print(total_score)
        return total_score

    def max_heartrate(self, total_score):
        max_rate = self.baseline+total_score
        print(max_rate)
        return max_rate

    def age(self):
        return self.age

    def illness_maj(self):
        if self.illness_major:
            return (-10)
        else:
            return 0

    def illness_min(self):
        if self.illness_minor:
            return -5
        else:
            return 0

    def injury_maj(self):
        if self.injury_major:
            return -10
        else:
            return 0

    def injury_min(self):
        if self.injury_minor:
            return -5
        else:
            return 0

    def training_exp(self):
        if self.training_experience:
            return +5
        else:
            return 0

    def attributes(self):
        print(self.__dict__)
