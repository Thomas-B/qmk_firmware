from math import *
# Here are some "for instance" examples of leds based on groupings modify this to your needs
dark_gray = [36,52,53,54,42,58,59,60]
light_gray = []
back_light = range(0,120)

registers = [0,0,0,0]

# Now using the "for instance" arrays, putting them into a dict. Again, modify this based on your needs.
# However recommend doing it as a dict so the output is easier to parse, even if you only have one array
all_keys = {"dark gray":dark_gray, "light gray":light_gray, "back light":back_light}

#Loop through all_keys to do the calculation
for key_group_name, key_group_keys in all_keys.items():
    for led in key_group_keys:
        nled = led -1
        id = floor(nled / 32)
        element = nled % 32
        value = 2 ** element
        registers[id] = registers[id] + value

    print('%s .id0 = %s, .id1 = %s, .id2 = %s, .id3 = %s,'%(key_group_name, registers[0], registers[1], registers[2], registers[3]))
    registers = [0,0,0,0]
