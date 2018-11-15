## Fitness    


## Calculate Your Max Heart Rate

## Rules:
* (1). Beginning with a baseline of 180
* (2). Subtract your age from the baseline.
* (3). Subtract an additional 10 if you've had a major illness or injury, for each condition.
* (4). Subtract an additional 5 if you've had a minor illness or injury, for each condition
* (5). If you've been training for at least 2 years, add 5.

## Approach    
Build a questionnaire method to populate attributes for an instance of a class object representing an individual's profile, then use the 'Rules' to determind the max aerobic heart rate. 

## Questionnaire Structure - Max Heart Rate  
Used to organize the user input stage of the program, collects an integer age, boolean responses to illness/injury questions, and an integer number of years of previous aerobic training.

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

## Questionnaire Components - Max Heart Rate
Methods called by the questionnaire method.

### Age    
Check edge cases of non-number, 0 or negative age.     
Return integer age. 
```Python3
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
```

### Major Illness
```Python3    
def ask_maj_ill():
    choices = ['yes', 'no']
    response = input("Have you ever had a major illness? Enter Yes or No.")
    if response.lower() not in choices:
        print("Error, please enter Yes or No.")
        ask_maj_ill()
    elif response.lower() == 'yes':
        return True
    else:
        return False
```
### Major Injury
```Python3
def ask_maj_inj():
    choices = ['yes', 'no']
    response = input("Have you ever had a major injury? Enter Yes or No.")
    if response.lower() not in choices:
        print("Error, please enter Yes or No.")
        ask_maj_inj()
    elif response.lower() == 'yes':
        return True
    else:
        return False
```

### Minor Illness
```Python3
def ask_min_ill():
    choices = ['yes', 'no']
    response = input("Have you ever had a minor illness? Enter Yes or No.")
    if response.lower() not in choices:
        print("Error, please enter Yes or No.")
        ask_min_ill()
    elif response.lower() == 'yes':
        return True
    else:
        return False
```
### Minor Injury
```Python3
def ask_min_inj():
    choices = ['yes', 'no']
    response = input("Have you ever had a minor injury? Enter Yes or No.")
    if response.lower() not in choices:
        print("Error, please enter Yes or No.")
        ask_min_inj()
    elif response.lower() == 'yes':
        return True
    else:
        return False
```

### Training Experience
```Python3
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
## 'Runner' Class
```Python3
class Runner(object):
```
## Runner Class Constructor
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

## Runner Class Methods
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

## Calculate Total Score     
Applies conditional logic of '180 Rule' using the instantiated Runner object populated with Max Heart Rate questionnaire with a Python Switch-Case alternative.
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
Use `score()` result to calculate the maximum aerobic heart rate of the user. 

```Python3
    def max_heartrate(self, total_score):
        max_rate = self.baseline+total_score
        print("Your max aerobic heart rate is {} BPM".format(max_rate))
        return max_rate
 ```

## Calculate Calories Burned At Max Heart Rate

## Questionnaire Structure: Calories
```Python3
def cal_questions(age, heart):
    age = age
    time = ask_duration()
    weight = ask_weight()
    heart = heart
    sex = ask_sex()
    cals = Calories(sex, age, weight, time, heart)
    cals_burned = cals.binary_sex()
    return cals_burned
 ```

## Questionnaire Components: Calories
### Weight
```Python3
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
```
### Duration of Exercise
```Python3
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
```
### Sex
```Python3
def ask_sex():
    choices = ['male', 'female']
    response = input("Please enter your gender in the form: \'male\' or \'female\'")
    if response.lower() not in choices:
        print("Error, please enter Male or Female.")
        ask_sex()
    elif response.lower() == 'male':
        return 'male'
    else:
        return 'female'
```

## 'Calorie' Class
```Python3
class Calories(object):
```
## Calorie Constructor

```Python3
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
```

## Calorie Calculation - Male
```Python3
    def male_cals(self, age, weight, time, hr):
        burned = (((age * 0.2017) - (weight * 0.09036) + (hr * 0.6309) - 55.0969) * time / 4.184)
        print("You burned {} calories.".format(round(burned, 2)))
```

## Calorie Calculation - Female
```Python3
    def female_cals(self, age, weight, time, hr):
        burned = (((age * 0.074) - (weight * 0.05741) + (hr * 0.4472) - 20.4022) * time / 4.184)
        print("You burned {} calories.".format(round(burned, 2)))
 ```       

## Check Sex, Apply Calculation, Get Results
```Python3
    def binary_sex(self):
        if self.sex == 'male':
            return self.male_cals(self.age, self.weight, self.duration, self.heartRate)
        else:
            return self.female_cals(self.age, self.weight, self.duration, self.heartRate)
```




 

