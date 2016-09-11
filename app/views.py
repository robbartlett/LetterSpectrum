from flask import render_template
from flask import request, redirect
from flask import jsonify
from app import app
from app import db, models
import logging, sys
import random

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

@app.route('/')
@app.route('/index', methods=['GET','POST'])

def index():
	return render_template('index.html',
		title='Home')

@app.route('/colorize', methods=['GET','POST'])
def colorize():
	t = request.form["t"]
	counted = countCharacters(t)
	colorized = getMetaFromCounts(counted)
	jsonView = convertModelToView(colorized)
	return jsonify(jsonView)

def countCharacters(s=''):
	ss = {}
	for c in s:
		if c in ss.keys():
			ss[c] = ss[c] + 1
		else:
			ss[c] = 1
	return ss

def getMetaFromCounts(characterCounts):
	for c in characterCounts:
		meta = models.CharacterMetadata.query.filter(models.CharacterMetadata.character == c).one_or_none()
		if not meta:
			meta = models.CharacterMetadata(character=c, count=0, colorHex=generateRandomColor())
		meta.count = meta.count + characterCounts[c]
		db.session.add(meta)
	db.session.commit()
#TODO: Probably should just return new ones, and then merge outside of this function
	metas = models.CharacterMetadata.query.all()
	return metas

def generateRandomColor():
# Black background, so let's keep it light
	r = lambda: random.randint(64,255)
	c = (((r() << 8) ^ r()) << 8) ^ r()
	s = format(c, '06X')
	logging.debug("new color: " + s)
	return s

#TODO: Figure out how to do this automatically
def convertModelToView(metas):
	result = []
	for meta in metas:
		itm = { "l":meta.character, "c":meta.colorHex, "n":meta.count}
		result.append(itm)
	return result
