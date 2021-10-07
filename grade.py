def GC(Grade):
    if Grade > 90:
        return "A"
    elif Grade > 80:
        return "B"
    elif Grade > 70:
        return "C"
    elif Grade > 60:
        return "D"
    else:
        return "F"


print([GC(i) for i in [67, 75, 45, 23, 100, 96, 73, 45, 89, 91]])