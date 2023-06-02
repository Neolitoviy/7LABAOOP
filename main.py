import time
import json


class Ball:
    def __init__(self, num_stripes):
        self.num_stripes = num_stripes
        self.colors = ["Blue", "Yellow", "Green"]

    def __str__(self):
        output = ""
        i = 0
        j = 0
        l = len(self.colors)
        for _ in range(self.num_stripes):
            output += f"Sector {_ + 1}:\n"
            while j < l - 2:
                output += f"{self.colors[i % l]},"
                i += 1
                j += 1
            j = 0
            output += f"{self.colors[i % l]},"
            i -= 1
            output += f"{self.colors[i % l]}.\n"
            i += 2
        return output


def read_input(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data['num_stripes']


def write_output(file_name, output):
    with open(file_name, 'w') as f:
        f.write(output)


def main():
    input_file = "input.json"
    output_file = "output.txt"

    num_stripes = read_input(input_file)

    ball = Ball(num_stripes)

    start_time = time.time()
    output = str(ball)
    end_time = time.time()

    print(f"Time taken: {end_time - start_time} seconds")
    print(output)

    write_output(output_file, output)


if __name__ == "__main__":
    main()
