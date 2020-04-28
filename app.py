from flask import Flask, render_template,abort
app = Flask(__name__)	

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html")

@app.route('/potencia/<int:base>/<int:exponente>',methods=["GET","POST"])
def potencia(base,exponente):
	if exponente >= 1:
		resultado=base**exponente
	elif exponente == 0:
		resultado=1
	elif exponente < 0:
		resultado=1/(base**abs(exponente))
	else:
		abort(404)
	return render_template("potencia.html",base=base,exponente=exponente,resultado=resultado)


app.run(debug=True)