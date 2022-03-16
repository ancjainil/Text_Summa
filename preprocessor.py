{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ee4b9d4a",
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "cannot import name 'WordTokenizer' from 'tokenizer' (/home/jazzyy/anaconda3/lib/python3.9/site-packages/tokenizer/__init__.py)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_41293/1700810879.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mre\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mtokenizer\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mWordTokenizer\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;32mclass\u001b[0m \u001b[0mPreprocessor\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mImportError\u001b[0m: cannot import name 'WordTokenizer' from 'tokenizer' (/home/jazzyy/anaconda3/lib/python3.9/site-packages/tokenizer/__init__.py)"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "\n",
    "class Preprocessor():\n",
    "    def __init__(self):\n",
    "        self.suffixes = []\n",
    "        pass\n",
    "\n",
    "    def compulsory_preprocessing(self, text):\n",
    "        '''This is a function to preprocess the text and make the necessary changes which are compulsory for any type of Gujarati NLP task'''\n",
    "        text = re.sub(r'\\u200b', '', text)\n",
    "        text = re.sub(r'\\ufeff', \"\", text)\n",
    "        text = re.sub(r'…', \" \", text)\n",
    "        text = re.sub(r'  ', ' ', text)\n",
    "        text = re.sub(r'”“', '', text)\n",
    "        text = WordTokenizer(text)\n",
    "        for i in range(len(text)):\n",
    "            text[i] = text[i].rstrip(':')\n",
    "        return ' '.join(text)\n",
    "\n",
    "    def remove_tek(self, text, tek_string):\n",
    "        '''\n",
    "        Tek is the Gujarati word for the initial line of the poem. Whenever, one stanza of any poem is sung, the initial line of the poem is sung once again before starting the\n",
    "        next stanza. This is called as singing a \"Tek\". Written poems mention the tek string too many a times. This will cause a problem of redundancy. Hence, removing it is\n",
    "        necessary.\n",
    "        '''\n",
    "        if str(type(tek_string))==\"<class 'NoneType'>\" or not tek_string:\n",
    "            raise TypeError('tek_string needs to be a valid string')\n",
    "        if str(type(text))==\"<class 'list'>\":\n",
    "            for i in range(len(text)):\n",
    "                text[i] = text[i].rstrip(tek_string)\n",
    "        elif str(type(text))==\"<class 'str'>\":\n",
    "            text = text.rstrip(tek_string)\n",
    "        else:\n",
    "            raise TypeError(\"Argument 'text' must be either a str or list\")\n",
    "        return text\n",
    "\n",
    "    def poetic_preprocessing(self, text, remove_tek=False, tek_string=None):\n",
    "        '''This function is only required when dealing with poetic corpora. Make sure to use this function along with the compulsory preprocessing to have decently accurate results with poetic corpora'''\n",
    "        text = re.sub(r'।','.',text)\n",
    "        text = re.sub(' ।।[૧૨૩૪૫૬૭૮૯૦]।।', '.', text)\n",
    "        if remove_tek:\n",
    "            text = self.remove_tek(text, tek_string)\n",
    "        tokens = WordTokenizer(text, corpus='poetry', keep_punctuations=False)\n",
    "\n",
    "        for i in range(len(tokens)):\n",
    "            # Rule 1\n",
    "            if tokens[i].endswith('જી'):\n",
    "                tokens[i] = tokens[i].strip('જી')\n",
    "            # Rule 2\n",
    "            if tokens[i].endswith('ૈ'):\n",
    "                tokens[i] = tokens[i].strip('ૈ')+'ે'\n",
    "            # Rule 3\n",
    "            index = tokens[i].find('ર')\n",
    "            if index == -1:\n",
    "                pass\n",
    "            elif index<len(tokens[i])-1 and tokens[i][index-1]=='િ':\n",
    "                tokens[i] = re.sub('િર', 'ૃ', tokens[i])\n",
    "\n",
    "        return ' '.join(tokens)"
   ]
  }
  
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
