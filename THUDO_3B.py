import ast

if __name__ == '__main__':
    for _ in range(int(input())):
        s = input().strip()

        data_dict = ast.literal_eval(s)

        vowels = {'a','e','i','o','u'}

        country = []
        cnt_cntry = 0
        cnt_thdo = 0

        for key, value in data_dict.items():
            if value[0].lower() in vowels:
                country.append(key)

            if len(key) > 5: cnt_cntry += 1
            if len(value) < 6: cnt_thdo += 1

        print(f'({country}, {cnt_cntry}, {cnt_thdo})')
