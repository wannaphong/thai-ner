# Thai NER 1.1

[![สัญญาอนุญาตของครีเอทีฟคอมมอนส์](https://i.creativecommons.org/l/by/3.0/th/88x31.png)]

licensed under [CC-BY 3.0](http://creativecommons.org/licenses/by/3.0/)

There are 6306 sentences. Using CRF + postag.

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
0.867959652466252
                precision    recall  f1-score   support

        B-DATE      0.902     0.828     0.863       377
        I-DATE      0.917     0.944     0.930       832
       B-EMAIL      0.667     0.667     0.667         3
       I-EMAIL      1.000     0.889     0.941        18
         B-LAW      0.708     0.531     0.607        32
         I-LAW      0.823     0.718     0.767       110
         B-LEN      1.000     1.000     1.000        15
         I-LEN      1.000     1.000     1.000        30
    B-LOCATION      0.865     0.797     0.830       869
    I-LOCATION      0.865     0.758     0.808       843
       B-MONEY      0.930     0.898     0.914       118
       I-MONEY      0.811     0.938     0.870       306
B-ORGANIZATION      0.922     0.792     0.852      1113
I-ORGANIZATION      0.852     0.761     0.804      1236
     B-PERCENT      0.972     0.921     0.946        38
     I-PERCENT      0.966     0.949     0.957        59
      B-PERSON      0.931     0.825     0.874       604
      I-PERSON      0.908     0.907     0.907      2141
       B-PHONE      0.929     0.619     0.743        21
       I-PHONE      0.945     0.963     0.954        54
        B-TIME      0.831     0.790     0.810       162
        I-TIME      0.899     0.854     0.876       343
         B-URL      1.000     1.000     1.000        21
         I-URL      1.000     1.000     1.000       315
         B-ZIP      1.000     0.833     0.909        12

     micro avg      0.896     0.844     0.869      9672
     macro avg      0.906     0.847     0.873      9672
  weighted avg      0.895     0.844     0.868      9672
```

**File**

- data.model - ThaiNER full model
- data-pos.model0 - ThaiNER test model
- data.txt - train dataset
- train.ipynb - train



By Mr.Wannaphong Phatthiyaphaibun

Bachelor of Science Program in Computer and Information Science, Nong Khai Campus, Khon Kaen University

https://iam.wannaphong.com/

E-mail : wannaphong@kkumail.com
