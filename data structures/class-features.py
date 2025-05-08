# Stack klassini yaratamiz
class Stack:
    def __init__(self):
        # Stack (ustuncha) elementlarini saqlash uchun bo'sh ro'yxat
        self.stack = []

    # Elementni stack'ga qo'shish (push operatsiyasi)
    def push(self, x):
        self.stack.append(x)

    # Stack'ning eng yuqori (oxirgi) elementini olish
    def top(self):
        if len(self.stack) == 0:
            # Stack bo'sh bo'lsa, xato chiqaramiz
            raise IndexError("top from empty stack")
        return self.stack[-1]

    # Stack'ning eng yuqori elementini olib tashlash (pop)
    def pop(self):
        if len(self.stack) == 0:
            # Stack bo'sh bo'lsa, xato chiqaramiz
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    # Stack obyektini chiroyli ko'rinishda chiqarish uchun
    def __repr__(self):
        return str(self.stack)

    # Stack uzunligini (elementlar sonini) olish uchun
    def __len__(self):
        return len(self.stack)

# Stack obyektini yaratamiz
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)       # [1, 2, 3]
print(len(s))  # 3
print(s.top()) # 3

# Elementlarni olib tashlaymiz
s.pop()        # 3 ni olib tashlaydi
print(s)       # [1, 2]

# Bo'sh stackdan pop qilish xatolik beradi
s.pop()        # 2
s.pop()        # 1
s.pop()        # IndexError: pop from empty stack
