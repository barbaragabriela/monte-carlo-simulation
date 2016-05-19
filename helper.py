import networkx as nx
import matplotlib.pyplot as plt

def convert_nxgraph_to_dict(nxgraph):
  graph = {}

  for node in nxgraph.nodes():
    attributes = {
      'neighbors': nxgraph.neighbors(node),
      'actual_state': 'N'
    }
    graph[node] = attributes

  return graph


def write_results(network_name, n, mu, betas, average):
  '''
  Function that writes the results of the Monte Carlo simulation
  prints the type of network used and the values for beta and the average of infected nodes
  '''
  file = open('results/'+network_name+'_'+str(n)+'_'+str(mu)+'.txt', 'w')

  file.write('{}\n'.format(network_name))
  for i in range(len(betas)):
    file.write('{}\t{}\n'.format(betas[i], average[i]))

  file.close()


def plot_results(name, n, mu, betas, averages):
  plt.scatter(betas, averages)
  plt.title('{}\n Nodes = {}, mu = {}'.format(name, n, round(mu,2)))
  plt.ylabel('p', fontsize=16);
  plt.xlabel('Beta', fontsize=16);
  plt.xlim(xmin = 0, xmax = 1)
  plt.ylim(ymin = 0)
  fig = plt.gcf()
  fig.savefig('plots/'+name+'_dd_'+str(n)+'_'+str(mu)+'.png')

  plt.show()
