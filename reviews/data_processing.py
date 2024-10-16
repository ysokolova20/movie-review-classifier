{\rtf1\ansi\ansicpg1251\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0      import pandas as pd\
     import os\
\
     def load_data():\
         pos_reviews = []\
         neg_reviews = []\
\
         # \uc0\u1055 \u1091 \u1090 \u1100  \u1082  \u1087 \u1072 \u1087 \u1082 \u1077  \u1089  \u1087 \u1086 \u1083 \u1086 \u1078 \u1080 \u1090 \u1077 \u1083 \u1100 \u1085 \u1099 \u1084 \u1080  \u1086 \u1090 \u1079 \u1099 \u1074 \u1072 \u1084 \u1080 \
         pos_path = 'aclImdb/train/pos/'\
         neg_path = 'aclImdb/train/neg/'\
\
         for filename in os.listdir(pos_path):\
             with open(os.path.join(pos_path, filename), 'r', encoding='utf-8') as file:\
                 pos_reviews.append(file.read())\
\
         for filename in os.listdir(neg_path):\
             with open(os.path.join(neg_path, filename), 'r', encoding='utf-8') as file:\
                 neg_reviews.append(file.read())\
\
         return pos_reviews, neg_reviews\
          from sklearn.feature_extraction.text import CountVectorizer\
     from sklearn.linear_model import LogisticRegression\
     from sklearn.pipeline import make_pipeline\
\
     def train_model(pos_reviews, neg_reviews):\
         labels = [1] * len(pos_reviews) + [0] * len(neg_reviews)\
         reviews = pos_reviews + neg_reviews\
\
         model = make_pipeline(CountVectorizer(), LogisticRegression())\
         model.fit(reviews, labels)\
\
         return model\
          from joblib import dump\
\
     def save_model(model):\
         dump(model, 'movie_review_model.joblib')\
     }