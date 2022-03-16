{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c2486c0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "prose_stopwords= ['લેતા',\n",
    " 'શા',\n",
    " 'ઉભા',\n",
    " 'હો',\n",
    " 'હોઈ',\n",
    " 'મા',\n",
    " 'મૂકી',\n",
    " 'નહી',\n",
    " 'બધું',\n",
    " 'હા',\n",
    " 'મી',\n",
    " 'એન',\n",
    " 'તું',\n",
    " 'નો',\n",
    " 'છો',\n",
    " 'જી',\n",
    " 'લેવા',\n",
    " 'આર',\n",
    " 'છીએ',\n",
    " 'નં',\n",
    " 'એવો',\n",
    " 'હોવા',\n",
    " 'તેથી',\n",
    " 'નું',\n",
    " 'છ',\n",
    " 'એવા',\n",
    " 'એની',\n",
    " 'થતાં',\n",
    " 'જેવી',\n",
    " 'બંને',\n",
    " 'હશે',\n",
    " 'માં',\n",
    " 'ની',\n",
    " 'હતાં',\n",
    " 'તેવી',\n",
    " 'થયો',\n",
    " 'એવી',\n",
    " 'થી',\n",
    " 'થયું',\n",
    " 'ત્યાં',\n",
    " 'બની',\n",
    " 'ગયો',\n",
    " 'છતાં',\n",
    " 'આપી',\n",
    " 'રહે',\n",
    " 'તેઓ',\n",
    " 'પાસે',\n",
    " 'તેમ',\n",
    " 'ને',\n",
    " 'તેને',\n",
    " 'હું',\n",
    " 'બાદ',\n",
    " 'શકે',\n",
    " 'જો',\n",
    " 'અંગે',\n",
    " 'રહી',\n",
    " 'એમ',\n",
    " 'તેના',\n",
    " 'કરે',\n",
    " 'થઇ',\n",
    " 'સુધી',\n",
    " 'જાય',\n",
    " 'રૂા',\n",
    " 'કોઈ',\n",
    " 'ના',\n",
    " 'હવે',\n",
    " 'તેની',\n",
    " 'સામે',\n",
    " 'આવે',\n",
    " 'બે',\n",
    " 'થઈ',\n",
    " 'ન',\n",
    " 'જે',\n",
    " 'આવી',\n",
    " 'તા',\n",
    " 'પર',\n",
    " 'હોય',\n",
    " 'હતું',\n",
    " 'એ',\n",
    " 'કરી',\n",
    " 'તે',\n",
    " 'હતી',\n",
    " 'માટે',\n",
    " 'તો',\n",
    " 'જ',\n",
    " 'પણ',\n",
    " 'કે',\n",
    " 'આ',\n",
    " 'અને',\n",
    " 'છે']\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a721ad4d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['લેતા',\n",
       " 'શા',\n",
       " 'ઉભા',\n",
       " 'હો',\n",
       " 'હોઈ',\n",
       " 'મા',\n",
       " 'મૂકી',\n",
       " 'નહી',\n",
       " 'બધું',\n",
       " 'હા',\n",
       " 'મી',\n",
       " 'એન',\n",
       " 'તું',\n",
       " 'નો',\n",
       " 'છો',\n",
       " 'જી',\n",
       " 'લેવા',\n",
       " 'આર',\n",
       " 'છીએ',\n",
       " 'નં',\n",
       " 'એવો',\n",
       " 'હોવા',\n",
       " 'તેથી',\n",
       " 'નું',\n",
       " 'છ',\n",
       " 'એવા',\n",
       " 'એની',\n",
       " 'થતાં',\n",
       " 'જેવી',\n",
       " 'બંને',\n",
       " 'હશે',\n",
       " 'માં',\n",
       " 'ની',\n",
       " 'હતાં',\n",
       " 'તેવી',\n",
       " 'થયો',\n",
       " 'એવી',\n",
       " 'થી',\n",
       " 'થયું',\n",
       " 'ત્યાં',\n",
       " 'બની',\n",
       " 'ગયો',\n",
       " 'છતાં',\n",
       " 'આપી',\n",
       " 'રહે',\n",
       " 'તેઓ',\n",
       " 'પાસે',\n",
       " 'તેમ',\n",
       " 'ને',\n",
       " 'તેને',\n",
       " 'હું',\n",
       " 'બાદ',\n",
       " 'શકે',\n",
       " 'જો',\n",
       " 'અંગે',\n",
       " 'રહી',\n",
       " 'એમ',\n",
       " 'તેના',\n",
       " 'કરે',\n",
       " 'થઇ',\n",
       " 'સુધી',\n",
       " 'જાય',\n",
       " 'રૂા',\n",
       " 'કોઈ',\n",
       " 'ના',\n",
       " 'હવે',\n",
       " 'તેની',\n",
       " 'સામે',\n",
       " 'આવે',\n",
       " 'બે',\n",
       " 'થઈ',\n",
       " 'ન',\n",
       " 'જે',\n",
       " 'આવી',\n",
       " 'તા',\n",
       " 'પર',\n",
       " 'હોય',\n",
       " 'હતું',\n",
       " 'એ',\n",
       " 'કરી',\n",
       " 'તે',\n",
       " 'હતી',\n",
       " 'માટે',\n",
       " 'તો',\n",
       " 'જ',\n",
       " 'પણ',\n",
       " 'કે',\n",
       " 'આ',\n",
       " 'અને',\n",
       " 'છે']"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prose_stopwords"
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
