#   Reynard, a character generator script.
#   Copyright (C) 2025  CosmicJester
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#   To contact via email: cosmicaljester40@gmail.com

# A portion of the comments written in this file are from the initial creation of the script circa early 2024, but which ones specifically, I'll never tell >:D

import os
from pathlib import Path
import pickle
import sys

persdb = {}

def firstRun():
    hasRun = {'key': 'hasRunBefore', 'value': 'true'}
    persdb['hasRunBefore'] = hasRun
    return persdb

match os.name:
    case 'nt':
        perspath = f'{os.getenv('LOCALAPPDATA')}{os.sep}CosmicJester{os.sep}Persist{os.sep}Reynard{os.sep}'
    case _:
        perspath = f'~{os.sep}.cosmicjester{os.sep}persist{os.sep}reynard{os.sep}'

def loadData(data):
    try:
        match data:
            case 'firstrun':
                persDBFile = open(f'{perspath}reynardFirstRun', 'rb')
                hasRun = pickle.load(persDBFile)
                for keys in hasRun:
                    runDB = hasRun[keys]
                persDBFile.close()
                return runDB['value']
            case 'dateformat':
                formatDBFile = open(f'{perspath}reynardDateFormat', 'rb')
                dateFormat = pickle.load(formatDBFile)
                for keys in dateFormat:
                    formDB = dateFormat[keys]
                formatDBFile.close()
                return formDB['value']
    except:
        return 'false'

import kit # All the generation functions are stored in here, there are some other functions and other things (like the dictionaries) but not *all* of the functions are in there, evident by the  ones up above.
# All the variables are stored in Vixen, though I plan to replace it with a dynamically-loaded variant at some point (as in, a text file or something, so it can be updated easier). However, it's not loaded here, since it's not accessed by anything here.

class strlin:
    KEYINT = 'Goodbye! (quit called by KeyboardInterrupt)'
    GENEXT = 'Goodbye!'
    SELFAL = 'Invalid option.'
    GENFAL = 'Failed.'

# Hey hey hey, folks! This is my goofy, funky, really cool main generator script! I'm losing my mental sanity!
match loadData('firstrun'):
    case 'false':
        print(f'Reynard  Copyright (C) 2025  CosmicJester\nThis program comes with ABSOLUTELY NO WARRANTY; for details type \'show w\'.\nThis is free software, and you are welcome to redistribute it\nunder certain conditions; type \'show c\' for details.\n')
        print(f'To preface: All inputs must be typed to the letter, but are case insensitive. There\'s no error correction here yet, and probably never will be.\nDate of birth is set up with the base point of December 31, 2024.\nI\'m not here claiming that everything output by this will be ready to use immediately if you want anything with substance.\nI can\'t do everything for you and I can\'t provide a preset list of backgrounds, medical history, usernames, and relationships.\nThis isn\'t an end-all do-all, it\'s an aid.\n\nThis is just a notice, and will only show up on the first run per user account.\n(Persistent data is stored in "{perspath}".)\n')
        try:
            persDBFile = open(f'{perspath}reynardFirstRun', 'ab')
        except FileNotFoundError: # If the directory doesn't exist,
            os.makedirs(perspath, exist_ok=True) # make it,
            persDBFile = open(f'{perspath}reynardFirstRun', 'xb') # make the file since it won't exist otherwise (not sure I need this, DateFormat doesn't seem to),
            persDBFile.close() # close the file again,
            persDBFile = open(f'{perspath}reynardFirstRun', 'ab') # then reopen it with the right permissions,
        persdb = firstRun() # before doing the proper initialization,
        pickle.dump(persdb, persDBFile) # then dumping the contents to the persistent file,
        persDBFile.close() # and closing it once more.
doformat = Path(f'{perspath}reynardDateFormat') 
if doformat.is_file() is False: # If the date format file doesn't exist on first run,
    dateFormat = {'key': 'dateFormatSelected', 'value': 'yyyy/mm/dd'} # it'll set the key to the ISO 8601 format, default standard,
    formatpersdb = {}
    formatpersdb['dateFormat'] = dateFormat
    persDFFile = open(f'{perspath}reynardDateFormat', 'ab') # before creating *that* file,
    pickle.dump(formatpersdb, persDFFile) # dumping the contents,
    persDFFile.close() # and closing the file.

