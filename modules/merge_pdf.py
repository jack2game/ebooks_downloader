import os
from PIL import Image


def merge_all_folders_to_pdf(output_dir='output'):
    """
    讀取 output/images 內所有資料夾，將每個資料夾內的 jpg 圖片合併成 PDF，PDF 存於 output/PDF/
    """
    images_root = os.path.join(output_dir, 'images')
    pdf_root = os.path.join(output_dir, 'PDF')
    if not os.path.exists(images_root):
        print("找不到 images 目錄，請確認圖片已下載。")
        return
    if not os.path.exists(pdf_root):
        os.makedirs(pdf_root)

    for folder in sorted(os.listdir(images_root)):
        folder_path = os.path.join(images_root, folder)
        if os.path.isdir(folder_path):
            images = []
            for file in sorted(os.listdir(folder_path)):
                if file.lower().endswith('.jpg'):
                    img_path = os.path.join(folder_path, file)
                    img = Image.open(img_path).convert('RGB')
                    images.append(img)
            if images:
                pdf_path = os.path.join(pdf_root, f"{folder}.pdf")
                images[0].save(pdf_path, save_all=True,
                               append_images=images[1:])
                print(f"{folder} PDF 合併完成：{pdf_path}")
            else:
                print(f"{folder} 沒有找到圖片，無法合併 PDF。")
