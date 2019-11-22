#
# Python: 3.8.0
#
# Author: Ethan Buss
#
# Purpose: Creating a basic game using all learned skills thus far in the course
#


def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)


def describe_game(name):
    """
        Check if this is a new game or not.
        If it is new, get the user's name.
        if it is not a new game, thank the
        player for playing again and continue.
    """
    # meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name.
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>>").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people.")
                    print("\nYou can choose to be nice or mean, \nbut at the end, your fate will be \ndecided by your actions. Choose wisely.")
                    stop = False
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a conversation. \nWill you be Nice or Mean? (N/M) \n>>>").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger walks away steaming...")
            mean = (mean + 1)
            stop = False

    score(nice,mean,name) # pass the 3 variables to the score()


def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) \n({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    # score function is being passed the values stored within the three variables
    if nice > 2: # if condition is valid, call nice function
        nice_win(nice,mean,name)
    if mean > 2: # if condition is valid, call the mean function
        mean_win(nice,mean,name)
    else: # else, call nice_mean function passing the variables so they can be used
        nice_mean(nice,mean,name)


def nice_win(nice,mean,name):
    print("\nYou're a very nice person, {}.".format(name))
    again(nice,mean,name)

def mean_win(nice,mean,name):
    print("\nYou're a mean person, {}.".format(name))
    again(nice,mean,name)



def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nWould you like to play again? (Y/N) \n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nSorry to see you go.")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES' \nEnter ( N ) for 'NO' \n>>>")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    # notice no reset of the NAME variable
    start(nice,mean,name)



if __name__ == "__main__":
    start()
