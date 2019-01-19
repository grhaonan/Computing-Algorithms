class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        result = set()
        morse_code_of_a_word = ''
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        #create a to z alpha_letters
        alpha_letters = list(map(chr, range(97, 123)))
        
        #create alpha letters to morse code mapping
        alpha_morse_dict = dict(zip(alpha_letters, morse_code))

        for word in words:
            for letter in word:
                morse_code_of_a_word += alpha_morse_dict[letter]
            result.add(morse_code_of_a_word)
            morse_code_of_a_word = ''
        return len(result)
        
#利用Set的特性