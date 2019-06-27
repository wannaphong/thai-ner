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
0.8665275752238095
                precision    recall  f1-score   support

        B-DATE      0.921     0.866     0.892       350
        I-DATE      0.955     0.948     0.952       767
       B-EMAIL      1.000     1.000     1.000         3
       I-EMAIL      1.000     1.000     1.000        22
         B-LAW      0.875     0.600     0.712        35
         I-LAW      0.910     0.633     0.747       128
         B-LEN      0.931     0.794     0.857        34
         I-LEN      0.938     0.833     0.882        72
    B-LOCATION      0.869     0.746     0.803       897
    I-LOCATION      0.851     0.703     0.770       883
       B-MONEY      0.952     0.909     0.930       110
       I-MONEY      0.969     0.947     0.958       264
B-ORGANIZATION      0.917     0.784     0.845      1198
I-ORGANIZATION      0.833     0.738     0.782      1289
     B-PERCENT      1.000     0.974     0.987        39
     I-PERCENT      0.969     0.984     0.976        63
      B-PERSON      0.969     0.857     0.910       616
      I-PERSON      0.939     0.904     0.921      2094
       B-PHONE      0.938     0.833     0.882        18
       I-PHONE      1.000     0.963     0.981        54
        B-TIME      0.894     0.747     0.814       170
        I-TIME      0.927     0.838     0.881       334
         B-URL      0.955     0.913     0.933        23
         I-URL      0.975     0.986     0.980       278
         B-ZIP      1.000     0.667     0.800         3

     micro avg      0.913     0.828     0.869      9744
     macro avg      0.939     0.847     0.888      9744
  weighted avg      0.911     0.828     0.867      9744
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
