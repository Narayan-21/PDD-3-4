from random import seed, choices
from collections import Counter


eye_color = ("amber", "blue", "brown", "gray", "green", "hazel", "red", "violet")

class Person:
    def __init__(self, eye_color):
        self.eye_color = eye_color

seed(0)
persons = [Person(color) for color in choices(eye_color[2:], k=50)]

counts = Counter(p.eye_color for p in persons)
print(counts)

result = {color: counts.get(color, 0) for color in eye_color}
print(result)

def count_eye_colors(persons, possible_eye_colors):
    counts = Counter({color: 0 for color in possible_eye_colors})
    counts.update(p.eye_color for p in persons)
    return counts.most_common()

print(count_eye_colors(persons, eye_color))
