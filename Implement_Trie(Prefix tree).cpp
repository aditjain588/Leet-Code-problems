#include <bits/stdc++.h> 
using namespace std;

class TrieNode{
    public:
    char c;
    bool isEnd;
    TrieNode *child[26]={};
    
    TrieNode(char c){
        this->c = c;
        this->isEnd = false;
    }
};

class Trie {
private:
    TrieNode *root;
public:
    /** Initialize data structure. */
    Trie() {
        root = new TrieNode('\0');
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode *curr = root;
        for(int i=0;i<word.size();i++){
            char c = word[i];
            if(curr->child[c-'a']==NULL){
                curr->child[c-'a'] = new TrieNode(c);
            }
            curr=curr->child[c-'a'];
        }
        curr->isEnd = true;
    }
    
    TrieNode *getNode(string word){
        TrieNode *curr = root;
        for(int i=0;i<word.size();i++){
            char c = word[i];
            if(curr->child[c-'a']==NULL){
                return NULL;
            }
            else{
                curr=curr->child[c-'a'];
            }  
        }
        return curr;
    }
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode *node = getNode(word);
        return (node !=NULL && node->isEnd);
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        return (getNode(prefix)!=NULL);
    }
};


/**
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */