# CAO 命令行工具

这是一个简单的命令行工具，用于修正命令行的指令，你只需要在输入错误的指令后在命令行输入cao即可自动修正。
在使用
## 使用教程
1.克隆仓库到本地
```sh
git clone https://github.com/FlyingCY600/cmd_cao.git
# 如果网络原因打不开，可以科学上网
#也可直接下载zip文件
```
2.使用pip安装
```sh
#cd到文件所在文件夹
cd /d ./cmd_cao
#安装
pip install .
#可能需要梯子
```
3.获取api_key:推荐[免费apikey](https://github.com/chatanywhere/GPT_API_free)获取
  免费用过这个项目的，一天200次免费请求，挺好用的，也可付费（无广）
4.添加api_key
```sh
#向配置文件中添加api_key
cao -add sk-rdf*************
```
5.愉快地使用吧
## 示例
![tu](https://github.com/FlyingCY600/cmd_cao/blob/main/126.png)
模型输出后会自动复制在粘贴板，鼠标右键粘贴即可
## 目前存在的问题
1. 只适配window的cmd
2. 极少数情况模型输出不正确
## 欢迎提pr
## 联系作者：CYF6000@proton.me
