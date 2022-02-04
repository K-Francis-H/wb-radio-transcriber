'''
INSTALLATION

pyaudio
	maybe: pip3 install pyaudio
	wk4me: sudo apt install python3-pyaudio

pocketsphinx, sphinxbase
	you need swig: 	sudo apt install swig
	now it works: 		pi3 install pocketsphinx
'''

from os import environ, path
import pyaudio

#from pocketsphinx.pocketsphinx import *
#from sphinxbase.sphinxbase import *
from pocketsphinx import LiveSpeech, get_model_path

model_path = get_model_path()
print(model_path)

speech = LiveSpeech(
	verbose=False,
	sampling_rate=16000,
	buffer_size=2048,
	no_search=False,
	full_utt=False,
	hmm=path.join(model_path, 'en-us'),
	lm=path.join(model_path, 'en-us.lm.bin'),
	dic=path.join(model_path, 'cmudict-en-us.dict')
)

for phrase in speech:
	print(phrase)

