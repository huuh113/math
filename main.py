import random
from fractions import Fraction

# Class Math để chứa số nguyên và hỗ trợ thực hiện các phép toán số học cơ bản.
class Math:
    def __init__(self, num):
        self.num = num

    @staticmethod
    def operations(a, b):
        """
        Thực hiện các phép toán cơ bản giữa hai số a và b.
        Trả về danh sách gồm:
        - Tổng của a và b.
        - Hiệu của a và b.
        - Tích của a và b.
        - Thương của a và b (nếu b khác 0, ngược lại trả về "0").
        """
        return [a + b, a - b, a * b, a / b if b != 0 else "0"]

# Hàm `ko_chia_het` để xử lý việc chia số không hết, trả về kết quả dưới dạng số thập phân tuần hoàn nếu cần.
def ko_chia_het(a, b):
    """
    Chia hai số a và b, trả về kết quả dưới dạng chuỗi:
    - Phần nguyên của kết quả.
    - Phần thập phân không tuần hoàn (nếu có).
    - Phần thập phân tuần hoàn (nếu có).
    """
    frac = Fraction(a, b)  # Tạo phân số từ a và b.
    integer_part = frac.numerator // frac.denominator  # Phần nguyên của phép chia.
    decimal_part = frac.numerator % frac.denominator  # Phần dư của phép chia.

    if decimal_part == 0:  # Nếu chia hết.
        return str(integer_part)

    seen_remainders = {}  # Lưu vết các phần dư đã gặp để phát hiện tuần hoàn.
    decimals = []
    index = 0
    recurring_start = None

    # Tìm phần thập phân tuần hoàn (nếu có).
    while decimal_part != 0:
        if decimal_part in seen_remainders:
            recurring_start = seen_remainders[decimal_part]
            break
        seen_remainders[decimal_part] = index
        decimal_part *= 10
        decimals.append(decimal_part // frac.denominator)
        decimal_part %= frac.denominator
        index += 1

    if recurring_start is not None:  # Nếu có phần tuần hoàn.
        non_recurring = ''.join(map(str, decimals[:recurring_start]))
        recurring = ''.join(map(str, decimals[recurring_start:]))
        return f"{integer_part},{non_recurring}({recurring})"
    else:  # Nếu không có phần tuần hoàn.
        non_recurring = ''.join(map(str, decimals))
        return f"{integer_part},{non_recurring}"

# Hàm skibidi để thực hiện các phép toán ngẫu nhiên với nhiều lần lặp.
def skibidi(a, b, max_skibidi=10):
    # tối đa 10 phép tính(max_skibidi)
    for i in range(max_skibidi):
        a.num = random.randint(1, 100000000)
        b.num = random.randint(1, 100000000)

        results = Math.operations(a.num, b.num)

        print(f"{i+1}:")
        print(f"{a.num} + {b.num} = {results[0]}")
        print(f"{a.num} - {b.num} = {results[1]}")
        print(f"{a.num} * {b.num} = {results[2]}")
        print(f"{a.num} / {b.num} = {ko_chia_het(a.num, b.num) if b.num != 0 else '0'}")
        print("-" * 20)

def main():
    # Tạo a và b với các số random từ 1 đến 100000000
    a = Math(num=random.randint(1, 100000000))
    b = Math(num=random.randint(1, 100000000))
    # sử dụng hàm để tính
    skibidi(a, b)

# bắt đầu
if __name__ == "__main__":
    main()

# Code made by huh?
