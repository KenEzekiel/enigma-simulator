from string import ascii_uppercase as alc

def read_config(txt):
    f = open(txt, "r")
    f = f.read().split("\n")
    r_one = f[0].split(" ")
    [s_one, f_one] = f[1].split(" ")
    r_two = f[2].split(" ")
    [s_two, f_two] = f[3].split(" ")
    r_three = f[4].split(" ")
    [s_three, f_three]= f[5].split(" ")

    s_one = r_one.index(s_one)
    f_one = r_one.index(f_one)
    s_two = r_two.index(s_two)
    f_two = r_two.index(f_two)
    s_three = r_three.index(s_three)
    f_three = r_three.index(f_three)

    cnt = 0
    dr_one = {}
    dr_two = {}
    dr_three = {}
    for i in alc:
        dr_one[i] = r_one[cnt]
        dr_two[i] = r_two[cnt]
        dr_three[i] = r_three[cnt]
        cnt += 1

    return dr_one, dr_two, dr_three, s_one, s_two, s_three, f_one, f_two, f_three

# print(read_config("./txt/test.txt"))