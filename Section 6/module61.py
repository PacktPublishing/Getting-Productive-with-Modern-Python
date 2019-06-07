# 2 - Resuable python code with Plac

# importing our library
# plac is more easier then argparse (a python inbuilt library)
import plac

#-------------------------------------------------------

def main(dsn, car_name='Swift Dzire', price=800000):
    
    "------------------------------\nEnter name in first argument\nSecond argument will be your Car name (Default- swift)\nThird argument is price of car\n------------------------------"
    print("\n------------------------------")
    print("It means,",dsn, "has", car_name,"bought in",price,"\b!!")
    if price>800000:
        print("Oh, come on you're Millionare!")
    else:
        print("Dude save something, You're a Middle-man!")

    print("------------------------------\n")
    
#-------------------------------------------------------

# The below part is used to acess the plac and main function-
if __name__ == '__main__':
    plac.call(main)
    
#-------------------------------------------------------   
    
# Type -
    # python module61.py -h  # to get help instructions
    # python module61.py --help # to get help instructions
    # python module61.py Aditya HondaCity 12,00,000