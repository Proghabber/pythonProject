import datetime
class Search():

    def __init__(self, list_):

        for i in list_:
            setattr(self,i[0],i[1])


    def whats_search(self, data,word,parametr):
        last_=[]
        next_=[]
        word_=[]
        key=[]
        for i in self.__dict__:
            if data[0] in i:
                last_.append(self.__dict__[i])
            elif data[1] in i:
                next_.append(self.__dict__[i])
            elif parametr[0] in  i:
                    if self.__dict__[i]!="":
                        word_.append(self.__dict__[i])
                    else:
                        word_.append(None)


            elif word[0] in i:
                if self.__dict__[i]!="Все":
                    key.append(self.__dict__[i])
                else:
                    key.append("*")

        next_=[int(i) for i in next_ if i != ""]
        last_=[int(i) for i in last_ if i != ""]
        next_.reverse()
        last_.reverse()
        try:
            last_1=datetime.date(*last_)
        except:
            last_1=None
        try:
            next_1=datetime.date(*next_)
        except:
            next_1=None

        rez={}
        rez["last"]=last_1
        rez["next"]=next_1
        rez["word"]=word_
        rez["key"]=key
        c=self.select_fun(rez)
        return c

    def select_fun(self,dict_):
        complet=""
        if (dict_["last"] != None and dict_["next"] != None) and dict_["word"][0]!=None:
            complet= "all"
        elif (dict_["last"] != None and dict_["next"] != None) and dict_["word"][0]==None:
            complet= "period"
        elif (dict_["last"] != None and dict_["next"] == None) and dict_["word"][0]!=None:
            complet= "day_word"
        elif (dict_["last"] != None and dict_["next"] == None) and dict_["word"][0]==None:
            complet= "day"
        elif (dict_["last"] == None and dict_["next"] == None) and dict_["word"][0]!=None:
            complet= "word"
        elif (dict_["last"] == None and dict_["next"] == None) and dict_["word"][0]==None:
            complet= "list"
        return [complet,dict_]
