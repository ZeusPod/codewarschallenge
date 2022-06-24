"""

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'

"""

def get_grade(s1, s2, s3):
    promedio = (s1 + s2 + s3) / 3 
    if promedio <= 60:
        return "F"
    elif promedio >=61 and promedio <=69:
        return "D"
    elif promedio >=70 and promedio <=79:
        return "C"
    elif promedio >=80 and promedio <=89:
        return "B"
    elif promedio >=90:
        return "A"
