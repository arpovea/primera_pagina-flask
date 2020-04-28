from flask import Flask, render_template,abort
app = Flask(__name__)	

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("principal.html")

@app.route('/potencia/<int:base>/<exponente>',methods=["GET","POST"])
def potencia(base,exponente):
	exponente=int(exponente)
	if exponente >= 1:
		resultado=base**exponente
	elif exponente == 0:
		resultado=1
	elif exponente < 0:
		resultado=1/(base**abs(exponente))
	else:
		abort(404)
	return render_template("potencia.html",base=base,exponente=exponente,resultado=resultado)

@app.route('/cuenta/<palabra>/<letra>',methods=["GET","POST"])
def cuenta_letra_palabra(palabra,letra):
	if len(letra) == 1:
		resultado=palabra.count(letra)
	else:
		abort(404)
	return render_template("cuenta_letras.html",palabra=palabra,letra=letra,resultado=resultado)


app.run(debug=True)