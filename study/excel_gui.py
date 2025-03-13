import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if not file_path:
        return
    
    try:
        df = pd.read_excel(file_path)

        # 아이디 값 추가 (예: 1부터 순차 번호)
        df['ID'] = range(1, len(df) + 1)

        # 저장할 파일 이름 설정
        save_path = os.path.splitext(file_path)[0] + "_with_id.xlsx"
        df.to_excel(save_path, index=False)

        messagebox.showinfo("완료", f"파일 저장 완료:\n{save_path}")
    except Exception as e:
        messagebox.showerror("에러", f"파일 처리 중 오류 발생:\n{e}")

# GUI 설정
root = tk.Tk()
root.title("엑셀 아이디 추가기")

btn_open = tk.Button(root, text="엑셀 파일 열기", command=open_file)
btn_open.pack(pady=20)

root.mainloop()
