"""Function scripts for Reynard."""
from random import randrange, sample # love me my pseudo-random numbers
import os # CLEAR THE TEXT, BOSS

import vixen # we need the variables, they important

class InvalidFormatError(Exception):
    """Exception raised for an invalid format.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidGenOption(Exception):
    """Exception raised if the massGen() option is invalid.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message + self.__context__)

class tc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

bool_map = {"1": True, "true": True, "yes": True, "y": True, 'woof': True, 'bark': True, 'meow': True, 'mreow': True, 'marp': True, 'mrrp': True, 'arf': True, 'mow': True,
            "0": False, "false": False, "no": False, "n": False, "2": False}
gender_map = {'male': 'masc', 'm': 'masc', 'masc': 'masc', '2': 'masc', 'man': 'masc', 'boy': 'masc', 'b': 'masc', 'trans male': 'masc',
              '1': 'fem', 'female': 'fem', 'woman': 'fem', 'fem': 'fem', 'girl': 'fem', 'f': 'fem', 'g': 'fem', 'trans female': 'fem',
              'androgynous': 'andro', 'andro': 'andro', '3': 'andro', 'a': 'andro', 'either': 'andro', 'non-binary': 'andro', 'nb': 'andro', 'nonbinary': 'andro', 'trans androgynous': 'andro', 'non-binary androgynous': 'andro', 'non-binary male': 'andro', 'non-binary female': 'andro',
              'any': 'any', 'either': 'any', 'it matters not': 'any', '4': 'any'}
uod_map = {'first': 'first', '1': 'first', 'one': 'first',
           '2': 'last', 'last': 'last', 'two': 'last',
           '3': 'both', 'both': 'both', 'three': 'both'}
age_map = {'child': 'child', 'kid': 'child', 'c': 'child', 'k': 'child', '1': 'child',
           'teen': 'teen', 'teenager': 'teen', 't': 'teen', '2': 'teen',
           'young': 'young adult', 'y': 'young adult', 'ya': 'young adult', 'young adult': 'young adult', '3': 'young adult',
           'adult': 'adult', 'a': 'adult', '4': 'adult',
           'old': 'old', 'elder': 'old', 'o': 'old', 'e': 'elder', '5': 'old',
           'immortal': 'abnormal', 'i': 'abnormal', 'abnormal': 'abnormal', 'ab': 'abnormal', 'inhuman': 'abnormal', 'i': 'abnormal', '6': 'abnormal',
           'any': 'any', 'doesn\'t matter': 'any', 'whatever': 'any', '7': 'any'}
format_map = {'basic': 'basic', 'b': 'basic', '1': 'basic',
              'formatted': 'formatted', 'f': 'formatted', '2': 'formatted',
              'full': 'full', 'fu': 'full', '3': 'full',
              'blank basic': 'blank basic', 'bb': 'blank basic', '4': 'blank basic',
              'blank formatted': 'blank formatted', 'bf': 'blank formatted', '5': 'blank formatted',
              'blank full': 'blank full', 'bfu': 'blank full', '6': 'blank full'}
generate_map = {'1': 'all', 'all': 'all', 'everything': 'all', 'all of it': 'all',
                '2': 'name', 'name': 'name', '3': 'gender', 'gender': 'gender',
                '4': 'species', 'race': 'species', 'species': 'species',
                '5': 'age', 'age': 'age', '6': 'bulk', 'bulk': 'bulk'}

# 1. All 2. Name 3. Gender 4. Species 5. Age 6. Bulk

def genderGen(nonstand):
    match nonstand:
        case True:
            gendernum = randrange(0, vixen.GENDER_MAX)
            gendersuf = randrange(0, vixen.GENDER_SUFFIX_MAX)
            match gendersuf:
                case 8|9:
                    return f"{vixen.gender_suffixes[gendersuf]} {vixen.genders[gendernum]}"
                case _:
                    return f"{vixen.genders[gendernum]}"
        case False:
            return vixen.genders[randrange(0, 2)]

