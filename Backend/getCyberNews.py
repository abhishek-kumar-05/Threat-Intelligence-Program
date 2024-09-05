from flask import Flask, jsonify
from cybernews.cybernews import CyberNews
app=Flask(__name__)

news=CyberNews()
keyword=["cyberAttack","dataBreach","iot","cloud","tech"]
@app.route('/api/cybernews', methods=['GET'])

def get_CyberNews_Data():
    all_news=[]
    try:
        for key in keyword:
            data=news.get_news(key)
            for i in data:
                news_data = {
                    "id": i.get("id"),
                    "headlines": i.get("headlines"),
                    "fullNews": i.get("fullNews"),
                    "newsURL": i.get("newsURL"),
                    "newsImgURL": i.get("newsImgURL"),
                    "newsDate": i.get("newsDate")
                }
                all_news.append(news_data)

    except exception as e:
        return jsonify({'error':str(e)})
    
    return jsonify(all_news)


if __name__ == '__main__':
    app.run(debug=True)


