import time
jeda = 1.5
time.sleep(jeda)

print("Let's learn some types of data :)")
print()

#Tipe data dasar
print("====TIPE DATA====")

data_int   = 8
data_float = 8.5
data_str   = "hello"
data_bool  = True
print()

print("data integer =", data_int, ", type data=", type(data_int))
print("data float =", data_float, ", type data=", type(data_float))
print("data string =", data_str, ", type data=", type(data_str))
print("data boolean =", data_bool, ", type data=", type(data_bool))
print()
#ada error ya ges ya, nanti admin benerin
time.sleep(jeda)

#Casting Data

##Casting Integer
print("====INTEGER====")
data_int = 9
print("data integer =", data_int)
print("data casted:")

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int)
print("in float = ", data_float)
print("in string = ", data_str)
print("in boolean = ", data_bool)
print()
time.sleep(jeda)

##Casting Float
print("====FLOAT====")
data_float = 9.5
print(data_float)
print("data casted:")

data_integer = int(data_float)
data_str     = str(data_float)
data_bool    = bool(data_float)
print("in integer = ", data_integer)
print("in string = ", data_str)
print("in boolean = ", data_bool)
print()
time.sleep(jeda)

##String
print("====STRING====")
data_str = "byan"
print(data_str)
print("data casted:")

data_bool  = bool(data_str)
print("data boolean = ", data_bool)
print()
time.sleep(jeda)

##Boolean
print("====BOOLEAN====")
data_bool = True
print(data_bool)
print("data casted:")


data_str   = str(data_bool)
print("data string = ", data_str)
print()
time.sleep(jeda)

#Pengertian
pengertian = [
    "did you guys have a question like..",
    "what are those for?, right?"
]

for baris in pengertian:
    for huruf in baris:
        print(huruf, end="", flush=True)
        time.sleep(0.05)
    print()
    time.sleep(0.30)

print()
time.sleep(jeda)

pengertian2 = [
    "okay chill chill you don't have to feel like",
    "-oh no im so stupid...-",
    "-even this is the basic of the point i didn't even know-",
    "it's okay guys... my name is abyan and i created this little program",
    "and now im gonna explain you the definiton of those types of datas",
    "hope you enjoy what i made :)"
]

for baris in pengertian2:
    for huruf in baris:
        print(huruf, end="", flush=True)
        time.sleep(0.05)
    print()
    time.sleep(0.30)

print()
time.sleep (jeda)

#pengertian Integer
pengertian_integer = [
    "first, integer",
    "integer is the type of data that are real numbers",
    "for example like 1, 2, 3, others",
    "it doesn't matter what types the number is",
    "odd or even",
    "if you guys are questioning like 'how about the numbers that has decimal in it?'",
    "good question right here",
    "if there's a number that has decimal in it it's not integer",
    "now, let me introduce you the second type of data, float"
]

for baris in pengertian_integer:
    for huruf in baris:
        print(huruf, end="", flush=True)
        time.sleep(0.05)
    print()
    time.sleep(0.30)

time.sleep(jeda)
print()

#pengertian float
pengertian_float = [
    "float, as i explain that before",
    "float is type of data that has decimal numbers",
    "for example like 1.5, 4.8 and other decimal numbers",
    "but you have to know the difference between integer and float depends the decimal in the numbers",
    "if the data just single or even bunch of numbers it's integer",
    "and, if the data contains a decimal in numbers it's automatically call float",
    "i hope you guys already know between integer and float",
    "i can say it's easy to see the difference cause you just have to focus on the decimal to decide what type those datas"
]

for baris in pengertian_float:
    for huruf in baris:
        print(huruf, end="", flush=True)
        time.sleep(0.05)
    print()
    time.sleep(0.30)

time.sleep(jeda)
print()

#pengertian string
pengertian_string = [
    "now we move to the third data type, string",
    "before i start, the string that i mention it's not the string that you see inside of your house corner that made from spider",
    "no it's not",
    "the string that i mention it's the type of data that contains a letter",
    "no matter if it's a single word, single sentence or even a paragraph",
    "if you ever make a journal",
    "it is made of string that i've explain to you",
    "but i remind you",
    "string just contain letters",
    "not the simbol like '.' or '()'",
    "i hope you understand"
]

for baris in pengertian_string:
    for huruf in baris:
        print(huruf, end="", flush=True)
        time.sleep(0.05)
    print()
    time.sleep(0.30)

time.sleep(jeda)
print()

#pengertian Boolean
pengertian_boolean = [
    "now the fourth type or the last data type that i explain in this session is boolean",
    "boolean is type of data that determine of the output is it false of true",
    "for example like this:",
    "if 8 = eight is true",
    "and",
    "if 8 = besides-eight is false",
    "then you write 'eight' the output is 'true'",
    "but if you write the word of numbers that is not eight; for example like:",
    "'one' or 'five'",
    "the output must be 'false' cause the data that you put in input it's not true based on the code that already you set before"
]

for baris in pengertian_boolean:
    for huruf in baris:
        print(huruf, end="", flush=True)
        time.sleep(0.05)
    print()
    time.sleep(0.30)

time.sleep(jeda)
print()

pengertian_boolean2 = [
    "i have other example of boolean",
    "if you set the the question code:",
    "what's the food the rabbit usually eat?",
    "then you set the true code is 'carrot'",
    "and the false one is 'manggo'",
    "when you run the program, you enter the input and if it says carrot it will say 'true'",
    "but, if you enter manggo for the input, the output is false",
    "yeah just like that",
    "i hope you understand from what i explain before"
]

for baris in pengertian_boolean2:
    for huruf in baris:
        print(huruf, end="", flush=True)
        time.sleep(0.05)
    print()
    time.sleep(0.30)

time.sleep(jeda)
print()

#penutup
penutup = [
    "okay guys, maybe that's all from me",
    "i hope you guys like this little program that i made around for hours",
    "and i hope you understand what i explain about the types of data that usually been used for programming",
    "honestly, It doesn't feel like the end is already here",
    "i made this little program for hours but when i run, it's already at the end just for minutes",
    "i know this is not good as other programs out there",
    "cause im just starting to learn about programming for a few days ago",
    "i hope i can make a bigger project than this",
    "okay guys thank you for enjoying my little program",
    "im sorry if there any mistakes or you have bored when the program is runned",
    "i'll see you at the my next program that are more interesting and more educating",
    "i can say now coding is fun, goodbye :)"
]

for baris in penutup:
    for huruf in baris:
        print(huruf, end="", flush=True)
        time.sleep(0.05)
    print()
    time.sleep(0.30)

print()
