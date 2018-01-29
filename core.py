import Algorithmia
import praw
import time
from login import Algor, Prawo
#Made by Alex Dekker aka SadAlbatross/HighPriestCthulhu, the author of messy code

def dictify(name, interests):

    interests=list(interests)
    dict = {}
    dict['name'] = name
    dict['interests']=interests
    return dict
class Robot:

    match=[]
    interest_l={'group1': [] ,'group2': []} #Interest group
    group1=[]
    group2=[]
    client = Algor()
    algo = client.algo('matching/DatingAlgorithm/0.1.3')

    def __init__(self):

        print("initialised")

    def login(self):
        self.r=Prawo()

    def read_messages(self):
        r=self.r
        for submission in self.r.inbox.unread(limit=None):
            print(submission.author)
            self.match.append(str(submission.author))

    def test(self):
        print(self.match)

    def write_file(self):
        file = open('goodlyfilesystem\%s.dat' %  (round(time.time())), 'w+')
        file.write(str(algo.pipe(cRobot.interest_l).result))
        file.close()

    def reduce_list(self):
        self.match = list(set(self.match))
        if 'None' in self.match:
            self.match.remove('None') #Make into set then unmakes, removes multiple occurence.

    def get_subreddits(self):
        m=self.match
        r=self.r
        x=0
        for i in m:
            x+=1
            temp= set('')
            for p in r.redditor(i).comments.new(limit=500):
                temp |= set([p.subreddit.display_name])
            for p in r.redditor(i).submissions.new(limit=500):
                temp |= set([p.subreddit.display_name])
            if x%2==0:
                self.interest_l['group1'].append(dictify(i,temp))
            else :
                self.interest_l['group2'].append(dictify(i,temp))

            print(dictify(i,temp))

    def matcher(self):
        self.dict=algo.pipe(cRobot.interest_l.result  #sends data to Algorithmia site

cRobot=Robot()
cRobot.login()
cRobot.read_messages()
cRobot.reduce_list()
cRobot.get_subreddits()
cRobot.write_file()
cRobot.matcher()

print(cRobot.interest_l)


print(cRobot.dict)
