def Main():
    try:
        countries = []
        populations = []
        land_mass = []
        avg_density = []

        countries_num = sum(1 for line in open('WorldData2012.txt'))
        print(countries_num)
        file = open('WorldData2012.txt', 'r')
        line = file.readline().rstrip()

        for i in range(0,countries_num):
            line = line.split(',')
            #print(line[0], line[1], line[2])
            country = line[0]
            pop = float(line[1])
            land = float(line[2])
            density = float(pop/land)
            countries.append(country)
            populations.append(pop)
            land_mass.append(land)
            avg_density.append(format(float(density), '.2f'))
            line = file.readline().rstrip()

        file.close()
        total_pop = sum(int(i) for i in populations)
        total_density = (sum(float(i) for i in avg_density))/countries_num
        max_pop = 0
        min_pop = 999999999
        max_land = 0
        min_land = 999999999
        max_density = 0
        min_density = 999999999
        hi_density_index = []
        lo_density_index = []
        max_pop_index = 0
        min_pop_index = 0
        max_land_index = 0
        min_land_index = 0
        max_density_index = 0
        min_density_index = 0

        for i in range(0, countries_num):
            density = float(avg_density[i])
            if populations[i] > max_pop:
                max_pop = populations[i]
                max_pop_index = i
            if land_mass[i] > max_land:
                max_land = land_mass[i]
                max_land_index = i
            if density > max_density:
                max_density = density
                max_density_index = i

        for i in range(0, countries_num):
            density = float(avg_density[i])
            if populations[i] < min_pop:
                min_pop = populations[i]
                min_pop_index = i
            if land_mass[i] < min_land:
                min_land = land_mass[i]
                min_land_index = i
            if density < min_density:
                min_density = density
                min_density_index = i


        for i in range(0, countries_num):
            density = float(avg_density[i])
            hi_density = total_density * 2
            lo_density = (total_density * (1 / 100))
            if density > hi_density:
                hi_density_index.append(i)
            elif density <= lo_density:
                lo_density_index.append(i)


        print("Total number of countries is {} countries".format(countries_num))
        print("Total world population is {} people".format(total_pop))
        print("{} has the highest population - {} people.".format(countries[max_pop_index], max_pop))
        print("{} has the lowest population - {} people.".format(countries[min_pop_index], min_pop))
        print("{} has the greatest land area - {} sq.km".format(countries[max_land_index], max_land))
        print("{} has the smallest land area - {} sq.km".format(countries[min_land_index], min_land))
        print("{} has the highest population density - {} people/sq.km".format(countries[max_density_index], max_density))
        print("{} has the lowest population density - {} people/sq.km".format(countries[min_density_index], min_density))
        print("****************************************")
        print("Average population density is  {}".format(format(total_density, '.2f')))
        print("****************************************")
        print("----------------------------------------")
        print("Densely populated Countries")
        print("----------------------------------------")
        for index in hi_density_index:
            print("{}, {:>1} people/sq.km".format(countries[index], avg_density[index]))
        print("****************************************")
        print("----------------------------------------")
        print("Sparsly populated Countries")
        print("----------------------------------------")
        for index in lo_density_index:
            print("{}, {:>1} people/sq.km".format(countries[index], avg_density[index]))


    except IOError as err:
        print(err)
    except ValueError as err:
        print(err)
Main()