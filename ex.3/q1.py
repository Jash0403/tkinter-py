class SRMIST:
    school = "School of computing"

a = SRMIST()
a.dept1 = "Engineering and Technology"
a.dept2 = "CSE"
a.dept3 = "2nd year"
a.dept4 = "E1"
a.special = "core"
print(a.school,a.dept1,a.dept2,a.dept3,a.dept4,a.special)
del a.dept1
del a.dept2
print(a.school,a.dept3,a.dept4,a.special)