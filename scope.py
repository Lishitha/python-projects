def checkscope():
    def do_local():
        test = "local test"
        print(test)
    def do_non_local():
        nonlocal test
        test = "non local test"
    def do_global():
        global test
        test = "global test"
    test = "default"
    do_local()
    print("test value after do lacal : " + test)
    do_non_local()
    print("after do non local : "+test)
    do_global()
    print("after do global: "+test)


checkscope()
print("after globL : " + test)

