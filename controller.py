from model import InputForm
from flask import Flask, render_template, request, Response
from compute import comp
import csv, io, os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = comp(form.index_5p.data, form.motif_size.data,
                      form.mirna_list)
    else:
        result = None

    return render_template('view.html', form=form, result=result)

@app.route('/all_mirna')
def all_mirna():
    return render_template('all_mirna.html')

if __name__ == '__main__':
     app.debug = True
     port = int(os.environ.get("PORT", 5000))
     app.run(host='0.0.0.0', port=port)
