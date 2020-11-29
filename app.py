from flask import Flask, render_template, request
import requests
#exchangerate mail id - sifatap726@ofdow.com
#pwd 123456
#{'result': 'success', 'documentation': 'https://www.exchangerate-api.com/docs', 'terms_of_use': 'https://www.exchangerate-api.com/terms', 'time_last_update_unix': 1606435200, 'time_last_update_utc': 'Fri, 27 Nov 2020 00:00:00 +0000', 'time_next_update_unix': 1606521720, 'time_next_update_utc': 'Sat, 28 Nov 2020 00:02:00 +0000', 'base_code': 'INR', 'conversion_rates': {'INR': 1, 'AED': 0.04968, 'ARS': 1.0932, 'AUD': 0.0184, 'BGN': 0.02225, 'BRL': 0.07214, 'BSD': 0.01353, 'CAD': 0.01761, 'CHF': 0.0123, 'CLP': 10.392, 'CNY': 0.08904, 'COP': 49.7143, 'CZK': 0.2975, 'DKK': 0.08465, 'DOP': 0.7838, 'EGP': 0.2116, 'EUR': 0.01137, 'FJD': 0.02825, 'GBP': 0.01014, 'GTQ': 0.1053, 'HKD': 0.105, 'HRK': 0.08596, 'HUF': 4.1078, 'IDR': 194.5515, 'ILS': 0.04496, 'ISK': 1.8317, 'JPY': 1.4122, 'KRW': 14.9854, 'KZT': 5.7049, 'MVR': 0.2086, 'MXN': 0.2712, 'MYR': 0.05518, 'NOK': 0.1201, 'NZD': 0.01935, 'PAB': 0.01353, 'PEN': 0.04879, 'PHP': 0.6515, 'PKR': 2.1437, 'PLN': 0.05086, 'PYG': 94.9091, 'RON': 0.05541, 'RUB': 1.0255, 'SAR': 0.05079, 'SEK': 0.1155, 'SGD': 0.01814, 'THB': 0.4102, 'TRY': 0.1071, 'TWD': 0.3861, 'UAH': 0.3841, 'USD': 0.01354, 'UYU': 0.5755, 'ZAR': 0.206}}
key = "5766082b2fa38456b69ea8e3"
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')
@app.route("/convall", methods=["GET"])
def convall():
    return render_template('convall.html')
@app.route("/currency-rates",methods = ["GET", "POST"])
def rates():
    cntryCodesData = [
        {"code" :"", "desc" : "- Select Country - -"},
        {"code" :"AED","desc" : "United Arab Emirates Dirham"},
        {"code" :"ARS","desc" : "Argentine Peso"},
        {"code" :"AUD","desc" : "Australian Dollar"},
        {"code" :"BGN","desc" : "Bulgarian Lev"},
        {"code" :"BRL","desc" : "Brazilian real"},
        {"code" :"BSD","desc" : "Bahamian dollar"},
        {"code" :"CAD","desc" : "Canadian dollar"},
        {"code" :"CHF","desc" : "Swiss Franc"},
        {"code" :"CLP","desc" : "Chilean peso"},
        {"code" :"CNY","desc" : "renminbi"},
        {"code" :"COP","desc" : "Colombian peso"},
        {"code" :"CZK","desc" : "Czech koruna"},
        {"code" :"DKK","desc" : "Danish Krone"},
        {"code" :"DOP","desc" : "Dominican peso"},
        {"code" :"EGP","desc" : "Egyptian Pound"},
        {"code" :"EUR","desc" : "Euro"},
        {"code" :"FJD","desc" : "Fijian dollar"},
        {"code" :"GBP","desc" : "British Pound"},
        {"code" :"GTQ","desc" : "Guatemalan quetzal"},
        {"code" :"HKD","desc" : "Hong Kong dollar"},
        {"code" :"HRK","desc" : "Croatian kuna"},
        {"code" :"HUF","desc" : "Hungarian forint"},
        {"code" :"ILS","desc" : "Israeli new shekel"},
        {"code" :"INR","desc" : "Indian Rupee"},
        {"code" :"ISK","desc" : "Iceland Krona"},
        {"code" :"JPY","desc" : "Japanese yen"},
        {"code" :"KZT","desc" : "Kazakhstan tenge"},
        {"code" :"MVR","desc" : "Maldivian Rufiyaa"},
        {"code" :"MXN","desc" : "Mexican peso"},
        {"code" :"MYR","desc" : "Malaysian ringgit"},
        {"code" :"NOK","desc" : "Norwegian Krone"},
        {"code" :"NZD","desc" : "New Zealand dollar"},
        {"code" :"PAB","desc" : "Panama Balboa"},
        {"code" :"PEN","desc" : "Peruvian Sol"},
        {"code" :"PHP","desc" : "Philippine peso"},
        {"code" :"PKR","desc" : "Pakistani rupee"},
        {"code" :"PLN","desc" : "Polish zloty"},
        {"code" :"PYG","desc" : "Paraguay guarani"},
        {"code" :"RON","desc" : "Romanian new leu"},
        {"code" :"RUB","desc" : "Russian ruble"},
        {"code" :"SAR","desc" : "Saudi Riyal"},
        {"code" :"SEK","desc" : "Swedish krona"},
        {"code" :"SGD","desc" : "Singapore Dollar"},
        {"code" :"THB","desc" : "Thai Baht"},
        {"code" :"TRY","desc" : "Turkish currency"},
        {"code" :"TWD","desc" : "New Taiwan dollar "},
        {"code" :"UAH","desc" : "Hryvnia"},
        {"code" :"USD","desc" : "US Dollar"},
        {"code" :"UYU","desc" : "Uruguayan peso"},
        {"code" :"ZAR","desc" : "South African rand"},
    ]
    if request.method == "POST":
        url = 'https://v6.exchangerate-api.com/v6/'+key+'/latest/'+str(request.form['from'])
        # Making our request
        response = requests.get(url)
        data = response.json()
        rate = data['conversion_rates'][str(request.form['to'])]
        dataToSend = {"success" : data['result'], "total_rate" : rate*int(request.form['units']),"each_unit" : rate, "from" : request.form['from'], "to" : request.form['to'], "units" : request.form['units']}
        return render_template('currency-rates.html',dataToSend = dataToSend,cntryCodesData = cntryCodesData)
    else:
        return render_template('currency-rates.html',cntryCodesData = cntryCodesData)

@app.errorhandler(404)
def not_found(e):
    return render_template('noroutefound.html')


if __name__ == "__main__":
    app.run(debug=True)
