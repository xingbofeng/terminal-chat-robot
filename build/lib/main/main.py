# 输入输出各种颜色的字体
from .lib.colors.colors import colormsg
# 打印版本详情信息
from .lib.infos.infos import printinfos
# 引入robot类
from .lib.robot.robot import Robot


def main():
    printinfos()
    userName = input(colormsg('green', '👉   请输入您的姓名：'))
    robot = Robot(userName)
    chatString = input(colormsg('red', '👉   请输入您想说的的话（输入为空自动结束）：'))
    while chatString != '':
        print(colormsg('blue', '💁   ' + robot.Chatting(chatString)))
        chatString = input(colormsg('red', '👉   请输入您想说的的话（输入为空自动结束）：'))

main()
