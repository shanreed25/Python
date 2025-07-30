with open("/Users/shann/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

# with open("../../Desktop/my_file.txt", mode='a' ) as file:
#     file.write("\nI am a mother of four")

    # Relative: ../../Desktop/my_file.txt OR
# Absolute: /Users/shann/Desktop/my_file.txt