# Thai NER 1.5

[![สัญญาอนุญาตของครีเอทีฟคอมมอนส์](https://i.creativecommons.org/l/by/3.0/th/88x31.png)]

licensed under [CC-BY 3.0](http://creativecommons.org/licenses/by/3.0/)

Thai Named Entity Recognition for PyThaiNLP 2.3

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

| **Tag**           | **newmm-orchid** | **newmm-lst20** | **newmm-lst20  (lst20 dict)** | **attacut-lst20** | **attacut-orchid** |
| ----------------- | ---------------- | --------------- | ----------------------------- | ----------------- | ------------------ |
| B-DATE            | 0.86             | **0.87**        | 0.86                          | 0.85              | 0.86               |
| I-DATE            | 0.92             | **0.95**        | 0.93                          | 0.92              | 0.92               |
| B-LAW             | 0.66             | 0.66            | **0.68**                      | 0.66              | 0.67               |
| I-LAW             | 0.74             | 0.73            | **0.76**                      | 0.74              | 0.73               |
| B-LEN             | 0.86             | 0.86            | **0.91**                      | 0.87              | **0.91**           |
| `I-LEN`           | 0.82             | 0.82            | **0.88**                      | 0.82              | **0.88**           |
| B-LOCATION        | **0.75**         | **0.75**        | **0.75**                      | 0.70              | 0.68               |
| I-LOCATION        | 0.72             | **0.73**        | **0.73**                      | 0.47              | 0.46               |
| B-MONEY           | 0.93             | 0.95            | **0.96**                      | 0.95              | 0.94               |
| `I-MONEY`         | 0.95             | 0.97            | **0.98**                      | 0.97              | 0.96               |
| `B-ORGANIZATION`  | 0.79             | 0.80            | **0.81**                      | 0.77              | 0.75               |
| `I-ORGANIZATION`  | 0.75             | 0.76            | **0.82**                      | 0.61              | 0.55               |
| `B-PERCENT`       | 0.88             | **0.91**        | **0.91**                      | **0.91**          | **0.91**           |
| `I-PERCENT`       | 0.91             | 0.93            | 0.93                          | **0.95**          | **0.95**           |
| `B-PERSON`        | 0.85             | **0.86**        | **0.86**                      | 0.65              | 0.68               |
| `I-PERSON`        | **0.91**         | **0.91**        | 0.88                          | 0.51              | 0.50               |
| `B-PHONE`         | **0.67**         | **0.67**        | **0.67**                      | **0.67**          | **0.67**           |
| `I-PHONE`         | **1.0**          | **1.0**         | **1.0**                       | **1.0**           | **1.0**            |
| `B-TIME`          | **0.77**         | **0.77**        | 0.76                          | 0.76              | 0.75               |
| `I-TIME`          | 0.85             | **0.86**        | 0.82                          | 0.83              | 0.84               |
| `B-URL`           | **0.87**         | **0.87**        | **0.87**                      | 0.32              | 0.67               |
| `I-URL`           | **0.94**         | **0.94**        | **0.94**                      | 0.92              | 0.92               |
|                   |                  |                 |                               |                   |                    |
| `F1 micro avg`    | 0.83             | **0.84**        | **0.84**                      | 0.76              | 0.75               |
| `F1 macro avg `   | 0.84             | 0.84            | **0.85**                      | 0.77              | 0.78               |
| `F1 weighted avg` | 0.83             | **0.84**        | 0.84                          | 0.75              | 0.74               |

**File**

- thai-ner-1-5.crfsuite - ThaiNER full model
- thainer.ipynb - Notebook train
- train.txt - train file
- val.txt - val file
- test.txt - test file

[WIP]



By Mr.Wannaphong Phatthiyaphaibun

Bachelor of Science Program in Computer and Information Science, Nong Khai Campus, Khon Kaen University

https://iam.wannaphong.com/

E-mail : wannaphong@kkumail.com
