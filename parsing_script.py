import random
import re

def rando_sentences_final(file_name, num_sentences):
    COUNT = 0  # Initialize the count of sentences
    random_sentences = []

    try:
        with open(file_name, 'r') as file:
            text = file.read()
            # Replace abbreviations
            text = text.replace("e.g.", "for example")
            text = text.replace("i.e.", "in other words")
            # Remove blank lines
            text = "\n".join([line for line in text.splitlines() if line.strip() != ''])

            # Split the text into sentences using multiple delimiters while keeping the delimiters
            sentences = re.split('([.!?;])', text)  # Split but keep delimiters
            sentences = [''.join(s) for s in zip(sentences[0::2], sentences[1::2])]  # Rejoin delimiters with sentences

            # Filter sentences based on word count
            filtered_sentences = [s for s in sentences if 5 <= len(s.split()) <= 500]
            COUNT = len(filtered_sentences)  # Update the count with filtered sentences

            if COUNT >= num_sentences:
                random_sentences = random.sample(filtered_sentences, num_sentences)  # Randomly pick sentences
            else:
                raise ValueError(f"File contains only {COUNT} filtered sentences, which is less than the requested {num_sentences} sentences.")
            
            # Save the random sentences to a CSV file
            with open('random_sentences.csv', 'w') as csv_file:
                for sentence in random_sentences:
                    csv_file.write(sentence.strip() + '\n\n')
            
            return f"Generated random_sentences.csv with {num_sentences} sentences from filtered text which originally had {COUNT} sentences."
    except FileNotFoundError:
        return "The file does not exist."
    except Exception as e:
        return str(e)


# Example Usage (Dummy Run):
result = rando_sentences_final('Plato_Test.txt', 250)
print(result)
# This is a dummy run, as the actual file needs to be present in the directory.
