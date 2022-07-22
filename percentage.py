Maths = input("Maths Marks: ")
English = input("English Marks: ")
Hindi= input("Hindi Marks: ")
Science = input("Science Marks: ")
Socialsci = input("Social Science Marks: ")

Maths = int(Maths)
English = int(English)
Hindi = int(Hindi)
Science = int(Science)
Socialsci = int(Socialsci)

percentage_calc = (Maths + English + Hindi +Science + Socialsci)
percentage_calc = int(percentage_calc)
final_score = (percentage_calc / 5)

print(final_score)