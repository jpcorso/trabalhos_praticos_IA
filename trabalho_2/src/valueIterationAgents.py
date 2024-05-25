# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util
from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount=0.9, iterations=100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """

        
        self.mdp = mdp
        self.discount = discount    #fator de desconto (gamma)
        print(f"discount: {self.discount}")
        self.iterations = iterations #numero de vezes que o alguritmo de interação de valor sera executado
        self.values = util.Counter()  # A Counter is a dict with default 0

        print(f"MDP type: {type(self.mdp)}")
        print(f"Discount type: {type(self.discount)}")
        print(f"Iterations type: {type(self.iterations)}")
        print(f"Values type: {type(self.values)}")

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        for i in range(self.iterations):
            new_values = util.Counter()
            for state in self.mdp.getStates():
                if self.mdp.isTerminal(state):
                    new_values[state] = 0
                else:
                    max_q_value = float('-inf')
                    for action in self.mdp.getPossibleActions(state):
                        q_value = self.computeQValueFromValues(state, action)
                        if q_value > max_q_value:
                            max_q_value = q_value
                    new_values[state] = max_q_value
            self.values = new_values
        
        # Para ver os valores iniciais das variáveis
        print(f"Initial values: {self.values}")

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        # print(f"self.values: {self.values}")
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        
        q_value = 0
        for next_state, prob in self.mdp.getTransitionStatesAndProbs(state, action):
            reward = self.mdp.getReward(state, action, next_state)
            q_value += prob * (reward + self.discount * self.getValue(next_state))
        return q_value

    #retorna melhor ação
    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        if self.mdp.isTerminal(state):
            return None

        actions = []

        #percorre todas ações para ver seus valores
        for action in self.mdp.getPossibleActions(state):
            sum = 0
            #proximos estados e suas probabilidades
            for next_state, prob in self.mdp.getTransitionStatesAndProbs(state,action):
                #aqui aplicamos o somatorio feito no slide para determinar o somatório
                sum += prob*self.discount*self.values[next_state]

            actions.append({"action": action, "value": sum})
        #aqui nós pegamos a ação de valor máximo
        best_action = max(actions, key=lambda x: x["value"])['action']

        return best_action  

        #util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

