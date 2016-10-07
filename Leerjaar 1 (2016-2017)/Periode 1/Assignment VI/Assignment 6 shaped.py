shape = input(
    "What shape do you want?\n(1=full square, 2=hollow square, 3=full rectangle triangle, 4=full isosceles triangle, 5=full circle or 6=smiley) \n")
shape = int(shape)

size = (input("What size do you want? \n"))
size = int(size)
cnt = size
if shape == 1:
    full_square = ""
    line = ""

    while cnt > 0:
        line = line + "*"
        cnt = cnt - 1

    cnt = size

    while cnt > 0:
        full_square = full_square + line + "\n"
        cnt = cnt - 1
    result = full_square

if shape == 2:
    upper_line = ""
    middle_line = ""

    while cnt > 0:
        upper_line = upper_line + "*"
        cnt = cnt - 1

    cnt = size - 1

    if size > 2:
        middle_line = "*"
        while cnt > 1:
            middle_line = middle_line + " "
            cnt = cnt - 1
        middle_line = middle_line + "*"

    lower_line = upper_line
    hollow_square = upper_line + "\n"

    if size > 2:
        cnt = size - 1
        while cnt > 1:
            hollow_square = hollow_square + middle_line + "\n"
            cnt = cnt - 1
        hollow_square = hollow_square + lower_line
    else:
        hollow_square = hollow_square + lower_line
    result = hollow_square

if shape == 3:
    full_rectangle_triangle = ""
    cnt = 1
    cnt2 = 0
    line2 = ""
    while cnt <= size:
        while cnt2 < cnt:
            line2 = line2 + "*"
            cnt2 = cnt2 + 1
        cnt2 = 0
        full_rectangle_triangle = full_rectangle_triangle + line2 + "\n"
        line2 = ""
        cnt = cnt + 1
    result = full_rectangle_triangle

if shape == 4:
    cnt = 1
    cnt2 = 1
    cnt3 = 0
    line2 = "*"
    full_triangle = ""

    while cnt <= size:
        while cnt3 < (size - cnt):
            line2 = " " + line2
            cnt3 = cnt3 + 1
        while cnt2 < cnt:
            line2 = line2 + "**"
            cnt2 = cnt2 + 1
        cnt2 = 1
        full_triangle = full_triangle + line2 + "\n"
        line2 = "*"
        cnt = cnt + 1
        cnt3 = 0
    result = full_triangle

if shape == 5:
    full_circle = ""
    line3 = ""
    radius = size
    topleft_x = -radius
    topleft_y = radius
    cnt_x = -radius
    cnt_y = radius
    while cnt_y >= -radius and cnt_y <= radius:
        while cnt_x >= -radius and cnt_x <= radius:
            if (((cnt_x ** 2) + (cnt_y ** 2)) ** 0.5) < radius:
                line3 = line3 + "*"
            else:
                line3 = line3 + " "
            cnt_x = cnt_x + 1
        line3 = line3 + "\n"
        cnt_y = cnt_y - 1
        cnt_x = -radius
    full_circle = line3
    result = full_circle

if shape == 6:
    smiley = ""
    line3 = ""
    radius = size
    topleft_x = -radius
    topleft_y = radius
    cnt_x = -radius
    cnt_y = radius
    while cnt_y >= -radius and cnt_y <= radius:
        while cnt_x >= -radius and cnt_x <= radius:
            if (((cnt_x ** 2) + (cnt_y ** 2)) ** 0.5) > (radius - 1) and (((cnt_x ** 2) + (cnt_y ** 2)) ** 0.5) < radius:
                line3 = line3 + "*"
            else:
                if cnt_y == 2:
                    if cnt_x == -2 or cnt_x == 2:
                        line3 = line3 + "_"
                    else:
                        line3 = line3 + " "
                if cnt_y == 0:
                    if cnt_x == -2 or cnt_x == 2:
                        line3 = line3 + "0"
                    else:
                        line3 = line3 + " "
                if cnt_y == -2:
                    if cnt_x == -2:
                        line3 = line3 + "'\'"
                    elif cnt_x == 0:
                        line3 = line3 + "#"
                    elif cnt_x == 2:
                        line3 = line3 + "/"
                    if cnt_x != -2 and cnt_x != 0 and cnt_x != 2:
                        line3 = line3 + " "
                if cnt_y == -3:
                    if cnt_x == 4 or cnt_x == 5 or cnt_x == 6:
                        line3 = line3 + "_"
                    else:
                        line3 = line3 + " "
                if cnt_y != -3 and cnt_y != -2 and cnt_y != 0 and cnt_y != 2:
                    line3 = line3 + " "

            cnt_x = cnt_x + 1
        line3 = line3 + "\n"
        cnt_y = cnt_y - 1
        cnt_x = -radius
    smiley = line3
    result = smiley

print(result)
