from django.shortcuts import render
from PyDictionary import PyDictionary
# Create your views here.
def index(request):
	return render(request,'index.html')

def word(request):
	search = request.GET.get('search')
	dictionary = PyDictionary()

	meaning = dictionary.meaning(search)
	synonyms = dictionary.synonym(search)
	antonyms = dictionary.antonym(search)
	# print(meaning.items[0])
	# key,value = meaning.items()[0]
	keys_of_meaning = list(meaning.keys())[0]
	context = {
		'meaning':meaning[keys_of_meaning][0],
		'synonyms':synonyms,
		'antonyms':antonyms
	}
	
	# context['meaning']=meaning[key]

	return render(request,'word.html',context)
