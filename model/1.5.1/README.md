# Thai NER 1.5.1

[![สัญญาอนุญาตของครีเอทีฟคอมมอนส์](https://i.creativecommons.org/l/by/3.0/th/88x31.png)]

licensed under [CC-BY 3.0](http://creativecommons.org/licenses/by/3.0/)

Thai Named Entity Recognition for PyThaiNLP 2.4

There are 6,456 sentences. Using CRF + postag. It's used same Thai NER 1.5 Dataset.

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

| **Tag**           | F1-score |
| ----------------- | -------- |
| B-DATE            | 0.87     |
| I-DATE            | 0.94     |
| B-LAW             | 0.66     |
| I-LAW             | 0.74     |
| B-LEN             | 0.86     |
| `I-LEN`           | 0.82     |
| B-LOCATION        | 0.75     |
| I-LOCATION        | 0.73     |
| B-MONEY           | 0.95     |
| `I-MONEY`         | 0.97     |
| `B-ORGANIZATION`  | 0.79     |
| `I-ORGANIZATION`  | 0.76     |
| `B-PERCENT`       | 0.91     |
| `I-PERCENT`       | 0.93     |
| `B-PERSON`        | 0.86     |
| `I-PERSON`        | 0.91     |
| `B-PHONE`         | 0.67     |
| `I-PHONE`         | 1.0      |
| `B-TIME`          | 0.77     |
| `I-TIME`          | 0.86     |
| `B-URL`           | 0.87     |
| `I-URL`           | 0.94     |
|                   |          |
| `F1 micro avg`    | 0.84     |
| `F1 macro avg `   | 0.84     |
| `F1 weighted avg` | 0.84     |

**File**

- thainer_crf_1_5_1.model- ThaiNER full model
- thai-ner-1-5-newmm-lst20.ipynb - Notebook train
- train.txt - train file
- val.txt - val file
- test.txt - test file



By Mr.Wannaphong Phatthiyaphaibun

https://iam.wannaphong.com/

E-mail : wannaphong@kkumail.com
