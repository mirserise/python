import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import sqlite3
import os
import subprocess

# 암호 설정 (사용자가 직접 설정 가능)
DB_PASSWORD = "nadia"

def create_database():
    if not os.path.exists('internal_data_encrypted.db'):
        file_a = filedialog.askopenfilename(title="자체 데이터 선택", filetypes=[("Excel files", "*.xlsx *.xls")])
        if not file_a:
            return
        
        try:
            df_a = pd.read_excel(file_a)

            # 기존 파일 삭제 후 새로 생성
            if os.path.exists('internal_data_encrypted.db'):
                os.remove('internal_data_encrypted.db')

            # sqlcipher 명령어로 암호화된 DB 생성
            command = f"""
            sqlcipher internal_data_encrypted.db <<EOF
            PRAGMA key = '{DB_PASSWORD}';
            CREATE TABLE IF NOT EXISTS data (
                성명 TEXT,
                기관명 TEXT,
                구분 TEXT,
                아이디 TEXT
            );
            .quit
            EOF
            """
            subprocess.run(command, shell=True, check=True)

            # SQLite 연결 후 데이터 저장 (암호화 상태)
            conn = sqlite3.connect('internal_data_encrypted.db')
            conn.execute(f"PRAGMA key = '{DB_PASSWORD}';")

            # 데이터 삽입
            df_a.to_sql("data", conn, if_exists="replace", index=False)
            conn.close()

            messagebox.showinfo("완료", "데이터베이스에 암호화된 데이터를 저장했습니다.")
        except Exception as e:
            messagebox.showerror("에러", f"파일 처리 중 오류 발생:\n{e}")
    else:
        messagebox.showinfo("이미 처리됨", "데이터는 이미 암호화된 데이터베이스에 저장되었습니다.")

def process_files():
    file_b = filedialog.askopenfilename(title="입력 데이터 선택", filetypes=[("Excel files", "*.xlsx *.xls")])
    if not file_b:
        return
    
    try:
        df_b = pd.read_excel(file_b, usecols="A:C", names=["성명", "기관명", "구분"])

        # 암호화된 DB 열기
        conn = sqlite3.connect('internal_data_encrypted.db')
        conn.execute(f"PRAGMA key = '{DB_PASSWORD}';")

        query = "SELECT 성명, 기관명, 구분, 아이디 FROM data"
        df_a = pd.read_sql(query, conn)
        conn.close()

        # 입력 데이터와 자체 데이터 매칭
        merged_df = df_b.merge(
            df_a[['성명', '기관명', '구분', '아이디']],
            on=['성명', '기관명', '구분'],
            how='left'
        )

        # 저장할 파일 이름 설정
        save_path = os.path.splitext(file_b)[0] + "_with_id.xlsx"
        merged_df.to_excel(save_path, index=False)

        messagebox.showinfo("완료", f"파일 저장 완료:\n{save_path}")
    except Exception as e:
        messagebox.showerror("에러", f"처리 중 오류 발생:\n{e}")

# GUI 설정
root = tk.Tk()
root.title("암호화된 아이디 매칭 프로그램")

btn_create_db = tk.Button(root, text="암호화된 DB 생성 (A.xlsx)", command=create_database)
btn_create_db.pack(pady=20)

btn_process = tk.Button(root, text="엑셀 파일 처리", command=process_files)
btn_process.pack(pady=20)

root.mainloop()
