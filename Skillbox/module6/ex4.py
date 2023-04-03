like = 0
dislike = 0
review = int


while review != 0:
    review = int(input("Review: "))
    if review > 0:
        like += 1
    elif review < 0:
        dislike += 1
    

print(f"Dislike: {dislike}")
print(f"Like: {like}")
