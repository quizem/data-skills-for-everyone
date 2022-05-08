def get_grade_letter(grade):
    """
    Returns grade letter for a given numerical grade

    Parameters
    ----------
    grade : float
        input grade

    Returns
    -------
    str
        grade letter

    """
    if grade >= 0 and grade <=59.0:
        return 'F'
    elif grade > 59.0 and grade <= 69.0:
        return 'D'
    elif grade > 69.0 and grade <= 79.0:
        return 'C'
    elif grade > 79.0 and grade <= 89.0:
        return 'B'
    elif grade > 89.0:
        return 'A'
    else:
        print ('Please enter positive numbers only')
        return get_grade_letter(abs(grade))
    

# Calculate GPA
def calculate_gpa(grade):
    """
    Grade to GPA converter

    Parameters
    ----------
    grade : float
        grade to convert

    Returns
    -------
    float
        GPA of corresponding score

    """
    if grade >= 0 and grade <=59.0:
        return 0.0
    elif grade > 59.0 and grade <= 69.0:
        return 1.0
    elif grade > 69.0 and grade <= 79.0:
        return 2.0
    elif grade > 79.0 and grade <= 89.0:
        return 3.0
    elif grade > 89.0:
        return 4.0
    else:
        print ('Please enter a positive numbers only')
        return calculate_gpa(abs(grade))
    

def total_gpa(*grades):
    """
    Return over  all gpa for all grades obtained
    """
    result = [calculate_gpa(grade) for grade in grades]
    result = sum(result)/len(result)
    return round(result,1)
