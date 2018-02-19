import Algorithmia
import praw
import time
from login import Algor, Prawo
#Made by Alex Dekker aka SadAlbatross/HighPriestCthulhu, the author of messy code



class Robot:
    dict={}
    participants=[]
    interest_l={'group1': [] ,'group2': []} #Interests
    client = Algor()
    algo = client.algo('matching/DatingAlgorithm/0.1.3')

    def __init__(self):

        print("initialised")

    def login(self):
        self.r=Prawo()
        print("logged in as: " + str(self.r.user.me()))

    def read_messages(self, read=False): #if read == True, will print messages recieved
        r=self.r
        self.participants=[]
        for submission in self.r.inbox.unread(limit=None):
            #print(submission.author)

            if isinstance(submission, praw.models.Message):
                self.participants.append(str(submission.author))
                if read:
                    print('\nAUTHOR:')
                    print(submission.author)
                    print('SUBJECT:')
                    print(submission.subject)
                    print('BODY:')
                    print(submission.body)
                    time.sleep(2)
        if read:
            print('\n'+'-'*20+'End Messages'+'-'*20+'\n'+'-'*18+str(len(self.participants))+' participants'+'-'*18+'\n')
            #Above word soup is just for instant feedback, participant count

    def test(self):
        print(self.participants)

    def write_file(self):
        file = open('goodlyfilesystem\%s.dat' %  (round(time.time())), 'w+')
        file.write(str(self.algo.pipe(self.interest_l).result))
        file.close()

    def reduce_list(self):
        self.participants = list(set(self.participants))
        if 'None' in self.participants:
            self.participants.remove('None') #Make into set then unmakes, removes multiple occurence. Removes reddit and null values
        if 'null' in self.participants:
            self.participants.remove('null')
        if 'reddit' in self.participants:
            self.participants.remove('reddit')

    def get_subreddits(self):
        m=self.participants
        r=self.r
        x=0
        for i in m:
            x+=1
            temp= set('')
            for p in r.redditor(i).comments.new(limit=200):
                temp |= set([p.subreddit.display_name])
                #print(temp)
            for p in r.redditor(i).submissions.new(limit=200):
                temp |= set([p.subreddit.display_name])
                #print(temp) 
            if x%2==0:
                self.interest_l['group1'].append(self.dictify(i,temp))
            else :
                self.interest_l['group2'].append(self.dictify(i,temp))
            print(temp)

    def matcher(self):
        self.dict=self.algo.pipe(self.interest_l).result  #sends data to Algorithmia site
        print(self.dict)

    def send_messages(self):
        dict = self.dict
        for i in dict:
            self.r.redditor(i).message(subject="You've been matched! ", message="You're matched with %s!\n \n bot made by u/HighPriestCthulhu" % ('u/'+dict[i]))
            self.r.redditor(dict[i]).message(subject="You've been matched! ", message="You're matched with %s!\n \n bot made by u/HighPriestCthulhu" % ('u/'+i))
            print("Sent")

    def status(self):
        self.login()
        self.read_messages(True)
        self.participants = []

    def activate(self):
        self.login()
        self.read_messages()
        self.reduce_list()
        self.get_subreddits()
        self.write_file()
        self.matcher()
        self.send_messages()

    def dictify(self, name, interests):

        interests=list(interests)
        dict = {}
        dict['name'] = name
        dict['interests']=interests
        return dict
#Create instance of class and makes the robot run
