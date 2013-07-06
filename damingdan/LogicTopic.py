from database import database

"""
CREATE TABLE IF NOT EXISTS `tbl_bang_topic` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
  `bang_id` int(11) NOT NULL,
  `topic_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=168 ;




CREATE TABLE IF NOT EXISTS `tbl_topic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(64) DEFAULT NULL,
  `description` text NOT NULL,
  `logo` varchar(512) DEFAULT NULL,
  `fans` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=58 ;
"""

class LogicTopic(database):
    def __init__(self):
        database.__init__(self)
        self.bangTopicTable = "tbl_bang_topic"
        self.topicTable = "tbl_topic"
    
    # link a topic to a bang
    def addBangTopic(self, bangId, topicId):
        bangTopic = {}
        bangTopic["bang_id"] = bangId
        bangTopic["topic_id"] = topicId
        database.create(self, self.bangTopicTable, bangTopic)
    
    # add a new topic
    def addTopic(self, title, description, logo):
        topic = {}
        topic["title"] = title
        topic["description"] = description
        topic["logo"] = logo
        topic["fans"] = 0
        database.create(self, topic)
    
    # add serieous of topic
    def addBangTopicArray(self, bangId, topicNameArray):
        for topic in topicNameArray:
            topicId = topic.get("title")
            if topicId != False:
                # if this topic exist, link to the this bang
                self.addBangTopic(bangId, topicId)
            else:
                topicId = self.addTopic(topic, topic, '')
                if topicId != False:
                    self.addBangTopic(bangId, topicId)
        
    
    def getTopicByTitle(self, title):
        condition = {}
        condition["title"] = title
        return database.checkExist(self, self.topicTable, condition)

if __name__ == '__main__':
    logicTopic = LogicTopic()
    
    
    
