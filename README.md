## Calculate Your Max Heart Rate

Let's construct a quick program to calculate your maximum aerobic heart rate, and use it to find out how many calories you could burn if you maintained it over the duration of your next run. (Spoiler: You **won't** and you also **shouldn't**, you'll **hurt yourself**.) We'll also figure out a safe range, and calculate how many calories you can burn under that condition as well.

I sincerely hope you choose to eat pie while surrounded by your friends and family this holiday season, rather than think about hypothetical calories.


_______________________________________________________________________________________________________________________________________
## Heart Rates via The 180 Methodology    
*Rules*:    
* Begin with a baseline of 180 beats per minute (bpm)    
* Subtract your age from the baseline.    
* Subtract an additional 10 if you've had a major illness or injury, for each condition.    
* Subtract an additional 5 if you've had a minor illness or injury, for each condition    
* If you've been training for at least 2 years, add 5.    

_______________________________________________________________________________________________________________________________________
## Program Approach    
### Part I - Heart Rate:    

In Part I, we'll build a questionnaire method to populate attributes for an instance of a class object representing an individual's profile, then use the 'Rules' we've outlined above to determine the max aerobic heart rate and a subsequent 'safe' heart rate.

### Part II - Calories:    

In Part II, we'll then construct a second questionnaire to populate an instance of a class object to calculate the sweet total caloric burn you could achieve if you could maintain your peak level of activity.


_______________________________________________________________________________________________________________________________________

# PART I - Max Heart Rate
<img src="https://github.com/ajh1143/ajh1143.github.io/blob/master/Images/Aerobic/heartbeat3.jpg" class="inline"/><br>    
*Image Source: https://peterdewit.wordpress.com/tag/heartbeat/

We'll begin by defining a method to procedurally call our subset of question methods to gather information about you, our user.

## Questionnaire Structure
Used to organize the user input stage of the program, collects an integer age, boolean responses to illness/injury questions, and an integer number of years of previous aerobic training.

```Python3
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
Let's take a closer look at the individual methods being called by the questionnaire.



## Age - ask_age()
Example: 18 Years Old

Check edge cases of non-number, 0 or negative age, loop input request if invalid.
Return user's integer age.

```Python3
def ask_age():while True:
        try:
            response = int(input("Please enter your age.\n"))
            if response <= 0:
                print("Please enter a valid age.")
            else:
                breakexcept ValueError:
            print("Please enter a number.")
    return response
```
## Major Illness - ask_maj_ill()
Example: Heart Disease

Check edge cases of non-'yes'/'no' input, loop input request if invalid.
Return boolean response.
```Python3
def ask_maj_ill():
    choices = ['yes', 'no']
    response = input("Have you ever had a major illness? Enter Yes or No.\n")
    if response.lower() not in choices:
        print("Error, please enter Yes or No.")
        ask_maj_ill()
    elif response.lower() == 'yes':
        return Trueelse:
        return False
```
## Major Injury - ask_maj_inj()
Example: Heart related surgery

Check edge cases of non-'yes'/'no' input, loop input request if invalid.
Return boolean response.
```Python3
def ask_maj_inj():
    choices = ['yes', 'no']
    response = input("Have you ever had a major injury? Enter Yes or No.\n")
    if response.lower() not in choices:
        print("Error, please enter Yes or No.")
        ask_maj_inj()
    elif response.lower() == 'yes':
        return Trueelse:
        return False
```
## Minor Illness - ask_min_ill()
Example: Allergies/Asthma

Check edge cases of non-'yes'/'no' input, loop input request if invalid.
Return boolean response.
```Python3
def ask_min_ill():
    choices = ['yes', 'no']
    response = input("Have you ever had a minor illness? Enter Yes or No.\n")
    if response.lower() not in choices:
        print("Error, please enter Yes or No.")
        ask_min_ill()
    elif response.lower() == 'yes':
        return Trueelse:
        return False
