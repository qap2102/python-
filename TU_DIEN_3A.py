import ast

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input().strip()

        data_dict = ast.literal_eval(s)

        key_value = []
        sum_value = 0
        nums_string = 0

        for key, value in data_dict.items():
            if isinstance(value, int):
                sum_value += value
                if int(value)%2 == 0:
                    key_value.append(key)

            if isinstance(value, str):
                nums_string += 1

        print(f'({key_value}, {sum_value}, {nums_string})')
