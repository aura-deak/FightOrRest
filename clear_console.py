import platform
import subprocess


def clear_console():
    """
    跨平台清空控制台输出（Windows/Linux/macOS通用）
    """
    # 判断操作系统类型
    if platform.system() == "Windows":
        # Windows系统：执行cls命令
        subprocess.call("cls", shell=True)
        # 备选方案（兼容旧版Windows）：os.system('cls')
    else:
        # Linux/macOS系统：执行clear命令
        subprocess.call("clear", shell=True)
        # 备选方案：os.system('clear')


# 测试使用
if __name__ == "__main__":
    print("这是清空前的内容")
    input("按回车清空控制台...")  # 等待用户确认
    clear_console()
    print("控制台已清空，这是新内容")