def nameGen(type,gender):
    match type:
        case 'first':
            match gender:
                case 'fem':
                    return str(vixen.fem_names[randrange(0,vixen.FEM_NAMES_MAX)])
                case 'masc':
                    return str(vixen.masc_names[randrange(0,vixen.MASC_NAMES_MAX)])
                case 'andro':
                    return str(vixen.andro_names[randrange(0,vixen.ANDRO_NAMES_MAX)])
                case 'any':
                    gendor = randrange(0,2)
                    match gendor:
                        case 0:
                            return str(vixen.fem_names[randrange(0,vixen.FEM_NAMES_MAX)])
                        case 1:
                            return str(vixen.masc_names[randrange(0,vixen.MASC_NAMES_MAX)])
                        case 2:
                            return str(vixen.andro_names[randrange(0,vixen.ANDRO_NAMES_MAX)])
                case _:
                    return "Failed"
        case 'last':
            return str(vixen.last_names[randrange(0,vixen.LAST_NAMES_MAX)])
        case 'both':
            match gender:
                case 'fem':
                    return f'{str(vixen.fem_names[randrange(0,vixen.FEM_NAMES_MAX)])} {str(vixen.last_names[randrange(0,vixen.LAST_NAMES_MAX)])}'
                case 'masc':
                    return f'{str(vixen.masc_names[randrange(0,vixen.MASC_NAMES_MAX)])} {str(vixen.last_names[randrange(0,vixen.LAST_NAMES_MAX)])}'
                case 'andro':
                    return f'{str(vixen.andro_names[randrange(0,vixen.ANDRO_NAMES_MAX)])} {str(vixen.last_names[randrange(0,vixen.LAST_NAMES_MAX)])}'
                case 'any':
                    gendor = randrange(0,2)
                    match gendor:
                        case 0:
                            return f'{str(vixen.fem_names[randrange(0,vixen.FEM_NAMES_MAX)])} {str(vixen.last_names[randrange(0,vixen.LAST_NAMES_MAX)])}'
                        case 1:
                            return f'{str(vixen.masc_names[randrange(0,vixen.MASC_NAMES_MAX)])} {str(vixen.last_names[randrange(0,vixen.LAST_NAMES_MAX)])}'
                        case 2:
                            return f'{str(vixen.andro_names[randrange(0,vixen.ANDRO_NAMES_MAX)])} {str(vixen.last_names[randrange(0,vixen.LAST_NAMES_MAX)])}'
                case _:
                    return "Failed"
        case _:
            return "Failed"

def eyeGen():
    eye_color_num = randrange(0,vixen.EYE_COLORS_MAX)
    match eye_color_num:
        case vixen.EYE_COLORS_MAX:
            eye_1 = randrange(0,vixen.EYE_COLORS_MAX)
            eye_2 = randrange(0,vixen.EYE_COLORS_MAX)
            while eye_1 == eye_2:
                eye_2 = randrange(0,vixen.EYE_COLORS_MAX)
            return f'{str(vixen.eye_colors[eye_1])} Left and {str(vixen.eye_colors[eye_2])} Right'
        case _:
            return vixen.eye_colors[eye_color_num]

def hairGen(unnatur):
    match unnatur:
        case True:
            hair_color_num = randrange(0,vixen.FUR_COLORS_MAX)
            match hair_color_num:
                case vixen.FUR_COLORS_MAX:
                    hairc1 = randrange(0,vixen.FUR_COLORS_MAXLESS)
                    hairc2 = randrange(0,vixen.FUR_COLORS_MAXLESS)
                    while hairc2 == hairc1:
                        hairc2 = randrange(0,vixen.FUR_COLORS_MAXLESS)
                    return f'{vixen.fur_colors[hairc1]} and {vixen.fur_colors[hairc2]}'
                case _:
                    return f'{vixen.fur_colors[hair_color_num]}'
        case False:
            return f'{vixen.natural_hair_colors[randrange(0,vixen.NATURAL_HAIR_COLORS_MAX)]}'

def skinGen(nonstand):
    match nonstand:
        case True:
            skin_color_num = randrange(0,vixen.SKIN_COLORS_MAX)
            match skin_color_num:
                case vixen.SKIN_COLORS_MAX:
                    return vixen.fur_colors[randrange(0,vixen.FUR_COLORS_MAXLESS)]
                case _:
                    return vixen.skin_colors[skin_color_num]
        case False:
            return vixen.skin_colors[randrange(0,vixen.SKIN_COLORS_STANDMAX)]
        case _:
            return vixen.skin_colors[randrange(0,vixen.SKIN_COLORS_STANDMAX)]

