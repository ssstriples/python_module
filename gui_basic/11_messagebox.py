import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("SHLEE GUI")
root.geometry("640x480")    # 가로 * 세로



# 기차 예매 시스템이라고 가정
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n저장 후 프로그램을 종료하시겠습니까?")
    # 네 : 저장 후 종료
    # 아니오 : 저장하지 않고 종료
    # 취소 : 프로그램 종료 취소(현재 화면에서 계속 작업)
    print(response) # True, False, None -> 예 1, 아니오 0, 그 외
    if response == 1: # 네, ok
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")

Button(root, text="알림", command=info).pack()
Button(root, text="경고", command=warn).pack()
Button(root, text="에러", command=error).pack()

Button(root, text="확인 취소", command=okcancel).pack()
Button(root, text="재시도 취소", command=retrycancel).pack()
Button(root, text="예 아니오", command=yesno).pack()
Button(root, text="예 아니오 취소", command=yesnocancel).pack()

root.mainloop()