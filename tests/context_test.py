from context import Context

objects = ['Knife', 'Man', 'Woman', 'Car', 'Garbage Can']

if __name__ == '__main__':
    contexual_analysis = Context()
    crime = contexual_analysis.find_crime(objects)
    print(crime)