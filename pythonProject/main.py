import pypowsybl as pp
import numpy as np
def getVoltageAndPowerAfterAddingDG(location,size):

    n = pp.network.create_ieee14()

    parameters = pp.loadflow.Parameters(distributed_slack=False)
    '''
    n.create_generators(id='DG',
                        bus_id='B'+str(location),
                        voltage_level_id='VL'+str(location),
                        target_p=size,
                        target_q=0,
                        min_p=0,
                        max_p=400,
                        voltage_regulator_on=False)
    '''

    pp.loadflow.run_ac(n, parameters)

    voltages = n.get_voltage_levels()
    buses = n.get_buses()

    voltL = np.array(voltages['nominal_v'])
    busVL = np.array(buses['v_mag'])

    LoadPL = np.array(n.get_loads()['p'])
    LoadQL = np.array(n.get_loads()['q'])

    GeneratorPL = np.array(n.get_generators()['p'])
    GeneratorQL = np.array(n.get_generators()['q'])

    LoadL = [LoadPL,LoadQL]
    GeneratorL = [GeneratorPL, GeneratorQL]

    '''
    
    return value : [ V_PU[]  ,
                      [ PD[], QD[] ]
                      [ PG[], QD[] ]
                      
    '''


    return [(np.divide(busVL,voltL)),LoadL,GeneratorL]



if __name__ == '__main__':
    print(getVoltageAndPowerAfterAddingDG(6,300))

