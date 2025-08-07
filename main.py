print("Hello VSCode!")
fruit_list = ["apple", "banana", "cherry"]
# リストから偶数だけを抽出する関数
def extract_even_fruits(fruits):
    return [fruit for fruit in fruits if len(fruit) % 2 == 0]
# 関数「extract_even_fruits」に要素数が10のリストを渡して、戻り値のリストの合計値と平均値を計算して表示する
result = extract_even_fruits(fruit_list)
if result:
    total_length = sum(len(fruit) for fruit in result)
    average_length = total_length / len(result)
    print(f"合計: {total_length}, 平均: {average_length}")
else:
    print("条件を満たす果物はありませんでした。")


# 数値のリストを受け取り、各値に基づいてカテゴリを分類する関数を作成してください

# 条件:

# 1. 値が0以下の場合は "Low" カテゴリに分類してください

# 2. 値が1以上10以下の場合は "Medium" カテゴリに分類してください

# 3. 値が10を超える場合は "High" カテゴリに分類してください

# 4. 入力リストには整数が含まれるものとします

# 結果を辞書形式で返してください。キーがカテゴリ名で、値が該当する数値のリストとします

def categorize_numbers(numbers):
    categories = {
        "Low": [],
        "Medium": [],
        "High": []
    }
    for num in numbers:
        if num <= 0:
            categories["Low"].append(num)
        elif 1 <= num <= 10:
            categories["Medium"].append(num)
        else:
            categories["High"].append(num)
    return categories
# 出力 例
numbers = [-5, 0, 3, 7, 12, 15, -2, 8]
categorized_numbers = categorize_numbers(numbers)
print(categorized_numbers)






def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    bmi = weight / (height ** 2)
    return bmi



# BMIを計算する関数
def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    bmi = weight / (height ** 2)
    return bmi

# BMIを表示してから戻り値を返す
def display_bmi(weight, height):
    bmi = calculate_bmi(weight, height)
    print(f"BMI: {bmi}")
    return bmi





person = {"name": "山田太郎", "age": 30, "prefecture": "東京都"}
person["job"] = "エンジニア"

if isinstance(person, dict):
    for key, value in person.items():
        print(f"{key}: {value}")
else:
    print("person is not a dictionary.")

# personの各値を要素に持つリストを作成
person_values = list(person.values())
print(person_values)



def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle given its base and height.
    Parameters:
        base (float): The length of the base of the triangle.
        height (float): The height of the triangle.
    Returns:
        float: The area of the triangle.
    """

    return base * height / 2




# リストから偶数だけを抽出する関数
def extract_even_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result