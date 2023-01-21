list_numbers=[66, 98, 98, 98, 100, 98, 98, 100, 100, 100, 98]
def average(list_numbers):
    print("The mean is =",sum(list_numbers) / len(list_numbers))

if __name__ == '__main__':
    print(average(list_numbers))