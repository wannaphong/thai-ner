# Thai NER 1.4

[![สัญญาอนุญาตของครีเอทีฟคอมมอนส์](https://i.creativecommons.org/l/by/3.0/th/88x31.png)]

licensed under [CC-BY 3.0](http://creativecommons.org/licenses/by/3.0/)

Thai Named Entity Recognition for PyThaiNLP 2.2

There are 6,456 sentences. Using CRF + postag. It's used same Thai NER 1.3 Dataset.

**Tag**

- DATA - date
- TIME - time
- EMAIL - email
- LEN - length
- LOCATION - Location
- ORGANIZATION - Company / Organization
- PERSON - Person name
- PHONE - phone number
- URL - url
- ZIP - Zip code
- MONEY - amount
- LAW - legislation


## Performance

The ThaiNER is trained from 80 % of ThaiNER corpus and test on the rest 20 %.

```
                precision    recall  f1-score   support

        B-DATE       0.92      0.86      0.89       375
        I-DATE       0.94      0.94      0.94       747
       B-EMAIL       1.00      1.00      1.00         5
       I-EMAIL       1.00      1.00      1.00        28
         B-LAW       0.71      0.56      0.62        43
         I-LAW       0.74      0.70      0.72       154
         B-LEN       0.96      0.93      0.95        29
         I-LEN       0.98      0.94      0.96        69
    B-LOCATION       0.88      0.77      0.82       864
    I-LOCATION       0.86      0.73      0.79       852
       B-MONEY       0.98      0.85      0.91       105
       I-MONEY       0.96      0.95      0.95       239
B-ORGANIZATION       0.90      0.78      0.84      1166
I-ORGANIZATION       0.84      0.77      0.81      1338
     B-PERCENT       1.00      0.97      0.99        34
     I-PERCENT       1.00      0.96      0.98        51
      B-PERSON       0.96      0.82      0.88       676
      I-PERSON       0.94      0.92      0.93      2424
       B-PHONE       1.00      0.72      0.84        29
       I-PHONE       0.96      0.92      0.94        78
        B-TIME       0.87      0.73      0.79       172
        I-TIME       0.94      0.83      0.88       336
         B-URL       0.89      1.00      0.94        24
         I-URL       0.96      1.00      0.98       371
         B-ZIP       1.00      1.00      1.00         4

     micro avg       0.91      0.84      0.87     10213
     macro avg       0.93      0.87      0.89     10213
  weighted avg       0.91      0.84      0.87     10213
   samples avg       0.17      0.17      0.17     10213
```

**File**

- thai-ner-1-4.crfsuite - ThaiNER full model
- thai-ner-1-4-test.crfsuite - ThaiNER test model
- train.ipynb - Notebook train



By Mr.Wannaphong Phatthiyaphaibun

Bachelor of Science Program in Computer and Information Science, Nong Khai Campus, Khon Kaen University

https://iam.wannaphong.com/

E-mail : wannaphong@kkumail.com
