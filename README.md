### About
This project is for Digital Signal Processing 2020 project with GUI. Relies heavily on the [python_speech_features](https://github.com/jameslyons/python_speech_features) library. Use softmax function to output the probability. Convert to mono if the origin audio if stereo. Forked from [crouchred/speaker-recognition-py3](https://github.com/crouchred/speaker-recognition-py3/crouchred/speaker-recognition-py3)

For more details of this project, please see:
+ Our [presentation slides](https://drive.google.com/file/d/1XVP6a3eVT2zNxvHJGtSgyCAqQ2VecQk_/view?usp=sharing)
+ Our [complete report](https://drive.google.com/file/d/1_uKR-8sr9Yy1jCgaGxb2wQUTpabLGMiy/view?usp=sharing)

### Install requirements
```sh
Windows:
pip install -r requirements.txt

Ubuntu:
pip3 install -r requirements.txt
```

## Algorithms Used
_Feature_: [Mel-Frequency Cepstral Coefficient](http://en.wikipedia.org/wiki/Mel-frequency_cepstrum) (MFCC)
_Model_: [Gaussian Mixture Model](http://en.wikipedia.org/wiki/Mixture_model#Gaussian_mixture_model) (GMM)

## GUI Demo
Our GUI has basic functionality for recording, and a speaker recognition. In /gui/, start with demo.py
```sh
Windows:
python demo.py

Ubuntu:
python3 demo.py
```

### Command Line Tools
```sh
usage: speaker-recognition.py [-h] -t TASK -i INPUT -m MODEL

Speaker Recognition Command Line Tool

optional arguments:
  -h, --help            show this help message and exit
  -t TASK, --task TASK  Task to do. Either "enroll" or "predict"
  -i INPUT, --input INPUT
                        Input Files(to predict) or Directories(to enroll)
  -m MODEL, --model MODEL
                        Model file to save(in enroll) or use(in predict)

Wav files in each input directory will be labeled as the basename of the directory.
Note that wildcard inputs should be *quoted*, and they will be sent to glob module.

Examples:
    Train:
    ./speaker-recognition.py -t enroll -i "./train/Dung ./train/Hien ./train/Huy ./train/Lan ./train/Long ./train/Minh ./train/Quang ./train/Thao ./train/Vinh" -m model.out

    Predict:
    ./speaker-recognition.py -t predict -i "./test/*.wav" -m model.out
```
