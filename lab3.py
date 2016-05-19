import networkx as nx
import time

import sis
import mc
import helper

class Lab3(object):
  def __init__(self):
    self.nodes = 500
    self.mu_values = [ 0.1, 0.5, 0.9 ]

    self.rep = 50 # 100
    self.p0 = 0.2
    self.t_max = 1000
    self.t_trans = 900
    self.seed = int(self.nodes * self.p0)
    

  def run(self):
    # Run simulation for several type of networks, in this case Erdos-Renyi and Random Network
    self.networks = [
      {
        'network': nx.scale_free_graph(n = self.nodes),
        'name': 'ScaleFree'
      },
      {
        'network': nx.erdos_renyi_graph(n = self.nodes, p = 0.1), # 0.2, 0.5
        'name': 'ErdosRenyi'
      },
      {
        'network': nx.random_regular_graph(n = self.nodes, d = 10),
        'name': 'RandomNetwork'
      }
    ]

    for network in self.networks:
      nxgraph = network['network']
      graph = helper.convert_nxgraph_to_dict(nxgraph)

      # write network in pajek
      filename = 'pajek/'+ network['name'] + '_' + str(self.nodes) + '.net'
      nx.write_pajek(nxgraph, filename)
      
      for mu in self.mu_values:
        print 'Starting...'
        start_time = time.time()

        # B beta (at least 51 values, B=0.02)
        beta = 0.0
        betas = []
        averages = []
        for i in range(0, 51):
          start_time_beta = time.time()
          sis_initial_model = sis.SIS(graph, mu, beta, self.p0)
          simulation = mc.MonteCarlo(sis_initial_model, self.rep, self.t_max, self.t_trans)
          total_average = simulation.run()

          total_time_beta = time.time() - start_time_beta
          betas.append(beta)
          averages.append(total_average)

          print 'B: {}, average: {}, time: {}s'.format(beta, total_average, total_time_beta)
          beta += 0.02

        total_time = time.time() - start_time
        print 'total time: {}'.format(total_time)

        # plot results and save in file
        helper.plot_results(network['name'], self.nodes, mu, betas, averages)
        helper.write_results(network['name'], self.nodes, mu, betas, averages)

      break 


lab3 = Lab3()
lab3.run()