def heightGen():
    hf = randrange(4,7)
    hi = randrange(0,11)
    return f'{hf}\'{hi}"'

def furGen():
    fur_color_num = randrange(0,vixen.FUR_COLORS_MAX)
    match fur_color_num:
        case vixen.FUR_COLORS_MAX:
            fur_col_1 = randrange(0,vixen.FUR_COLORS_MAXLESS)
            fur_col_2 = randrange(0,vixen.FUR_COLORS_MAXLESS)
            while fur_col_1 is fur_col_2:
                fur_col_2 = randrange(0,vixen.FUR_COLORS_MAX - 1)
            return f'{str(vixen.fur_colors[fur_col_1])} and {str(vixen.fur_colors[fur_col_2])}'
        case _:
            return vixen.fur_colors[fur_color_num]

def massGen(which):
    match which:
        case 'sexuality':
            return str(vixen.sexualities[randrange(0,vixen.SEXUALITIES_MAX)])
        case 'hat':
            return vixen.hats[randrange(0,vixen.HAT_MAX)]
        case 'hatcolor':
            return vixen.hat_colors[randrange(0,vixen.HAT_COLOR_MAX)]
        case 'hatsize':
            return vixen.cloth_sizes[randrange(0,vixen.SIZE_MAX)]
        case 'nationality':
            return vixen.nationalities[randrange(0,vixen.NATIONALITIES_MAX)]
        case 'top':
            return vixen.tops[randrange(0,vixen.TOP_MAX)]
        case 'topcolor':
            return str(vixen.top_colors[randrange(0,vixen.TOP_COLOR_MAX)])
        case 'outertop':
            return f'{vixen.out_tops[randrange(0,vixen.OUT_TOP_MAX)]}'
        case 'outertopcolor':
            return f'{vixen.top_colors[randrange(0,vixen.TOP_COLOR_MAX)]}'
        case 'bottom':
            return str(vixen.bottoms[randrange(0,vixen.BOTTOM_MAX)])
        case 'bottomcolor':
            return str(vixen.bottom_colors[randrange(0,vixen.BOTTOM_COLOR_MAX)])
        case 'sock':
            return str(vixen.socks[randrange(0,vixen.SOCKS_MAX)])
        case 'sockcolor':
            return str(vixen.bottom_colors[randrange(0,vixen.BOTTOM_COLOR_MAX)])
        case 'shoe':
            return str(vixen.shoes[randrange(0,vixen.SHOE_MAX)])
        case 'shoecolor':
            return str(vixen.shoe_colors[randrange(0,vixen.SHOE_COLOR_MAX)])
        case 'hairstyle':
            return f'{vixen.hair_styles[randrange(0,vixen.HAIR_STYLES_MAX)]}'
        case _:
            raise InvalidGenOption('massGen() was given an invalid option.')

def ageGen(rang):
    match rang:
        case 'child':
            return str(randrange(8,12))
        case 'teen':
            return str(randrange(13,17))
        case 'young adult':
            return str(randrange(18,35))
        case 'adult':
            return str(randrange(36,64))
        case 'old':
            return str(randrange(65,120))
        case 'abnormal':
            return str(randrange(18,500))
        case 'any':
            return str(randrange(8,120))

def speciesGen(furbro):
    match furbro:
        case True:
            specnum = randrange(0, vixen.SPECIES_MAX)
            match specnum:
                case 0:    
                    specnum1 = randrange(0, vixen.SPECIES_MAX)
                    while specnum1 == 0:
                        specnum1 = randrange(1, vixen.SPECIES_MAX)
                    if specnum1 == 3:
                        return "Robot"
                    else:
                        return f"Robot {vixen.species[specnum1]}"
                case 1:
                    specnum1 = randrange(0, vixen.SPECIES_MAX)
                    while specnum1 == 1:
                        specnum1 = randrange(0, vixen.SPECIES_MAX)
                    if specnum1 == 3:
                        return "Angel"
                    else:
                        return f"{vixen.species[specnum1]} Angel"
                case 2:
                    specnum1 = randrange(0, vixen.SPECIES_MAX)
                    while specnum1 == 2:
                        specnum1 = randrange(0, vixen.SPECIES_MAX)
                    if specnum1 == 3:
                        return "Demon"
                    else:
                        return f"{vixen.species[specnum1]} Demon"
                case 4:
                    specnum1 = randrange(5, vixen.SPECIES_MAX)
                    specnum2 = randrange(5, vixen.SPECIES_MAX)
                    while specnum1 == specnum2:
                        specnum2 = randrange(5, vixen.SPECIES_MAX)
                    return f"{vixen.species[specnum1]} {vixen.species[specnum2]} Hybrid"
                case _:
                    return vixen.species[specnum]
        case False:
            specnum = randrange(0, 12)
            match specnum:
                case 0:
                    return "Robot"
                case 1:
                    return "Angel"
                case 2:
                    return "Demon"
                case _:
                    return "Human"
        case _:
            print(vixen.tc.FAIL + 'Whuh?' + vixen.tc.ENDC)
            return f'{vixen.tc.FAIL}Whuh?{vixen.tc.ENDC}'

