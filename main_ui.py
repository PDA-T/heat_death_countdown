import tkinter as tk
from heat_death_timer import get_heat_death_seconds


def format_time(seconds):
    # 格式化为 年-天-时-分-秒
    years, rem = divmod(seconds, 365 * 24 * 60 * 60)
    days, rem = divmod(rem, 24 * 60 * 60)
    hours, rem = divmod(rem, 60 * 60)
    minutes, sec = divmod(rem, 60)
    return f"{years} 年 {days} 天 {hours} 时 {minutes} 分 {sec} 秒"


def update_timer():
    secs = get_heat_death_seconds()
    label.config(text=f"距离宇宙热寂还剩：\n{format_time(secs)}")
    if secs > 0:
        root.after(1000, update_timer)
    else:
        label.config(text="宇宙热寂已到来！", fg="#D7263D", bg="#fff1f1")


root = tk.Tk()
root.title("宇宙热寂倒计时")
root.geometry("1700x400")
# 主窗口深色背景
root.configure(bg="#22223b")

# 标题
title = tk.Label(
    root,
    text="🔥 宇宙热寂倒计时 🔥",
    font=("微软雅黑", 28, "bold"),
    bg="#22223b",
    fg="#f2e9e4",
    pady=30
)
title.pack()

# 副标题
subtitle = tk.Label(
    root,
    text="距离宇宙归于静寂，还有多久？",
    font=("微软雅黑", 18, "italic"),
    bg="#22223b",
    fg="#c9ada7",
    pady=10
)
subtitle.pack()

# 主计时
label = tk.Label(
    root,
    text="",
    font=("微软雅黑", 16),
    justify="center",
    # 背景
    bg="#4a4e69",
    # label字体颜色
    fg="#f2e9e4",
    # 边框粗细
    bd=6,
    # 边框样式
    relief="groove",
    padx=30,
    pady=30
)
label.pack(expand=True, padx=40, pady=40, fill="both")

update_timer()

root.mainloop()
