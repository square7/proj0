from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import re
import numpy as np
from cStringIO import StringIO
import string

aToken="281256880-tgYIZBkXKtQf5kkZjetWNrcAmAFbkWpzZtCMUXX7"
aSec="7fodreiazWIyENqNxxo6L3B5bcycTVeBSUhqfUy5ZoejO"
cKey="bD5LhSfmWh7YRVBuQZyh7r37a"
cSec="eesi1kPUOZMVD60AQBzaz9VzOWB4oTDoZTQYaFhX1JYPSrActP"

lowSet=[]
medSet=[]
keyValues=['iran', 'nuclear', 'deal', 'lausanne']
threshold=2
class StdOutListener(StreamListener):

    def on_data(self, data):
        try:
            tex=json.loads(data)
            str=string.lower(tex['text'])
            cnt=0
            valid=[]
            for k in keyValues:
                if string.find(str,k)!=-1:
                    cnt=cnt+1
                    valid.append(k)
            if cnt>=threshold:
                #print tex['created_at'], tex['coordinates'], tex['place']
                #print tex['text']
                print data
            #if tex['filter_level']=='low':
            #    lowSet.append(tex)
            #elif tex['filter_level']=='medium':
            #    medSet.append(tex)
            #print data
        except:
            pass
        return True

    def on_error(self, status):
        print status

def extSource(ele):
    s=ele['source']
    bg=re.search('<[^<]*>',s).end()
    ed=bg+re.search('<',s[bg:]).start()
    return s[bg:ed]

l = StdOutListener()
auth = OAuthHandler(cKey, cSec)
auth.set_access_token(aToken,aSec)
stream = Stream(auth, l)

stream.filter(track=keyValues,async='True')
    



#lSet=np.array(lowSet)
#data=pd.DataFrame()
#data['lang']=map(lambda x:x['lang'], lSet)
#data['source']=map(extSource, lSet)
