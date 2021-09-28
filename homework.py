import math
import pandas as pd

n = int(input("Enter number of students: "))
print("\n")

hs_gpa = []
college_gpa = []

for i in range(1, n + 1):
    print("Student", i)
    hs_gpa.append(float(input("HS GPA: ")))
    college_gpa.append(float(input("College GPA: ")))
    print("\n")

df = pd.DataFrame(data={'HS GPA': hs_gpa, 'College GPA': college_gpa})
#df = pd.read_csv("gpa.csv")
hs_gpa = df['HS GPA']
#n = hs_gpa.size
x_div_mean_x = hs_gpa - hs_gpa.mean()
x_div_mean_x_pow = x_div_mean_x * x_div_mean_x
s_xx = math.sqrt(x_div_mean_x_pow.sum() / (n - 1))
#print(s_xx)
#print(x_div_mean_x)
#print(x_div_mean_x_pow)

college_gpa = df['College GPA']
y_div_mean_y = college_gpa - college_gpa.mean()
y_div_mean_y_pow = y_div_mean_y * y_div_mean_y
s_yy = math.sqrt(y_div_mean_y_pow.sum() / (n - 1))
#print(s_yy)
#print(y_div_mean_y)
#print(y_div_mean_y_pow)

s_xy = (x_div_mean_x * y_div_mean_y).sum() / (n - 1)
#print(s_xy)

correlation = s_xy / (s_xx * s_yy)
print("The correlation coefficient is: ", correlation)

if correlation > 0.9:
    print("Strong positive correlation")
elif correlation < -0.9:
    print("Strong negative correlation")
elif -0.1 < correlation < 0.1:
    print("No correlation")

