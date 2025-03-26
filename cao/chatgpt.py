from openai import OpenAI
import yaml
from datetime import datetime

class ChatGPT:
    def __init__(self, config):
        """初始化 ChatGPT 客户端"""
        # 创建 OpenAI 客户端
        self.client = OpenAI(
            api_key=config['api_key'],
            base_url=config.get('api_base', 'https://api.openai.com/v1')
        )
        
        self.model = config.get('model', 'gpt-3.5-turbo')  # 默认使用 gpt-3.5-turbo
        self.messages = []  # 存储对话历史
    
    def get_response(self, prompt):
        """发送消息到 ChatGPT 并获取回复"""
        # 添加用户消息到历史记录
        self.messages.append({"role": "user", "content": prompt})
        
        try:
            # 调用 API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages
            )
            
            # 获取助手回复
            reply = response.choices[0].message.content
            
            # 添加助手回复到历史记录
            self.messages.append({"role": "assistant", "content": reply})
            
            return reply
            
        except Exception as e:
            return f"错误：{str(e)}"

def load_config():
    """加载配置文件"""
    try:
        with open('E:\\APP\\VScode\\project\\cao\\config.yaml', 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print("错误：未找到 config.yaml 文件")
        return None

def get_commend_from_gpt(input_text):
    # 加载配置
    config = load_config()
    if not config:
        print("配置加载失败")
        return
    
    required_keys = ['api_key']
    missing_keys = [key for key in required_keys if key not in config]
    if missing_keys:
        print(f"配置文件缺少必要的键: {', '.join(missing_keys)}")
        return

    # 创建 ChatGPT 实例
    chat = ChatGPT(config)
    # print(f"当前使用的模型: {chat.model}")
    # print(f"当前使用的API地址: {chat.client.base_url}")

    user_input = '我在Windows的cmd中输入了一串错误的指令：'+input_text+'告诉我它的正确指令是什么？只需要告诉我正确的指令，不要有任何其他的回答。尤其注意不要输出多余的汉字，只输出正确的指令。'
    
    start_time = datetime.now()
    response = chat.get_response(user_input)
    time_taken = (datetime.now() - start_time).total_seconds()
    
    # print(f"ChatGPT: {response}")
    # print(f"用时: {time_taken:.2f}秒")
    return response

if __name__ == "__main__":
    input_text = 'dir /a /s /b /o:gn /p'
    print(get_commend_from_gpt(input_text))