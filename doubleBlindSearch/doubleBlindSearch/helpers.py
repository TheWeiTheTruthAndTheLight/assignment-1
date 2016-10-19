from random import shuffle

from .searchResults import search


defaultFields = {
  'valueA'     : 0,
  'valueB'     : 0,
  'valueC'     : 0,
  'nameA'      : 'Bing',
  'nameB'      : 'Google',
  'nameC'      : 'Yahoo',
  'meanBing'   : 0,
  'meanGoogle' : 0,
  'meanYahoo'  : 0,
  'trialNumber': 0,
}


def searchAndCollect(query, fields, resultsCount):
    results = search(query)
    return {
        'resultsA': results[fields['nameA']][:resultsCount],
        'resultsB': results[fields['nameB']][:resultsCount],
        'resultsC': results[fields['nameC']][:resultsCount],
    }


def shuffleLabels():
    names = ['Bing', 'Google', 'Yahoo']
    shuffle(names)
    labels = ['a', 'b', 'c']

    return dict(zip(labels, names))


def updateMeans(fields, resultsCount, scoreFormulaConstant):
    labelToNames = {
        'a': fields['nameA'],
        'b': fields['nameB'],
        'c': fields['nameC'],
    }
    values = {
        'a': fields['valueA'],
        'b': fields['valueB'],
        'c': fields['valueC'],
    }
    means = {
        'Bing'  : fields['meanBing'],
        'Google': fields['meanGoogle'],
        'Yahoo' : fields['meanYahoo'],
    }

    for label in labelToNames:
        # Validate value, compute trial score
        value = int(values[label])
        if (value < 1) or (value > resultsCount):
            trialScore = 0
        else:
            trialScore = 1 / pow(scoreFormulaConstant, value - 1)

        # Update mean
        initialMean = float(means[labelToNames[label]])
        intialTrialNumber = float(fields['trialNumber'])
        newMean = ((initialMean * intialTrialNumber) + trialScore) / (intialTrialNumber + 1)
        means[labelToNames[label]] = newMean

    return means


def updateMeansLabelsAndFields(fields, resultsCount, scoreFormulaConstant):
    newMeans = updateMeans(fields, resultsCount, scoreFormulaConstant)
    newLabels = shuffleLabels()
    newFields = {
      'valueA'     : 0,
      'valueB'     : 0,
      'valueC'     : 0,
      'nameA'      : newLabels['a'],
      'nameB'      : newLabels['b'],
      'nameC'      : newLabels['c'],
      'meanBing'   : newMeans['Bing'],
      'meanGoogle' : newMeans['Google'],
      'meanYahoo'  : newMeans['Yahoo'],
      'trialNumber': int(fields['trialNumber']) + 1,
    }

    return newFields
