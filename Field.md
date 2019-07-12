### Toutiao 数据字段说明

#### KOL 基本信息字段

```
  "long_video_price",
  "is_star",
  "rank",                                               // 排名
  "follower",
  "create_time",
  "total_favour_cnt",
  "avg_play",
  "abandon_sign_result",
  "id",
  "appeal_id",
  "city",
  "short_id",
  "tags",
  "platform_source",
  "cut_rate",
  "recommend",                                              //是否是系统的推荐
  "lowest_price",                                           //最低价格
  "next_month_price",                                       //下月价格
  "author_type",
  "province",
  "online_status",
  "next_month_long_video_price",                            //下月长视频价格
  "price",
  "is_online",
  "has_phone",
  "core_user_id",
  "category_id",
  "protocol_id",
  "nick_name",                                              // 昵称
  "gender",
  "aweme_tags",
  "order_cnt",                                               //订单数
  "rate",
  "modify_time",
  "avatar_uri",                                             // 头像URi
  "price_info",                                             // 详细价格信息
  "task_status",                                            // 任务状态
  "unique_id"
```


#### KOL 详情字段 (有很多重复)

```
  "is_visible",                                             // 是否可见
  "long_video_price",                                       // 长视频价格
  "platform_source",                                        // 平台来源（1 未知）
  "follower",                                               // 粉丝数
  "create_time",                                            // 创建时间
  "total_favour_cnt",                                       // 总点赞数
  "avg_play",                                               // 平均播放量
  "abandon_sign_result",                                    // ？？？
  "id",
  "appeal_id",                                              // ???
  "city",
  "short_id",
  "platform",                                               // 平台
  "mcn_logo",                                               // MCN 图标
  "tags",                                                   // 分类标签，美食，美妆等
  "is_star",                                                // 是否星标
  "star_video_count",                                       // 星标视频数
  "lowest_price",                                           // 最低价
  "next_month_price",                                       // 下月价格
  "author_type",                                            // 类型
  "province",
  "mcn_id",                                                 // MCN id
  "mcn_name",
  "online_status",                                          // 在线状态
  "next_month_long_video_price",                            // 下月长视频价格
  "price",
  "phone",                                                  // 手机号
  "is_online",
  "order_done_count",                                       // 完成作品订单数
  "has_phone",
  "core_user_id",                                           // 用户ID
  "category_id",                                            // 类型Id
  "protocol_id",
  "nick_name",                                              // 昵称
  "gender",                                                 // 性别
  "aweme_tags",                                             // 类似上面的tag
  "rate",
  "modify_time",
  "avatar_uri",
  "price_info",
  "task_status",
  "mcn_name",
  "unique_id"
```
#### KOL 订单信息

```
order_avg_time_cost: 7                                      // 订单平均耗时
order_complete_cnt: 10                                      // 完成数量
order_complete_rate: 0.8333333333333334                     // 完成率
```

#### KOL 内容基本信息


```
{
  "latest_item_info": [],                                   // 个人作品，结构同下
  "latest_star_item_info": [                                // 任务作品信息
    {
      "comment": 744,                                       // 评论数
      "play": 302713,                                       // 播放数
      "item_animated_cover": "https://p3-dy.byteimg.com/obj/23703000240b916f31d86",  // 封面动态链接
      "share": 146,                                         // 分享数
      "item_date": "2019-05-13",                            // 时间戳
      "item_id": "6690150979733654791",                     // 内容id
      "item_cover": "https://p3-dy.byteimg.com/obj/236ed00016551d6bcddc6", // 内容图片
      "like": 29283,                                        // 喜欢数
      "item_title": "我们有彼此，我们从不孤单，因为粑知道布永远在我身边#当你孤单你会想起谁 #一条狗的使命2", // 内容标题
      "video_id": "v0200f770000bjcks5pdli3po8aavmn0",       // 视频ID
      "create_timestamp": 1557745181                        // 创建时间戳
    }
  ],
   "latest_item_statics_antispam": {                         // 最新内容信息反垃圾统计数据
    "avg_share": 298,                                       // 平均分享数
    "avg_comment": 444,                                     // 平均评论数
    "max_comment": 1866,                                    // 最大评论数
    "max_share": 1222,                                      // 最大分享数
    "max_like": 141114,                                     // 最大喜欢量
    "avg_play": 403795,                                     // 平均播放量
    "avg_like": 31877,                                      // 平均喜欢量
    "max_play": 1780231                                     // 最大播放量
  },
}
```


#### 内容详情字段

```
{
  "ltm_item_statics": [
    {
      "comment": 12,   // 评论数
      "status": 1,     // 状态 1 表示什么还未知？？
      "play": 14549,   // 播放量
      "like": 120,     // 喜爱数
      "url": "https://www.iesdouyin.com/share/video/6695233502327082248/?region=CN&mid=6695176493506808583",                // 视频地址
      "original_status": 102,
      "video_id": "v0200fce0000bjl3ukga2pesgqm8ujqg",
      "share": 6,                            // 分享数
      "item_title": "最近实在不知道吃什么了，做了点凉粉配上万能料汁，嗯，惬意~ #美食 @抖音美食 @抖音小助手 ",                               // 标题
      "create_time": 1558855526,
      "head_image_uri": "261f200062dcc0cf53129",
      "item_id": "6695233502327082248",
      "core_user_id": 62854908733
    }
  ]
}
```

#### 每天粉丝趋势数据

```
date: "2019-03-30"
fans_cnt: 18267327
```

#### 粉丝分布

有性别、省份、年龄、设备、活跃度等维度

```
{
    "distribution_list":[
        {
            "distribution_key":"male",
            "distribution_value":2484189
        },
        {
            "distribution_key":"female",
            "distribution_value":22421753
        }
    ],
    "type_display":"性别分布",
    "type":1
},
```