outfile = open('output.txt','w')
try: # for the command-line argument
    match sys.argv[1]:
        case '-r'|'--reset':
            try:
                match sys.argv[2]:
                    case 'firstrun'|'fr'|'run'|'first':
                        try:
                            os.remove(f'{perspath}reynardFirstRun')
                        except:
                            exc_type, exc_value, exc_traceback = sys.exc_info()
                            print('Could not remove FirstRun file.')
                            input(f'at :{exc_traceback.tb_lineno}\nPress Enter to exit.')
                        else:
                            print('Successfully removed FirstRun file! Notice will show on next run.')
                        quit(0)
                    case 'dateformat'|'df'|'format'|'date':
                        try:
                            os.remove(f'{perspath}reynardDateFormat')
                        except:
                            exc_type, exc_value, exc_traceback = sys.exc_info()
                            print('Could not remove DateFormat file.')
                            input(f'at :{exc_traceback.tb_lineno}\nPress Enter to exit.')
                        else:
                            print('Successfully removed DateFormat file! Format will be set to default upon starting the script.')
                        quit(0)
            except:
                try:
                    os.remove(f'{perspath}reynardFirstRun')
                except:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    print('Could not remove FirstRun file.')
                    input(f'at :{exc_traceback.tb_lineno}\nPress Enter to exit.')
                else:
                    print('Successfully removed FirstRun file! Notice will show on next run.')
                try:
                    os.remove(f'{perspath}reynardDateFormat')
                except:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    print('Could not remove DateFormat file.')
                    input(f'at :{exc_traceback.tb_lineno}\nPress Enter to exit.')
                else:
                    print('Successfully removed DateFormat file! Format will be set to default upon starting the script.')
                quit(0)
