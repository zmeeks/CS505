import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

def extract_verbs_and_output(fn):
    # Initialize the list to hold sentences
    sents = []

    try:
        # Read the file and load non-blank lines
        with open(fn, 'r') as file:
            sents = [line.strip() for line in file if line.strip()]

        # Open the output file
        with open('sents_and_verbs.txt', 'w') as out_file:
            # Process each sentence for verbs
            for s in sents:
                # Tokenize the sentence
                words = word_tokenize(s)
                # Get the part-of-speech tags
                pos_tags = pos_tag(words)

                # Extract verbs and write to file
                out_file.write(s + '\n')  # Write the original sentence
                verbs = [word for word, tag in pos_tags if tag.startswith('VB')]  # Get verbs
                
                # Write each verb on its own line
                for verb in verbs:
                    out_file.write(verb + '\n')
                
                # Add a blank line after each sentence's verbs
                out_file.write('\n')
        
        return "sents_and_verbs.txt has been created."

    except FileNotFoundError:
        return "The file does not exist."
    except Exception as e:
        return str(e)

# Example Usage:
res = extract_verbs_and_output('Rando_sents.txt')
print(res)
