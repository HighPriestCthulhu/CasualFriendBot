import Algorithmia
import praw
import time
from login import Algor, Prawo

client = Algor()
algo = client.algo('matching/DatingAlgorithm/0.1.3')

def dictify(name, interests):

    interests=list(interests)
    dict = {}
    dict['name'] = name
    dict['interests']=interests
    return dict
class Robot:

    match=[]
    dict=[]
    interest_l={'group1': [] ,'group2': []}
    group1=[]
    group2=[]

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
        file.write(str(self.interest_l))
        file.close()
        time.sleep(1)

    def reduce_list(self):
        self.match = list(set(self.match))
        if 'None' in self.match:
            self.match.remove('None')

    def get_subreddits(self):
        m=self.match
        d=self.dict
        r=self.r
        temp= set('')
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

        self.dict=d

    def send_messages(self, dict):
        pass

cRobot=Robot()
cRobot.login()
cRobot.read_messages()
'''cRobot.reduce_list()
cRobot.get_subreddits()
cRobot.write_file()

print(cRobot.interest_l)


print(algo.pipe(cRobot.interest_l).result)
'''
