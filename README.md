# image_comparison

Image comparison using different approaches
  1) Comparing Image Histogram
  2) Siamese Network Training
  
Histogram Model is a ready to use API
- Configure FILE_PATH variable
- Instantiate ImageProcessor class pass pivot_img(image to compare) and compare_img (image to be compared with)
- Call check_similarity_score on Imageprocessor object to get similarity score

To test Histogram model flower dataset is used https://www.kaggle.com/alxmamaev/flowers-recognition
Training and Testing of Siamese network is done on https://www.kaggle.com/ayanzadeh93/color-classification dataset



