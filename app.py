from flask import Flask, render_template, request, redirect, url_for, session, flash
from function.datapreprocessing import DataPreprocessing
from function.User_file import User
from function.Phone_file import Phone
from function.UserDao_file import UserDao
from function.PhoneDao_file import PhoneDao
from keras.models import load_model
import numpy as np

app = Flask(__name__)
app.secret_key = 'sentiment'

dp = DataPreprocessing("./data/data_processed/trainprocessed.csv", "./data/data_processed/generate.csv")

# Function to generate text
def generate_text(comment):
    model_generate = load_model("./model/model_lstm_generate_text.h5")
    temp = ""
    for _ in range(3):
        comment_processed = dp.fit_transform_generate(comment)
        predicted_probs = model_generate.predict(comment_processed)
        word = dp.generate.index_word[np.argmax(predicted_probs)]
        comment += " " + word
        temp += " " + word
    return temp

# Function to predict sentiment
def predict_sentiment(comment):
    model_sentiment = load_model("./model/model_sentiment_lstm.h5")
    result = model_sentiment.predict(comment)
    label_index = np.argmax(result, axis=1)
    predicted_label = dp.labelEn.inverse_transform(label_index)
    return predicted_label[0]  # Assuming single comment prediction

@app.route('/sentiment_analysis', methods=['GET', 'POST'])
def sentiment_analysis():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    userDao = UserDao()
    user = User(userid=session['user_id'], username=session['username'])
    if user.getUserId == 1:
        if request.method == 'POST' and 'predict' in request.form:
            comment_of_user = userDao.get_comment_by_user()
            results = []
            for comment in comment_of_user:
                if comment[0] is not None:
                    processed_comment = dp.fit_transform(comment[0])
                    full_name = userDao.get_full_name(User(comment=comment[0]))
                    prediction = predict_sentiment(processed_comment)
                    prediction = dp.Standardization(prediction)
                    user_result = User(username=full_name, comment=comment[0], predict=prediction)
                    results.append(user_result)
            return render_template('sentiment_analysis.html', user_id=user.getUserId, results=results)
    else:
        if request.method == 'POST':
            comment_input = request.form.get('comment_input')
            user = User(userid=session['user_id'], username=session['username'], comment=comment_input)
            userDao.insert_comment(user)
            flash('Comment posted successfully!', 'success')
            return render_template('sentiment_analysis.html', user_id=user.getUserId, username=user.getUserName)
    return render_template('sentiment_analysis.html', user_id=user.getUserId, username=user.getUserName)

@app.route('/phone', methods=['GET', 'POST'])
def phone():
    phoneDao = PhoneDao()
    phone_of_db = phoneDao.get_phone()

    results = []
    for phone in phone_of_db[:30]:  # Chỉ lấy 30 điện thoại đầu tiên
        if phone[0] is not None:
            phone_result = Phone(id=phone[0], phone_name=phone[1], specifications=phone[2], photo=phone[3])
            results.append(phone_result)

    return render_template('phone.html', results=results)

@app.route('/phone/<int:phone_id>')
def phone_detail(phone_id):
    phoneDao = PhoneDao()
    phone_of_db = phoneDao.get_phone_by_id(phone_id)
    if phone_of_db:
        phone = Phone(id=phone_of_db[0], phone_name=phone_of_db[1], specifications=phone_of_db[2], photo=phone_of_db[3])
        return render_template('sentiment_analysis.html', phone=phone)
    else:
        return "Phone not found", 404



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username, password)
        userDao = UserDao()

        if userDao.check_login(user):
            user_id = userDao.get_user_id(user)
            session['username'] = username
            session['user_id'] = user_id
            return redirect(url_for('phone'))
        else:
            flash('Invalid username or password.', 'error')

    return render_template('login.html')

@app.route('/generate_text', methods=['POST'])
def generate_text_route():
    comment = request.form.get('comment')
    if comment:
        generated_text = generate_text(comment)
        return {'generated_text': generated_text}
    return {'error': 'No comment provided'}, 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
