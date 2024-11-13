import asyncio
import os
import tkinter as tk
from tkinter import filedialog

from config import *
from modules.translate import pdf_translate


async def translate_local(deepl_url, deepl_key, disble_translate=False):
    # GUIでファイル選択のための設定
    root = tk.Tk()
    root.withdraw()  # GUIのメインウィンドウを表示しない
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")]
    )  # PDFファイルのみ選択

    if not file_path:
        print("ファイルが選択されませんでした。")
        return

    with open(file_path, "rb") as f:
        input_pdf_data = f.read()

    result_pdf = await pdf_translate(
        deepl_key,
        input_pdf_data,
        api_url=deepl_url,
        debug=False,
        disable_translate=disble_translate,
    )

    if result_pdf is None:
        return

    _, file_name = os.path.split(file_path)
    output_path = Output_folder_path + "result_" + file_name

    with open(output_path, "wb") as f:
        f.write(result_pdf)


if __name__ == "__main__":
    asyncio.run(translate_local(DeepL_URL, DeepL_API_Key))
