import numpy as np




class SIS(object):
  '''
  graph: networks of several kinds (e.g. Erdos-Renyi, scale-free, real), with different sizes
  mu (u): spontaneous recovery probability.
  beta (B): infection probability of a susceptible (S) individual when it is contacted by aninfected (I) one.
  p0: probability of each node being initially infected.
  '''

  def __init__(self, graph, mu, beta, p0):
    self.graph = graph
    self.mu = mu
    self.beta = beta
    self.p0 = p0

    self.number_of_nodes = len(self.graph)

    self.start()


  def start(self):
    '''
    function that starts the nodes with I or S depending on p0
    '''
    self.infected_nodes = []
    self.susceptible_nodes = []

    for node in self.graph:
      if np.random.random() < self.p0: # is infected
        self.graph[node]['actual_state'] = 'I'
        self.infected_nodes.append(node)
      else:
        self.graph[node]['actual_state'] = 'S'
        self.susceptible_nodes.append(node)


  def step(self):
    '''
    1. For each infected node at time step t, we recover it with probability mu: we generate
    a uniform random number between 0.0 and 1.0, and if the value is lower than mu 
    the state of that node in the next time step t+1 will be susceptible, otherwise it will
    remain being infected.
    2. For each susceptible node at time step t, we traverse all of its neighbors. For each
    infected neighbor (at time step t), the reference node becomes infected with
    probability B. For example, if node A has 6 neighbors, 4 of them being infected, we
    repeat 4 times the generation of a random number and its comparison with B. If at
    the third attempt the random number is lower than B, node A will be infected in
    the next time step t+1, and we may stop the generation of the remaining random
    number; otherwise, node A will continue to be susceptible at time step t+1. Of
    course, the larger the number of infected neighbors, the larger the probability of
    becoming infected.

    returns the fraction of infected nodes
    '''
    next_infected_nodes = []
    next_susceptible_nodes = []

    # recovery of a node
    for infected in self.infected_nodes:
      if np.random.random() < self.mu:
        next_susceptible_nodes.append(infected) # recovered!
      else:
        next_infected_nodes.append(infected) # still infected :(

    # infect nodes
    for susceptible in self.susceptible_nodes:
      infected = False
      neighbors = self.graph[susceptible]['neighbors']

      i = 0
      while i < len(neighbors) and not infected:
        neighbor = neighbors[i]
        if self.graph[neighbor]['actual_state'] == 'I':
          infected = np.random.random() < self.beta
        i += 1

      if infected:
        next_infected_nodes.append(susceptible)
      else:
        next_susceptible_nodes.append(susceptible)

    for node in next_infected_nodes:
      self.graph[node]['actual_state'] = 'I'

    for node in next_susceptible_nodes:
      self.graph[node]['actual_state'] = 'S'

    self.infected_nodes = next_infected_nodes
    self.susceptible_nodes = next_susceptible_nodes

    if len(self.infected_nodes) == 0:
      fraction_of_infected_nodes = 0.0
    else:   
      fraction_of_infected_nodes = float(len(self.infected_nodes)) / self.number_of_nodes

    return fraction_of_infected_nodes




