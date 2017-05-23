var chalk = require('chalk');

module.exports = function() {
  var infos = infos = [
    "   .______            ______     .______       ______     .___________. ",
    "    |   _  \\         /  __  \\    |   _  \\     /  __  \\    |           | ",
    "    |  |_)  |       |  |  |  |   |  |_)  |   |  |  |  |   `---|  |----` ",
    "    |      /        |  |  |  |   |   _  <    |  |  |  |       |  |      ",
    "    |  |\\  \\----.   |  `--'  |   |  |_)  |   |  `--'  |       |  |      ",
    "    | _| `._____|    \\______/    |______/     \\______/        |__|      ",
    "",
    "",
    "                        ---- 👽   A chat-robot which runs in terminal",
    "                                @author Encounter (me@xingbofeng.com)",
    "                                         last_update 2017-05-23 14:10"
  ];
  console.log(chalk.blue(infos.join('\n')));
};
