
def print_color_map(printFtn):
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            value = value_calculation(i,j)
           colorCodeManualItem= append_colour(value,major,minor)
           printFtn(colorCodeManualItem);
    return len(major_colors) * len(minor_colors)


def value_calculation(i,j):
    val = (5*i) + i
    return val
    
def append_colour(value,major,minor):
    mes = str(value) + '|' + major + '|' + minor
    return mes
def printColorCodeManualItem(item)
    print(item);


generatedManual=[]
def fakePrintFtn(colorCodeManualItem)
   

result = print_color_map(fakePrintFtn)
assert(result == 25)

##value_calculation() checks
#0 value check
assert(value_calculation(0,3) == 3)
assert(value_calculation(4,0) == 20)
assert(value_calculation(0,0) == 0)
#-ve value check
assert(value_calculation(-1,15) == 10)
assert(value_calculation(2,-6) == 4)
assert(value_calculation(-2,-8) == -18)

##append_colour() checks
#Empty string checks
assert(append_colour(4,'','') == '4||')
#Valid values
assert(append_colour(0, "White", "Blue") == '0|White|Blue')
assert(append_colour(24, "Violet", "Slate") == '24|Violet|Slate')
assert(append_colour(12, "Black", "Green") == "12|Black|Green")
#Numeric values
assert(append_colour(5, "234", "5465") == '5|234|5465')


print("All is well (maybe!)")
