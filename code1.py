def check_circle_inscribed_square(r, a):
    r, a = int(r), int(a) # float 
    if r == int(a / 2): # без int
        return True
    return False # в один рядок 

print(check_circle_inscribed_square(4, 1))
print(check_circle_inscribed_square(4, 8))
