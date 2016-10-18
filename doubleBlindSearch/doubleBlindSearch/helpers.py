from random import shuffle


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


def shuffleLabels():
    names = ['Bing', 'Google', 'Yahoo']
    shuffle(names)
    labels = ['a', 'b', 'c']

    return dict(zip(labels, names))


def updateMeans(fields):
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
        initialMean = int(means[labelToNames[label]])
        intialTrialNumber = int(fields['trialNumber'])
        newMean = ((initialMean * intialTrialNumber) + int(values[label])) / (intialTrialNumber + 1)
        means[labelToNames[label]] = newMean

    return means


def updateMeansLabelsAndFields(fields):
    newMeans = updateMeans(fields)
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
    newFields['valueC'] = 1000
    return newFields
