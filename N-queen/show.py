import tkinter as tk
from PIL import Image, ImageTk

def show_image():
    root = tk.Tk()  # ابتدا ساخت پنجره اصلی
    root.title("Test Image Display")

    try:
        # بارگذاری و تغییر اندازه تصویر
        queen_img = Image.open("queen.png")
        queen_img = queen_img.resize((100, 100))
        queen_image = ImageTk.PhotoImage(queen_img)

        # نمایش تصویر در یک Label
        label = tk.Label(root, image=queen_image)
        label.image = queen_image  # نگه‌داری رفرنس برای جلوگیری از حذف شدن
        label.pack()

    except Exception as e:
        print(f"Error: {e}")

    root.mainloop()

show_image()
