"""
Count the number of times the first letter of the English alphabet appears in the following
paragraph.

"A machine is a great moral educator. If a horse or a donkey won't go, men lose their
tempers and beat it; if a machine won't go, there is no use beating it. You have to think and
try till you find what is wrong. That is real education."

- Gilbert Murray

"""

paragraph = "A machine is a great moral educator. If a horse or a donkey won't go, men lose their tempers and beat it; if a machine won't go, there is no use beating it. You have to think and try till you find what is wrong. That is real education."

print(f"The first letter of the English alphabet appears : {paragraph.count('a', 1, len(paragraph))}")



paragraph = "A machine is a great moral educator. If a horse or a donkey won't go, men lose their tempers and beat it; if a machine won't go, there is no use beating it. You have to think and try till you find what is wrong. That is real education.".lower()

print(f"The first letter of the English alphabet appears : {paragraph.count('a', 0, len(paragraph))}")
