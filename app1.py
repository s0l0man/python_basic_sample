import app2
import converters
import Utils
from converters import lbs_to_kg
from Utils import find_max

# name = ["John", "Marry"]
# print("start")
# for nm in name:
#     app2.greet_user(nm)
#
# num = input("Enter number: ")
# app2.number_text_conversion(num)
# print("finish")

# print(app2.square(16))

# message1 = input("")
# print(app2.emoji_convertor(message1))

# cat1 = cat()
# cat1.walk()
# cat1.be_annoying()

print(converters.lbs_to_kg(170))

numbers = [1,2,3,4,5,6,7,10]
maximum = find_max(numbers)
print(maximum)