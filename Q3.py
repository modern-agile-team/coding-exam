# -*- coding: utf-8 -*-
name, gender, age, height, weight = input().split( )

while (1):
    if (gender == "³²ÀÚ"):
        if (age >= 18 or age < 60):
            if (weight >= 70):
                if (height >= 170):
                    print(name)
                else:
                    break
            else:
                break
        else:  
            break     
    else:
        break


""" 
age >= 18 or age < 60
weight >= 70
height >= 170

"""
