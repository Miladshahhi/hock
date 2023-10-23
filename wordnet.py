import nltk
from nltk.corpus import words
import random

# دانلود دیتابیس Wordnet اگر اجرا نشده باشد
nltk.download('wordnet')

# لیست کلمات انگلیسی از Wordnet
english_words = words.words()

# تابعی برای ساخت کلمه رمز با معنی
def generate_password_with_meaning(length):
    # انتخاب یک کلمه انگلیسی تصادفی از Wordnet
    word = random.choice(english_words)

    # اگر کلمه انتخابی کوتاه‌تر از طول مورد نظر باشد، آن را دوباره انتخاب کنید
    while len(word) < length:
        word = random.choice(english_words)

    # اگر کلمه بلند‌تر از طول مورد نظر باشد، آن را به طول مورد نظر ببرید
    word = word[:length]

    return word

# دریافت ورودی از کاربر
password_length = int(input("تعداد حروف کلمه رمز با معنی را وارد کنید: "))

# ساخت کلمه رمز با معنی
password_with_meaning = generate_password_with_meaning(password_length)

# نمایش کلمه رمز به کاربر
print("کلمه رمز با معنی: ", password_with_meaning)
