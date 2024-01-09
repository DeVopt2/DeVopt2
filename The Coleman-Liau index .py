
import math 

//function definition 
def grade_level():
	"""https://en.m.wikipedia.org/wiki/
The Coleman-Liau index was designed to be easily calculated mechanically from samples of hard-copy text. Unlike syllable-based readability indices, it does not require that the character content of words be analyzed, only their length in characters. Therefore, it could be used in conjunction with theoretically simple mechanical scanners that would only need to recognize character, word, and sentence boundaries, removing the need for full optical character recognition or manual keypunching.A score of 6 is 6th grade in the US schooling system. If you are writing for the public, you should aim for a grade level of around 8-10."""

""" Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8,
    L is the average number of letters per 100 words any sequence of characters separated by spaces should count as a word, and that any occurrence of a period, exclamation point, or question mark indicates the end of a sentence."""	
    
    coleman_liau_index = 0
    isalpha = input("To determine
         Grade Level using Coleman-Liau 
        formula input 100 words:     " )
    words = len(isalpha.split())
    if words == 100:
        sentences = isalpha.count('.') + isalpha.count('!') + isalpha.count('?')
        L = (len(isalpha) / words) * 100
        S = (sentences / words) * 100
        coleman_liau_index = 0.0588 * L -
        0.296 * S - 15.8
        grade = coleman_liau_index
    if grade => 16:
        grade = 16+
        print("Grade Level:", grade)
    else:
        print("For an adequate assessment,
        please input 100 words")

def main():
    grade_level()
    return 0


if __name__ == "__main__":
    main()
 