```

## Minor Injury - ask_min_inj()
Example: Old sports injury

Check edge cases of non-'yes'/'no' input, loop input request if invalid.
Return boolean response.
```Python3
def ask_min_inj():
    choices = ['yes', 'no']
    response = input("Have you ever had a minor injury? Enter Yes or No.\n")
    if response.lower() not in choices:
        print("Error, please enter Yes or No.")
        ask_min_inj()
    elif response.lower() == 'yes':
        return Trueelse:
        return False
```

## Training Experience - ask_exp()
Example: Consistent Cardio Routine in years

Check edge cases of non-number, 0 or negative training, loop input request if invalid.
Check if training condition `years >= 2` is met for a +5 bonus.
Return boolean of user's training.
```Python3
def ask_exp():
    while True:
        try:
            response = int(input("How many years of training do you have? Enter a numeric value.\n"))
            if response < 0:
                print("Please enter a non-negative number.")
                ask_exp()
            if response >= 2:
                return Trueelse:
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
    def attributes(self):
        print(self.__dict__)


    def age(self):return self.age

    def illness_maj(self):if self.illness_major:
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
```
## Calculate Total Score
Applies conditional logic of '180 Rule' using the instantiated Runner object populated with Max Heart Rate questionnaire through a Python Switch-Case alternative. We'll build a dictionary of user responses, then iterate over k,v pairs to sum the values into a score we'll use in the next step.
```Python3
    def score(self):
        options = self.__dict__
        print("Summary:")
        print(options)
        print("\n")
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
        total_score = sum(attrb_switcher.values())
        print(total_score)
        return total_score
```
## Calculate Max Heart Rate
Use score() result to calculate the maximum aerobic heart rate of the user. In the previous step, we calculated a total score, now we'll use this method to augment the starting value of 180 to a customized bpm value for the user.
```Python3
    def max_heartrate(self, total_score):
        max_rate = self.baseline+total_score
        print("Your max aerobic heart rate is {} BPM".format(max_rate))
        return max_rate
```

## Calculate Safe Heart Rate
Now that we know our max heart rate, we can use it to generate a safer heart rate by printing and returning 80% of our max. Or, alternatively we could simply calculate 0.8 * the max later on at the calorie burn stage, which we will also do.
```Python3
   def safe_heartrate(self, max_hr):
       safe_rate = .8*max_hr
       print("Your safe aerobic heart rate is {} BPM".format(round(safe_rate,2)))
       return safe_rate
```

### Command Line Interface:
Example: 18, perfect health, 2 years of previous training.
<img src="https://github.com/ajh1143/ajh1143.github.io/blob/master/Images/Aerobic/1.png" class="inline"/><br>

_______________________________________________________________________________________________________________________________________

# PART II - Calories Burned

## Calculate Calories Burned At Max Heart Rate
Now that we've calculated our max heart rate, let's use it to find out how many calories we could burn by sustaining our peak level.
```Python3
Questionnaire Structure: Calories
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
Weight - ask_weight()
Example: 170 lbs

Check edge cases of non-integer, 0 or negative weight, loop input if invalid.
Return user's integer weight.
```Python3
def ask_weight():
    while True:
        try:
            response = int(input("Please enter your weight in integer pounds.\n"))
            if response <= 0:
                print("Please enter a valid weight.")
            else:
                break
        except ValueError:
            print("Please enter an integer value.")
    return response
```
## Duration of Exercise - ask_duration()
Example: 30 Minutes

Check edge cases of non-number, 0 or negative duration, loop input if invalid.
Return user's float exercise duration.
```Python3
def ask_duration():
    while True:
        try:
            response = float(input("Please enter your the duration of your aerobic activity in minutes.\n"))
            if response <= 0:
                print("Please enter a valid time.")
            else:
                break
        except ValueError:
            print("Please enter a float value.")
    return response
```

