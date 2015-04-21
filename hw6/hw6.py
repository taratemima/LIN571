import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic

code = nltk.data.load('file:thewrittencode.txt', format='raw')
resnik = wordnet_ic.ic('ic-brown-resnik-add1.dat')

#Then you would get a word and a context word



for line in code
    keys, values = code.split(':')

for k in keys
    wordContext = dict([key, values])

n = len(wordContext.keys())
for word in wordContext.keys()
    all_contexts = wordContext[word].split(',')
    p = len(all_contexts)
        for s in wn.synsets(word, pos='n'):
            for context in all_contexts
                (support, normal) = myResnik(word, context, n, p)
                #print the word, context, length of normal, and support
      
#    print s.hypernym_paths()

#This is how to get a list of hypernyms for the word

#How do I simulate the behavior of this?
#>>> dog.res_similarity(cat, brown_ic)
#7.9116665090365768

def myResnik(word, context, ic = resnik, num_sense_word, num_sense_context):

   (first_sub, sub_ic) = myIC(word, context, ic)
#similiarity(word, context)

    source = word.hypernyms()
    target = context.hypernyms()
    sourcePath = source.hypernym_paths()
    targetPath = target.hypernym_paths()

#subsumer(word, context)

    support = sub_ic
    normalization[0] = first_sub

for count = 0 to 
    for k = 1 to num_senses_word:
        t = 0
    

#I am sorry, I cannot remember how to access index of target or source while in sourcePath or targetPath

        if [name in targetPath[k]] == [name[k-1] in sourcePath[k]]:
#if subsumer(word, context) is the ancestor of sense(word, k):
            support = support + sub_ic
#increment support(word, k) by similiarity(word, context)
            normalization[t] = name
            t++

     for m = 1 to num_senses_context:
         v = t
         if [name in sourcePath[m]] == [name2 in target[m -1]]:
#if subsumer(word, context) is the ancestor of sense(context, m)
            support = support + sub_ic
#increment support(context, m) by similiarity(word, context)
            normalization[v] = name
            v++

     return (support, normalization) 

def myIC(word, context, ic):
    subsumer = None
    subsumer_ic = -1
    subsum = word.hypernyms() & context.hypernyms()

    init_similiar = word.GetIC(noun_freqs) + context.GetIC(noun_freqs)

    if init_similiar > subsumer_ic:
         subsumer_ic = init_similiar

    for candidate in subsum:
        ic = candidate.GetIC(noun_freqs)
        if subsumer = None or ic > subsumer_ic:
            subsumer = candidate
            
#I looked at the NLTK source code, but I also added features as I understood them in the text.

    return(subsumer, subsumer_ic)


#for k = 1 to num_senses_word:
#if normalization(word) > 0.0:
#phi(word, k) =  support(word, k) / normalization(word)
#else
#phi(word, k) = 1/num_senses(word)

    






    
