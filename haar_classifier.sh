## http://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html
## https://github.com/mrnugget/opencv-haar-classifier-training

git clone https://github.com/mrnugget/opencv-haar-classifier-training

brew tap homebrew/science
brew install --with-tbb opencv

cd positive_images
find ./positive_images -iname "*.jpg" > positives.txt
cd negative_images
find ./negative_images -iname "*.jpg" > negatives.txt
cd ..
perl bin/createsamples.pl positives.txt negatives.txt samples 5000\
  "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1\
  -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 80 -h 40"

cd samples
find . -size  0 -print0 |xargs -0 rm
cd ../
rm samples.vec
python ./tools/mergevec.py  -v samples/ -o samples.vec


opencv_traincascade -data classifier -vec samples.vec -bg negatives.txt\
  -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 1000\
  -numNeg 465 -w 80 -h 40 -mode ALL -precalcValBufSize 1024\
  -precalcIdxBufSize 1024 &


cd ~/opencv-2.4.9/samples/c
chmod +x build_all.sh
./build_all.sh
./facedetect --cascade="~/finished_classifier.xml"




