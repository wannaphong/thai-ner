# ThaiNER 0.44 (Bi-LSTM CRF)

using pytorch

By Mr.Wannaphong Phatthiyaphaibun

Bachelor of Science Program in Computer and Information Science, Nong Khai Campus, Khon Kaen University

<https://iam.wannaphong.com/>

E-mail : [wannaphong@kkumail.com](mailto:wannaphong@kkumail.com)



Thank you Faculty of Applied Science and Engineering, Nong Khai Campus, Khon Kaen University for server.



## Performance

The Bi-LSTM CRF is trained from 80 % of ThaiNER 0.44 corpus and test on the rest 20 %.

```
                precision    recall  f1-score   support

        B-DATE     0.9056    0.7892    0.8434       389
         B-LAW     0.8367    0.5125    0.6357        80
         B-LEN     0.8889    0.7273    0.8000        11
    B-LOCATION     0.7608    0.6877    0.7224       666
       B-MONEY     0.9478    0.8074    0.8720       135
B-ORGANIZATION     0.7970    0.7077    0.7497      1365
     B-PERCENT     1.0000    0.7895    0.8824        19
      B-PERSON     0.9086    0.7391    0.8152       713
       B-PHONE     0.6667    0.4000    0.5000         5
        B-TIME     0.7529    0.6737    0.7111        95
         B-URL     0.9167    0.8462    0.8800        13
        I-DATE     0.9144    0.8423    0.8769       761
         I-LAW     0.8561    0.4248    0.5678       266
         I-LEN     0.7273    0.6667    0.6957        24
    I-LOCATION     0.7031    0.5839    0.6380       584
       I-MONEY     0.9423    0.8802    0.9102       334
I-ORGANIZATION     0.7153    0.7258    0.7205      1426
     I-PERCENT     1.0000    0.8400    0.9130        25
      I-PERSON     0.9324    0.8147    0.8696      2574
       I-PHONE     0.4000    0.4286    0.4138        14
        I-TIME     0.7844    0.7706    0.7774       170
         I-URL     0.9407    0.9250    0.9328       120

   avg / total     0.9299    0.9318    0.9296     47901
```



## License

Copyright 2018-2019 Wannaphong Phatthiyaphaibun

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

```
   http://www.apache.org/licenses/LICENSE-2.0
```

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the Licens
