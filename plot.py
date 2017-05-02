import plotly
import plotly.graph_objs as go
import numpy as np

import getAverageRating

if __name__ == "__main__":

	byUser = getAverageRating.genAverages("rawData/reviews_Electronics_5Big.json", groups = ["reviewerID"], pruneMin = 5)

	average = []
	sd = []
	voteCount = []

	for i,x in byUser[0].items():
		average.append(x.get("average"))
		sd.append(x.get("sd"))
		voteCount.append(x.get("voteCount"))

	trace1 = go.Scatter3d(
		x=average,
		y=sd,
		z=voteCount,
		mode='markers',
		marker=dict(
			size=12,
			color=average,          # set color to an array/list of desired values
			colorscale='Viridis',   # choose a colorscale
			opacity=0.8
		)
	)

	data = [trace1]
	layout = go.Layout(
		margin=dict(
			l=0,
			r=0,
			b=0,
			t=0
		)
	)

	fig = go.Figure(data=data, layout=layout)

	plotly.plotly.plot(fig, filename='3d-scatter-colorscale')