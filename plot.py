# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 15:54:09 2019

@author: Pete
"""


import pandas as pd
import matplotlib.pyplot as plt


def signaturebar(fig,text,fontsize=10,pad=10,xpos=20,ypos=7.5,
                 rect_kw = {"facecolor":"grey", "edgecolor":None},
                 text_kw = {"color":"w"}):
    w,h = fig.get_size_inches()
    height = ((fontsize+2*pad)/72.)/h
    rect = plt.Rectangle((0,0),1,height, transform=fig.transFigure, clip_on=False,**rect_kw)
    fig.axes[0].add_patch(rect)
    fig.text(xpos/72./h, ypos/72./h, text,fontsize=fontsize,**text_kw)
    fig.subplots_adjust(bottom=fig.subplotpars.bottom+height)

petition_df = pd.read_csv('all.csv')

petition_df['color'] = 'gray'

for idx in range(len(petition_df)):
    if petition_df.loc[idx,'party'] == 'Labour':
        petition_df.loc[idx,'color'] = 'red'
    elif petition_df.loc[idx,'party'] == 'Conservative':
        petition_df.loc[idx,'color'] = 'blue'
    elif petition_df.loc[idx,'party'] == 'Green':
        petition_df.loc[idx,'color'] = 'green'
    elif petition_df.loc[idx,'party'] == 'SNP':
        petition_df.loc[idx,'color'] = 'orange'
    elif petition_df.loc[idx,'party'] == 'Lib Dem':
        petition_df.loc[idx,'color'] = 'yellow'
    
""" influential figues """
tm = petition_df[petition_df['mp']  == 'Rt Hon Theresa May MP'].index.values
jrm = petition_df[petition_df['mp']  == 'Mr Jacob Rees-Mogg MP'].index.values
bj = petition_df[petition_df['mp']  == 'Rt Hon Boris Johnson MP'].index.values
mg = petition_df[petition_df['mp']  == 'Rt Hon Michael Gove MP'].index.values
jb = petition_df[petition_df['mp']  == 'Rt Hon John Bercow MP'].index.values
jc = petition_df[petition_df['mp']  == 'Rt Hon Jeremy Corbyn MP'].index.values

petition_df = petition_df.sort_values('PercSigned', ascending=False)
petition_df = petition_df.reset_index(drop='true')

plot_range_top = list(range(1,16)) 
plot_range_bottom =  list(range(len(petition_df)-10,len(petition_df)))
plot_range_spec = [int(tm), int(jrm), int(bj), int(mg), int(jb), int(jc)]


fig = plt.figure(figsize=[22,9])
plt.title('Breakdown of signatures for Revoke Art. 50 online petition - ' + 
          ' Broken down into 3 groups: ' +
              '\n Top & bottom constituencies (Constituency name)' + 
              '\n Constituencies of influential figures (MP Name)')

plt.barh(petition_df['name'][plot_range_top],100*petition_df['PercSigned'][plot_range_top],color=petition_df['color'][plot_range_top])
plt.barh('...',0)
plt.barh(petition_df['name'][plot_range_bottom],100*petition_df['PercSigned'][plot_range_bottom],color=petition_df['color'][plot_range_bottom])
plt.barh('  ',0)

plt.barh(petition_df['mp'][plot_range_spec],100*petition_df['PercSigned'][plot_range_spec],color=petition_df['color'][plot_range_spec])
plt.grid( which='major', axis='x', zorder=0)
plt.yticks(rotation='10')
plt.gca().invert_yaxis()
plt.xlabel('Registered as signing online petition (%)')
signaturebar(fig,"Reddit user - Funky_see_funky_do")

plt.savefig('plot.png')

