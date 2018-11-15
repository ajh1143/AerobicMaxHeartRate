## Max Aerobic heartrate with 180 Rule

## Rules:
* (1). Beginning with a baseline of 180
* (2). Subtract your age from the baseline.
* (3). Subtract an additional 10 if you've had a major illness or injury, for each condition.
* (4). Subtract an additional 5 if you've had a minor illness or injury, for each condition
* (5). If you've been training for at least 2 years, add 5.

## Questionnaire
```Python
def questionnaire():
    age = ask_age()
    maj_ill = ask_maj_ill()
    maj_inj = ask_maj_inj()
    min_ill = ask_min_ill()
    min_inj = ask_maj_inj()
    exp = ask_exp()
    runner = Runner(age, maj_ill, min_ill, maj_inj, min_inj, exp)
    return runner
```
## User Input
```Python3
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

```
## Class
```Python3
class Runner(object):
```
## Constructor
```Python3
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
```
## Calculate Total Score
```Python3
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
        for k in options.keys():
            attrb_switcher[k]
        print(attrb_switcher)
        total_score = sum(attrb_switcher.values())
        print(total_score)
        return total_score
```

## Calculate Max Heart Rate
```Python3
    def max_heartrate(self, total_score):
        max_rate = self.baseline+total_score
        print("Your max aerobic heart rate is {} BPM".format(max_rate))
        return max_rate
 ```
 
## Pythonic Switch-Case Alternative Framework

```Python3
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
 ```