except:
    try:
        while True: # Main initialization
            instantion = input('\nReynard active! What are you here for?\n\n1. Generate\n2. Settings\n3. Show C (License)\n4. Show W (License)\n5. Exit\n')
            match instantion.lower():
                case 'generate'|'gen'|'g'|'1':
                    break
                case 'settings'|'set'|'s'|'2':
                    while True:
                        setInst = input('\nWhat are we configuring?\n\n1. DateFormat\n2. Reset\n3. Back\n')
                        match setInst.lower():
                            case 'df'|'format'|'dateformat'|'date format'|'date'|'1':
                                format_sel = input('\nEnter your preferred date format.\n\n1. mm/dd/yyyy\n2. dd/mm/yyyy\n3. yyyy/mm/dd (ISO 8601)\n4. yyyy/dd/mm\n')
                                returned_format = kit.dateFormatSwitch(format_sel.lower())
                                match returned_format.lower():
                                    case 'invalid':
                                        print(strlin.SELFAL)
                                    case _:
                                        dateFormat = {'key': 'dateFormatSelected', 'value': returned_format.lower()}
                                        formatpersdb = {}
                                        formatpersdb['dateFormat'] = dateFormat
                                        persDBFile = open(f'{perspath}reynardDateFormat', 'ab')
                                        pickle.dump(formatpersdb, persDBFile)
                                        persDBFile.close()
                            case 'reset'|'res'|'r'|'2':
                                while True:
                                    resInst = input('\nWhat are we resetting?\n\n1. FirstRun\n2. DateFormat\n3. Both\n4. Back\n')
                                    match resInst.lower():
                                        case 'both'|'3':
                                            errorexit = 0
                                            try:
                                                os.remove(f'{perspath}reynardFirstRun')
                                            except:
                                                exc_type, exc_value, exc_traceback = sys.exc_info()
                                                print('\nFailed to remove FirstRun file.')
                                                input(f' at :{exc_traceback}\nCreate a bug report on the GitHub page\nhttps://github.com/OrangeBlock0421/reynard-generator/issues \nPress Enter to exit')
                                                errorexit = 1
                                            else:
                                                print('\nSuccessfully removed FirstRun file! Notice will show on next run.')
                                            try:
                                                os.remove(f'{perspath}reynardDateFormat')
                                            except:
                                                exc_type, exc_value, exc_traceback = sys.exc_info()
                                                print('Failed to remove DateFormat file.')
                                                input(f' at :{exc_traceback}\nCreate a bug report on the GitHub page\nhttps://github.com/OrangeBlock0421/reynard-generator/issues \nPress Enter to exit')
                                                errorexit = 1
                                            else:
                                                print('Successfully removed DateFormat file! Format will be set to default upon starting the script.')
                                            quit(errorexit)
                                        case 'firstrun'|'run'|'1':
                                            try:
                                                os.remove(f'{perspath}reynardFirstRun')
                                            except:
                                                exc_type, exc_value, exc_traceback = sys.exc_info()
                                                print('\nFailed to remove FirstRun file.')
                                                input(f' at :{exc_traceback}\nCreate a bug report on the GitHub page\nhttps://github.com/OrangeBlock0421/reynard-generator/issues \nPress Enter to exit')
                                                quit(1)
                                            else:
                                                print('Successfully removed FirstRun file! Notice will show on next run.')
                                                quit(0)
                                        case 'date'|'format'|'dateformat'|'2':
                                            try:
                                                os.remove(f'{perspath}reynardDateFormat')
                                            except:
                                                exc_type, exc_value, exc_traceback = sys.exc_info()
                                                print('Failed to remove DateFormat file.')
                                                input(f' at :{exc_traceback}\nCreate a bug report on the GitHub page\nhttps://github.com/OrangeBlock0421/reynard-generator/issues \nPress Enter to exit')
                                                quit(1)
                                            else:
                                                print('Successfully removed DateFormat file! Format will need to be manually reset.')
                                            quit(0)
                                        case 'back'|'4':
                                            break
                                        case 'exit'|'e'|'q'|'quit'|'nevermind':
                                            print(strlin.GENEXT)
                                            quit(0)
                                        case _:
                                            print(strlin.SELFAL)
                                            continue
                            case 'back'|'b'|'3':
                                break
                            case 'exit'|'e'|'q'|'quit'|'nevermind':
                                print(strlin.GENEXT)
                                quit(0)
                            case _:
                                print('Invalid option.')
                                continue
                case 'show w'|'w'|'4':
                    print('\nThis program is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\nGNU General Public License for more details.\n')
                case 'show c'|'c'|'3':
                    print(f'\nThis program is free software: you can redistribute it and/or modify\nit under the terms of the GNU General Public License as published by\nthe Free Software Foundation, either version 3 of the License, or\n(at your option) any later version.\n')
                case 'exit'|'ex'|'e'|'5':
                    print(strlin.GENEXT)
                    quit(0)
                case _:
                    print(strlin.SELFAL)
                    continue
        while True: # Generation choice
            genInt = input('What kind of generation (all or individual)?\n\n1. All\n2. Name\n3. Gender\n4. Species\n5. Age\n6. Bulk\n7. Exit\n')
            gen_type = kit.generate_map.get(genInt.strip().lower(), 'all')
            match gen_type:
                case 'all'|'name'|'gender'|'species'|'age'|'bulk':
                    break
                case 'nevermind'|'quit'|'exit'|'7':
                    print(strlin.GENEXT)
                    quit(0)
                case _:
                    print(strlin.SELFAL)
                    continue
    except KeyboardInterrupt: # I don't need to have ^C work like this, but I like having that not be considered an unhandled exception
            print(strlin.KEYINT)
            quit(0)

# Because collectively, we can't get our stuff in order and working.
# PYTHON. TELL ME WHY 'OUTPUT_TOFILE' IS UNBOUND. *TELL ME WHY.*
# IT'S A SIMPLE BOOLEAN. WHY DO I NEED A FUNCTION TO DO YOUR JOB FOR YOU.

