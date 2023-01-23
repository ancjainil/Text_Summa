## Text_Summarization
This is a research based on Gujarati Text Summarization
Model : Transformer XL (Attention Layer)



## Dataset 

I have used a bifurgated dataset available on Indic nlp website. Besides,  I have also created a dataset using Web Scraping also which can be utilized for Gujarati Text Classification.



## **Goals**

Make a Gujarati news dataset. (I used webscraping here)

Generate some output in Gujarati language itself (regardless of the Accuracy) which gives 20% to 30% of the Input Text. 
If this is accomplished then go for accuracy and focus on fine tuning of the model.



## **INPUTS**

![image](https://user-images.githubusercontent.com/80884488/213648083-eeb2373a-19b4-497c-af45-886ffd055d4f.png)


## **OUTPUT**

![image](https://user-images.githubusercontent.com/80884488/213648522-026a2866-222b-443f-aead-007acf384a70.png)


## **Generated Output**

![image](https://user-images.githubusercontent.com/80884488/213648662-81faa8e1-471b-4afc-ad59-e833f30dd3a1.png)






## **FUNCTIONALITY**

The intention is to create a coherent and fluent summary having only the main points outlined in the document. Automatic text summarization is a common problem in machine learning and natural language processing (NLP).

Summary can be Utilized as News Headline for the news.





## LOGIC

--> Web Scraping for News Datset Generation.

--> Use Html Classes to extract URLs especially anchor tags.

--> Try pre-processing this dataset and divide them into pkls.

--> For summarization process, the flow would be as follows:

![image](https://user-images.githubusercontent.com/80884488/213650914-dad117b1-92ee-471d-a85c-f502fa8638f3.png)


Here I have implemented TF-IDF to predict words around the target words.



