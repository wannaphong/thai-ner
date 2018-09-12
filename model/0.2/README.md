# Thai NER 0.2

ใช้ข้อมูล Train ทั้งหมด 5003 ประโยค โดย CRF + POS TAG ในการ train

แท็กที่รองรับ

- DATA วันเดือนปี
- TIME เวลา/ช่วงเวลา
- EMAIL อีเมล
- LEN ความยาว
- LOCATION สถานที่/ที่ตั้ง
- ORGANIZATION บริษัท/องค์กร
- PERSON ชื่อบุคคล
- PHONE เบอร์มือถือ
- URL ลิงค์
- ZIP รหัสไปรษณีย์
- MONEY เงิน



f1

```
0.8684440396975384
                precision    recall  f1-score   support

        B-DATE      0.931     0.838     0.882       320
        I-DATE      0.939     0.948     0.944       670
       B-EMAIL      1.000     1.000     1.000         3
       I-EMAIL      1.000     1.000     1.000        18
         B-LEN      0.833     0.800     0.816        25
         I-LEN      0.863     0.772     0.815        57
    B-LOCATION      0.882     0.773     0.824       766
    I-LOCATION      0.842     0.759     0.798       806
       B-MONEY      0.978     0.916     0.946        95
       I-MONEY      0.991     0.916     0.952       250
B-ORGANIZATION      0.910     0.764     0.830       833
I-ORGANIZATION      0.808     0.712     0.757      1070
     B-PERCENT      0.792     0.792     0.792        24
     I-PERCENT      0.968     0.769     0.857        39
      B-PERSON      0.956     0.854     0.902       512
      I-PERSON      0.908     0.920     0.914      1834
       B-PHONE      0.929     0.788     0.852        33
       I-PHONE      0.959     1.000     0.979        94
        B-TIME      0.919     0.776     0.841       147
        I-TIME      0.935     0.889     0.911       289
         B-URL      1.000     0.950     0.974        20
         I-URL      1.000     0.994     0.997       317
         B-ZIP      1.000     1.000     1.000         4

   avg / total      0.901     0.840     0.868      8226
```

ไฟล์

- thainer-0.2.model เป็นไฟล์โมเดลที่เรา train ด้วยข้อมูลทั้งหมด
- data-pos.model0 เป็นไฟล์โมเดลที่เรา train 80 % และแบ่ง val 20 % ตามรายละเอียดข้างบน
- data.txt เป็นไฟล์ข้อมูลใช้ train
- data.conll ไฟล์ข้อมูล conll ที่ใช้ train แบบไม่มี postag
- data-pos.conll ไฟล์ข้อมูล conll ที่ใช้ train แบบมี postag
- train2.py เป็นไฟล์สำหรับ train data-pos.model0
- train2_all.py เป็นไฟล์สำหรับ train ข้อมูลทั้งหมด
- datatrain.data เป็นไฟล์ข้อมูลที่ได้จาก data.txt สำหรับนำไป train
- using2.py เป็นไฟล์สำหรับรันทดสอบ NER



พัฒนาโดย นาย วรรณพงษ์  ภัททิยไพบูลย์

นักศึกษาชั้นปีที่ 2 สาขาวิทยาการคอมพิวเตอร์และสารสนเทศ

คณะวิทยาศาสตร์ประยุกต์และวิศวกรรมศาสตร์

มหาวิทยาลัยขอนแก่น วิทยาเขตหนองคาย

<wannaphong@kkumail.com>