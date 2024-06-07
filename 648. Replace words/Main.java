// In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

// Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

// Return the sentence after the replacement.

 

// Example 1:

// Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
// Output: "the cat was rat by the bat"
// Example 2:

// Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
// Output: "a a b c"
 

// Constraints:

// 1 <= dictionary.length <= 1000
// 1 <= dictionary[i].length <= 100
// dictionary[i] consists of only lower-case letters.
// 1 <= sentence.length <= 106
// sentence consists of only lower-case letters and spaces.
// The number of words in sentence is in the range [1, 1000]
// The length of each word in sentence is in the range [1, 1000]
// Every two consecutive words in sentence will be separated by exactly one space.
// sentence does not have leading or trailing spaces.


import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
            List<String> dict= new ArrayList<String>();
            dict.add("cat");
        dict.add("rat"); dict.add("bat");

        String sentence = "the cattel was rattle by the battel";

        System.out.println(replaceWords(dict, sentence));

    }
    public static String replaceWords(List<String> dictionary, String sentence) {

        String[] words = sentence.split(" ");

        for(int i=0;i<words.length;i++){
            words[i] = giveReplacement(dictionary,words[i]);
        }

        String newString = String.join(" ", words);

        return newString;
    }

    public static  String giveReplacement(List<String> dictionary,String word){
        for(int i=0;i < dictionary.size();i++){
            String root = dictionary.get(i);
            if( root.length() <= word.length() && root.equals(word.substring(0,root.length())))
            {
                return root ;
            }
        }
        return word;
    }
}

