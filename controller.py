from model import InputForm
from flask import Flask, render_template, request, Response
from compute import unpack_to_set, generate_unique_subsequences
import csv, io, os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = generate_unique_subsequences(form.index_5p_begin.data,
                                              form.motif_size.data,
                                              unpack_to_set(form.mirna_list))
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
