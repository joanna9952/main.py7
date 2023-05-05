# exercise 1
def create_file(names):
    with open(names, 'w') as file:
        file.write("Anna, Elisabeth, Isabella, Maria, Meike, Valerie, Amelie, Hannah, Jessica, Helena")


create_file("names.txt")

# exercise 2
def transform_to_row(input_file, output_file):
    with open(input_file, "r") as file_1, open(output_file, "w") as file_2:
        text = file_1.read()
        words = text.split(",")
        for word in words:
            file_2.write(word.strip() + "\n")


transform_to_row("names.txt", "output.txt")

# exercise 3
def add_greeting(input_file, output_file):
    with open(input_file, "r") as file_1, open(output_file, "w") as file_2:
        text = file_1.read()
        words = text.split("\n")
        for word in words:
           if word.strip():
                file_2.write("Hello" + ' ' + word.strip() + "\n")


add_greeting("output.txt", "output_2.txt")

# exercise 4
def strip_greeting(input_file, output_file):
    with open(input_file, "r") as file_1, open(output_file, "w") as file_2:
        text = file_1.read()
        words = text.split()
        for word in words:
            if word != "Hello":
               file_2.write(word + "\n")


strip_greeting("output_2.txt", "stripped.txt")


# exercise 5
def create_file(surnames):
    with open(surnames, 'w') as file:
        file.write("Pichler ,Schmidt, Schneider, Fischer, Weber, Meyer, Wagner, Becker, Winter, Meier")


create_file("surnames.txt")

def transform_to_row(input_file, output_file):
    with open(input_file, "r") as file_1, open(output_file, "w") as file_2:
        text = file_1.read()
        words = text.split(",")
        for word in words:
            file_2.write(word.strip() + "\n")


transform_to_row("surnames.txt", "surnames_2.txt")

def combine_files(file1, file2, output_file):
    with open(file1, 'r') as file_1, open(file2, 'r') as file_2:
        # Read the contents of both files
        contents1 = file_1.readlines()
        contents2 = file_2.readlines()

    if len(contents1) != len(contents2):
        print("Error: Both files must have the same number of lines.")
        return

    with open(output_file, 'w') as file_out:
        for line1, line2 in zip(contents1, contents2):
            file_out.write(line1.strip() + ' ' + line2.strip() + '\n')


combine_files("output_2.txt", "surnames_2.txt", "combined.txt")

