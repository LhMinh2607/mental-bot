import time
import pandas as pd
from googletrans import Translator

# text= 'prey 2017'
# translator = Translator()
# dt = translator.translate(text, dest='en')
# dt = str(dt.text).replace("2017", " ")
# print(dt)
translator = Translator()
translator.raise_Exception = True
topics = []
questionID = []
questionTitle = []
questionText = []
upvotes = []
views = []
answerTexts = []
topicName = "workplace-relationships" #input topicName here


topicCol = "topic"
questionIdCol = "questionID"
questionTitleCol = "questionTitle"
questionTextCol = "questionText"
answerCol = "answerText"
upvoteCol = "upvotes"
viewCol = "views"
df = pd.read_csv('z_pythontest/counsel_chat.csv')


# topicArr = ["depression", "anxiety", "relationships", "parenting", "family-conflict", "self-esteem", "trauma", "marriage", "anger-management",]

for questionIndex in range(0, 845):
    topics = []
    questionID = []
    questionTitle = []
    questionText = []
    upvotes = []
    views = []
    answerTexts = []
    currentQuestionID = ''
    currentTopic = ''
    for i, j in df.iterrows():
        try:
            if int(j['questionID'])==questionIndex:
                dt3 = translator.translate(str(j['answerText']), dest='vi')
                answerTexts.append(str(dt3.text))
                dt1 = translator.translate(str(j['questionTitle']), dest='vi')
                questionTitle.append(str(dt1.text))
                dt2 = translator.translate(str(j['questionText']), dest='vi')
                questionText.append(str(dt2.text))
                upvotes.append(str(j['upvotes']))
                topics.append(str(j['topic']))
                views.append(str(j['views']))
                questionID.append(str(int(j['questionID'])))
                print(str(j['questionID'])+str(dt1.text))
                print(str(dt3.text))
                currentQuestionID=str(int(j['questionID']))
                currentTopic=str(j['topic'])
                time.sleep(0.5)
        except Exception as e:
            print(e)
    data = pd.DataFrame({topicCol: topics, questionIdCol: questionID, questionTitleCol:questionTitle, questionTextCol: questionText, answerCol: answerTexts, upvoteCol: upvotes, viewCol: views})
    data.to_csv('z_pythontest/dataset2/counselchat_vi_'+currentTopic+"_"+currentQuestionID+'.csv', index=False, encoding='utf8')

# list1 = [10,20,30,40]
# list2 = [40,30,20,10]
# col1 = "X"
# col2 = "Y"
# data = pd.DataFrame({col1:list1,col2:list2})
# data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)