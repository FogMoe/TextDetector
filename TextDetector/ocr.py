import time
import pygetwindow as gw
import pytesseract
from PIL import ImageGrab
import settings

# 设置Tesseract可执行文件的路径
pytesseract.pytesseract.tesseract_cmd = settings.tesseract_cmd


# 截取窗口截图
def capture_window(process_name):
    # 获取所有窗口
    windows = gw.getWindowsWithTitle(process_name)

    if not windows:
        print(f"没有找到进程窗口: {process_name}")
        return

    # 假设我们只截取第一个匹配的窗口
    window = windows[0]
    window.activate()

    scale_factor = settings.scale_factor
    # 获取窗口的坐标并调整
    bbox = (
        int(window.left * scale_factor),
        int(window.top * scale_factor),
        int(window.right * scale_factor),
        int(window.bottom * scale_factor)
    )
    print(f"窗口坐标: {bbox}")

    # 截取窗口截图
    screenshot = ImageGrab.grab(bbox)
    # screenshot.save(f'{process_name}_screenshot.png')

    return screenshot


# 检测窗口中是否存在“字”
def check_text_in_window(process_name, word):
    # 将截图转换为文本
    text = pytesseract.image_to_string(capture_window(process_name), lang='chi_sim')  # 使用简体中文语言包
    if word in text:
        print("检测到")
    else:
        print("未检测")
