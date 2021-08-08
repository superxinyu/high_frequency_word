from load_data import table_data_filter
from my_tokenize import tokenize_jieba_ch
from high_frequency import get_high_frequency_word

good_data = table_data_filter("./data.csv", star="1")
bad_data = table_data_filter("./data.csv", star="2")

good_comments = []
for d in good_data:
    good_comments.append(d["comment"])
bad_comments = []
for d in bad_data:
    bad_comments.append(d["comment"])

good_data = tokenize_jieba_ch(good_comments)
bad_data = tokenize_jieba_ch(bad_comments)

print(len(good_data))
print(good_data[:5])
good_words = get_high_frequency_word(good_data, 30)
bad_words = get_high_frequency_word(bad_data, 30)

print("good")
for w in good_words:
    print(w)

print("bad")
for w in bad_words:
    print(w)
