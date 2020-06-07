import spacy
from spacy import displacy

spacy_model = "en_core_web_md"
print("\nload spacy model:", spacy_model)
nlp = spacy.load(spacy_model)
visualize_dep = False
while(True):
    option_dic = {
            'q':'quit', 
            'v':'visualize'
            } 
    sample_sentences = [
            'dog cat',
            'king queen',
            'allien sfaafs',
            ]
    print("\n")
    for i in range(0 , len(sample_sentences)):
        print(i," - ", sample_sentences[i])
    print('\n')
    for option in option_dic:
        print(option,' - ', option_dic[option])

    text = input('choose an option or type your text[0]:')
    if(len(text) < 1): 
       text = '0'

    if(text.isnumeric()):
        inx = int(text)
        if(inx >= len(sample_sentences) or inx < 0):
            continue
        else:
            text = sample_sentences[inx]

    if(text == 'q' or text == 'quit'):
        break
    if(text == 'v'):
       visualize = not visualize 
       print('visualize is', visualize, 'not supported yet')
       continue

    doc = nlp(text)
    token_features = ['token.text', 'token.has_vector', 'token.vector_norm', 'token.is_oov']
    token_print_format = "{:<25}" * (len(token_features))
    print('')
    print(token_print_format.format(*token_features))

    for token in doc:
       print(token_print_format.format(token.text, token.has_vector, token.vector_norm, token.is_oov))
    while
    for token1 in doc:
        for token2 in doc:
            if(token2.has_vector and token1.has_vector):
                print(token1.text, token2.text, 'has similarity: ',token1.similarity(token2))



