import pickle
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static')
pickle_in = open('m-naivebayes.pickle', 'rb')
mnb = pickle.load(pickle_in)
tfid = open('tfidf.pickle', 'rb')
tfidf_vectorizer = pickle.load(tfid)


@app.route('/')
def page():
    return render_template('index.html')

@app.route('/NewsDetection', methods=['GET'])
def NewsDetection():
    return render_template('NewsDetection.html')

@app.route('/news', methods=['GET'])
def news():
    return render_template('news.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/newscheck', methods=['GET', 'POST'])
def newscheck():
    abc = request.args.get('news')
    input_data = [abc.rstrip()]
    # transforming input
    tfidf_test = tfidf_vectorizer.transform(input_data)
    # predicting the input
    y_pred = mnb.predict(tfidf_test)
    return jsonify(result=y_pred[0])


if __name__ == '__main__':
    app.run(debug=True)