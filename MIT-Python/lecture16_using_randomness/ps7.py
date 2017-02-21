# Problem Set 7: Simulating the Spread of Disease and Virus Population Dynamics 
# Name:
# Collaborators:
# Time:

import numpy as np
import random
import pylab
import matplotlib.pyplot as plt

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):

        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

        # TODO

    def doesClear(self):

        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.clearProb and otherwise returns
        False.
        """
        ran_p = random.random()
        # print ran_p
        if ran_p <= self.clearProb: return True
        else: return False
        # TODO

    
    def reproduce(self, popDensity):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        p = self.maxBirthProb * (1 - popDensity)
        ran_p = random.random()
        # print ran_p
        if  ran_p<= p: return SimpleVirus(self.maxBirthProb, self.clearProb) 
        else: raise NoChildException()
        # TODO


class SimplePatient(object):

    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):

        """

        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop
        # TODO


    def getTotalPop(self):

        """
        Gets the current total virus population. 
        returns: The total virus population (an integer)
        """
        return len(self.viruses)
        # TODO        


    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        new = list()
        for i in self.viruses:
            if i.doesClear(): continue
            else: new.append(i)
        self.viruses = new

        pop_dens = float(len(self.viruses)) / float(self.maxPop)

        for j in self.viruses:
            try: self.viruese.append(j.reproduce(pop_dens))
            except: None
        return len(self.viruses)
        # TODO




#
# PROBLEM 2
#
def simulationWithoutDrug():

    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """

    virus_q = 100
    maxPop = 1000

    maxBirthProb = .1
    # maxBirthProb = .99
    clearProb = .05
    # clearProb = .99

    update_q = 300

    vir_list = list()
    
    while virus_q > 0:
        vir_list.append(SimpleVirus(maxBirthProb, clearProb))
        virus_q -= 1
    
    patient = SimplePatient(vir_list, maxPop)

    y_pop = list()
    while update_q > 0:
        y_pop.append(patient.update())
        update_q -= 1

    return y_pop
    # TODO

if __name__ == '__main__':
    run_time = 20
    n = run_time

    while n > 0: 
        if n == run_time: 
            simulation_tot = np.matrix(simulationWithoutDrug())

        else: 
            temp = np.matrix(simulationWithoutDrug())
            simulation_tot = np.append(simulation_tot, temp, axis = 0)
        
        n -= 1
    simulation_avg = np.mean(simulation_tot, axis = 0)
    simulation_avg = np.array(simulation_avg)
    
    x = np.array(range(len(simulation_avg[0])))
    y = simulation_avg[0]
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('virus population vs time')
    ax.set_xlabel('elapsed time')
    ax.set_ylabel('population of the virus')
    plt.plot(x, y)
    plt.show()
    
    
