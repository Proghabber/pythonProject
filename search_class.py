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
            elif parametr != None:
                if parametr in i:
                    key.append(self.__dict__[i])
            else:
                if self.__dict__[i] !='':
                    word_.append(self.__dict__[i])
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
        la=""
        ne=""
        for i in  str(last_1):
            if i==":":
                i="-"
            la=la+i
        for i in  str(next_1):
            if i==":":
                i="-"
            ne=ne+i
        rez={}
        rez["last"]=la
        print(type(rez["last"]))
        rez["next"]=ne
        rez["word"]=word_
        rez["key"]=key
        c=self.select_fun(rez)
        return c

    def select_fun(self,dict_):
        complet=""
        if (dict_["last"] != None and dict_["next"] != None) and len(dict_["word"])!=0:
            complet= "all"
        elif (dict_["last"] != None and dict_["next"] != None) and len(dict_["word"])==0:
            complet= "period"
        elif (dict_["last"] != None and dict_["next"] == None) and len(dict_["word"])!=0:
            complet= "day_word"
        elif (dict_["last"] != None and dict_["next"] == None) and len(dict_["word"])==0:
            complet= "day"
        elif (dict_["last"] == None and dict_["next"] == None) and len(dict_["word"])!=0:
            complet= "word"
        elif (dict_["last"] == None and dict_["next"] == None) and len(dict_["word"])==0:
            complet= "list"
        return [complet,dict_]