# Rachel Hopping
# Complete
# Ask the user to input how many servings of sauce they want
# Display the serving size of sauce and the amount of each ingredient needed

SERVING_SIZE = 4
TOMATO_SAUCE = 2
TOMATO_PASTE = .333
GARLIC = 2
OREGANO = 1

serving_size = int(input("Enter the number of servings of spaghetti sauce you'd like to make: "))
portion = serving_size / 4
sauce = TOMATO_SAUCE * portion
paste = TOMATO_PASTE * portion
garlic = GARLIC * portion
oregano = OREGANO * portion

print(f'''To make {serving_size} servings of spaghetti sauce, you will need:
      {sauce:.2f} cups of tomato sauce,
      {paste:.2f} cups of tomato paste,
      {garlic:.2f} cloves of garlic,
      {oregano:.2f} tablespoon oregano''')
