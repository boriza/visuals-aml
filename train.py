from azureml.core import Run
from matplotlib import pyplot as plt

run = Run.get_context()
Foo = [1,2,3,4]
Bar = [4,3,2,1]

plt.title('Foo vs Bar')
plt.plot(Foo, label='Foo')
plt.plot(Bar, '-r', label='Bar')
run.log_image('Plot', plot= plt)
#test