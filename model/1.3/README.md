# Thai NER 1.3

[![สัญญาอนุญาตของครีเอทีฟคอมมอนส์](https://i.creativecommons.org/l/by/3.0/th/88x31.png)]

licensed under [CC-BY 3.0](http://creativecommons.org/licenses/by/3.0/)

Thai Named Entity Recognition

There are 6,456 sentences. Using CRF + postag.

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
0.8678830255745219
                precision    recall  f1-score   support

        B-DATE      0.945     0.879     0.911       389
        I-DATE      0.971     0.937     0.954       759
       B-EMAIL      0.000     0.000     0.000         0
       I-EMAIL      0.000     0.000     0.000         0
         B-LAW      0.789     0.600     0.682        50
         I-LAW      0.735     0.704     0.719       142
         B-LEN      0.967     0.725     0.829        40
         I-LEN      0.971     0.720     0.827        93
    B-LOCATION      0.890     0.736     0.805       965
    I-LOCATION      0.872     0.735     0.797      1018
       B-MONEY      0.972     0.875     0.921       120
       I-MONEY      0.971     0.927     0.948       288
B-ORGANIZATION      0.897     0.767     0.827      1133
I-ORGANIZATION      0.816     0.731     0.771      1352
     B-PERCENT      0.892     0.892     0.892        37
     I-PERCENT      0.927     0.911     0.919        56
      B-PERSON      0.955     0.860     0.905       737
      I-PERSON      0.926     0.912     0.919      2696
       B-PHONE      0.941     0.889     0.914        18
       I-PHONE      0.972     1.000     0.986        70
        B-TIME      0.949     0.794     0.865       209
        I-TIME      0.956     0.892     0.923       415
         B-URL      1.000     0.889     0.941        18
         I-URL      1.000     0.984     0.992       255
         B-ZIP      1.000     1.000     1.000         3

     micro avg      0.911     0.832     0.870     10863
     macro avg      0.853     0.774     0.810     10863
  weighted avg      0.909     0.832     0.868     10863
```

**File**

- data.model - ThaiNER full model
- data-pos.model0 - ThaiNER test model
- data.txt - train dataset
- train.ipynb - Notebook train
- train.data - Data for train full model



By Mr.Wannaphong Phatthiyaphaibun

Bachelor of Science Program in Computer and Information Science, Nong Khai Campus, Khon Kaen University

https://iam.wannaphong.com/

E-mail : wannaphong@kkumail.com
