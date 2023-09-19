from plotter import boxPlotGenerator

for i in range(10):
    boxPlotGenerator(30, 'results_iteration_' + str(i+1) +'.csv', 'boxplot' + str(i+1) + '.png')

