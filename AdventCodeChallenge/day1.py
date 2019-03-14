# Directions of North, East, South, West (by order in list)
faces = [0, 0, 0, 0]
# Start Direction 
face = 0

# Sets text file contents as variable f
with open('day1.txt') as f:
    data = f.read()

# tokens contain a letter and number, up to three digits on the number
blocks = data.split(', ')
for block in blocks:
    # First value in token, letter
    letter = block[0]
    # Second value in token, everything after the letter
    number = block[1:]
    # Left Direction
    if letter == 'L':
        face -= 1
    else:
        face += 1
    # %= Will not let the direction become an index of 4
    face %= len(faces)
    faces[face] += number

# Difference between north and south, difference between east and west
print(abs(faces[0] - faces[2]) + abs(faces[1] - faces[3]))
