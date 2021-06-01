import os
import wave

dataset_dir = './dataset/'

# nchannel: 1 (mono)
# with:     2 bytes
# sample:   16000
# nframes:  10*16000

# validate the wave file before process them
for root, sub_dir, items in os.walk(dataset_dir):
	if not sub_dir:
		for it in items:
			f = wave.open(os.path.join(root, it), 'rb')
			params = f.getparams()
			nchannel, width, sample_rate, nframs = params[:4]
			
			assert nchannel == 1 and width == 2 and sample_rate == 16000 and nframs == 10*16000

	print(os.path.split(root)[1], 'passed!')
print('dataset passed')
