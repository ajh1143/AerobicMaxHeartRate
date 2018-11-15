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
        print(options)
        attrb_switcher = {
            'baseline': 0,
            'training_experience':self.training_exp(),
            'injury_minor': self.injury_min(),
            'injury_major': self.injury_maj(),
            'illness_minor': self.illness_min(),
            'illness_major': self.illness_maj(),
            'age': -self.age
        }
        for k in options.keys():
            attrb_switcher[k]
        print(attrb_switcher)
        total_score = sum(attrb_switcher.values())
        return total_score

    def max_heartrate(self, total_score):
        max_rate = self.baseline+total_score
        print("Your max aerobic heart rate is {} BPM".format(max_rate))
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



def questionnaire():
    age = ask_age()
    maj_ill = ask_maj_ill()
    maj_inj = ask_maj_inj()
    min_ill = ask_min_ill()
    min_inj = ask_min_inj()
    exp = ask_exp()
    runner = Runner(age, maj_ill, min_ill, maj_inj, min_inj, exp)
    return runner


def ask_age():
    while True:
        try:
            response = int(input("Please enter your age."))
            if response <= 0:
                print("Please enter a valid age.")
            else:
                break
        except ValueError:
            print("Please enter a number.")
    return response

def ask_maj_ill():
    choices = ['yes','no']
    response = input("Have you ever had a major illness? Enter Yes or No.")
    if response.lower() not in choices:
        print("Error, please enter Yes or No.")
        ask_maj_ill()
    elif response.lower() =='yes':
        return True
    else:
        return False


def ask_maj_inj():
    choices = ['yes','no']
    response = input("Have you ever had a major injury? Enter Yes or No.")
    if response.lower() not in choices:
        print("Error, please enter Yes or No.")
        ask_maj_inj()
    elif response.lower() =='yes':
        return True
    else:
        return False


def ask_min_ill():
    choices = ['yes','no']
    response = input("Have you ever had a minor illness? Enter Yes or No.")
    if response.lower() not in choices:
        print("Error, please enter Yes or No.")
        ask_min_ill()
    elif response.lower() =='yes':
        return True
    else:
        return False


def ask_min_inj():
    choices = ['yes','no']
    response = input("Have you ever had a minor injury? Enter Yes or No.")
    if response.lower() not in choices:
        print("Error, please enter Yes or No.")
        ask_min_inj()
    elif response.lower() =='yes':
        return True
    else:
        return False


def ask_exp():
    while True:
        try:
            response = int(input("How many years of training do you have? Enter a numeric value."))
            if response < 0:
                print("Please enter a non-negative number.")
                ask_exp()
            if response >= 2:
                return True
            else:
                return False
        except ValueError:
            print("Please enter a valid number of years.")


def ask_weight():
    while True:
        try:
            response = int(input("Please enter your weight in integer pounds."))
            if response <= 0:
                print("Please enter a valid weight.")
            else:
                break
        except ValueError:
            print("Please enter an integer value.")
    return response


def ask_duration():
    while True:
        try:
            response = float(input("Please enter your the duration of your aerobic activity in minutes."))
            if response <= 0:
                print("Please enter a valid time.")
            else:
                break
        except ValueError:
            print("Please enter a float value.")
    return response



def ask_sex():
    choices = ['male','female']
    response = input("Please enter your gender in the form: \'male\' or \'female\'")
    if response.lower() not in choices:
        print("Error, please enter Male or Female.")
        ask_sex()
    elif response.lower() =='male':
        return 'male'
    else:
        return 'female'


def cal_questions(age, heart):
    age = age
    time = ask_duration()
    weight = ask_weight()
    heart = heart
    sex = ask_sex()
    cals = Calories(sex, age, weight, time, heart)
    cals_burned = cals.binary_sex()
    return cals_burned

class Calories(object):

    def attributes(self):
        print(self.__dict__)

    def __init__(self, sex, age, weight, duration, heartRate):
        """
        :string sex:
        :int age:
        :int weight:
        :float duration:
        :int heartRate:
        """
        self.sex = sex
        self.age = age
        self.weight = weight
        self.duration = duration
        self.heartRate = heartRate


    def binary_sex(self):
        if self.sex == 'male':
            return self.male_cals(self.age, self.weight, self.duration, self.heartRate)
        else:
            return self.female_cals(self.age, self.weight, self.duration, self.heartRate)



    def male_cals(self, age, weight, time, hr):
        burned = (((age * 0.2017) - (weight * 0.09036) + (hr * 0.6309) - 55.0969) * time/4.184)
        print("You burned {} calories.".format(round(burned,2)))


    def female_cals(self, age, weight, time, hr):
        burned = (((age * 0.074) - (weight * 0.05741) + (hr * 0.4472) - 20.4022) * time / 4.184)
        print("You burned {} calories.".format(round(burned, 2)))
