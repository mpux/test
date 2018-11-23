#!/bin/python


def write_car():
    """Za vpisovanje avtov datoteko"""
    car = input("Vpisi znamko avta: ")
    file = open("Avti.txt", "a")
    file.write(car)
    file.write("\n")
    file.close

write_car()
