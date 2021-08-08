
def get_high_frequency_word(data,rank_number):

    word2num = {}
    for sen in data:
        for word in sen:
            if word not in word2num.keys():
                word2num[word]=0
            else:
                word2num[word] +=1
    print(len(word2num.items()))
    return sorted(word2num.items(),key=lambda x:x[1],reverse=True)[:rank_number]
