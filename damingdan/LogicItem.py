# -*- coding: utf-8 -*-
import sys, time, os
from database import database
sys.path.append("..")
import webImage, send

'''
CREATE TABLE IF NOT EXISTS `tbl_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL COMMENT '藤名称',
  `image` varchar(512) NOT NULL COMMENT '第一张图片',
  `creator` int(11) NOT NULL COMMENT '创建者',
  `create_time` int(11) NOT NULL COMMENT '创建时间',
  `fans` int(11) NOT NULL COMMENT '粉丝数',
  `bangs` int(11) NOT NULL COMMENT '上榜数',
  `is_verified` tinyint(1) NOT NULL COMMENT '认证藤',
  `verified_word` varchar(512) NOT NULL COMMENT '认证说明',
  `status` tinyint(1) NOT NULL COMMENT '状态：0正常，1删除',
  `refered_to` int(11) DEFAULT NULL,
  `image_large` varchar(512) NOT NULL,
  `image_medium` varchar(512) NOT NULL,
  `image_small` varchar(512) NOT NULL,
  `catagory` int(11) NOT NULL,
  `subcatagory` varchar(256) DEFAULT NULL,
  `description` text,
  `url` varchar(256) NOT NULL,
  `source` int(11) NOT NULL,
  `foreign_id` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COMMENT='藤数据' AUTO_INCREMENT=10000053 ;

CREATE TABLE IF NOT EXISTS `tbl_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mingdan_id` int(11) NOT NULL COMMENT '外键名单, 评论是对一个名单的评论',
  `content` text NOT NULL COMMENT '评论的内容',
  `user_id` int(11) NOT NULL COMMENT '发表该评论的用户ID',
  `item_id` int(11) NOT NULL,
  `dings` int(11) NOT NULL DEFAULT '0',
  `cais` int(11) NOT NULL DEFAULT '0',
  `create_time` int(11) NOT NULL DEFAULT '0',
  `status` int(11) NOT NULL DEFAULT '0' COMMENT '0:正常, 1:删除，2：用户自删',
  `img_src` varchar(255) NOT NULL COMMENT '原图',
  `img_large` varchar(255) NOT NULL COMMENT ' 大图',
  `img_medium` varchar(255) NOT NULL COMMENT '中图',
  `img_small` varchar(255) NOT NULL COMMENT '小图 ',
  `video_link` varchar(255) NOT NULL COMMENT '视频链接',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=58 ;
'''

class LogicItem(database):
    def __init__(self):
        database.__init__(self)
        self.table = "tbl_item"
        self.itemNewsTable = "tbl_item_news"

    def __del__(self):
        pass

    # need add the comment image path
    def addItem(self, item):
        # check repeat
        itemId = self.checkItemExist(item["title"])
        if itemId != False and itemId != None:
            print "item %s already exist"%(item["title"])
            return int(itemId)
        
        
        # get the image
        imageUrl = item["image"]
        item["image"] = webImage.getWebImageName(imageUrl)
        # send the download order
        send.sendMessage("image_download", "url=%s,file_name=%s"%(imageUrl, item["image"]))
        item["image_large"] = webImage.renameFile(item["image"], "180x180")
        item["image_medium"] = webImage.renameFile(item["image"], "80x80")
        item["image_small"] = webImage.renameFile(item["image"], "50x50")
        
        itemId = database.create(self, self.table, item)

        # set the damingdan admin to be the owner
        self.addItemOwner(itemId, 1, 1)

        comment = {}
        comment["mingdan_id"] = -1
        comment["item_id"] = itemId
        comment["content"] = item["title"]
        comment["user_id"] = 1
        comment["dings"] = 0
        comment["cais"] = 0
        comment["create_time"] = int(time.time())
        comment["status"] = 0
        comment["img_src"] = item["image"]
        comment["img_large"] = webImage.renameFile(item["image"], "440")
        comment["img_medium"] = webImage.renameFile(item["image"], "192")
        comment["img_small"] = item["image_small"]
        database.create(self, "tbl_comment", comment)

        return itemId
    
    def addItemNews(self, itemId, newsContent):
        news = {}
        news["item_id"] = itemId
        news["content"] = newsContent
        news["post_time"] = int(time.time())
        database.create(self, self.itemNewsTable, news)

        
    def checkItemExist(self, title):
        condition = {}
        condition["title"] = title
        return database.checkExist(self, self.table, condition)

    def addItemOwner(self, itemId, userId, status = 0):
        itemOwner = {}
        itemOwner["item_id"] = itemId
        itemOwner["user_id"] = userId
        itemOwner["status"] = status
        return database.create(self, self.table, itemOwner)

    def incrItemStats(self, itemId, field, increment):
        condition = {}
        condition["id"] = itemId
        database.increse(self, self.table, field, increment, condition)

    def decrItemStats(self, itemId, field, decrement):
        condition = {}
        condition["id"] = itemId
        database.decrese(self, self.table, field, decrement, condition)



if __name__ == "__main__":
    logicItem = LogicItem()
    item = {}
    item["title"] = "cs";
    logicItem.addItem(item, item)
