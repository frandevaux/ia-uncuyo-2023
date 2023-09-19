from plotter import boxPlotGenerator

for i in range(1):
    boxPlotGenerator(10, 'results_iteration_' + str(i+1) +'.csv', 'boxplot' + str(i+1) + '.png')

