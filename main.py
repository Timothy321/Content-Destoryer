import tkinter as tk
import pyautogui
import math
import time
import threading


# tkinter 윈도우 설정
root = tk.Tk()
root.title("overlay")  # 창 제목 설정
root.geometry("1919x1079+0+0")  # 창 크기를 최소화하여 표시
root.overrideredirect(True)  # 창 테두리 없애기

# 투명 배경 및 클릭이 가능하게 설정
root.attributes("-topmost", True)  # 항상 위에 표시
root.attributes("-transparentcolor", "red")  # 빨간색을 투명색으로 설정
root.config(bg="red")  # 빨간색 배경을 설정하여 투명 처리

# 레이블 생성 (오버레이 텍스트)
label = tk.Label(root, text="⚫️", fg="white", font=("Arial", 100), bg="red")
label.pack()

# 마우스 좌표 구하기
def get_mouse_position():
    x, y = pyautogui.position()
    return x, y

# 0.5초마다 마우스 좌표에 텍스트 위치 업데이트하는 반복문
def repeat_every_half_second():
    while True:
        # 마우스 좌표 가져오기
        x, y = get_mouse_position()

        # 마우스 좌표에 텍스트 위치 업데이트
        label.place(x=x - label.winfo_width() // 2, y=y - label.winfo_height() // 2)

        # 0.5초 대기
        root.after(500, get_mouse_position)

# 절댓값 싸인 함수로 크기를 변화시키는 함수
def oscillating_size():
    angle = 0  # 각도 (싸인 함수에 사용할 값)
    while True:
        # 절댓값 싸인 함수로 크기 계산
        size = 50 + 50 * abs(math.sin(angle))  # 크기를 50 ~ 100 범위로 변동

        # 레이블 크기 업데이트
        label.config(font=("Arial", int(size)))

        # 각도를 업데이트하여 싸인 함수 반복
        angle += 0.1  # 각도를 조금씩 증가시켜 싸인 함수가 반복되게 함

        # 0.1초 대기 (크기 변화를 천천히 적용)
        time.sleep(0.1)
        root.update()  # tkinter 업데이트

# 반복문 실행
thread = threading.Thread(target=repeat_every_half_second)
thread.daemon = True  # 메인 프로그램 종료 시 함께 종료
thread.start()

# 크기 변화 반복 실행
size_thread = threading.Thread(target=oscillating_size)
size_thread.daemon = True  # 메인 프로그램 종료 시 함께 종료
size_thread.start()

# tkinter 루프 시작
root.mainloop()
