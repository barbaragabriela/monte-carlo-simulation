
class MonteCarlo(object):
  def __init__(self, model, rep, t_max, t_trans):
    self.model = model
    self.rep = rep
    self.t_max = t_max
    self.t_trans = t_trans


  def run(self):
    '''
    For every repetition do N steps (t_max)
    Each step returns the fraction of infected nodes (p) and with that we get the average
    
    returns the total average of the simulation
    '''
    total_average = 0
    average_infected_nodes_list = []

    for i in range(self.rep):
      simulation_data = []
      for step in range(self.t_max):
        p = self.model.step()
        simulation_data.append(p)

      stationary_data = simulation_data[self.t_trans:]
      average_infected_nodes = sum(stationary_data) / len(stationary_data)

      total_average += average_infected_nodes

      # restart model for next repetition
      self.model.start()

    total_average = total_average / self.rep

    return total_average