# create a function thst takes a list of numbers as input and returns the sum of those numbers
# write a function that takes a string as input and returns a number of vowels in that string
def sum_numbers(numbers):
    total=0
    for number in numbers:
        total+=number
    return total
number_list=(1,2,3,4,5,6)
print(sum_numbers(number_list))

def count_vowel(mystring):
    vowel="aeiou"
    count=0
    for letters in mystring:

        if letters.lower() in vowel:
            count+=1
    return count
word ="angela"
print(count_vowel(word))


