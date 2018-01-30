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
    dict={}
    match=[]
    interest_l={'group1': [] ,'group2': []} #Interest
    client = Algor()
    algo = client.algo('matching/DatingAlgorithm/0.1.3')

    def __init__(self):

        print("initialised")

    def login(self):
        self.r=Prawo()

    def read_messages(self):
        r=self.r
        print(self.r.user.me())
        for submission in self.r.inbox.unread(limit=None):
            #print(submission.author)

            self.match.append(str(submission.author))

    def test(self):
        print(self.match)

    def write_file(self):
        file = open('goodlyfilesystem\%s.dat' %  (round(time.time())), 'w+')
        file.write(str(self.algo.pipe(cRobot.interest_l).result))
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
            for p in r.redditor(i).comments.new(limit=100):
                temp |= set([p.subreddit.display_name])
                print(temp)
            for p in r.redditor(i).submissions.new(limit=100):
                temp |= set([p.subreddit.display_name])
                print(temp)
            if x%2==0:
                self.interest_l['group1'].append(dictify(i,temp))
            else :
                self.interest_l['group2'].append(dictify(i,temp))

    def matcher(self):
        self.dict=self.algo.pipe(self.interest_l).result  #sends data to Algorithmia site

    def send_messages(self):
        dict = self.dict
        for i in dict:
            self.r.redditor(i).message(subject="You've been matched!", message="You're matched with %s!\n \n bot made by HighPriestCthulhu" % ('u/'+dict[i]))
            self.r.redditor(dict[i]).message(subject="You've been matched!", message="You're matched with %s!\n \n bot made by HighPriestCthulhu" % ('u/'+i))
cRobot=Robot()
cRobot.login()
cRobot.read_messages()
cRobot.reduce_list()

cRobot.get_subreddits()
cRobot.matcher()
cRobot.send_messages()

print(cRobot.dict)
#print(cRobot.dict.result)
