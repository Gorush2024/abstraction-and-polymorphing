try:
    class Twowheel:
        def good(self):
            print("2-wheelers (cycles) are efficient because you can squeeze into small gaps and roads.\n")

        def bad(self):
            print("But 2-wheelers are sometimes not efficient because of rain.")

    class Fourwheel:
        def good(self):
            print("4-wheelers (e.g., trucks, cars) are efficient because some have AC, bright lights, and electric features, which are pretty cool.\n")

        def bad(self):
            print("But the downside of 4-wheelers is that they often get stuck in traffic and consume more fuel.")

    obj_2 = Fourwheel()
    obj_4 = Twowheel()

    for vehicle in (obj_2, obj_4):
        vehicle.good()
        vehicle.bad()

finally:
    while True:
        try:
            op = int(input("So what do you prefer? (type 2 or 4): "))
            if op == 2:
                print("Good choice. It's pretty cool!")
                break
            elif op == 4:
                print("Good choice. It has many features!")
                break
            else:
                print("Please type 2 or 4.")
        except ValueError:
            print("thats not a number. please type 2 or 4")

#miss i PROMISE i didnt use ai. i just really liked the concept and i thought nested try was inpossible but I tried it. this took 1 hour