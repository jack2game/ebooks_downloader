from modules.download_images import download_chapter_images
from modules.merge_pdf import merge_all_folders_to_pdf
from modules.utils import ensure_dir
import os


def main():
    print("==== 電子書自動下載與合併 PDF 工具 ====")
    output_dir = 'output'
    images_dir = os.path.join(output_dir, 'images')
    pdf_dir = os.path.join(output_dir, 'PDF')
    ensure_dir(images_dir)
    ensure_dir(pdf_dir)

    # 詢問是否需要下載圖片
    need_download = input("是否需要下載圖片？(y/n)：").strip().lower()
    chapters = []
    idx = 1
    if need_download == 'y':
        print("請依序輸入每個章節的第一頁頁數（空白代表結束）：")
        while True:
            inp = input(f"第 {idx} 章開始頁數：")
            if not inp.strip():
                break
            try:
                page = int(inp.strip())
                chapters.append((f"chapter{idx}", page))
                idx += 1
            except ValueError:
                print("請輸入正確的數字或留空結束。")
        if not chapters:
            print("未輸入任何章節，程式結束。")
            return
        # 輸入最後一頁頁數
        last_page = int(input("請輸入最後一頁的頁數：").strip())
        # 下載所有章節圖片
        for i, (chapter_name, start_page) in enumerate(chapters):
            next_start = chapters[i+1][1] if i+1 < len(chapters) else last_page
            print(f"開始下載 {chapter_name} ...")
            download_chapter_images(
                chapter_name, start_page, next_start, output_dir)
        print("\n所有圖片下載完成，請自行檢查 output/images 資料夾下的所有圖片是否正確。")
        input("檢查完畢後請按 Enter 繼續進行 PDF 合併...")

    # 合併 PDF
    merge_all_folders_to_pdf(output_dir)
    print("\n全部章節 PDF 合併完成！PDF 檔案請至 output/PDF/ 目錄查看。")


if __name__ == '__main__':
    main()
