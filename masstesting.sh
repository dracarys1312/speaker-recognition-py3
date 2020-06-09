for (( n=21; n<=31; n++ ))
do
./speaker-recognition.py -t predict -i "./test/$1/$1$n.wav" -m model.out
done
