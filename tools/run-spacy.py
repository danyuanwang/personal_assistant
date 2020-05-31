import spacy

spacy_model = "en_core_web_md"
print("load spacy model:", spacy_model)
nlp = spacy.load(spacy_model)

while(True):
    sample_sentences = [
            'quit', 
            'who is the smartest person in the world?',
            'where is the statue of liberty?',
            'how many have died due to covid-19 in the world',
            'what is memorial day for?',
            'when is easter?'
            ]
    for i in range(0 , len(sample_sentences)):
        print(i," - ", sample_sentences[i])

    text = input('choose an option or type your text[1]:')
    if(text.isnumeric()):
        inx = int(text)
        if(inx < len(sample_sentences) and inx > 0):
            text = sample_sentences[inx]
        else:
            text = '0'

    if(len(text) < 1): 
       text = sample_sentences[1]

    if(text == '0' or text == 'q'):
        break

    doc = nlp(text)
    token_features = ['token.text', 'token.lemma_', 'token.pos_', 'token.tag_', 'token.dep_',
        'token.shape_', 'token.is_alpha', 'token.is_stop']
    token_print_format = "{:>20}" * (len(token_features))
    print(token_print_format.format(*token_features))

    for token in doc:
       print(token_print_format.format(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop))


    chunk_features = ['chunk.text', 'chunk.root.text', 'chunk.root.dep_','chunk.root.head.text']
    chunk_print_format =  "{:>20}" * (len(chunk_features))
    print(chunk_print_format.format(*chunk_features))
    for chunk in doc.noun_chunks:
       print(chunk_print_format.format(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text))

