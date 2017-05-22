import requests
import json
import base64
from functools import reduce

class Robot(object):
  # 定义key
  key = 'b7eb33f02fd14c8e8316f617577764c2'

  # 定义用户姓名
  def __init__(self, userName):
    super(Robot, self).__init__()
    self.userName = bytes.decode(base64.urlsafe_b64encode(userName.encode()))

  # 聊天操作
  def Chatting(self, info):
    # 定义requestUrl
    requestUrl = 'http://www.tuling123.com/openapi/api?key=' + self.key + '&info=' + info + '&userid' + self.userName
    response = json.loads(requests.get(requestUrl).text)
    responseCode = int(response['code'])
    # 文本类信息
    if responseCode == 100000:
      return response['text']
    # 链接类信息 / 菜谱类信息
    elif responseCode == 200000:
      return response['text']+ '\n' + response['url']
    # 新闻类信息
    elif responseCode == 302000:
      # 定义reduce的迭代函数，使用join拼接字符串
      def computedStr(pre, current):
        stringArray = [
          '\n',
          '看点：',
          current['article'],
          '\n',
          '来源：',
          current['source'],
          '\n',
          '链接：',
          current['detailurl'],
        ]
        return pre + ' '.join(stringArray)
      return response['text'] + reduce(computedStr, response['list'], '')
    else:
      return response['text']

def main():
    userName = input('请输入您的姓名：')
    robot = Robot(userName)
    chatString = input('请输入您想说的的话（输入为空自动结束）：')
    while chatString != '':
      print(robot.Chatting(chatString))
      chatString = input('请输入您想说的的话（输入为空自动结束）：')

main()
