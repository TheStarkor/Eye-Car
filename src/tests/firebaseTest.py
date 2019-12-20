#-*-coding:utf-8 -*-

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./AccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

te = 'te'

doc_ref = db.collection(u'Home').document(u'Test')
doc_ref.set({
  te: 200
})
