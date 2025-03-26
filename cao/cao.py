import ctypes
import argparse
import yaml
from ctypes import wintypes
from cao.chatgpt import get_commend_from_gpt
from cao.Ctrl_C import copy_to_clipboard

# 定义控制台缓冲区信息结构
class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class SMALL_RECT(ctypes.Structure):
    _fields_ = [("Left", ctypes.c_short),
                ("Top", ctypes.c_short),
                ("Right", ctypes.c_short),
                ("Bottom", ctypes.c_short)]

class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
    _fields_ = [("dwSize", COORD),
                ("dwCursorPosition", COORD),
                ("wAttributes", ctypes.c_ushort),
                ("srWindow", SMALL_RECT),
                ("dwMaximumWindowSize", COORD)]

def get_cmd_history():
    STD_OUTPUT_HANDLE = -11
    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    
    # 获取控制台屏幕缓冲区信息
    csbi = CONSOLE_SCREEN_BUFFER_INFO()
    ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, ctypes.byref(csbi))
    
    # 读取可见区域的历史记录
    buffer_width = csbi.dwSize.X
    buffer_height = csbi.srWindow.Bottom - csbi.srWindow.Top + 1
    buffer_size = buffer_width * buffer_height
    
    buffer = (wintypes.CHAR * buffer_size)()
    coord = COORD(0, csbi.srWindow.Top)
    read_len = wintypes.DWORD()
    
    ctypes.windll.kernel32.ReadConsoleOutputCharacterA(
        handle,
        buffer,
        buffer_size,
        coord,
        ctypes.byref(read_len)
    )
    
    # 转换为字符串并清理空格
    raw_text = buffer.value.decode('gbk').replace('\x00', '')
    return raw_text
    
def get_second_last_history(raw_text):
    # 找到倒数第二个‘>’
    if raw_text.count('>') >= 2:
        last_gt = raw_text.rfind('>')#最后一个'>'
        second_last_gt = raw_text.rfind('>', 0, last_gt)#倒数第二个'>'
        command = raw_text[second_last_gt + 1:].strip()
        return command.replace('\r\n', '')
    else:
        return None
def clean_space(commend):
    # 如果command中的‘连续’的空格数量大于等于2，只输出连续的两个空格前的内容
    max_count=2
    count=0
    for i in range(len(commend)):
        if commend[i]==' ':
            count+=1
            if count==max_count:
                cleaned_commend=commend[:i]
                return cleaned_commend
        else:
            count=0
    print(commend)
    print(len(commend))
def update_api_key(new_key):
    """更新 config.yaml 中的 API key"""
    config_path = 'E:\\APP\\VScode\\project\\cao\\config.yaml'
    try:
        # 读取现有配置
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        # 更新 API key
        config['api_key'] = new_key
        
        # 写回文件
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config, f, allow_unicode=True)
        
        print(f"API key 已更新")
        return True
    except Exception as e:
        print(f"更新 API key 失败: {str(e)}")
        return False
def main():
    # 创建参数解析器
    parser = argparse.ArgumentParser(description='CAO 命令行工具')
    parser.add_argument('-add', help='更新 API key')
    
    args = parser.parse_args()
    
    # 如果指定了 -add 参数
    if args.add:
        return update_api_key(args.add)
    
    raw_text=get_cmd_history()
    commend=get_second_last_history(raw_text)
    cleaned_commend=clean_space(commend)
    allowed_char=set('/\\-%:;.,_()[]{}<>|')
    try:
        history=cleaned_commend
        # print("最后命令历史记录：")
        # print(history)
        if history:
            response = get_commend_from_gpt(history)
            # 去掉字符串中除了字母和空格和-以外的字符
            response = ''.join(e for e in response if e.isalnum() or e.isspace() or e in allowed_char)                 
            print(response)
        copy_to_clipboard(response)
    except Exception as e:
        print(f"API 调用失败：{str(e)}")
if __name__ == "__main__":
    main()