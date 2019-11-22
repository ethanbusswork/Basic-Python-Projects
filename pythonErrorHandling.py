

def getInfo():
    var1 = input("\nPlease provide the first numeric value: \n>>>")
    var2 = input("\nPlease provide the second numeric value: \n>>>")
    return var1,var2



def compute():
    go = True
    while go:
        var1,var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            go = False
        except ValueError as e:
            print("{}: \n\nYou did not provide a value in numeric form!".format(e))
        except:
            print("\n\nProgram will now close from fatal error")
    print("{} + {} = {}".format(var1,var2,var3))

        


if __name__ == "__main__":
    compute()
