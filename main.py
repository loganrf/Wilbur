import Wilbur

db = Wilbur.DataBlob('sampleConfig.yaml', 'SampleDataDir')
db.data.to_csv('sanitizedData.csv')
