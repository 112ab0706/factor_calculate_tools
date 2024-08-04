from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
recode = []
language = 'en'
calculationMode = ''

def csvWriter(): # write records to the file (records.csv)
    with open('records.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(recode)

@app.route('/')
def homePage():
    if language == 'en':
        return render_template('enHomePage.html', language = language)
    elif language == 'zh':
        return render_template('zhHomePage.html', language = language)
    
@app.route('/change_language', methods=['POST'])
def button_lanChange(): # press to change another language
    global language
    if request.method == 'POST':
        language = request.form['language']
        #print(language)
        return redirect(url_for('homePage'))
    return redirect(url_for('homePage'))

@app.route('/calculator', methods = ['POST'])
def calculator():
    if request.method == 'POST':
        language = request.form['language']
    return render_template('calculator.html', language = language)

@app.route('/records', methods=['POST', 'GET'])
def viewRecords():
    data = []
    if request.method == 'GET':
        language = request.args.get('language', 'en')   # get language, if there is no get, the default is English
        with open ('records.csv', 'r', newline='') as file: # read the file (records.csv)
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    return render_template('viewRecords.html', data = data, language = language)

@app.route('/button_clean', methods=['POST'])
def csvCleaner():   # press to clear the file (records.csv)
    global language
    if request.method == 'POST':
        with open('records.csv', 'w', newline=''):
            pass    # skip the write process to clear the file (records.csv)
    return render_template('viewRecords.html', language = language)

# calculator 1
@app.route('/button_FVF', methods = ['POST'])
def button_FVF():
    global calculationMode
    if language == 'en':
        calculationMode = 'Future Value of 1 calculation mode'    
        return render_template('calculator.html', language = language, calculationMode = calculationMode)
    elif language == 'zh':
        calculationMode = '1元複利終值計算模式'
        return render_template('calculator.html', language = language, calculationMode = calculationMode)

# calculator 2
@app.route('/button_PVF', methods = ['POST'])
def button_PVF():
    global calculationMode
    if language == 'en':
        calculationMode = 'Present Value of 1 calculation mode'
        return render_template('calculator.html', language = language, calculationMode = calculationMode)
    elif language == 'zh':
        calculationMode = '1元複利現值計算模式'
        return render_template('calculator.html', language = language, calculationMode = calculationMode)

# calculator 3
@app.route('/button_FVF_OA', methods = ['POST'])
def button_FVF_OA():
    global calculationMode
    if language == 'en':
        calculationMode = 'Future Value of an Ordinary Annuity of 1 calculation mode'
        return render_template('calculator.html', language = language, calculationMode = calculationMode)
    elif language == 'zh':
        calculationMode = '普通年金終值因子計算模式'
        return render_template('calculator.html', language = language, calculationMode = calculationMode)
    
# calculator 4
@app.route('/button_PVF_OA', methods = ['POST'])
def button_PVF_OA():
    global calculationMode
    if language == 'en':
        calculationMode = 'Present Value of an Ordinary Annuity of 1 calculation mode'
        return render_template('calculator.html', language = language, calculationMode = calculationMode)
    elif language == 'zh':
        calculationMode = '普通年金現值因子計算模式'
        return render_template('calculator.html', language = language, calculationMode = calculationMode)

# calculator 5
@app.route('/button_FVF_AD', methods = ['POST'])
def button_FVF_AD():
    global calculationMode
    if language == 'en':
        calculationMode = 'Future Value of an Annuity Due of 1 calculation mode'
        return render_template('calculator.html', language = language, calculationMode = calculationMode)
    elif language == 'zh':
        calculationMode = '期初年金終值因子計算模式'
        return render_template('calculator.html', language = language, calculationMode = calculationMode)

# calculator 6
@app.route('/button_PVF_AD', methods = ['POST'])
def button_PVF_AD():
    global calculationMode
    if language == 'en':
        calculationMode = 'Present Value of an Annuity Due of 1 calculation mode'
        return render_template('calculator.html', language = language, calculationMode = calculationMode)
    elif language == 'zh':
        calculationMode = '期初年金現值因子計算模式'
        return render_template('calculator.html', language = language, calculationMode = calculationMode)

@app.route('/button_calculate', methods = ['POST', 'GET'])
def button_calculate(): # press to calculate the result
    global calculationMode
    calculateResult = None
    if request.method == 'POST':
        user_input_n = request.form['user_input_n'] # get user's input (n)
        user_input_i = request.form['user_input_i'] # get user's input (i)
        if calculationMode == 'Future Value of 1 calculation mode' or calculationMode == '1元複利終值計算模式':
            calculateResult = FVF(user_input_n, user_input_i)
            return render_template('calculator.html', calculateResult = calculateResult)
        elif calculationMode == 'Present Value of 1 calculation mode' or calculationMode == '1元複利現值計算模式':
            calculateResult = PVF(user_input_n, user_input_i)
            return render_template('calculator.html', calculateResult = calculateResult)
        elif calculationMode == 'Future Value of an Ordinary Annuity of 1 calculation mode' or calculationMode == '普通年金終值因子計算模式':
            calculateResult = FVF_OA(user_input_n, user_input_i)
            return render_template('calculator.html', calculateResult = calculateResult)
        elif calculationMode == 'Present Value of an Ordinary Annuity of 1 calculation mode' or calculationMode == '普通年金現值因子計算模式':
            calculateResult = PVF_OA(user_input_n, user_input_i)
            return render_template('calculator.html', calculateResult = calculateResult)
        elif calculationMode == 'Future Value of an Annuity Due of 1 calculation mode' or calculationMode == '期初年金終值因子計算模式':
            calculateResult = FVF_AD(user_input_n, user_input_i)
            return render_template('calculator.html', calculateResult = calculateResult)
        elif calculationMode == 'Present Value of an Annuity Due of 1 calculation mode' or calculationMode == '期初年金現值因子計算模式':
            calculateResult = PVF_AD(user_input_n, user_input_i)
            return render_template('calculator.html', calculateResult = calculateResult)
        return render_template('calculator.html', calculateResult = calculateResult)
    return render_template('calculator.html', calculateResult = calculateResult)
    

def FVF(user_input_n, user_input_i):  # Future Value Factor of 1
    n = float(user_input_n)    # Num of period
    i = float(user_input_i) / 100     # Interest rate
    if 0 <= n <= 400 and 0 <= i <= 400:
        result = round((1 + i) ** n, 6)
        recode.append(('FVF', n, i, round(result, 6)))
        csvWriter() # record to file (records.csv)
    else:
        result = 'Error'
    return result
    
def PVF(user_input_n, user_input_i):  # Present Value Factor of 1
    n = float(user_input_n)    # Num of period
    i = float(user_input_i) / 100     # Interest rate
    if 0 <= n <= 400 and 0 <= i <= 400:
        result = round(1 / ((1 + i) ** n), 6)
        recode.append(('PVF', n, i, round(result, 6)))
        csvWriter() # record to file (records.csv)
    else:
        result = 'Error'
    return result

def FVF_OA(user_input_n, user_input_i):   # Future Value of an Ordinary Annuity of 1
    n = float(user_input_n)    # Num of period
    i = float(user_input_i) / 100     # Interest rate
    if 0 <= n <= 400 and 0 <= i <= 400:
        result = round((((1 + i) ** n) - 1) / i, 6)
        recode.append(('FVF-OA', n, i, round(result, 6)))
        csvWriter() # record to file (records.csv)
    else:
        result = 'Error'
    return result

def PVF_OA(user_input_n, user_input_i):   # Present Value of an Ordinary Annuity of 1
    n = float(user_input_n)    # Num of period
    i = float(user_input_i) / 100     # Interest rate
    if 0 <= n <= 400 and 0 <= i <= 400:
        result = round((1 - (1 / ((1 + i) ** n))) / i, 6)
        recode.append(('PVF-OA', n, i, round(result, 6)))
        csvWriter() # record to file (records.csv)
    else:
        result = 'Error'
    return result

def FVF_AD(user_input_n, user_input_i):   # Future Value of an Annuity Due of 1
    n = float(user_input_n)    # Num of period
    i = float(user_input_i) / 100     # Interest rate
    if 0 <= n <= 400 and 0 <= i <= 400:
        result = round((1 + i) * ((((1 + i) ** n) - 1) / i), 6)
        recode.append(('FVF-AD', n, i, round(result, 6)))
        csvWriter() # record to file (records.csv)
    else:
        result = 'Error'
    return result

def PVF_AD(user_input_n, user_input_i):   # Present Value of an Annuity Due of 1
    n = float(user_input_n)    # Num of period
    i = float(user_input_i) / 100     # Interest rate
    if 0 <= n <= 400 and 0 <= i <= 400:
        result = round(1 + ((1 - (1 / ((1 + i) ** (n - 1)))) / i), 6)
        recode.append(('PVF-AD', n, i, round(result, 6)))
        csvWriter() # record to file (records.csv)
    else:
        result = 'Error'
    return result

#enHonePage.html
#zhHomePage.html
#calculator.html
#viewRecords.html

if __name__ == '__main__':
    app.run(debug=True)