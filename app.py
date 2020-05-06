import os
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

@app.route('/libro/<int:codigo>',methods=["GET","POST"])
def libros(codigo):
	from lxml import etree
	doc=etree.parse('libros.xml')
	codigos=doc.xpath('/biblioteca/libro/codigo/text()')
	codigo=str(codigo)
	if codigo in codigos:
		titulo=doc.xpath('/biblioteca/libro[codigo=%s]/titulo/text()'%codigo)
		autor=doc.xpath('/biblioteca/libro[codigo=%s]/autor/text()'%codigo)
	else:
		abort(404)
	return render_template("libros.html",titulo=titulo[0],autor=autor[0])
port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=True)
