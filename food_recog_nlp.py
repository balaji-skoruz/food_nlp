import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
import re,time
# from words_to_number import text2int
from NLP import words_to_number
from NLP import att
# from att import Transcribe


class Food_Recog():
    def __init__(self):
        self.trans = att.Transcribe()
        self.food_list = ['Honey Boba', 'Creamer','Chocolate Drizzle','Matcha Concentrate','Black Tea','Biryani','Matcha Latte','Boba Tea','Milk Boba']
        self.activity_list = ['cook','pack']

    def get_food_items(self,text):
        food_list = []
        for i in self.food_list:
            mat = re.search(i.lower(),text.lower()) 
            if mat:
                food_list.append(i)
        # print(food_list)
        if len(food_list)>0:
            return food_list[0]
        else:
            return '' # instead of False

    def get_synonyms(self):
        synonyms = []
        for activity in self.activity_list:
            for syn in wordnet.synsets(activity):
                for lm in syn.lemmas():
                    synonyms.append(lm.name())
        activity_list =  list(set(synonyms))
        # print(activity_list)
        return activity_list
    
    def cook_or_pack(self,word):
        synonyms = []
        for syn in wordnet.synsets(word):
            for lm in syn.lemmas():
                synonyms.append(lm.name())
        synonyms = list(set(synonyms))

        if 'cook' in synonyms:
            return 'Cooking'
        elif 'pack' in synonyms:
            return 'Packing'
        else:
            return 'Cooking' # instead of False

    def get_activity(self,text):
        act_list = []
        word_list = self.get_synonyms()
        for i in word_list:
            mat = re.search(i.lower(),text.lower())
            if mat:
                act_list.append(i)
        # print(act_list)
        if len(act_list)>0:
            return self.cook_or_pack(act_list[0])
        else:
            return 'Cooking' # instead of False
        
    def get_step_number(self,text):

        text_num = words_to_number.text2int(text)
        numbers = [int(s) for s in text_num.split() if s.isdigit()]
        # print(numbers)
        if len(numbers)>0:
            return numbers[0]
        else:
            return 0


    def get_food_params(self,audio_file): # to test use text instead of audio file
        text = self.trans.audio_to_text(audio_file)
        food = self.get_food_items(text)
        # print(food)
        activity = self.get_activity(text)
        # print(activity)
        step_num = self.get_step_number(text)
        # print(step_num)

        food_params = {"item_name":food,"primary_activity":activity,"step": step_num,'text':text}
        return food_params

if __name__ == "__main__":
    audio_file = 'wav1.wav' # use WAV format only
    # text = "how to prepare boba tea 2 ?"
    # text = " second step to make boba tea"
    # text = "packing steps for boba tea"
    # text = "how to cook boba tea ?"
    s = time.time()
    food_recog = Food_Recog()
    # result  = food_recog.get_food_params(audio_file) # to test use text instead of audio file
    result  = food_recog.get_food_params(audio_file)
    e = time.time()
    print(result)
    print(f'total time taken to process {e-s} secods')




    