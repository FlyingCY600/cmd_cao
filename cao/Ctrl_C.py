import pyperclip

def copy_to_clipboard(text):
    """
    将文本复制到剪贴板
    Args:
        text: 要复制的文本
    Returns:
        bool: 复制成功返回 True，失败返回 False
    """
    try:
        pyperclip.copy(text)
        return True
    except Exception as e:
        print(f"复制到剪贴板失败: {str(e)}")
        return False

def paste_from_clipboard():
    """
    从剪贴板获取文本
    Returns:
        str: 剪贴板中的文本，如果失败返回空字符串
    """
    try:
        return pyperclip.paste()
    except Exception as e:
        print(f"从剪贴板读取失败: {str(e)}")
        return ""

# 测试代码
if __name__ == "__main__":
    # 测试复制
    test_text = "Hello, 这是测试文本！"
    if copy_to_clipboard(test_text):
        print("文本已复制到剪贴板")
    
    # 测试粘贴
    clipboard_content = paste_from_clipboard()
    print(f"剪贴板内容: {clipboard_content}")