## Sex - ask_sex()
Example: Male

Check edge cases of non-'male'/'female' input, loop if invalid.
Return String response of sex category.
```Python3
def ask_sex():
    choices = ['male', 'female']
    response = input("Please enter your gender in the form: \'male\' or \'female\'\n")
    if response.lower() not in choices:
        print("Error, please enter Male or Female.")
        ask_sex()
    elif response.lower() == 'male':
        return 'male'else:return 'female'

## 'Calorie' Class
```Python3
class Calories(object):
```

## Calorie Constructor
```Python3
def __init__(self, sex, age, weight, duration, heartRate):"""
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
Inputs:

Age, Weight, Time(duration), hr(heart rate)
```Python3
    def male_cals(self, age, weight, time, max_hr):
        max_burned = (((age * 0.2017) - (weight * 0.09036) + (max_hr * 0.6309) - 55.0969) * time / 4.184)
        safe_burned = (((age * 0.2017) - (weight * 0.09036) + (0.8*max_hr * 0.6309) - 55.0969) * time / 4.184)
        print("You could burn {} calories with a max heart rate.".format(round(max_burned, 2)))
        print("You could burn {} calories with a safe heart rate.".format(round(safe_burned, 2)))
```
## Calorie Calculation - Female
Inputs:

Age, Weight, Time(duration), hr(heart rate)
```Python3
    def female_cals(self, age, weight, time, max_hr):
        max_burned = (((age * 0.074) - (weight * 0.05741) + (max_hr * 0.4472) - 20.4022) * time / 4.184)
        safe_burned = (((age * 0.074) - (weight * 0.05741) + (0.8*max_hr * 0.4472) - 20.4022) * time / 4.184)
        print("You could burn {} calories with a max heart rate.".format(round(max_burned, 2)))
        print("You could burn {} calories with a safe heart rate".format(round(safe_burned, 2)))

```

## Check Sex, Apply Calculation, Get Results
```Python3
def binary_sex(self):
    if self.sex == 'male':
        return self.male_cals(self.age, self.weight, self.duration, self.heartRate)
    else:
        return self.female_cals(self.age, self.weight, self.duration, self.heartRate)
```
### Command Line Interface
<img src="https://github.com/ajh1143/ajh1143.github.io/blob/master/Images/Aerobic/2.png" class="inline"/><br

_______________________________________________________________________________________________________________________________________
## Run It!
Main
```Python3
if __name__ == '__main__':
    user= questionnaire()
    total = user.score()
    hr = user.max_heartrate(total)
    cal_questions(user.age, hr)
Command Line Interface
```

_______________________________________________________________________________________________________________________________________
## Full Code:
```Python3
class Runner(object):

    def __init__(self, age, illness_major, illness_minor, injury_major, injury_minor, training_experience):"""
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
        print("Summary:")
        print(options)
        print("\n")
        attrb_switcher = {
            'baseline': 0,
            'training_experience': self.training_exp(),
            'injury_minor': self.injury_min(),
            'injury_major': self.injury_maj(),
            'illness_minor': self.illness_min(),
            'illness_major': self.illness_maj(),
            'age': -self.age
        }
        for k in options.keys():
            attrb_switcher[k]
        total_score = sum(attrb_switcher.values())
        return total_score

    def max_heartrate(self, total_score):
        max_rate = self.baseline + total_score
        print("Your max aerobic heart rate is {} BPM".format(max_rate))
        return max_rate

    def safe_heartrate(self, max_hr):
        safe_rate = .8*max_hr
        print("Your safe aerobic heart rate is {} BPM".format(round(safe_rate,2)))
        return safe_rate

    def age(self):return self.age

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


def ask_age():while True:
        try:
            response = int(input("Please enter your age.\n"))
            if response <= 0:
                print("Please enter a valid age.")
            else:
                breakexcept ValueError:
            print("Please enter a number.")
    return response


