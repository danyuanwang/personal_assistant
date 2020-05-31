import spacy
from spacy import displacy

spacy_model = "en_core_web_md"
print("\nload spacy model:", spacy_model)
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
    print("\n")
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
        'token.shape_', 'token.is_alpha', 'token.is_stop', 'toekn.children']
    token_print_format = "{:<15}" * (len(token_features))
    print('')
    print(token_print_format.format(*token_features))

    for token in doc:
       print(token_print_format.format(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop, str([child for child in token.children])))


    chunk_features = ['chunk.text', 'chunk.root.text', 'chunk.root.dep_','chunk.root.head.text']
    chunk_print_format =  "{:<25}" * (len(chunk_features))
    print('')
    print(chunk_print_format.format(*chunk_features))
    for chunk in doc.noun_chunks:
       print(chunk_print_format.format(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text))

    ent_features = ['ent.text', 'ent.start_char', 'ent.end_char', 'ent.label_']
    ent_feature_format = "{:<15}" * (len(ent_features))
    print('')
    print(ent_feature_format.format(*ent_features))
    for ent in doc.ents:
       print(ent_feature_format.format(ent.text, ent.start_char, ent.end_char, ent.label_))

#    displacy.serve(doc, style="dep")
