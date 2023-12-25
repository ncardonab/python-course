from sys import path


# print(path)
# path.append('..\\extrapack.zip')

REPRESENTATIONS = {
    "0": (
        '🟧🟧🟧',
        '🟧  🟧',
        '🟧  🟧',
        '🟧  🟧',
        '🟧🟧🟧',
        ), 
    "1": (
        '    🟧',
        '  🟧🟧',
        ' 🟧 🟧',
        '    🟧',
        '    🟧',
        ), 
    "2": (
        '🟧🟧🟧',
        '    🟧',
        '🟧🟧🟧',
        '🟧    ',
        '🟧🟧🟧',
        ), 
    "3": (
        '🟧🟧🟧',
        '    🟧',
        '🟧🟧🟧',
        '    🟧',
        '🟧🟧🟧',
        ), 
    "4": (
        '🟧  🟧',
        '🟧  🟧',
        '🟧🟧🟧',
        '    🟧',
        '    🟧',
        ), 
    "5": (
        '🟧🟧🟧',
        '🟧    ',
        '🟧🟧🟧',
        '    🟧',
        '🟧🟧🟧',
        ),
    "6": (
        '🟧🟧🟧',
        '🟧    ',
        '🟧🟧🟧',
        '🟧  🟧',
        '🟧🟧🟧',
        ), 
    "7": (
        '🟧🟧🟧',
        '    🟧',
        '   🟧 ',
        '  🟧  ',
        ' 🟧   ',
        ), 
    "8": (
        '🟧🟧🟧',
        '🟧  🟧',
        '🟧🟧🟧',
        '🟧  🟧',
        '🟧🟧🟧',
        ), 
    "9": (
        '🟧🟧🟧',
        '🟧  🟧',
        '🟧🟧🟧',
        '    🟧',
        '🟧🟧🟧',
        ), 
}

number = input("Enter the number you want to display in seven-segment: ")

NUMBER_DISPLAY_HEIGHT = 5

BORDERS_STYLE = "🀄️"

OFFSET = BORDERS_STYLE * 3
NUMBERS_REPRESENTATION_WIDTH = BORDERS_STYLE * 4

top_bottom_borders = OFFSET + NUMBERS_REPRESENTATION_WIDTH * len( number )
LEFT_BORDER = f"{BORDERS_STYLE}  "
RIGHT_BORDER = f"  {BORDERS_STYLE}"
padding = LEFT_BORDER + ' ' * len(number) * 8 + BORDERS_STYLE

print(top_bottom_borders)
print(padding)

digits = [REPRESENTATIONS[digit] for digit in number]
for i in range(NUMBER_DISPLAY_HEIGHT):
    # print("  ".join([segment[i] for segment in digits]))
    for index, digit in enumerate( number ):
        number_representation = REPRESENTATIONS [digit][i]

        if len(number) == 1:
            print(LEFT_BORDER + number_representation, end=RIGHT_BORDER)
            continue
        if index == 0:
            print(LEFT_BORDER + number_representation, end="")
        elif index == len(number) - 1:
            print("  " + number_representation, end=RIGHT_BORDER)
        else:
            print("  " + number_representation, end="")

    print()

print(padding)
print(top_bottom_borders)


# import extra.good.best.sigma as sig
# import extra.good.alpha as alp
# from extra.iota import funI
# from extra.good.beta import funB
#
# print(sig.funS())
# print(alp.funA())
# print(funI())
# print(funB())