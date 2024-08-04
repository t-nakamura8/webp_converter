import os
from PIL import Image


def convert_to_webp(input_folder, output_folder, quality=80, delete_original=False):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpeg', 'jpg', '.png')):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            output_path = os.path.join(
                output_folder, os.path.splitext(filename)[0] + '.webp')
            img.save(output_path, 'webp', quality=quality)
            print(f"Converted {filename} to WebP with quality {quality}")

            if delete_original:
                os.remove(img_path)
                print(f"Deleted original file: {filename}")


if __name__ == "__main__":
    input_folder = '/app/input_folder'  # コンテナ内の固定パス
    output_folder = '/app/output_folder'  # コンテナ内の固定パス
    quality = 80  # クオリティを0-100の範囲で設定
    delete_original = True  # 変換後に元画像を削除するかどうか

    convert_to_webp(input_folder, output_folder, quality, delete_original)
