var request = require('request');
var chalk = require('chalk');

/**
 * 根据返回的类型输出指定的结果
 * @param  {[object]} responseText [返回的报文主体]
 * @return {[string]}              [给用户的输出内容]
 */
var computedString = function(responseText) {
  switch (responseText.code) {
    case 100000: // 文本类信息
      {
        return responseText.text;
      }
    case 200000: // 链接类信息 或 菜谱类信息
      {
        return responseText.text + '\n' + responseText.url;
      }
    case 302000: // 新闻类信息
      {
        return responseText.text + responseText.list.reduce(function(pre, current) {
          var stringArray = [
            '\n',
            '看点：',
            current.article,
            '\n',
            '来源：',
            current.source,
            '\n',
            '链接：',
            current.detailurl,
          ]
          return pre + stringArray.join(' ');
        }, '');
      }
    default:
      {
        return responseText.text;
      }
  }
}

/**
 * 机器人操作的函数
 * @param  {[string]} info     [用户输入的对话字符串]
 * @param  {[string]} userName [用户姓名]
 * @param  {[func]}   callback [回调函数，这里是如果用户输入不为空会递归执行]
 * @return {[string]}          [返回机器人的回应]
 */
var robot = function(info, userName, callback) {
  var key = 'b7eb33f02fd14c8e8316f617577764c2';
  var requestUrlArray = [
    'http://www.tuling123.com/openapi/api?key=',
    key,
    '&info=',
    info,
    '&userid=',
    userName
  ];
  var requestUrl = encodeURI(requestUrlArray.join('')); // 一定要使用encodeURI否则无法识别中文
  request(requestUrl, function(error, response, body) {
    if (error) {
      console.log(chalk.red('💁   亲~网络错误啦，请稍后再试~'));
    }
    var stdout = '💁   ' + computedString(JSON.parse(body));
    console.log(chalk.blue(stdout));
    callback(); // 递归执行，执行回调
  });
}

module.exports = robot;