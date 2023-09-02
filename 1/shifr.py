while True:
    alf_UA_EU = "абвгґдуєжзиіїйкльмншщпрстуфхцчшщьюяабвгґдуєжзиіїйкльмншщпрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWABCDEFGHIJKLMNOPQRSTUVW"
    step_key = int(input("Enter key: "))
    text = input("Message: ")
    result = ""
    for i in text:
        cell = alf_UA_EU.find(i)
        new_cell = cell + step_key
        if i in alf_UA_EU:
            result += alf_UA_EU[new_cell]
        else:
            result += i
    print(result)
