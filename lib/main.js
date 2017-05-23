var readline = require('readline');
var chalk = require('chalk');
var robot = require('./robot.js');
var infos = require('./infos.js');

/**
 * 与机器人对话的函数
 */
var inputChat = function() {
  var info = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  info.question(chalk.red.bold('👉   请输入您想说的话（输入为空自动结束）：'), function(input) {
    if (!input) {
      info.close();
      process.exit(0); // 如果输入为空则退出进程
      return;
    }
    process.stdin = '';
    info.close();
    robot(input, userName, inputChat); // 否则与机器人聊天
  });
}

var userName = ''; // 用户的姓名

/**
 * 输入姓名的函数
 */
var inputName = function() {
  var name = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  name.question(chalk.green.bold('👉   请输入您的姓名：'), function(input) {
    userName = input;
    process.stdin = ''; // 把标准输入清零，否则会累加如下面您想说的话
    name.close(); // 关闭name
    inputChat(); // 开始聊天
  });
}

var main = function() {
  infos();
  inputName();
};

module.exports = main;
