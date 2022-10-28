import datetime
import matplotlib.pyplot as plt
import numpy as np

### Alle
#plot_range = range(2,10)
#legend_range = slice(8)

### Til
plot_range = range(2,6)
legend_range = slice(4)

### Fra
#plot_range = range(6,10)
#legend_range = slice(4,8)

legend = ["Stensparken", "Pilestredet", "Thereses gate", "Bislett Stadion", "Henrik Ibsens gate", "Sørvest for Slottsparken",
        "7. juni-plassen", "Saga Kino"]

data_b = np.loadtxt("data/num_bikes.txt", str)

plt.figure(figsize=(30, 14))

timestamp = np.core.defchararray.add(data_b[:,0], data_b[:,1])
timestamp_obj = [datetime.datetime.strptime(ts, "%Y-%m-%d%H:%M:%S") for ts in timestamp]

#for i in range(2, np.shape(data_b)[1]):
for i in plot_range:
    plt.plot(timestamp_obj, data_b[:,i].astype(int), marker = 'o')
    #plt.bar(data_b[:,-1], data_b[:,-1].astype(int))

#plt.legend(legend)
plt.legend(legend[legend_range])
plt.ylabel("Number of bikes available")
plt.title("Number of bikes")
plt.gcf().autofmt_xdate()

data_d = np.loadtxt("data/num_docks.txt", str)

plt.figure(figsize=(30, 14))

timestamp = np.core.defchararray.add(data_d[:,0], data_d[:,1])
timestamp_obj = [datetime.datetime.strptime(ts, "%Y-%m-%d%H:%M:%S") for ts in timestamp]

#for i in range(2, np.shape(data_d)[1]):
for i in plot_range:
    plt.plot(timestamp_obj, data_d[:,i].astype(int), marker = 'o')
    #plt.bar(data_d[:,-1], data_d[:,-1].astype(int))

#plt.legend(legend)
plt.legend(legend[legend_range])
plt.ylabel("Number of docks available")
plt.title("Number of docks")
plt.gcf().autofmt_xdate()


plt.show()
