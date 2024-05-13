import keyboard
import time

def main():
    print("按下 'Ctrl + Q' 来启动文本输入")
    while True:
        if keyboard.is_pressed('ctrl+q'):
            text = ""  # 更换成你想要输入的文本
            time.sleep(0.5)  # 等待一段时间以确保焦点切换完成
            keyboard.write(text)
            print("已输入文本")
            break

if __name__ == "__main__":
    main()
