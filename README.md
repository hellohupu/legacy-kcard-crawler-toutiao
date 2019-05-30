### 说明

1. ./src 下创建 creds.js , 写入如下内容：
```
  module.exports = {
    username: <your-account@email.com>,
    password: <password>
};
```

2. 运行 ``` node ./src/cookie.js ```, 获取cookie

3. 修改将cookie 写入 run.sh

4. sh run.sh

5. 参数说明：

```
    --cookie 抓取用的cookie
    --max_time 最大sleep 时间，秒
    --min_time 最小时间
    --start_page 页码范围
    --end_page 页码范围
    --output_dir 输出文件目录
    <task_name> 运行的任务名， 可选 author detail item item_detail 或者 all 
```
