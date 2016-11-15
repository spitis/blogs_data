import tempfile
import pandas as pd
import os
import pickle

#define the function to join the chunks of files into a single file
def loadBlogs(fileName=os.path.dirname(__file__) + '/blogs.h5',noOfChunks=3,chunkSize=99*1000*1000):
    dataList = []
    for i in range(noOfChunks):
        chunkNum=i * chunkSize
        chunkName = fileName+'_%s'%i
        f = open(chunkName, 'rb')
        dataList.append(f.read())
        f.close()
    f2 = tempfile.NamedTemporaryFile()
    for data in dataList:
        f2.write(data)
    df = pd.read_hdf(f2.name)
    f2.close()

    return df

def loadVocab():
    with open(os.path.dirname(__file__) + '/blogs_vocab.pickle', 'rb') as file:
        vocab = pickle.load(file)
    reverse_vocab = {v:k for k, v in vocab.items()}

    return vocab, reverse_vocab

"""Random code bytes used to prepare data

# define the function to split the file into smaller chunks
def splitFile(inputFile,chunkSize):
	#read the contents of the file
	f = open(inputFile, 'rb')
	data = f.read()
	f.close()

# get the length of data, ie size of the input file in bytes
	bytes = len(data)

#calculate the number of chunks to be created
	noOfChunks= bytes/chunkSize
	if(bytes%chunkSize):
		noOfChunks+=1

#create a info.txt file for writing metadata
	f = open('info.txt', 'w')
	f.write(inputFile+','+'chunk,'+str(noOfChunks)+','+str(chunkSize))
	f.close()

	chunkNames = []
	for idx,i in enumerate(range(0, bytes+1, chunkSize)):
		fn1 = inputFile + "_%s" % idx
		chunkNames.append(fn1)
		f = open(fn1, 'wb')
		f.write(data[i:i+ chunkSize])
		f.close()

#define the function to join the chunks of files into a single file
def joinFiles(fileName,noOfChunks,chunkSize):
	dataList = []
	for i in range(noOfChunks):
		chunkNum=i * chunkSize
		chunkName = fileName+'_%s'%i
		f = open(chunkName, 'rb')
		dataList.append(f.read())
		f.close()
	f2 = open(fileName, 'wb')
	for data in dataList:
		f2.write(data)
	f2.close()

def unkify(sentence):
    res = []
    for word in sentence.split(' '):
        if word in vocab:
            res.append(word)
        else:
            res.append("<UNK>")
    return ' '.join(res)

with mp.Pool(processes=8) as pool:
    unked_s = pool.map(unkify, list(df['string']))

def string_to_numlist(string):
    return list(map(lambda w: vocab[w], string.split(' ')))

with mp.Pool(processes=8) as pool:
    numbered_s = pool.map(string_to_numlist, list(df['string']))

with mp.Pool(processes=8) as pool:
    lengths = pool.map(len, list(df['as_numbers']))

filenames = glob.glob('blogs/*.xml')
len(filenames)

post_id = 0
dfs = []
for idx, f in enumerate(filenames):
    print(idx, "/19320", end='\r')
    split = f.split('.')
    gender = split[1]
    if int(split[2]) < 20:
        age = 0
    elif int(split[2]) < 30:
        age = 1
    else:
        age = 2

    try:
        tree = ET.iterparse(f)
    except:
        continue

    while(True):
        try:
            _, node = next(tree)
        except:
            break

        if node.tag == 'post':
            post = nlp(node.text.strip().lower())
            for sent in list(post.sents):
                res = []
                for lex in sent:
                    if lex.like_num:
                        res.append('<#>')
                    elif not lex.is_space:
                        res.append(lex.orth_)
                if len(sent) > 9:
                    dfs.append(pd.DataFrame([[post_id, gender, age, ' '.join(res)]]))
            post_id += 1

df = pd.concat(dfs)
df = df.reset_index(drop=True)
df.columns = ['post_id', 'gender', 'age_bracket', 'sentence']
#df.to_hdf('blogs.h5','df')
df.head()
"""
