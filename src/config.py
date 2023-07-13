from string import ascii_uppercase as alc

def read_config(txt):
    f = open(txt, "r")
    f = f.read().split("\n")
    r_one = f[0].split(" ")
    [s_one, f_one, r_s_one] = f[1].split(" ")
    r_two = f[2].split(" ")
    [s_two, f_two, r_s_two] = f[3].split(" ")
    r_three = f[4].split(" ")
    [s_three, f_three, r_s_three]= f[5].split(" ")

    s_one = alc.index(s_one)
    f_one = alc.index(f_one)
    r_s_one = alc.index(r_s_one)
    s_two = alc.index(s_two)
    f_two = alc.index(f_two)
    r_s_two = alc.index(r_s_two)
    s_three = alc.index(s_three)
    f_three = alc.index(f_three)
    r_s_three = alc.index(r_s_three)
    # print(s_one, s_two, s_three)


    return r_one, r_two, r_three, s_one, s_two, s_three, f_one, f_two, f_three, r_s_one, r_s_two, r_s_three

# print(read_config("./txt/test.txt"))