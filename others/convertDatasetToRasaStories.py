import pandas as pd
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

topics = []
questionID = []
questionTitle = []
questionText = []
upvotes = []
views = []
answerTexts = []


topicCol = "topic"
questionIdCol = "questionID"
questionTitleCol = "questionTitle"
questionTextCol = "questionText"
answerCol = "answerText"
upvoteCol = "upvotes"
viewCol = "views"

topicNames = [
"depression", #0 - 138
"anxiety", #140 - 229
"parenting", #230 - 285
"self-esteem", #286 - 334
"workplace-relationships", #335 - 380
"spirituality", #381 - 387
"trauma", #388 - 411
"domestic-violence", #412 - 427
"sleep-improvement", #428 - 459
"intimacy" #460 - 557
"grief-and-loss", #568 - 580
"substance-abuse", #581 - 591
"family-conflict", #592 - 652
"marriage", #653 - 672
"eating-disorders", #674 - 678
"relationships", #679 - 781
"lgbtq", #783 - 801
"behavioral-change", #804 - 837
"addiction", #839 - 841
"legal-regulatory", #842 - 844
# "self-harm",
# "eating-disorders",
# "legal-regulatory",
# "stress",
# "children-adolescents",
# "addiction",
# "human-sexuality",
# "military-issues"
]

length = len(topicNames)

# df = pd.read_csv('D:\\UNIVERSITY STUFFS\THESUS\MentalBotV2\z_pythontest\dataset2\counselchat_vi_depression_0.csv', encoding="utf8")
# df = pd.read_csv('z_pythontest/dataset/counselchat_vi_depression_0.xlsx')
# BASE_DIR = os.getcwd()
# BASE_DIR = "D:\\UNIVERSITY STUFFS\THESUS\MentalBotV2\z_pythontest\dataset2"
# csv_path = "z_pythontest\dataset2\counselchat_vi_depression_0.csv"

# df = pd.read_csv(os.path.join(csv_path))

# df = pd.read_csv('z_pythontest/counsel_chat.csv')
print("df")

# f = open("others/StoriesDataset.yml", 'w', encoding="utf-8")
f = open("others/RulesDataset.yml", 'w', encoding="utf-8")


# f = open("z_pythontest/dataset2/counselchat_vi_depression_0.csv", 'r')

# for id in range(length):
#     # f.write("Topic: "+topicNames[id])
#     topics = []
#     questionID = []
#     questionTitle = []
#     questionText = []
#     upvotes = []
#     views = []
#     answerTexts = []
#     currentQuestionID = ''
#     currentTopic = ''

def csvToRasaStoriesYaml(topicName, range1, range2):
    try:
        for i in range(range1, range2):
            print(topicName)
            # print('z_pythontest/dataset/counselchat_vi_'+topicName+'_'+str(i)+'.csv')
            try:
                df = pd.read_csv('z_pythontest/dataset2/counselchat_vi_'+topicName+'_'+str(i)+'.csv', encoding="utf-8")
                f.write("- rule: "+str(topicName)+" "+str(i)+"\n")
                f.write("  steps:"+"\n")
                f.write("  - intent: "+str(topicName)+"_"+str(i)+"\n")
                f.write("  - action: utter_"+str(topicName)+"_"+str(i)+"\n")
            except Exception as e:
                print(e)
                continue
    except Exception as e:
        print(e)
        pass

print(length)

# for id in range(length):
    # print(id)
    # print(topicNames[id])
    # topics = []
    # questionID = []
    # questionTitle = []
    # questionText = []
    # upvotes = []
    # views = []
    # answerTexts = []
    # currentQuestionID = ''
    # currentTopic = ''
    # csvToRasaStoriesYaml(topicNames[id])
csvToRasaStoriesYaml("depression",0,138+1)#
csvToRasaStoriesYaml("anxiety",140 , 229+1)#
csvToRasaStoriesYaml("parenting",230 , 285+1)#
csvToRasaStoriesYaml("self-esteem",335 , 380+1)#
csvToRasaStoriesYaml("workplace-relationships",381 , 387+1)#
csvToRasaStoriesYaml("spirituality",0,138+1)#
csvToRasaStoriesYaml("trauma",388 , 411+1)#
csvToRasaStoriesYaml("domestic-violence",412 , 427+1) #
csvToRasaStoriesYaml("sleep-improvement",428 , 459+1) #
csvToRasaStoriesYaml("intimacy",460 , 557+1) #
csvToRasaStoriesYaml("grief-and-loss",568 , 580+1) #
csvToRasaStoriesYaml("substance-abuse",581 , 591+1) #
csvToRasaStoriesYaml("family-conflict",592 , 652+1) #
csvToRasaStoriesYaml("marriage",653 , 672 +1) #
csvToRasaStoriesYaml("eating-disorders",674 , 678+1) #
csvToRasaStoriesYaml("relationships",679 , 781+1) #
csvToRasaStoriesYaml("lgbtq",783 , 801+1) #
csvToRasaStoriesYaml("behavioral-change",804 , 837+1) #
csvToRasaStoriesYaml("addiction",839 , 841+1) #
csvToRasaStoriesYaml("legal-regulatory",842 , 844+1) #
"anxiety", #140 , 229 v
"parenting", #230 , 285 v
"self-esteem", #286 , 334 v
"workplace-relationships", #335 , 380 v
"spirituality", #381 , 387 v
"trauma", #388 , 411 v
"domestic-violence", #412 , 427 v
"sleep-improvement", #428 , 459 v
"intimacy" #460 , 557 v
"grief-and-loss", #568 , 580 v
"substance-abuse", #581 , 591 v
"family-conflict", #592 , 652 v
"marriage", #653 , 672 v
"eating-disorders", #674 , 678 v
"relationships", #679 , 781 v
"lgbtq", #783 , 801 v
"behavioral-change", #804 , 837 v
"addiction", #839 , 841 v
"legal-regulatory", #842 , 844 v
