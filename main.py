from csv import reader
import matplotlib.pyplot as plt
import tweepy
import csv
import pandas as pd

#Function To Extract Tweets From  Twitter Of A Particular Hashtag.
def scrap_twitter():
	
	####input your credentials here From Developer Account OF Twitter
	consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
	consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
	access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
	access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth,wait_on_rate_limit=True)
	csvFile = open('result.csv', 'a')
	csvWriter = csv.writer(csvFile)

	for tweet in tweepy.Cursor(api.search,q="#USelections2020",count=15000,
	lang="en",
	since="2020-11-03").items():
		print (tweet.created_at, tweet.text)
		csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    
#To Analyze The Extracted Csv and PLot The Graph
def analysis():
	trump=0
	biden=0
	visa =0
	jobs=0
	covid=0
	with open('result.csv', 'r') as read_obj:
	    
	    csv_reader = reader(read_obj)
	   
	    for row in csv_reader:
	       word=' '.join([str(elem) for elem in row])
	       word =word.lower()
	       if(word.find('trump will win')!=-1 or word.find('red win')!=-1 or word.find('vote for trump')!=-1 ):
	       	trump+=1
	       if(word.find('biden will win')!=-1 or word.find('blue win')!=-1) or word.find('vote for biden')!=-1:
	       	biden+=1
	       if(word.find('h1b visa')!=-1):
	       	visa+=1
	       if(word.find('jobs')!=-1):
	       	jobs+=1
	       if(word.find('covid19')!=-1 or word.find('covid19 cases')!=-1 or word.find('covid')!=-1):
	       	covid+=1
	       
	print(trump)
	print(biden)
	print(visa)
	print(jobs)
	print(covid)

	fig=plt.figure()
	fig = plt.figure(figsize = (10, 5)) 

	plt.title("Twitter Analysis",fontstyle='italic',fontsize='20',color='#00bcd4')
	plt.xlabel("Topics ",fontstyle='italic',fontsize='15',color='#00bcd4')

	plt.ylabel("Count",fontstyle='italic',fontsize='15',color='#00bcd4')
	topics=['Covid19 Cases','Trump Win','Biden Win','Jobs','H1B_Visa']
	values=[covid,trump,biden,jobs,visa]
	plt.bar(topics,values, color ='#251f44',  
	        width = 0.4) 
	plt.show()


if __name__=="__main__":
    scrap_twitter()
    analysis()

        
        
