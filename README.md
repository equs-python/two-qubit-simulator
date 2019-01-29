# `__equs.Python__` workshop 2019 - Code project


**Note: to participate in this project you will need a GitHub account.**

Now that we have covered how to build Python packagaes and how to work on Python projects on GitHub, let's all collaborate together and build a Python package that can simulate one and two qubit quantum circuits.

We build a skeleton for this package and your task is to write the content and tests for it.

The package is structured as followed:

```shell
two_qubit_simulator/
    - __init__.py
    - qubit_register.py
    - quantum_circuit.py
    - quantum_gates/
        - __init__.py
        - quantum_gate.py
        - hadamard.py
        - cnot.py
        - ...
tests/
    - test_qubit_register.py
    - test_quantum_circuit.py
    - test_quantum_gates.py
setup.py
README.md
.pylintrc
```

The project is hosted here:

[https://github.com/equs-python/two-qubit-simulator](https://github.com/equs-python/two-qubit-simulator)

Start by making a local clone of the repository and create your own branch. Depending on what part of the project you decide to work on, give your branch a descripitve name.

The plan is to divide the project into the following parts:

- Write the `qubit_register.py` module + tests
- Write the `quantum_circuit.py` module + tests
- Write the `quantum_gates` module + tests
- Write documentation and usage examples
- Optional: write applications

The `README.md` file contains information of how the individual modules are expected to work. Once you finished writing (and testing!) a piece of your code, make a pull request to the `master` branch. Any PR made to this branch will have to pass the automated tests and linting before it can be merged. We encourage all of you to review each others PRs.


## The `QubitRegister` class

This class defines a quantum register consisting of one or two qubits. It should have the following attributes:

**Attributes**

- **state** The qubit state, represented in whatever form you choose (e.g. density matrices)


## The `QuantumGate` class

This class is an abstract class that defines the structure of a quantum gate. Your task is to derive classes from that which implement a quantum gate in the form of a unitary operator.

**Attributes**

- **unitary_operator** a Numpy array representing the operator
- **symbol** a string representing the gate (e.g. `'CNOT'` for a CNOT gate)


