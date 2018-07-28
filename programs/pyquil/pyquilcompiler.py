from pyquil.api import CompilerConnection, get_devices
from pyquil.quil import Pragma, Program
from pyquil.gates import CNOT, H, X


def compiletoquil(myprogram):
    devices = get_devices(as_dict=True)
    agave = devices['8Q-Agave']
    compiler = CompilerConnection(agave)

    #myprogram=Program(H(0), CNOT(0,1), CNOT(1,2), X(1), H(1))
    print('\n# Original pyQuil program,\n\n', myprogram)

    job_id = compiler.compile_async(myprogram)
    job = compiler.wait_for_job(job_id)

    print('\n# Compiled quil code,\n\n', job.compiled_quil())
    print('# gate volume', job.gate_volume())
    print('# gate depth', job.gate_depth())
    print('# topological swaps', job.topological_swaps())
    print('# program fidelity', job.program_fidelity())
    print('# multiqubit gate depth', job.multiqubit_gate_depth())
    print('\n# End of compiling info\n')

    return myprogram, job.compiled_quil()


# compiletoquil(Program(X(0)))
