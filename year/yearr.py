# input the year they are born
born = int(input('please input your year you were born : '))

# the code for couting which generation they are
if born <= 1945:
    yearoutput = 'silent generation'
elif born <= 1964:
    yearoutput = 'baby boomer'
elif born <= 1980:
    yearoutput = 'generation X'
elif born <= 1996:
    yearoutput = 'millennials'
elif born <= 2012:
    yearoutput = 'generation z'
elif born <= 2025:
    yearoutput = 'generation alpha'

# printing the generation
print(f'you belong to:{yearoutput}')
