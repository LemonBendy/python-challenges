#Snow Poem Algorithm - www.101computing.net/snow-poem-algorithm
#A Python algorithm inspired by a poem by Brian Bilston: "Snow Poem"

import random

poem = "Words fell from the sky today I stood and watched them snowin'"
ending = "and as they settled on the ground, \nthey turned into this poem."
author = "Brian Bilston"

#Generating a list of all the words used in this poem
words = poem.split(" ")

print(" *   * *  *  Snow Poem  *   *  **   *")
print("")

#Accessing each word from the list, one at time
for word in words:
  indentation = random.randint(1,30) * " "
  print(indentation + word)

#The last section of this poem represents the snow covering the floor
print("")
print(ending)
print("")
print("_" * len(author))
print(author)
print(" **    * *   * * *  *  ** *  *  *  * ")