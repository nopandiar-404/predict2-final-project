# Introduction PredictNews App
Perancangan aplikasi ini dibuat untuk mendeteksi keaslian isi dari sebuah berita. Dataset yang digunakan untuk model klasifikasi berita ini adalah train.csv. Pada dataset tersebut terdapat berita atau informasi palsu, seperti clickbait (headline berita yang tidak sesuai dengan isi berita), disinformasi (informasi yang menyesatkan publik), misinformasi (informasi palsu dari motif yang sebenarnya), dan bentuk lainnya. Dalam menggunakan aplikasi ini pengguna dapat memilih sebuah artikel berita yang relevan sesuai dengan minat atau berita yang disukainya, pengguna dapat langsung memastikan berita tersebut benar atau tidak (misinformasi) dengan menyalin beberapa kalimat atau sebuah paragraf dari berita tersebut lalu menaruhnya ke dalam form aplikasi deteksi dan menekan tombol prediksi untuk melihat hasilnya.

## Installation / Setup instruction
The application requires the following installations to operate:
- pip
- gunicorn
- flask

## Technologies Used
- python 3.8.5

## Project Setup Instructions
1) Git clone the repository 
```
https://github.com/nopandiar-404/predict2-final-project.git
```
2. cd into pa-predict-news
```
cd pa-predict-news
```
3. create a virtual env
```
conda create -n predict-news python=3.8.5
```
4. activate env
```
activate predict-news
```
5. Open CMD & Install Dependancies
```
pip install -r requirements.txt
```
6. Execute app.py
```
python app.py
```

© 2022 Predict-2
