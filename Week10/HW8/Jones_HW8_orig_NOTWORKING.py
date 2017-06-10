def main():
    try:
        # First Loop lists and accumulators
        countries = []
        avg_density = []
        total_pop = 0
        total_avg_density = 0

        # Second loop accumulators
        max_pop = 0
        max_pop_country = ""
        min_pop = 999999999999
        min_pop_country = ""
        max_land = 0
        max_land_country = ""
        min_land = 999999999999
        min_land_country = ""

        file = open('test.txt', 'r')
        line = file.readline().rstrip()
        while line != '':
            line_num = 0

            for i in range(0,8):
                line = line.split(',')
                countries.append(line[0])
                total_pop += int(line[1])
                density = int(line[1]) / int(line[2])
                avg_density.append(density)
                total_avg_density += float(density)
                line_num += 1
                line = file.readline().rstrip()

        file.close()
        countries_num = len(countries)
        total_avg_density = float(total_avg_density/countries_num)
        lo_density = int(total_avg_density * (1/100))
        hi_density = int(total_avg_density * 2)


        file = open('test.txt', 'r')
        line = file.readline().rstrip()

        lo_density_countries = []
        lo_density_pop_list = []
        hi_density_countries = []
        hi_density_pop_list = []
        max_density = 0
        max_density_country = ""
        min_density = 999999999999
        min_density_country = ""

        for line_num in range(0,int(len(countries))):
            density = float(format(avg_density[line_num],'.2f'))
            country = countries[line_num]
            print(country, density)
            line_num = int(line_num)
            line = line.split(",")

            if line == "":
                break

            elif int(line[1]) > int(max_pop):
                max_pop = line[1]
                max_pop_country = countries[line_num]

                if density > max_density:
                    print("TEST")
                    max_density = density
                    max_density_country = country
                elif density < min_density:
                    print("TEST")
                    min_density = density
                    min_density_country = country


            elif int(line[1]) < int(min_pop):
                min_pop = line[1]
                min_pop_country = countries[line_num]
                if density > max_density:
                    print("TEST")
                    max_density = density
                    max_density_country = country
                elif density < min_density:
                    print("TEST")
                    min_density = density
                    min_density_country = country


            elif int(line[2]) > int(max_land):
                max_land = line[2]
                max_land_country = countries[line_num]
                if density > max_density:
                    print("TEST")
                    max_density = density
                    max_density_country = country
                elif density < min_density:
                    print("TEST")
                    min_density = density
                    min_density_country = country



            elif int(line[2]) < int(min_pop):
                min_land = line[2]
                min_land_country = countries[line_num]
                if density > max_density:
                    print("TEST")
                    max_density = density
                    max_density_country = country
                elif density < min_density:
                    print("TEST")
                    min_density = density
                    min_density_country = country

                if density > hi_density:
                    print("TEST")
                    hi_density_country = country
                    hi_density_pop = avg_density[line_num]
                    hi_density_countries.append(hi_density_country)
                    hi_density_pop_list.append(hi_density_pop)
                elif density <= lo_density:
                    print("TEST")
                    lo_density_country = country
                    lo_density_pop = avg_density[line_num]
                    lo_density_countries.append(lo_density_country)
                    lo_density_pop_list.append(lo_density_pop)



            else:
                print("PROBLEM")
            line = file.readline().rstrip()
        file.close()

        print("Total number of countries is {}".format(countries_num))
        print("Total world population is {} people".format(total_pop))
        print(max_pop_country + " has the highest population - " + max_pop + " people")
        print(min_pop_country + " has the lowest population - " + min_pop + " people")
        print(max_land_country + " has the greatest land area - " + max_land + " sq.km")
        print(min_land_country + " has the smallest land area - " + min_land + " sq.km")
        print("{} has the highest population density - {} people/sq.km".format(max_density_country, max_density))
        print("{} has the lowest population density - {} people/sq.km".format(min_density_country, min_density))
        print("****************************************")
        print("Average population density is  {}".format(format(total_avg_density, '.2f')))
        print("****************************************")
        print("----------------------------------------")
        print("Densely populated Countries")
        print("----------------------------------------")
        for i in range(0, len(hi_density_countries)):
            print("{}, {}".format(hi_density_countries[i], hi_density_pop_list[i]))
        print("****************************************")
        print("----------------------------------------")
        print("Sparsly populated Countries")
        print("----------------------------------------")
        for i in range(0, len(lo_density_countries)):
            print("{}, {}".format(lo_density_countries[i], lo_density_pop_list[i]))

    except IOError as err:
        pass
    except ValueError as err:
        pass
    except IndexError as err:
        pass

main()