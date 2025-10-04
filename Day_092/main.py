from flask import Flask, request, redirect, url_for, render_template
from PIL import Image
import io
import base64
import math


app = Flask(__name__)

NUM_OF_COLORS = 8
MAX_SIZE = (800, 800)

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

@app.route('/')
def index():
    return render_template("index.html", num_colors=NUM_OF_COLORS)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect(url_for('index'))


    f = request.files['image']
    if f.filename == '':
        return redirect(url_for('index'))


    try:
        num_colors = int(request.form.get('num_colors') or NUM_OF_COLORS)
        num_colors = max(1, min(64, num_colors))
    except ValueError:
        num_colors = NUM_OF_COLORS

    img = Image.open(f.stream).convert('RGBA')
    orig_w, orig_h = img.size
    img.thumbnail(MAX_SIZE, Image.LANCZOS)

    if img.mode == 'RGBA':
        bg = Image.new('RGB', img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[3])  # 3 is alpha
        img_rgb = bg
    else:
        img_rgb = img.convert('RGB')

    quant = img_rgb.quantize(colors=num_colors, method=Image.MEDIANCUT)

    counts = quant.getcolors(maxcolors=img_rgb.size[0] * img_rgb.size[1] + 1)

    palette = quant.getpalette()

    color_data = []
    total = 0
    for count, idx in counts:
        total += count
        r = palette[idx * 3]
        g = palette[idx * 3 + 1]
        b = palette[idx * 3 + 2]
        color_data.append((count, (r, g, b)))

    color_data.sort(reverse=True, key=lambda x: x[0])

    colors = []
    for count, rgb in color_data:
        pct = round((count / total) * 100, 2)
        colors.append({'count': count, 'rgb': rgb, 'hex': rgb_to_hex(rgb), 'percent': pct})

    buf = io.BytesIO()
    img_rgb.save(buf, format='PNG')
    b64 = base64.b64encode(buf.getvalue()).decode('ascii')

    return render_template("result.html",img_b64=b64,img_format='png',orig_w=orig_w,orig_h=orig_h,pixel_count=img_rgb.size[0] * img_rgb.size[1],colors=colors)

if __name__ == '__main__':
    app.run(debug=True)