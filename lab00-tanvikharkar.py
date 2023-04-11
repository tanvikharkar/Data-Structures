def weight_on_planets():
    weight = input("What do you weigh on earth? ")
    mars_weight = int(weight) * 0.38    # converts user input string (weight) to integer for calculation
    jupiter_weight = int(weight) * 2.34
    print("On Mars you would weigh " + str(mars_weight) + " pounds")    # convert (weight) back to string to print to terminal
    print("On Jupiter you would weigh " + str(jupiter_weight) + " pounds")

if __name__ == '__main__':
    weight_on_planets()