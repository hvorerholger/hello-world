
#Python doesnt have a main() function unless you code for it
#Python interpreter only executes the launched script file internally known as __main__
#if the launched script wants to reuse qnd run code from another module, the imported or
#called module will be known to the Python interpreter with its own file name and therefore
#not be confused with the __main__ script

def OutSideScript():
    import MyScript
    MyScript.main()


if __name__ == '__main__':
    print("From Outside script")
    OutSideScript()
