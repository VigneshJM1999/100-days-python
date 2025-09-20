import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps, ImageDraw, ImageFont

original_img = None
last_watermarked = None

def select_image():
    global original_img, last_watermarked
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")], title="Select a picture")
    if file_path:
        original_img = Image.open(file_path)
        last_watermarked = None
        size = (500, 600)
        fit_img = ImageOps.fit(original_img, size, Image.Resampling.LANCZOS, centering=(0.5, 0.5))
        tk_img = ImageTk.PhotoImage(fit_img)
        image_label.config(image=tk_img)
        image_label.image = tk_img

def water_mark(event=None):
    global last_watermarked
    global original_img

    if original_img is None:
        return

    user_text = text_entry.get().strip()

    if not user_text:
        return

    watermarked = original_img.copy()

    if watermarked.mode != 'RGBA':
        watermarked = watermarked.convert('RGBA')

    image_width, image_height = watermarked.size
    draw = ImageDraw.Draw(watermarked)

    font_size = int(image_width / 8)

    font = ImageFont.truetype('arial.ttf', font_size)

    x, y = int(image_width / 2) - 10, int(image_height / 2) - 10
    draw.text((x, y), user_text, font=font, fill="#FFF", stroke_width=1)

    last_watermarked = watermarked
    size = (500, 600)
    fit_img = ImageOps.fit(last_watermarked, size, Image.Resampling.LANCZOS, centering=(0.5, 0.5))
    tk_img = ImageTk.PhotoImage(fit_img)
    image_label.config(image=tk_img)
    image_label.image = tk_img

def save_image():
    if last_watermarked is None:
        return
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
    )
    if save_path:
        last_watermarked.save(save_path)

window = tk.Tk()
window.wm_title("Image Watermark App")
window.geometry("800x600")

left_frame = tk.Frame(window, width=500, height=600, bg="white")
left_frame.pack(side="left", fill="both", expand=True)

right_frame = tk.Frame(window, width=300, height=600, bg="lightgray")
right_frame.pack(side="right", fill="y")

image_label = tk.Label(left_frame, bg="white")
image_label.pack(expand=True)

open_button = tk.Button(right_frame, text="Open Image", command=select_image)
open_button.pack(pady=20)

text_entry = tk.Entry(right_frame, width=30)
text_entry.pack(pady=10)
text_entry.bind("<Return>", water_mark)

watermark_button = tk.Button(right_frame, text="Add Watermark", command=water_mark)
watermark_button.pack(pady=10)

save_button = tk.Button(right_frame, text="Save Image", command=save_image)
save_button.pack(pady=10)

window.mainloop()
