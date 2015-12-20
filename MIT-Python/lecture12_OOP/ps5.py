# 6.00 Problem Set 5
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# Problem Set 5

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_subject(self):
        return self.subject
    def get_summary(self):
        return self.summary
    def get_link(self):
        return self.link


#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger
def deal_word(strg):
    for i in string.punctuation:
        if i not in strg: continue
        else: strg = strg.replace(i, ' ')
    return strg.split()

class WordTrigger(Trigger):
    def __init__(self, text):
        Trigger.__init__(self)
        self.text = text.lower()
    def is_word_in(self, story_word):
        compare = deal_word(story_word)
        # print self.text
        # print compare
        if self.text in compare: return True
        else: return False

# TODO: TitleTrigger
class TitleTrigger(WordTrigger):
    def __init__(self, text):
        WordTrigger.__init__(self, text)

    def evaluate(self, story):
        story_word = story.get_title().lower()
        return self.is_word_in(story_word)

# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):
    def __init__(self, text):
        WordTrigger.__init__(self, text)

    def evaluate(self, story):
        story_word = story.get_subject().lower()
        return self.is_word_in(story_word)

# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):
    def __init__(self, text):
        WordTrigger.__init__(self, text)

    def evaluate(self, story):
        story_word = story.get_summary().lower()
        return self.is_word_in(story_word)

# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, judge):
        Trigger.__init__(self)
        self.judge = judge
    def evaluate(self, story):
        j = self.judge.evaluate(story)
        if not j: return True
        else: return False

# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, judge1, judge2):
        Trigger.__init__(self)
        self.judge1 = judge1
        self.judge2 = judge2
    def evaluate(self, story):
        j1 = self.judge1.evaluate(story)
        j2 = self.judge2.evaluate(story)
        if j1 and j2: return True
        else: return False

# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, judge1, judge2):
        Trigger.__init__(self)
        self.judge1 = judge1
        self.judge2 = judge2
    def evaluate(self, story):
        j1 = self.judge1.evaluate(story)
        j2 = self.judge2.evaluate(story)
        if j1 or j2: return True
        else: return False

# Phrase Trigger
# Question 9
class PhraseTrigger(Trigger):
    def __init__(self, text):
        Trigger.__init__(self)
        self.text = text
    def evaluate(self, story):
        j1 = self.text in story.get_subject()
        j2 = self.text in story.get_title()
        j3 = self.text in story.get_summary()
        if j1 or j2 or j3: return True
        else: return False

# TODO: PhraseTrigger


#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering) 
    # Feel free to change this line!
    stories_ft = list()
    for st in stories:    
        for key in triggerlist: 
            if key.evaluate(st): 
                stories_ft.append(st)
                break

    return stories_ft

#======================
# Part 4
# User-Specified Triggers
#======================

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)
    
    # TODO: Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a set of triggers from it and
    # return the appropriate ones

    # wendy's code from here
    addition = list()
    triggerlist = list()
    trigger_dict_all = dict()   # this is to get all the info
    trigger_dict_basic = dict() # this is just to make the title/ subject/ summary/ phrase trigger

    word_t = ['SUBJECT', 'TITLE', 'SUMMARY', 'PHRASE']
    judge_t = ['AND', 'OR', 'NOT']
    for item in lines: 
        w_1 = item[: item.find(' ')]
        w_2 = item[item.find(' ')+1: item.find(' ', item.find(' ')+1)]
        if w_1 == 'ADD': 
            value = item.split()
            for v in value[1: ]:
                addition.append(v)
        elif w_2 in judge_t: 
            value = item.split()
            trigger_dict_all[w_1] = value[1: ]
        else:
            trigger_dict_all[w_1] = [w_2, item[item.find(' ', item.find(' ')+1)+1: ]]
    
    
    for k in trigger_dict_all.keys():
        print k, trigger_dict_all[k][0]
        if trigger_dict_all[k][0] in word_t:
            if trigger_dict_all[k][0] == 'TITLE': trigger_dict_basic[k] = TitleTrigger(trigger_dict_all[k][1])
            elif trigger_dict_all[k][0] == 'SUMMARY': trigger_dict_basic[k] = SummaryTrigger(trigger_dict_all[k][1])
            elif trigger_dict_all[k][0] == 'SUBJECT': trigger_dict_basic[k] = SubjectTrigger(trigger_dict_all[k][1])
            elif trigger_dict_all[k][0] == 'PHRASE': trigger_dict_basic[k] = PhraseTrigger(trigger_dict_all[k][1])

    for k in trigger_dict_all.keys():
        if trigger_dict_all[k][0] in judge_t:
            if trigger_dict_all[k][0] == 'AND': trigger_dict_basic[k] = AndTrigger(trigger_dict_basic[trigger_dict_all[k][1]], trigger_dict_basic[trigger_dict_all[k][2]])
            elif trigger_dict_all[k][0] == 'OR': trigger_dict_basic[k] = OrTrigger(trigger_dict_basic[trigger_dict_all[k][1]], trigger_dict_basic[trigger_dict_all[k][2]])
            elif trigger_dict_all[k][0] == 'NOT': trigger_dict_basic[k] = NotTrigger(trigger_dict_basic[trigger_dict_all[k][1]])
    print trigger_dict_basic
    print trigger_dict_all
    print addition
    for i in addition:
        triggerlist.append(trigger_dict_basic[i])
    print triggerlist
    return triggerlist

import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    t1 = SubjectTrigger("Obama")
    t2 = SummaryTrigger("MIT")
    t3 = PhraseTrigger("Supreme Court")
    t4 = OrTrigger(t2, t3)
    triggerlist = [t1, t4]
    
    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line 
    triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []
    
    while True:
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)
    
        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)
        
        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print "Sleeping..."
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()