# There used to be a function here to set OUTPUT_TOFILE to True, because it kept throwing NameError. Turns out, the problem was that I didn't have the 'if' statement set it to False when the input said no. I'm leaving those comments there because one, funny, and two, it's historical.
## LMAO THE PROBLEM WASN'T THAT, IT WAS THE LACK OF DEFAULT VARIABLES :P
## I am very sanded brain, if you couldn't tell.
### AND THE FUNNIEST PART. I ditched that segment anyway.

# The situation: I stopped using OUTPUT_TOFILE and that method of picking output type because, as rey.py (my mini script that got merged into this one) taught me, if you don't make it export, and you run the script from say, a self-contained EXE, you're physically incapable of doing anything with the output before the terminal closes. Instead of implementing a pause function, it just outputs automatically. Frankly, why wouldn't you want it to do that?

# age_gen used to be here because as is, I couldn't move it to Kit. But now I know how to define a function. :)
try:
    match gen_type.lower():
        case 'all'|'everything'|'all of it'|'1':
            while True: # Fur initialization
                furint = input('Non-human species alright?\n\n1. Yes\n2. No\n3. Exit\n')
                if furint in ('3', 'exit', 'e'):
                    print(strlin.GENEXT)
                    quit(0)
                else:
                    fur_bool = kit.bool_map.get(furint.strip().lower(), True)
                    match fur_bool:
                        case True|False:
                            break
                        case _:
                            print(strlin.SELFAL)
                            continue
            while True: # Age range initialization
                ageint = input('What age range?\n\n1. Child (8-12)\n2. Teen (13-17)\n3. Young Adult (18-35)\n4. Adult (36-64)\n5. Old (65-120)\n6. Immortal/Abnormal (18-500)\n7. Any (8-120)\n8. Exit\n') # yea I'm classing 35 as 'young adult', fight me
                if ageint in ('8', 'exit', 'e'):
                    print(strlin.GENEXT)
                    quit(0)
                else:
                    chosen_age = kit.age_map.get(ageint.strip().lower(), 'any')
                    match chosen_age.lower():
                        case 'child'|'teen'|'young adult'|'adult'|'old'|'abnormal':
                            break
                        case _:
                            print(strlin.SELFAL)
                            continue
            while True: # Gender initialization
                nonstand_gender = input('Non-binary gender options (non-binary, trans)?\n\n1. Yes\n2. No\n')
                gender_bool = kit.bool_map.get(nonstand_gender.strip().lower(), True)
                match gender_bool:
                    case True|False:                        
                        break
                    case _:
                        print(strlin.SELFAL)
                        continue
            while True: # Hair color initialization
                unnatur_hair = input('Non-standard hair colors?\n\n1. Yes\n2. No\n')
                haircolor_bool = kit.bool_map.get(unnatur_hair.strip().lower(), True)
                match haircolor_bool:
                    case True|False:
                        break
                    case _:
                        print(strlin.SELFAL)
                        continue
            while True: # Format initialization
                templint = input('What output format?\n\n1. Basic\n2. Formatted\n3. Full\n4. Blank Basic\n5. Blank Formatted\n6. Blank Full\n7. Exit\n')
                chosen_template = kit.format_map.get(templint.strip().lower(), 'basic')
                match chosen_template:
                    case 'basic'|'formatted'|'full'|'blank basic'|'blank formatted'|'blank full':
                        break
                    case '7'|'exit'|'e':
                        print(strlin.GENEXT)
                        quit(0)
                    case _:
                        print(strlin.SELFAL)
                        continue
            try:
                match chosen_template:
                    case 'basic':
                        species_sel = kit.speciesGen(fur_bool)
                        match species_sel.lower():
                            case 'human'|'robot'|'demon'|'angel'|'elf':
                                skin_color = f'{kit.skinGen(fur_bool).lower()} skin'
                            case _:
                                skin_color = f'{kit.furGen().lower()} fur'
                        eye_color = f'{kit.eyeGen()} eyes'
                        hat_sel = kit.massGen('hat')
                        match hat_sel.lower():
                            case 'none':
                                hat_out = 'no hat'
                            case _:
                                hat_color_sel = kit.massGen('hatcolor')
                                hat_size_sel = kit.massGen('hatsize')
                                hat_out = f'a {hat_size_sel.lower()} {hat_color_sel.lower()} {hat_sel.lower()}'
                        gender_sel = kit.genderGen(gender_bool)
                        genduh = kit.gender_map.get(gender_sel, 'fem')
                        top_sel = kit.massGen('top')
                        outtop_sel = kit.massGen('outertop')
                        match outtop_sel.lower():
                            case 'none':
                                top_out = f'a {str.lower(kit.massGen('topcolor'))} {top_sel.lower()}'
                            case _:
                                top_out = f'a {str.lower(kit.massGen('topcolor'))} {top_sel.lower()}, a {str.lower(kit.massGen('outertopcolor'))} {outtop_sel.lower()}'
                        print(f'''Name: {kit.nameGen('both',genduh)}
Aliases: None
Gender: {gender_sel}
Species: {str(species_sel)}
Age: {str(kit.ageGen(chosen_age))}
Appearance: {kit.heightGen()}, {skin_color}, {str.lower(eye_color)}, wears {top_out.lower()}, {str.lower(kit.massGen('bottomcolor'))} {str.lower(kit.massGen('bottom'))}, {str.lower(kit.massGen('sockcolor'))} {str.lower(kit.massGen('sock'))}, {str.lower(kit.massGen('shoecolor'))} {str.lower(kit.massGen('shoe'))}, and {hat_out}
Skills: {kit.skillGen()}
Abilities: {', '.join(kit.abilityGen())}
Personality: {kit.personalityGen()} (Note, if you get a conflict, just remove it, don't have error correction set up yet)
Background: {str(kit.massGen('nationality'))}.''', file=outfile)
                            # This entire section used to please the italians. But now it's split off to the segment above!
                    case 'formatted':
                        species_sel = kit.speciesGen(fur_bool)
                        match species_sel.lower():
                            case 'human'|'robot'|'demon'|'angel'|'elf':
                                skin_color = f'Skin Color: {kit.skinGen(fur_bool)}'
                            case _:
                                skin_color = f'Fur Color: {kit.furGen()}'
                        eye_color = f'{kit.eyeGen()}'
                        gender_sel = kit.genderGen(gender_bool)
                        genduh = kit.gender_map.get(gender_sel, 'fem')
                        top_sel = kit.massGen('top')
                        outtop_sel = kit.massGen('outertop')
                        match outtop_sel.lower():
                            case 'none':
                                top_out = f'{kit.massGen('topcolor')} {top_sel}'
                            case _:
                                top_out = f'{kit.massGen('topcolor')} {top_sel}, {kit.massGen('topcolor')} {outtop_sel}'
                        hat_sel = kit.massGen('hat')
                        match hat_sel.lower():
                            case 'none':
                                hat_out = 'No Hat'
                            case _:
                                hat_color_sel = kit.massGen('hatcolor')
                                hat_size_sel = kit.massGen('hatsize')
                                hat_out = f'{hat_size_sel} {hat_color_sel} {hat_sel}'
                        print(f'''Name: {kit.nameGen('both',genduh)}
Aliases: None
Species: {species_sel}
Date of Birth: {kit.birthDateGen(chosen_age.lower(),loadData('dateformat'))}
Gender: {gender_sel}
Sexuality: {kit.massGen('sexuality')}
Occupation: No Table
Nationality: {kit.massGen('nationality')}
{skin_color}
Hair Color: {kit.hairGen(haircolor_bool)}
Hair Style: {kit.massGen('hairstyle')}
Eye Color: {eye_color}
Height: {kit.heightGen()}
Clothes: {top_out}, {kit.massGen('bottomcolor')} {kit.massGen('bottom')}, {kit.massGen('sockcolor')} {kit.massGen('sock')}, {kit.massGen('shoecolor')} {kit.massGen('shoe')}, {hat_out}
Abilities: {', '.join(kit.abilityGen())}
Skills: {kit.skillGen()}
Personality: {kit.personalityGen()} (Note, if you get a conflict, just remove it, don't have error correction set up yet)
Likes: No Table
Dislikes: No Table
Medical History: Manually
Username: Manually
Backstory: Manually
Relationships: Manually
Misc. Info: Manually''',file=outfile)
                    case 'full':
                        species_sel = kit.speciesGen(fur_bool)
                        match species_sel.lower():
                            case 'human'|'robot'|'demon'|'angel'|'elf':
                                skin_color = f'Skin Color: {kit.skinGen(fur_bool)}'
                            case _:
                                skin_color = f'Fur Color: {kit.furGen()}'
                        eye_color = f'{kit.eyeGen()}'
                        gender_sel = kit.genderGen(gender_bool)
                        genduh = kit.gender_map.get(gender_sel, 'fem')
                        top_sel = kit.massGen('top')
                        outtop_sel = kit.massGen('outertop')
                        match outtop_sel.lower():
                            case 'none':
                                top_out = f'{kit.massGen('topcolor')} {top_sel}'
                            case _:
                                top_out = f'{kit.massGen('topcolor')} {top_sel}, {kit.massGen('outertopcolor')} {outtop_sel}'
                        hat_sel = kit.massGen('hat')
                        match hat_sel.lower():
                            case 'none':
                                hat_out = 'No Hat'
                            case _:
                                hat_color_sel = kit.massGen('hatcolor')
                                hat_size_sel = kit.massGen('hatsize')
                                hat_out = f'{hat_size_sel} {hat_color_sel} {hat_sel}'
                        print(f'''Name: {kit.nameGen('both',genduh)}
Aliases: None
Species: {species_sel}
Date of Birth: {kit.birthDateGen(chosen_age.lower(),loadData('dateformat'))}
Gender: {gender_sel}
Sexuality: {kit.massGen('sexuality')}
Occupation: No Table
Nationality: {kit.massGen('nationality')}
{skin_color}
Hair Color: {kit.hairGen(haircolor_bool)}
Hair Style: {kit.massGen('hairstyle')}
Eye Color: {eye_color}
Height: {kit.heightGen()}
Head: {hat_out}
Top: {top_out}
Bottom: {kit.massGen('bottomcolor')} {kit.massGen('bottom')}
Feet: {kit.massGen('shoecolor')} {kit.massGen('shoe')}
Hands: No Table
Abilities: {', '.join(kit.abilityGen())}
Skills: {kit.skillGen()}
Personality: {kit.personalityGen()} (Note, if you get a conflict, just remove it, don't have error correction set up yet)
Likes: No Table
Dislikes: No Table
Medical History: Manually
Username: Manually
Backstory: Manually
Relationships: Manually
Misc. Info: Manually''', file=outfile)
                    case 'blank basic':
                        print(f'''Name: 
Aliases: 
Gender: 
Species: 
Age: 
Appearance: 
Skills: 
Abilities: 
Personality: 
Background:''',file=outfile)
                    case 'blank formatted':
                        print(f'''Name: 
Aliases: 
Species: 
Date of Birth: 
Gender: 
Sexuality: 
Occupation: 
Nationality: 
Fur Color: 
Hair Color: 
Hair Style: 
Eye Color: 
Height: 
Clothes: 
Abilities: 
Skills: 
Personality: 
Likes: 
Dislikes: 
Medical History: 
Username: 
Backstory: 
Relationships: 
Misc. Info: ''',file=outfile)
                    case 'blank full':
                        print(f'''Name: 
Aliases: 
Species: 
Date of Birth: 
Gender: 
Sexuality: 
Occupation: 
Nationality: 
Fur Color: 
Hair Color: 
Hair Stule: 
Eye Color: 
Height: 
Head: 
Top: 
Bottom: 
Feet: 
Hands: 
Abilities: 
Skills: 
Personality: 
Likes: 
Dislikes: 
Medical History: 
Username: 
Backstory: 
Relationships: 
Misc. Info: ''', file=outfile)
            except kit.InvalidGenOption:
                print(f'Generation failed ({str(kit.InvalidGenOption.message)})', file=outfile)
        case 'name':
            oneortwo = input("First, last, or both?\n\n1. First\n2. Last\n3. Both\n4. Exit\n")
            if oneortwo.lower() in ('4','exit','e'):
                print(strlin.GENEXT)
                quit(0)
            else:
                uod = kit.uod_map.get(oneortwo.strip().lower(), "both") # Mapping user input to one of: 'first', 'last', or 'both' to make the code less of a mess
                match uod:
                    case 'first'|'both': # If you aren't asking for just a last name
                        gendin = input("What gender?\n\n1. Female\n2. Male\n3. Androgynous\n4. Any\n") # It prompts for gender input
                        genduh = kit.gender_map.get(gendin.strip().lower(), "fem")
                    case 'last':
                        genduh = "irrelevant"
                reso = str(kit.nameGen(uod, genduh))
                print(reso,file=outfile)
        case 'gender':
            while True:
                nons = input("Non-binary gender options (non-binary, trans)?\n\n1. Yes\n2. No\n")
                gender_nonstand = kit.bool_map.get(nons.strip().lower(), True)
                match gender_nonstand:
                    case True|False:
                        break
                    case _:
                        print(strlin.SELFAL)
                        continue
            print(kit.genderGen(gender_nonstand), file=outfile)
        case 'species'|'race':
            while True:
                furinst = input("Non-human species alright?\n\n1. Yes\n2. No\n")
                furpillow = kit.bool_map.get(furinst.strip().lower(), True)
                match furpillow:
                    case True|False:
                        break
                    case _:
                        print(strlin.SELFAL)
                        continue
            print(kit.speciesGen(furpillow), file=outfile)
        case 'age':
            while True:
                ageint = input('What age range?\n\n1. Child (8-12)\n2. Teen (13-17)\n3. Young Adult (18-35)\n4. Adult (36-64)\n5. Old (65-120)\n6. Immortal/Abnormal (18-500)\n7. Any (8-120)\n8. Exit\n')
                if ageint in ('8', 'exit', 'e'):
                    print(strlin.GENEXT)
                    quit(0)
                else:
                    chosen_age = kit.age_map.get(ageint.strip().lower(), 'any')
                    match chosen_age:
                        case 'child'|'teen'|'young adult'|'adult'|'old'|'abnormal':
                            break
                        case _:
                            print(strlin.SELFAL)
                            continue
            print(kit.ageGen(chosen_age), file=outfile)
        case 'bulk':
            while True:
                manno = input("Of what?\n\n1. Name\n2. Gender\n3. Species\n")
                match manno.lower():
                    case 'quit':
                        quit(0)
                    case 'name':
                        reygenset = input("First, last, or both?\n\n1. First\n2. Last\n3. Both\n")
                        uod = kit.uod_map.get(reygenset.strip().lower(), "both")
                        match uod:
                            case 'first'|'both':
                                gendin = input("What gender?\n\n1. Female\n2. Male\n3. Androgynous\n4. Any\n")
                                reygen = kit.gender_map.get(gendin.strip().lower(), "fem")
                            case 'last':
                                reygen = 'fem'
                        break
                    case 'gender':
                        reynonstand = input("Non-standard allowed?\n\n1. Yes\n2. No\n")
                        nonstand = kit.bool_map.get(reynonstand.strip().lower(), True)
                        break
                    case 'species':
                        reynonspec = input("Furries allowed?\n\n1. Yes\n2. No\n")
                        nonspec = kit.bool_map.get(reynonspec.strip().lower(), True)
                        break
                    case _:
                        print(strlin.SELFAL)
                        continue
            manny = input("How many generations?\n")
            manni = 0
            outpow = []
            match manno.lower():
                case 'name':
                    while manni != int(manny):
                        outpow.append(kit.nameGen(uod,reygen))
                        manni += 1
                case 'gender':
                    while manni != int(manny):
                        outpow.append(kit.genderGen(nonstand))
                        manni += 1
                case 'species':
                    while manni != int(manny):
                        outpow.append(kit.speciesGen(nonspec))
                        manni += 1
                case _:
                    print(strlin.GENFAL, file=outfile)
            print('\n'.join(outpow), file=outfile)
except KeyboardInterrupt:
    print(strlin.KEYINT)
    quit(0)