def dateFormatSwitch(format):
    match format.lower():
        case 'mm/dd/yyyy'|'m/d/yy'|'mm/dd/yy'|'m/d/yyyy'|'1':
            return 'mm/dd/yyyy'
        case 'dd/mm/yyyy'|'d/m/yy'|'dd/mm/yy'|'d/m/yyyy'|'2':
            return 'dd/mm/yyyy'
        case 'yyyy/mm/dd'|'yy/m/d'|'yy/mm/dd'|'yyyy/m/d'|'iso'|'iso 8601'|'default'|'3':
            return 'yyyy/mm/dd'
        case 'yyyy/dd/mm'|'yy/d/m'|'yy/dd/mm'|'yyyy/d/m'|'4':
            return 'yyyy/dd/mm'
        case _:
            return 'invalid'
        
def birthDateGen(rang,format):
    month = randrange(1,12)
    match month:
        case 2:
            day = randrange(1,28) # No leap years yet, that's a nightmare that I'm sleeping through for now :P
        case 1|3|5|7|8|10|12:
            day = randrange(1,31)
        case _:
            day = randrange(1,30)
    match rang.lower():
        case 'child'|'kid':
            year = randrange(2012,2016)
        case 'teen'|'teenager':
            year = randrange(2007,2011)
        case 'young':
            year = randrange(2007,2016)
        case 'young adult':
            year = randrange(1989,2006)
        case 'adult':
            year = randrange(1960,1988)
        case 'old'|'elder':
            year = randrange(1904,1959)
        case 'immortal'|'abnormal'|'inhuman':
            year = randrange(1524,2006)
        case _:
            year = randrange(1904,2016)
    match str.lower(format):
        case 'mm/dd/yyyy':
            return f'{str(month)}/{str(day)}/{str(year)}'
        case 'dd/mm/yyyy':
            return f'{str(day)}/{str(month)}/{str(year)}'
        case 'yyyy/mm/dd':
            return f'{str(year)}/{str(month)}/{str(day)}'
        case 'yyyy/dd/mm':
            return f'{str(year)}/{str(day)}/{str(month)}'
        case _:
            raise InvalidFormatError('Date not in format range.')

def magicLevel(abil):
    match abil:
        case 0:
            maglev = randrange(0,vixen.MAGIC_SKILL_CAP)
            return str(vixen.magic_skill[maglev])
        case _:
            return str(vixen.abilities[abil])

def abilityGen():
    try:
        numberOf = randrange(1,6)
        bilityNums = sample(range(0,vixen.ABILITY_MAX), numberOf)
        outputted = 0
        output = []
        while outputted != numberOf:
            output.append(str(vixen.abilities[bilityNums[outputted]]))
            outputted += 1
        return output
    except:
        errorLine = ['The function has failed','something broke somewhere']
        return errorLine

