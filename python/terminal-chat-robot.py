import requests
import json

class Robot(object):
  # 定义key
  key = 'b7eb33f02fd14c8e8316f617577764c2'
  # 定义用户姓名
  def __init__(self, userName):
    super(Robot, self).__init__()
    self.userName = userName


  def Chatting(self, info):
    # 定义requestUrl
    requestUrl = 'http://www.tuling123.com/openapi/api?key=' + self.key + '&info=' + info + '&userid' + self.userName
    responseText = requests.get(requestUrl)
    return json.loads(responseText.text)['text']

def main():
    userName = input('请输入您的姓名：')
    robot = Robot(userName)
    chatString = input('请输入您想说的的话（输入为空自动结束）：')
    while chatString != '':
      print(robot.Chatting(chatString))
      chatString = input('请输入您想说的的话：')

main()