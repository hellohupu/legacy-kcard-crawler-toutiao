### 说明

1. ./src 下创建 creds.js , 写入如下内容：
  module.exports = {
    username: <your-account@email.com>,
    password: <password>
};

2. 运行 ``` node ./src/cookie.js ```, 获取cookie

3. 修改将cookie 写入 run.sh

4. sh run.sh
