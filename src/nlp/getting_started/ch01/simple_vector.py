

doc1 = "meeting ... management ... meeting ... management ... meeting "
doc1 += "... management ... meeting ... meeting"

vector = [0, 0]

for word in doc1.split(" "):
    if word == "management":
        vector[0] = vector[0] + 1
    elif word == "meeting":
        vector[1] = vector[1] + 1

print(vector)

