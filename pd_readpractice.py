"""
Import Theresa's .csv file into pandas DataFrame, then find the mean, std, and
% relative std. I don't really understand how this sheet is structured
(what is the significance of the repeat sample IDs?), but I will make some
assumptions and further whittle things down. I'll also plot some things, but
haven't decided what yet.
"""

# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# name/location of file
csv_fn = '../EffComp_data/Whorley_C2016major_Grn.csv'

# load  into DataFrame
df_tw = pd.read_csv(csv_fn)

# extract only the columns of interest
df_tw2 = df_tw[['Int (Corr)1', 'Int (Corr)2', 'Int (Corr)3', 'Int (Corr)4',
    'Int (Corr)5']].copy()

# replace missing Int (Corr) values with NaNs, convert to floats
df_tw3 = df_tw2.replace(to_replace=' ',value='NaN')
df_tw4 = df_tw3.astype('float64')

# make new DataFrame and dump in statistics
df_tw_stats = df_tw[['Sample ID', 'Analyte Name']].copy()
df_tw_stats['mean'] = df_tw4.mean(1)
df_tw_stats['std'] = df_tw4.std(1)
df_tw_stats['rstd'] = 100 * df_tw_stats['std'] / df_tw_stats['mean']

"""
it looks like there are 15 unique analytes per sample, though there are
repeat sample names for blanks and standards. The best I can make sense of
Theresa's data/workflow description is that for each sample she would want the
mean, std, and rstd as rows and the 13 analytes as columns. This requires some
reorganization of the DataFrame, which could be fun. Maybe frustrating. We'll
see. I'm going to ignore all the blanks and standards because I don't know how
to deal with the repeat IDs.
"""

# useful for counting repeat entries
# df_tw_stats.groupby(['Sample ID']).size().reset_index(name='count')

# keep only data points of samples, get rid of std/blank
df_tw_less = df_tw_stats[df_tw_stats['Sample ID'].str.contains('Sample', na=False)].copy()
df_tw_least = df_tw_less[~df_tw_less['Sample ID'].str.contains('Blank')].copy()

# reshape, set the analyte name as index. There is probably a better way than
# to make 3 seperate DataFrames, but for now this works
df_tw_means = df_tw_least.pivot(index='Sample ID', columns='Analyte Name', values='mean').copy()
df_tw_stds = df_tw_least.pivot(index='Sample ID', columns='Analyte Name', values='std').copy()
df_tw_rstds = df_tw_least.pivot(index='Sample ID', columns='Analyte Name', values='rstd').copy()

# PLOTTING
# let's plot each sample with its std marked on a scatterplot
fs = 14 # primary fontsize
ms = 5 # primary markersize

# extract column (Analyte) names for plotting each individually

# loop through each column (Analyte)
for col in df_tw_means.columns:
    x = df_tw_means[col] # on the assumptions that samples correlate to depth
    xerr = df_tw_stds[col]
    n=x.size
    y = np.arange(1,n+1) # placeholder for Sample IDs

    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)

    ax.errorbar(x, -1*y, xerr=xerr, lw=1, c='black', marker='o', mfc='red',
        mec='black', ecolor='black', ms=ms, mew=1)

    ax.set_xlabel(col, fontsize=fs)
    ax.set_ylabel('Sample #', fontsize=fs)

    # some fun formatting things
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')
    ax.yaxis.set_ticks_position('left')
    ax.tick_params(labelsize=fs-2)

    fig.savefig('../EffComp_output/' + col + '.png')
    plt.close(fig)
