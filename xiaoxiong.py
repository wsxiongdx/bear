
from PIL import Image, ImageDraw, ImageFilter,ImageTk
import tkinter as tk
from tkinter import filedialog,ttk
import math



img = None

fill_intensity =255

def generate_image():
    global img
    img_size = (int(img_size_entry_w.get()), int(img_size_entry_h.get()))
    r = float(r_entry.get())
    d = float(d_entry.get())
    size_x = int(grid_size_entry_x.get())
    size_y = int(grid_size_entry_y.get())
    blur_radius = int(blur_radius_entry.get())
    distance_x = (img_size[0] - (size_x - 1) * d ) / 2
    distance_y = (img_size[1] - (size_y - 1) * d ) / 2

    img = Image.new('L', img_size, color='black')
    draw = ImageDraw.Draw(img)
    points = []

    for i in range(size_x):
        for j in range(size_y):
            x = distance_x + i * d
            y = distance_y + j * d

            points.append((x, y))

    for point in points:
        x, y = point

        if square1.get():
            draw.rectangle((x - r, y - r, x + r, y + r), fill=fill_intensity)
        else:
            draw.ellipse((x - r, y - r, x + r, y + r), fill=fill_intensity)
            if circle_ring.get():
                p = float(P.get())
                draw.ellipse((x-p*r, y-p*r, x+p*r, y+p*r), fill='black')

    img = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))



    image_window = tk.Toplevel()
    image_window.title("生成的图像")

    resized_img = img.resize((800, 600))

    photo = ImageTk.PhotoImage(resized_img)

    image_label = tk.Label(image_window, image=photo)
    image_label.image = photo
    image_label.pack()


    image_window.mainloop()

def triangle_image():
    global img
    img_size = (int(img_size_entry_w.get()), int(img_size_entry_h.get()))
    r = float(r_entry.get())
    d = float(d_entry.get())
    size_x = int(grid_size_entry_x.get())
    size_y = int(grid_size_entry_y.get())

    blur_radius = int(blur_radius_entry.get())

    img = Image.new('L', img_size, color='black')
    draw = ImageDraw.Draw(img)
    points = []

    distance_x = (img_size[0] - (size_x - 1) * d + 2 * r) / 2
    distance_y = (img_size[1] - (size_y - 1) * math.sqrt(3 / 4) * d ) / 2

    for i in range(size_x):
        for j in range(0, size_y, 2):
            x = distance_x + i * d - d / 4
            y = distance_y + j * d * math.sqrt(3 / 4)
            points.append((x, y))

    for i in range(size_x - 1):
        for j in range(1, size_y, 2):
            x = distance_x + i * d + d / 4
            y = distance_y + j * d * math.sqrt(3 / 4)
            points.append((x, y))

    for i in range(size_x + 6):
        for j in range(3):
            x = distance_x - 3 * d + i * d - d / 4
            y = distance_y - 3 * d * math.sqrt(3 / 4) + j * d * math.sqrt(3 / 4)
            points.append((x, y))

    # 下方矩阵
    for i in range(size_x + 6):
        for j in range(3):
            x = distance_x - 3 * d + i * d - d / 4
            y = distance_y + size_y * math.sqrt(3 / 4) * d + j * d * math.sqrt(3 / 4)
            points.append((x, y))

    # 左方矩阵
    for i in range(3):
        for j in range(size_y + 6):
            x = distance_x - 3 * d + i * d - d / 4
            y = distance_y - 3 * d * math.sqrt(3 / 4) + j * d * math.sqrt(3 / 4)
            points.append((x, y))

    # 右方矩阵
    for i in range(3):
        for j in range(size_y + 6):
            x = distance_x + (size_x) * d + i * d - d / 4
            y = distance_y - 3 * d * math.sqrt(3 / 4) + j * d * math.sqrt(3 / 4)
            points.append((x, y))

    for point in points:
        x, y = point
        if square1.get():
            draw.rectangle((x - r, y - r, x + r, y + r), fill=fill_intensity)
        else:
            draw.ellipse((x - r, y - r, x + r, y + r), fill=fill_intensity)
            if circle_ring.get():
                p = float(P.get())
                draw.ellipse((x-p*r, y-p*r, x+p*r, y+p*r), fill='black')


    img = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))
    # Convert image to numpy array and show

    # 创建一个新的窗口来显示图像
    image_window = tk.Toplevel()
    image_window.title("生成的图像")

    # 将图像调整大小以适应窗口大小
    resized_img = img.resize((800, 600))

    # 将调整大小后的图像转换为PhotoImage对象
    photo = ImageTk.PhotoImage(resized_img)

    # 创建一个带有图像的标签
    image_label = tk.Label(image_window, image=photo)
    image_label.image = photo  # 保持对图像对象的引用，以防止被垃圾回收
    image_label.pack()

    # 显示新窗口
    image_window.mainloop()

