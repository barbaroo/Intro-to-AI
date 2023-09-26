from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the structure
model = BayesianModel([('rain', 'maintenance'), 
                       ('rain', 'train'), 
                       ('maintenance', 'train'),
                       ('train', 'appointment')])

# Rain node has no parents
cpd_rain = TabularCPD(variable='rain', 
                      variable_card=3, 
                      values=[[0.7], [0.2], [0.1]],
                      state_names={'rain': ["none", "light", "heavy"]})

# Track maintenance node is conditional on rain
cpd_maintenance = TabularCPD(variable='maintenance', 
                             variable_card=2, 
                             values=[[0.4, 0.2, 0.1],
                                     [0.6, 0.8, 0.9]],
                             evidence=['rain'],
                             evidence_card=[3],
                             state_names={'maintenance': ["yes", "no"], 'rain': ["none", "light", "heavy"]})

# Train node is conditional on rain and maintenance
cpd_train = TabularCPD(variable='train', 
                       variable_card=2, 
                       values=[[0.8, 0.9, 0.6, 0.7, 0.4, 0.5],
                               [0.2, 0.1, 0.4, 0.3, 0.6, 0.5]],
                       evidence=['rain', 'maintenance'],
                       evidence_card=[3, 2],
                       state_names={'train': ["on time", "delayed"], 'rain': ["none", "light", "heavy"], 'maintenance': ["yes", "no"]})

# Appointment node is conditional on train
cpd_appointment = TabularCPD(variable='appointment', 
                             variable_card=2, 
                             values=[[0.9, 0.6],
                                     [0.1, 0.4]],
                             evidence=['train'],
                             evidence_card=[2],
                             state_names = {'appointment': ["attend", "miss"], 'train': ["on time", "delayed"]})

# Associating the CPDs with the network
model.add_cpds(cpd_rain, cpd_maintenance, cpd_train, cpd_appointment)

# Check model consistency
assert model.check_model()

# Initialize inference object
infer = VariableElimination(model)

# Query the probability of train being on time given heavy rain
result = infer.query(variables=['appointment'], evidence={'rain': 'light', 'maintenance': 'yes'})
print(result)