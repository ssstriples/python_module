# Python GUI

## 1. 기본 프레임
```
    - 1_create_frame.py
```
<pre>
<code>
from tkinter import *

root = Tk()
root.title("SHLEE GUI")
root.geometry("640x480")    # 가로 * 세로
# root.geometry("640x480+300+100")    # 가로 * 세로 + x좌표 + y좌표

root.resizable(False, False)    # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

root.mainloop()
</code>
</pre>

## 2. 버튼 widget
```
    - 2_button.py
```

## 3. 레이블
```
    - 3_label.py
```

## 4. 텍스트 & 엔트리
```
    - 4_text_entry.py
    - 텍스트 : 여러 줄에 걸쳐서 입력이 필요할 때 사용
    - 엔트리 : 한 줄로 입력받을때 사용하며 로그인 ID등등
```

## 5. 리스트 박스
```
    - 5_listbox.py
```

## 6. 체크 박스
```
    - 6_checkbox.py
```

## 7. 라디오 버튼
```
    - 7_radiobutton.py
    - 여러개 중에서 택 1
```

## 8. 콤보 박스
```
    - 8_combobox.py
    - import tkinter.ttk as ttk
    - ttk.Combobox() 사용
```

## 9. 프로그레스 바
```
    - 9_progressbar.py
    - import tkinter.ttk as ttk
    - ttk.Progressbar() 사용
```

## 10. 메뉴
```
    - 10_menu.py
```

## 11. 메시지 박스
```
    - 11_messagebox.py
    - import tkinter.messagebox as msgbox
```

## 12. 프레임
```
    - 12_frame.py
```

## 13. 스크롤 바
```
    - 13_scrollbar.py
    - 하나의 프레임에 리스트 박스와 스크롤을 서로 매핑
```

## 14. 그리드
```
    - 14_grid.py
    - sticky 속성 : sticky=N+E+W+S 지정한 방향으로 위젯을 늘려라!
```

## 15. 퀴즈 : 메모장 프로그램
```
    [GUI 조건]
    1. title : 제목 없음 - Windows 메모장
    2. 메뉴 : 파일, 편집, 서식, 보기 도움말
    3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
    3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
    3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
    3-3. 끝내기 : 프로그램 종료
    4. 프로그램 시작 시 본문은 비어있는 상태
    5. 하단 status 바는 필요없음
    6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야함 
    7. 본문 우측에 상하 스크롤 바 넣기

    - 
```