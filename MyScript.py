
def main():
    '''business logic for when running this module as the primary one!'''
    print("From inside MyScript")
    setup()
    do_important()
    do_even_more_important()
    print ("this was important")
    teardown()

def setup ():
    print ("setup")

def teardown():
    print ("teardown")
    
def do_important():
    print ("important")

def do_even_more_important():
    print ("even more important") 

# Here's our payoff idiom!
if __name__ == '__main__':
    main()
    print ("onnozelaar")  #something you dont want executed when called from Outside