def skillGen():
    skillnum = randrange(0,5)
    match skillnum:
        case 0:
            return 'None'
        case 1:
            skillsel = randrange(0,vixen.SKILL_MAX)
            return f'{vixen.skills_landd[skillsel]}'
        case 2:
            skil1 = randrange(0,vixen.SKILL_MAX)
            skil2 = randrange(0,vixen.SKILL_MAX)
            while skil1 == skil2:
                skil1 = randrange(0,vixen.SKILL_MAX)
            kill1 = vixen.skills_landd[skil1]
            kill2 = vixen.skills_landd[skil2]
            return f'{kill1}, {kill2}'
        case 3:
            skil1 = randrange(0,vixen.SKILL_MAX)
            skil2 = randrange(0,vixen.SKILL_MAX)
            skil3 = randrange(0,vixen.SKILL_MAX)
            while skil1 == skil2|skil3:
                skil1 = randrange(0,vixen.SKILL_MAX)
            while skil2 == skil1|skil3:
                skil2 = randrange(0,vixen.SKILL_MAX)
            while skil3 == skil1|skil2:
                skil3 = randrange(0,vixen.SKILL_MAX)
            kill1 = vixen.skills_landd[skil1]
            kill2 = vixen.skills_landd[skil2]
            kill3 = vixen.skills_landd[skil3]
            return f'{kill1}, {kill2}, {kill3}'
        case 4:
            skil1 = randrange(0,vixen.SKILL_MAX)
            skil2 = randrange(0,vixen.SKILL_MAX)
            skil3 = randrange(0,vixen.SKILL_MAX)
            skil4 = randrange(0,vixen.SKILL_MAX)
            while skil1 == skil2|skil3|skil4:
                skil1 = randrange(0,vixen.SKILL_MAX)
            while skil2 == skil1|skil3|skil4:
                skil2 = randrange(0,vixen.SKILL_MAX)
            while skil3 == skil1|skil2|skil4:
                skil3 = randrange(0,vixen.SKILL_MAX)
            while skil4 == skil1|skil2|skil3:
                skil4 = randrange(0,vixen.SKILL_MAX)
            kill1 = vixen.skills_landd[skil1]
            kill2 = vixen.skills_landd[skil2]
            kill3 = vixen.skills_landd[skil3]
            kill4 = vixen.skills_landd[skil4]
            return f'{kill1}, {kill2}, {kill3}, {kill4}'
        case 5:
            skil1 = randrange(0,vixen.SKILL_MAX)
            skil2 = randrange(0,vixen.SKILL_MAX)
            skil3 = randrange(0,vixen.SKILL_MAX)
            skil4 = randrange(0,vixen.SKILL_MAX)
            skil5 = randrange(0,vixen.SKILL_MAX)
            while skil1 == skil2|skil3|skil4|skil5:
                skil1 = randrange(0,vixen.SKILL_MAX)
            while skil2 == skil1|skil3|skil4|skil5:
                skil2 = randrange(0,vixen.SKILL_MAX)
            while skil3 == skil1|skil2|skil4|skil5:
                skil3 = randrange(0,vixen.SKILL_MAX)
            while skil4 == skil1|skil2|skil3|skil5:
                skil4 = randrange(0,vixen.SKILL_MAX)
            while skil5 == skil1|skil2|skil3|skil4:
                skil5 = randrange(0,vixen.SKILL_MAX)
            kill1 = vixen.skills_landd[skil1]
            kill2 = vixen.skills_landd[skil2]
            kill3 = vixen.skills_landd[skil3]
            kill4 = vixen.skills_landd[skil4]
            kill5 = vixen.skills_landd[skil5]
            return f'{kill1}, {kill2}, {kill3}, {kill4}, {kill5}'
        case _:
            return 'Failed'

def personalityGen():
    personum = randrange(1,3)
    match personum:
        case 1:
            return f'{vixen.personality_traits[randrange(0,vixen.PERSONALITY_MAX)]}'
        case 2:
            perso1 = randrange(0,vixen.PERSONALITY_MAX)
            perso2 = randrange(0,vixen.PERSONALITY_MAX)
            while perso1 == perso2:
                perso1 = randrange(0,vixen.PERSONALITY_MAX)
            return f'{vixen.personality_traits[perso1]}, {vixen.personality_traits[perso2]}'
        case 3:
            perso1 = randrange(0,vixen.PERSONALITY_MAX)
            perso2 = randrange(0,vixen.PERSONALITY_MAX)
            perso3 = randrange(0,vixen.PERSONALITY_MAX)
            while perso1 == perso2|perso3:
                perso1 = randrange(0,vixen.PERSONALITY_MAX)
            while perso2 == perso1|perso3:
                perso2 = randrange(0,vixen.PERSONALITY_MAX)
            return f'{vixen.personality_traits[perso1]}, {vixen.personality_traits[perso2]}, {vixen.personality_traits[perso3]}'
        case _:
            return 'Failed'

def clear_screen():
    """Clears the terminal."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')