def ask_maj_ill():
    choices = ['yes', 'no']
    response = input("Have you ever had a major illness? Enter Yes or No.\n")
    if response.lower() not in choices:
        print("Error, please enter Yes or No.")
        ask_maj_ill()
    elif response.lower() == 'yes':
        return Trueelse:
        return False


def ask_maj_inj():
    choices = ['yes', 'no']
    response = input("Have you ever had a major injury? Enter Yes or No.\n")
    if response.lower() not in choices:
        print("Error, please enter Yes or No.")
        ask_maj_inj()
    elif response.lower() == 'yes':
        return Trueelse:
        return False


def ask_min_ill():
    choices = ['yes', 'no']
    response = input("Have you ever had a minor illness? Enter Yes or No.\n")
    if response.lower() not in choices:
        print("Error, please enter Yes or No.")
        ask_min_ill()
    elif response.lower() == 'yes':
        return Trueelse:
        return False


def ask_min_inj():
    choices = ['yes', 'no']
    response = input("Have you ever had a minor injury? Enter Yes or No.\n")
    if response.lower() not in choices:
        print("Error, please enter Yes or No.")
        ask_min_inj()
    elif response.lower() == 'yes':
        return Trueelse:
        return False


def ask_exp():while True:
        try:
            response = int(input("How many years of training do you have? Enter a numeric value.\n"))
            if response < 0:
                print("Please enter a non-negative number.")
                ask_exp()
            if response >= 2:
                return Trueelse:
                return Falseexcept ValueError:
            print("Please enter a valid number of years.")


def ask_weight():while True:
        try:
            response = int(input("Please enter your weight in integer pounds.\n"))
            if response <= 0:
                print("Please enter a valid weight.")
            else:
                breakexcept ValueError:
            print("Please enter an integer value.")
    return response


def ask_duration():while True:
        try:
            response = float(input("Please enter your the duration of your aerobic activity in minutes.\n"))
            if response <= 0:
                print("Please enter a valid time.")
            else:
                breakexcept ValueError:
            print("Please enter a float value.")
    return response


def ask_sex():
    choices = ['male', 'female']
    response = input("Please enter your gender in the form: \'male\' or \'female\'\n")
    if response.lower() not in choices:
        print("Error, please enter Male or Female.")
        ask_sex()
    elif response.lower() == 'male':
        return 'male'else:
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

    def __init__(self, sex, age, weight, duration, heartRate):"""
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

    def binary_sex(self):if self.sex == 'male':
            return self.male_cals(self.age, self.weight, self.duration, self.heartRate)
        else:
            return self.female_cals(self.age, self.weight, self.duration, self.heartRate)

    def male_cals(self, age, weight, time, max_hr):
        max_burned = (((age * 0.2017) - (weight * 0.09036) + (max_hr * 0.6309) - 55.0969) * time / 4.184)
        safe_burned = (((age * 0.2017) - (weight * 0.09036) + (0.8*max_hr * 0.6309) - 55.0969) * time / 4.184)
        print("You could burn {} calories with a max heart rate.".format(round(max_burned, 2)))
        print("You could burn {} calories with a safe heart rate.".format(round(safe_burned, 2)))

    def female_cals(self, age, weight, time, max_hr):
        max_burned = (((age * 0.074) - (weight * 0.05741) + (max_hr * 0.4472) - 20.4022) * time / 4.184)
        safe_burned = (((age * 0.074) - (weight * 0.05741) + (0.8*max_hr * 0.4472) - 20.4022) * time / 4.184)
        print("You could burn {} calories with a max heart rate.".format(round(max_burned, 2)))
        print("You could burn {} calories with a safe heart rate".format(round(safe_burned, 2)))




if __name__ == '__main__':
    r1= questionnaire()
    total = r1.score()
    max_hr = r1.max_heartrate(total)
    cal_questions(r1.age, max_hr)
```

```




 

