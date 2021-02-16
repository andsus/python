rain = { 3: 'Pling', 5: 'Plang', 7: 'Plong'}

def convert(number):
    # Using list comprehension
    # result = [ rain[factor] for factor in [3,5,7] if number % factor == 0 ]
    # Using python 3.8, that support ordered dictionary
    result = [ v for k,v in rain.items() if number % k == 0 ]
    
    # for factor in [3,5,7]:
    #     if number % factor == 0:
    #         result += rain[factor]
    return "".join(result) or str(number)
