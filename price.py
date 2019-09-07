one = "Learn"
two = "python"

def get_summ(one, two, delimeter='&'):
    one = str(one)
    two = str(two)
    delimeter = str(delimeter)

    return f'{one}{delimeter}{two}'

print(get_summ(one, two).upper())

