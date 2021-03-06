# 6.00 Problem Set 8
#
# Name:
# Collaborators:
# Time:



import numpy
import random
import pylab
import matplotlib.pyplot as plt
# from ps7 import *

#
# PREVIOUS ONE
#
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
            new.append(i)
        self.viruses = new

        pop_dens = float(len(self.viruses)) / float(self.maxPop)

        new_viruses = list()
        for j in self.viruses:
            try: new_viruses.append(j.reproduce(pop_dens))
            except: None
        self.viruses = self.viruses + new_viruses
        return len(self.viruses)
        # TODO


#
# PREVIOUS END
#

#
# PROBLEM 1
#
class ResistantVirus(SimpleVirus):

    """
    Representation of a virus which can have drug resistance.
    """      

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):

        """

        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        

        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb
        # TODO



    def isResistantTo(self, drug):

        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.    

        drug: The drug (a string)
        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        if drug not in self.resistances.keys(): return False
        return self.resistances[drug]
        # TODO


    def reproduce(self, popDensity, activeDrugs):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        # TODO

        counter = 0 
        for drug in activeDrugs:
            if drug not in self.resistances.keys(): continue
            if not(self.resistances[drug]): continue
            counter += 1

        ran_p = random.random()
        p = self.maxBirthProb * ( 1- popDensity)
         
        if (ran_p > p) or (counter != len(activeDrugs)): raise NoChildException()

        else: 
            new_resistances = dict()
            for k in self.resistances.keys():   
                temp_p = random.random()
                if (self.resistances[k]):
                    if temp_p <= 1 - self.mutProb: temp_res = True
                    else: temp_res = False
                else: 
                    if temp_p <= self.mutProb: temp_res = True
                    else: temp_res = False
                new_resistances[k] = temp_res

            return ResistantVirus(self.maxBirthProb, self.clearProb, new_resistances, self.mutProb)
            

class Patient(SimplePatient):

    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        # TODO
        self.viruses = viruses
        self.maxPop = maxPop
        self.druglist = list()

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        # TODO
        # should not allow one drug being added to the list multiple times
        
        if newDrug not in self.druglist: 
            self.druglist.append(newDrug)


    def getPrescriptions(self):

        """
        Returns the drugs that are being administered to this patient.
        returns: The list of drug names (strings) being administered to this
        patient.
        """

        # TODO
        return self.druglist

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        # TODO
        counter = 0
        for v in self.viruses:
            if sum([self.viruese.isResistantTo(d) for d in drugResist]) == len(drugResist): counter += 1
                   
        return counter

    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:
        
        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly          
        - The current population density is calculated. This population density
          value is used until the next call to update().
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO

        new = list()
        for i in self.viruses:
            if i.doesClear(): continue
            new.append(i)
        self.viruses = new

        pop_dens = float(len(self.viruses)) / float(self.maxPop)

        new_viruses = list()
        for j in self.viruses:
            try: new_viruses.append(j.reproduce(pop_dens, self.druglist))
            except: None
        self.viruses = self.viruses + new_viruses
        return len(self.viruses)
        



#
# PROBLEM 2
#

def simulationWithDrug():

    """

    Runs simulations and plots graphs for problem 4.
    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.
    total virus population vs. time and guttagonol-resistant virus population
    vs. time are plotted
    """
    # TODO
    maxPop = 1000
    viruses_qty = 100 # ResistantVirus

    maxBirthProb = .1
    clearProb = .05
    resistances = {'guttagonol': False}
    mutProb = .005

    ResistantVirus_list = list()
    for n in range(viruses_qty):
        ResistantVirus_list.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    
    time_step = 150
    t_step = range(time_step)
    
    vir_qty = list()
    patient_1 = Patient(ResistantVirus_list, maxPop)
    for t in range(time_step):
        vir_qty.append(patient_1.update())
    
    vir_qty_drug = list()
    patient_1.addPrescription('guttagonol')
    for t in range(time_step):
        vir_qty_drug.append(patient_1.update())

    plt.title('Virus Qty versus Time Step')
    plt.xlabel('Time Step')
    plt.ylabel('Viruses Qty')
    plt.plot(t_step, vir_qty, label = 'viruses qty trend w/o drug')
    plt.plot(t_step, vir_qty_drug, label = 'viruses qyt trend w/ drug')
    plt.legend(loc = 'best')
    plt.show()

        
if __name__ == '__main__': 
    simulationWithDrug()

#
# PROBLEM 3
#        

def simulationDelayedTreatment():

    """
    Runs simulations and make histograms for problem 5.
    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.
    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """

    # TODO

#
# PROBLEM 4
#

def simulationTwoDrugsDelayedTreatment():

    """
    Runs simulations and make histograms for problem 6.
    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
   
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """

    # TODO



#
# PROBLEM 5
#    

def simulationTwoDrugsVirusPopulations():

    """

    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.
    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        

    """
    #TODO