def hexagonal_image():
    global img
    img_size = (int(img_size_entry_w.get()), int(img_size_entry_h.get()))
    r = float(r_entry.get())
    d = float(d_entry.get())
    size_x = int(grid_size_entry_x.get())
    size_y = int(grid_size_entry_y.get())
    # x_offset = float(x_offset_entry.get())
    # y_offset = float(y_offset_entry.get())
    blur_radius = int(blur_radius_entry.get())

    img = Image.new('L', img_size, color='black')
    draw = ImageDraw.Draw(img)
    points = []

    distance_x = (img_size[0] - (size_x - 1) * d + 2 * r) / 2
    distance_y = (img_size[1] - (size_y - 1) * math.sqrt(3 / 4) * d ) / 2

    # 偶数行(含0 索引)
    for i in range(size_x - 1):
        for j in range(0, size_y, 2):
            x = distance_x + i * d + d / 4
            y = distance_y + j * d * math.sqrt(3 / 4)
            points.append((x, y))

    # 奇数行(含0 索引)
    for i in range(size_x):
        for j in range(1, size_y, 2):
            x = distance_x + i * d - d / 4
            y = distance_y + j * d * math.sqrt(3 / 4)
            points.append((x, y))

    """外围方形格子"""
    # 上方矩阵
    for i in range(size_x + 6):
        for j in range(3):
            x = distance_x - 3 * d + i * d - d / 4
            y = distance_y - 3 * d * math.sqrt(3 / 4) + j * d * math.sqrt(3 / 4)
            points.append((x, y))

    # 下方矩阵
    for i in range(size_x + 6):
        for j in range(3):
            x = distance_x - 3 * d + i * d - d / 4
            y = distance_y + size_y * math.sqrt(3 / 4) * d + j * d * math.sqrt(3 / 4)
            points.append((x, y))
    # 左方矩阵
    for i in range(3):
        for j in range(size_y + 6):
            x = distance_x - 3 * d + i * d - d / 4
            y = distance_y - 3 * d * math.sqrt(3 / 4) + j * d * math.sqrt(3 / 4)
            points.append((x, y))
    # 右方矩阵
    for i in range(3):
        for j in range(size_y + 6):
            x = distance_x + (size_x) * d + i * d - d / 4
            y = distance_y - 3 * d * math.sqrt(3 / 4) + j * d * math.sqrt(3 / 4)
            points.append((x, y))

    for point in points:
        x, y = point
        if square1.get():
            draw.rectangle((x - r, y - r, x + r, y + r), fill=fill_intensity)
        else:
            draw.ellipse((x - r, y - r, x + r, y + r), fill=fill_intensity)
            if circle_ring.get():
                p = float(P.get())
                draw.ellipse((x-p*r, y-p*r, x+p*r, y+p*r), fill='black')

    points1 = []
    # 黑
    for i in range(1, size_x // 3 + 1):
        for j in range(1, size_y // 2 + 1):

            x = distance_x + (3 * i - 2) * d - d / 4
            y = distance_y + (2 * j - 1) * d * math.sqrt(3 / 4)
            points1.append((x, y))

    for i in range(1, size_x // 3 + 1):
        for j in range(1, size_y // 2 + 1):

            x = distance_x + (3 * i - 1) * d + d / 4
            y = distance_y + (2 * j - 2) * d * math.sqrt(3 / 4)
            points1.append((x, y))

    for point1 in points1:
        x, y = point1
        if square1.get():
            draw.rectangle((x - r, y - r, x + r, y + r), fill='black')
        else:
            draw.ellipse((x - r, y - r, x + r, y + r), fill='black')




    img = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))

    # 创建一个新的窗口来显示图像
    image_window = tk.Toplevel()
    image_window.title("生成的图像")

    # 将图像调整大小以适应窗口大小
    resized_img = img.resize((800, 600))

    # 将调整大小后的图像转换为PhotoImage对象
    photo = ImageTk.PhotoImage(resized_img)

    # 创建一个带有图像的标签
    image_label = tk.Label(image_window, image=photo)
    image_label.image = photo  # 保持对图像对象的引用，以防止被垃圾回收
    image_label.pack()

    # 显示新窗口
    image_window.mainloop()

def Kagome_image():
    global img
    img_size = (int(img_size_entry_w.get()), int(img_size_entry_h.get()))
    r = float(r_entry.get())
    d = float(d_entry.get())
    size_x = int(grid_size_entry_x.get())
    size_y = int(grid_size_entry_y.get())
    # x_offset = float(x_offset_entry.get())
    # y_offset = float(y_offset_entry.get())
    blur_radius = int(blur_radius_entry.get())

    img = Image.new('L', img_size, color='black')
    draw = ImageDraw.Draw(img)
    points = []

    distance_x = (img_size[0] - (size_x - 1) * d + 2 * r) / 2
    distance_y = (img_size[1] - (size_y - 1) * math.sqrt(3 / 4) * d ) / 2



    # 偶数行(含0 索引)
    for i in range(size_x):
        for j in range(0, size_y, 2):
            x = distance_x + i * d - d / 4
            y = distance_y + j * d * math.sqrt(3 / 4)
            points.append((x, y))

    # 奇数行(含0 索引)
    for i in range(size_x - 1):
        for j in range(1, size_y, 2):
            x = distance_x + i * d + d / 4
            y = distance_y + j * d * math.sqrt(3 / 4)
            points.append((x, y))
    """外围方形格子"""
    # 上方矩阵
    for i in range(size_x + 6):
        for j in range(3):
            x = distance_x - 3 * d + i * d - d / 4
            y = distance_y - 3 * d * math.sqrt(3 / 4) + j * d * math.sqrt(3 / 4)
            points.append((x, y))

    # 下方矩阵
    for i in range(size_x + 6):
        for j in range(3):
            x = distance_x - 3 * d + i * d - d / 4
            y = distance_y + size_y * math.sqrt(3 / 4) * d + j * d * math.sqrt(3 / 4)
            points.append((x, y))
    # 左方矩阵
    for i in range(3):
        for j in range(size_y + 6):
            x = distance_x - 3 * d + i * d - d / 4
            y = distance_y - 3 * d * math.sqrt(3 / 4) + j * d * math.sqrt(3 / 4)
            points.append((x, y))
    # 右方矩阵
    for i in range(3):
        for j in range(size_y + 6):
            x = distance_x + (size_x) * d + i * d - d / 4
            y = distance_y - 3 * d * math.sqrt(3 / 4) + j * d * math.sqrt(3 / 4)
            points.append((x, y))

    for point in points:
        x, y = point
        if square1.get():
            draw.rectangle((x - r, y - r, x + r, y + r), fill=fill_intensity)
        else:
            draw.ellipse((x - r, y - r, x + r, y + r), fill=fill_intensity)
            if circle_ring.get():
                p = float(P.get())
                draw.ellipse((x-p*r, y-p*r, x+p*r, y+p*r), fill='black')

    points1 = []
    # 黑
    for i in range(1, size_x // 2 + 1):
        for j in range(1, size_y // 3 + 1):
            x = distance_x + (2 * i - 1) * d - d / 4
            y = distance_y + (4 * (j - 1)) * d * math.sqrt(3 / 4)
            points1.append((x, y))

    for i in range(1, size_x // 2 + 1):
        for j in range(1, (size_y + 1) // 4 + 1):

            x = distance_x + (2 * i - 2) * d - d / 4
            y = distance_y + (4 * j - 2) * d * math.sqrt(3 / 4)
            points1.append((x, y))

    for point1 in points1:
        x, y = point1
        if square1.get():
            draw.rectangle((x - r, y - r, x + r, y + r), fill='black')
        else:
            draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


    img = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))

    # 创建一个新的窗口来显示图像
    image_window = tk.Toplevel()
    image_window.title("生成的图像")

    # 将图像调整大小以适应窗口大小
    resized_img = img.resize((800, 600))

    # 将调整大小后的图像转换为PhotoImage对象
    photo = ImageTk.PhotoImage(resized_img)

    # 创建一个带有图像的标签
    image_label = tk.Label(image_window, image=photo)
    image_label.image = photo  # 保持对图像对象的引用，以防止被垃圾回收
    image_label.pack()

    # 显示新窗口
    image_window.mainloop()

def triangle():
    global img
    img_size = (int(img_size_entry_w.get()), int(img_size_entry_h.get()))
    r = float(r_entry.get())
    d = float(d_entry.get())
    size_x = int(grid_size_entry_x.get())
    size_y = int(grid_size_entry_y.get())
    # x_offset = float(x_offset_entry.get())
    # y_offset = float(y_offset_entry.get())
    blur_radius = int(blur_radius_entry.get())

    img = Image.new('L', img_size, color='black')
    draw = ImageDraw.Draw(img)
    points = []

    distance_x = (img_size[0] - (size_x - 1) * d + 2 * r) / 2
    distance_y = (img_size[1] - (size_y - 1) * math.sqrt(3 / 4) * d ) / 2
    # 三角格子
    # 偶数行(含0 索引)
    for i in range(size_x):
        for j in range(0, size_y, 2):
            x = distance_x + i * d - d / 4
            y = distance_y + j * d * math.sqrt(3 / 4)
            points.append((x, y))

    # 奇数行(含0 索引)
    for i in range(size_x - 1):
        for j in range(1, size_y, 2):
            x = distance_x + i * d + d / 4
            y = distance_y + j * d * math.sqrt(3 / 4)
            points.append((x, y))

    for point in points:
        x, y = point
        if square1.get():
            draw.rectangle((x - r, y - r, x + r, y + r), fill=fill_intensity)
        else:
            draw.ellipse((x - r, y - r, x + r, y + r), fill=fill_intensity)
            if circle_ring.get():
                p = float(P.get())
                draw.ellipse((x-p*r, y-p*r, x+p*r, y+p*r), fill='black')

    img = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))

    # 创建一个新的窗口来显示图像
    image_window = tk.Toplevel()
    image_window.title("生成的图像")

    # 将图像调整大小以适应窗口大小
    resized_img = img.resize((800, 600))

    # 将调整大小后的图像转换为PhotoImage对象
    photo = ImageTk.PhotoImage(resized_img)

    # 创建一个带有图像的标签
    image_label = tk.Label(image_window, image=photo)
    image_label.image = photo  # 保持对图像对象的引用，以防止被垃圾回收
    image_label.pack()

    # 显示新窗口
    image_window.mainloop()

def hexagonal():
    global img
    img_size = (int(img_size_entry_w.get()), int(img_size_entry_h.get()))
    r = float(r_entry.get())
    d = float(d_entry.get())
    size_x = int(grid_size_entry_x.get())
    size_y = int(grid_size_entry_y.get())
    # x_offset = float(x_offset_entry.get())
    # y_offset = float(y_offset_entry.get())
    blur_radius = int(blur_radius_entry.get())

    img = Image.new('L', img_size, color='black')
    draw = ImageDraw.Draw(img)
    points = []

    distance_x = (img_size[0] - (size_x - 1) * d + 2 * r) / 2
    distance_y = (img_size[1] - (size_y - 1) * math.sqrt(3 / 4) * d ) / 2

    # 偶数行(含0 索引)
    for i in range(size_x - 1):
        for j in range(0, size_y, 2):
            x = distance_x + i * d + d / 4
            y = distance_y + j * d * math.sqrt(3 / 4)
            points.append((x, y))

    # 奇数行(含0 索引)
    for i in range(size_x):
        for j in range(1, size_y, 2):
            x = distance_x + i * d - d / 4
            y = distance_y + j * d * math.sqrt(3 / 4)
            points.append((x, y))


    for point in points:
        x, y = point
        if square1.get():
            draw.rectangle((x - r, y - r, x + r, y + r), fill=fill_intensity)
        else:
            draw.ellipse((x - r, y - r, x + r, y + r), fill=fill_intensity)
            if circle_ring.get():
                p = float(P.get())
                draw.ellipse((x-p*r, y-p*r, x+p*r, y+p*r), fill='black')

    points1 = []
    # 黑
    for i in range(1, size_x // 3 + 1):
        for j in range(1, size_y // 2 + 1):

            x = distance_x + (3 * i - 2) * d - d / 4
            y = distance_y + (2 * j - 1) * d * math.sqrt(3 / 4)
            points1.append((x, y))

    for i in range(1, size_x // 3 + 1):
        for j in range(1, size_y // 2 + 1):

            x = distance_x + (3 * i - 1) * d + d / 4
            y = distance_y + (2 * j - 2) * d * math.sqrt(3 / 4)
            points1.append((x, y))

    for point1 in points1:
        x, y = point1
        if square1.get():
            draw.rectangle((x - r, y - r, x + r, y + r), fill='black')
        else:
            draw.ellipse((x - r, y - r, x + r, y + r), fill='black')




    img = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))
    # 创建一个新的窗口来显示图像
    image_window = tk.Toplevel()
    image_window.title("生成的图像")

    # 将图像调整大小以适应窗口大小
    resized_img = img.resize((800, 600))

    # 将调整大小后的图像转换为PhotoImage对象
    photo = ImageTk.PhotoImage(resized_img)

    # 创建一个带有图像的标签
    image_label = tk.Label(image_window, image=photo)
    image_label.image = photo  # 保持对图像对象的引用，以防止被垃圾回收
    image_label.pack()

    # 显示新窗口
    image_window.mainloop()

def Kagome():
    global img
    img_size = (int(img_size_entry_w.get()), int(img_size_entry_h.get()))
    r = float(r_entry.get())
    d = float(d_entry.get())
    size_x = int(grid_size_entry_x.get())
    size_y = int(grid_size_entry_y.get())
    # x_offset = float(x_offset_entry.get())
    # y_offset = float(y_offset_entry.get())
    blur_radius = int(blur_radius_entry.get())

    img = Image.new('L', img_size, color='black')
    draw = ImageDraw.Draw(img)
    points = []

    distance_x = (img_size[0] - (size_x - 1) * d + 2 * r) / 2
    distance_y = (img_size[1] - (size_y - 1) * math.sqrt(3 / 4) * d ) / 2



    # 偶数行(含0 索引)
    for i in range(size_x):
        for j in range(0, size_y, 2):
            x = distance_x + i * d - d / 4
            y = distance_y + j * d * math.sqrt(3 / 4)
            points.append((x, y))

    # 奇数行(含0 索引)
    for i in range(size_x - 1):
        for j in range(1, size_y, 2):
            x = distance_x + i * d + d / 4
            y = distance_y + j * d * math.sqrt(3 / 4)
            points.append((x, y))


    for point in points:
        x, y = point
        if square1.get():
            draw.rectangle((x - r, y - r, x + r, y + r), fill=fill_intensity)
        else:
            draw.ellipse((x - r, y - r, x + r, y + r), fill=fill_intensity)
            if circle_ring.get():
                p = float(P.get())
                draw.ellipse((x-p*r, y-p*r, x+p*r, y+p*r), fill='black')

    points1 = []
    # 黑
    for i in range(1, size_x // 2 + 1):
        for j in range(1, size_y // 3 + 1):
            x = distance_x + (2 * i - 1) * d - d / 4
            y = distance_y + (4 * (j - 1)) * d * math.sqrt(3 / 4)
            points1.append((x, y))

    for i in range(1, size_x // 2 + 1):
        for j in range(1, (size_y + 1) // 4 + 1):

            x = distance_x + (2 * i - 2) * d - d / 4
            y = distance_y + (4 * j - 2) * d * math.sqrt(3 / 4)
            points1.append((x, y))

    for point1 in points1:
        x, y = point1
        if square1.get():
            draw.rectangle((x - r, y - r, x + r, y + r), fill='black')
        else:
            draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


    img = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))

    image_window = tk.Toplevel()
    image_window.title("生成的图像")

    # 将图像调整大小以适应窗口大小
    resized_img = img.resize((800, 600))

    # 将调整大小后的图像转换为PhotoImage对象
    photo = ImageTk.PhotoImage(resized_img)

    # 创建一个带有图像的标签
    image_label = tk.Label(image_window, image=photo)
    image_label.image = photo  # 保持对图像对象的引用，以防止被垃圾回收
    image_label.pack()

    # 显示新窗口
    image_window.mainloop()



def save_image():
    global img
    file_types = [('Bitmap', '*.bmp'), ('JPEG', '*.jpg'), ('PNG', '*.png')]
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=file_types)
    if save_path and img is not None:
        img.save(save_path)


def create_about_content(parent):
    version_number = "V18.0"
    software_name = "Lattice image generator"
    copyright_owner = "Copyright (C) 2024"
    developer_email = "wsxiongdx@163.com"

    about_text = (f"Version number: {version_number}\n\n"
                  f"All rights reserved: {copyright_owner}"
                  f"\n\nPlease contact us if you have any questions or suggestions:\n"
                  f" Email : {developer_email}\n\n"
                  "Please note: This software is for personal learning and non-commercial use only.\n Use of the software for commercial purposes without permission is prohibited.")

    software_label = tk.Label(parent, text=software_name, font=("Helvetica", 20, 'bold'), anchor='center')
    software_label.pack(pady=(80, 20), padx=50)

    label = tk.Label(parent, text=about_text, font=("Helvetica", 13), anchor='center', justify='left')
    label.pack(pady=(20, 100), padx=50)







root = tk.Tk()
root.title("Lattice image generator")

# 设置窗口大小
window_width = 800
window_height = 550
root.geometry(f"{window_width}x{window_height}")
# # 获取当前脚本文件所在的目录
# current_dir = os.path.dirname(os.path.abspath(__file__))
#
# # 构建图标文件的完整路径
# icon_path = os.path.join(current_dir, "bear1.ico")
# root.iconbitmap(icon_path)
# # 设置图标
# root.iconbitmap("bear1.ico")

# 计算窗口位置
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"+{x}+{y}")
font_size = 18

#设置选项卡
notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)

tab6 = ttk.Frame(notebook)
create_about_content(tab6)

notebook.add(tab1, text="   Image   ")

notebook.add(tab6, text="    About  ")
notebook.pack(expand=True, fill="both")

# 选项卡样式
style = ttk.Style()
style.configure("TNotebook.Tab", padding=(10, 5), foreground="#4682B4", font=("Helvetica", 12))



tab1.grid_rowconfigure(0, minsize=20) #相当与中间空一行

img_size_label = tk.Label(tab1, text="  Image Size (w/h):", font=("Helvetica", font_size))
img_size_label.grid(row=1, column=0)
img_size_entry_w = tk.Entry(tab1, width=10, font=("Installer", font_size))
img_size_entry_w.insert(0, "1024")
img_size_entry_w.grid(row=1, column=1)
img_size_entry_h = tk.Entry(tab1, width=10, font=("Installer", font_size))
img_size_entry_h.insert(0, "1024")
img_size_entry_h.grid(row=1, column=2)

r_label = tk.Label(tab1, text="  Radius               :", font=("Helvetica", font_size))
r_label.grid(row=2, column=0)
r_entry = tk.Entry(tab1, width=10, font=("Installer", font_size))
r_entry.insert(0, "0")
r_entry.grid(row=2, column=1)

d_label = tk.Label(tab1, text="  Distance            :", font=("Helvetica", font_size))
d_label.grid(row=3, column=0)
d_entry = tk.Entry(tab1, width=10, font=("Installer", font_size))
d_entry.insert(0, "5")
d_entry.grid(row=3, column=1)

grid_size_label_x = tk.Label(tab1, text="  Grid Size X        :", font=("Helvetica", font_size))
grid_size_label_x.grid(row=4, column=0)
grid_size_entry_x = tk.Entry(tab1, width=10, font=("Installer", font_size))
grid_size_entry_x.insert(0, "5")
grid_size_entry_x.grid(row=4, column=1)





grid_size_label_y = tk.Label(tab1, text="  Grid Size Y        :", font=("Helvetica", font_size))
grid_size_label_y.grid(row=5, column=0)
grid_size_entry_y = tk.Entry(tab1, width=10, font=("Installer", font_size))
grid_size_entry_y.insert(0, "5")
grid_size_entry_y.grid(row=5, column=1)


blur_radius_label = tk.Label(tab1, text="  GaussianBlur     :", font=("Helvetica", font_size))
blur_radius_label.grid(row=6, column=0)
blur_radius_entry = tk.Entry(tab1, width=10, font=("Installer", font_size))
blur_radius_entry.insert(0, "0")
blur_radius_entry.grid(row=6, column=1)


save_button = tk.Button(tab1, text="Triangular Lattice", command=triangle_image,fg="#4682B4",font=("Helvetica", font_size))
save_button.grid(row=2, column=3,pady=5)

save_button = tk.Button(tab1, text="hexagonal Lattice", command=hexagonal_image,fg="#4682B4",font=("Helvetica", font_size))
save_button.grid(row=4, column=3,pady=5)

save_button = tk.Button(tab1, text=" Kagome Lattice ", command=Kagome_image,fg="#4682B4",font=("Helvetica", font_size))
save_button.grid(row=6, column=3,pady=5)

tab1.grid_rowconfigure(7, minsize=15) #相当与中间空一行

circle_ring = tk.BooleanVar()
circle_ring.set(False)
style = ttk.Style()
style.configure("Custom.TCheckbutton",indicatorsize=10, indicatormargin=5)  # 设置复选框的样式
circle_ring_style = ttk.Style()
circle_ring_style.configure("Custom.TCheckbutton", font=("Times New Roman", font_size))
circle_ring_checkbutton = ttk.Checkbutton(tab1, text="Circular Ring", variable=circle_ring, style="Custom.TCheckbutton", takefocus=0)
circle_ring_checkbutton.grid(row=8, column=0)

square1 = tk.BooleanVar()
square1.set(True)
style = ttk.Style()
style.configure("Custom.TCheckbutton",indicatorsize=10, indicatormargin=5)  # 设置复选框的样式

square_style = ttk.Style()
square_style.configure("Custom.TCheckbutton", font=("Times New Roman", font_size))
square_checkbutton = ttk.Checkbutton(tab1, text="square", variable=square1, style="Custom.TCheckbutton", takefocus=0)
square_checkbutton.grid(row=8, column=3)


P = tk.Label(tab1, text="Proportion:", font=("Helvetica", font_size))
P.grid(row=8, column=1,sticky="e")
P = tk.Entry(tab1, width=10, font=("Installer", font_size))
P.insert(0, "0.8")
P.grid(row=8, column=2)

tab1.grid_rowconfigure(9, minsize=15) #相当与中间空一行

save_button = tk.Button(tab1, text="Triangular", command=triangle,bg="#F0FFFF",font=("Helvetica", font_size))
save_button.grid(row=10, column=0)

save_button = tk.Button(tab1, text="hexagonal", command=hexagonal,bg="#F0FFFF",font=("Helvetica", font_size))
save_button.grid(row=10, column=1)

save_button = tk.Button(tab1, text="  Kagome  ", command=Kagome,bg="#F0FFFF",font=("Helvetica", font_size))
save_button.grid(row=10, column=2, padx=40)

generate_button = tk.Button(tab1, text="    Lattice    ", command=generate_image, bg="#F0FFFF",fg="#4682B4",font=("Helvetica", font_size))
generate_button.grid(row=10, column=3)

tab1.grid_rowconfigure(11, minsize=25) #相当与中间空一行

save_button = tk.Button(tab1, text="Save Image", command=save_image,bg="lightblue",font=("Helvetica", font_size))
save_button.grid(row=12, column=3,pady=5)



root.mainloop()