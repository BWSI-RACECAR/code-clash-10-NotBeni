"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #10 - Song Analyzer (songanalyzer.py)


Author: Carter Berlind

Difficulty Level: 5/10

Prompt: Freddy is trying to write a song to impress his friends but needs help 
checking his lines. He decides to enlist you, a python programmer, to create a 
program to see if his lines are good. He tells you that he wants his lines to 
be judged off of whether they rhyme and how much alliteration is there.

Create a program in which the user can input a sentence and the program will 
report back how many words start with the same letters and what those letters 
are and how many words end in the same last three letters (If a word is less 
than three letters we do not consider its rhymes). 

Constraints: Words must be separated by a space. Only report if letters occur at the 
beginning of words multiple times. Don’t worry about commas and punctuation.

Test Cases:
Input: “carter is cool and not a fool”;                     Output: ”c=2,a=2, 2 rhyming words”
Input: “running jumping and swimming are really fun”;       Output: ”r=2, a=2, 3 rhyming words"
Input: “a ban on that book”;                                Output: ”b=2, 0 rhyming words”
Input: “good food for nice mice”;                           Output: ”f=2, 4 rhyming words”
Input: “howdy rowdy hikers hope you have a great time”;     Output: "h=4, 2 rhyming words”
"""

class Solution:
    def song_analyze(self,lyric):
        # type lyric: string
        # return: string 
        
        # TODO: Write code below to return a string with the solution to the prompt

        dict_allit = {}

        dict_end = {}

        return_str = ""
        counter = 0

        lyrics = lyric.split(" ")


        for i in lyrics:

            if i[0] not in dict_allit:
                dict_allit.update({i[0]: 1})
            else:
                dict_allit.update({i[0]: dict_allit.get(i[0])+1})
                
            if len(i) > 3:
                if i[len(i)-3:] not in dict_end:
                    print(i[len(i)-3:])
                    dict_end.update({i[len(i)-3:]: 1})
                else:
                    dict_end.update({i[len(i)-3:]: dict_end.get(i[len(i)-3:])+1})   

        for n in dict_allit:
            if dict_allit.get(n) > 1:
                return_str += n + "=" + str(dict_allit.get(n)) + ", "
        

        for b in dict_end:
            if dict_end.get(b) > 1:
                counter += dict_end.get(b)
        
        return_str += str(counter) + " rhyming words"

        return return_str


def main():
    string1 = input()
    tc1 = Solution()
    ans = tc1.song_analyze(string1)
    print(ans)

if __name__ == "__main__":
    main()