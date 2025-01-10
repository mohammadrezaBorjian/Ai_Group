# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xdn1Biwb9YB-xfJJSBi_HJxULdVIr2z4
"""

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense, Embedding
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers import AdamW
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences

max_len = 100   # طول حداکثر هر نظر (به کلمات)

# بارگذاری داده‌ها
(X_train, y_train), (X_test, y_test) = imdb.load_data()

X_train.shape

# پدینگ برای هم‌طول کردن نظرات
X_train = pad_sequences(X_train, maxlen=max_len)
X_test = pad_sequences(X_test, maxlen=max_len)

X_train.shape

"""batch size, time stamp, input"""

X_train = X_train.reshape(X_train.shape[0],X_train.shape[1],1)
X_test = X_test.reshape(X_test.shape[0],X_test.shape[1],1)

# 2. ساخت مدل RNN
model = Sequential()


# # لایه Embedding: تبدیل کلمات به بردارهای عددی
# model.add(Embedding(input_dim=vocab_size, output_dim=64))


# لایه RNN
model.add(SimpleRNN(128,input_shape=(max_len, 1), activation='relu'))
model.add(Dense(128, activation='sigmoid'))  # خروجی باینری (0 یا 1)
model.add(Dense(128, activation='sigmoid'))  # خروجی باینری (0 یا 1)
model.add(Dense(1, activation='sigmoid'))  # خروجی باینری (0 یا 1)
optimizer = Adam(learning_rate= 0.001)
# 3. کامپایل مدل
model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

# 4. آموزش مدل
model.fit(X_train, y_train, epochs=5, batch_size=512, validation_split=0.2)

# 5. ارزیابی مدل
accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy[1]}")

"""# New Section"""