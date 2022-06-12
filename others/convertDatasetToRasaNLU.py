import pandas as pd
import sys

from regex import E
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

f = open("others/NLUDataset.yml", 'w', encoding="utf-8")
# f = open("others/NLUDatasetInDomain.yml", 'w', encoding="utf-8")

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

def csvToRasaNLUYaml(topicName, range1, range2):
    try:
        for i in range(range1, range2):
            print(topicName)
            try:
                df = pd.read_csv('z_pythontest/dataset2/counselchat_vi_'+topicName+'_'+str(i)+'.csv', encoding="utf-8")
                #for intents in nlu.yml
                f.write("- intent: "+str(topicName)+"_"+str(i)+"\n")

                # #for intents in domain.yml
                # f.write("- "+str(topicName)+"_"+str(i)+"\n")
                for i, j in df.iterrows():
                    try:
                        #for intents in nlu.yml
                        f.write("  examples: |"+"\n")
                        question = str(j['questionTitle'])
                        f.write("    - "+' '.join(question.split())+"\n")
                        f.write("\n")
                        break
                    except Exception as e:
                        print(e)
                        continue
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
    # csvToRasaNLUYaml(topicNames[id])
csvToRasaNLUYaml("depression",0,138+1)#
csvToRasaNLUYaml("anxiety",140 , 229+1)#
csvToRasaNLUYaml("parenting",230 , 285+1)#
csvToRasaNLUYaml("self-esteem",335 , 380+1)#
csvToRasaNLUYaml("workplace-relationships",381 , 387+1)#
csvToRasaNLUYaml("spirituality",0,138+1)#
csvToRasaNLUYaml("trauma",388 , 411+1)#
csvToRasaNLUYaml("domestic-violence",412 , 427+1) #
csvToRasaNLUYaml("sleep-improvement",428 , 459+1) #
csvToRasaNLUYaml("intimacy",460 , 557+1) #
csvToRasaNLUYaml("grief-and-loss",568 , 580+1) #
csvToRasaNLUYaml("substance-abuse",581 , 591+1) #
csvToRasaNLUYaml("family-conflict",592 , 652+1) #
csvToRasaNLUYaml("marriage",653 , 672 +1) #
csvToRasaNLUYaml("eating-disorders",674 , 678+1) #
csvToRasaNLUYaml("relationships",679 , 781+1) #
csvToRasaNLUYaml("lgbtq",783 , 801+1) #
csvToRasaNLUYaml("behavioral-change",804 , 837+1) #
csvToRasaNLUYaml("addiction",839 , 841+1) #
csvToRasaNLUYaml("legal-regulatory",842 , 844+1) #
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
