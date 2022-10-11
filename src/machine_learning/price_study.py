import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import ppscore as pps

from src.data_management import load_house_data

def regression_per_variable(df_eda, target_var):
    
    for col in df_eda.drop([target_var], axis=1).columns.to_list():
            plot_numerical(df_eda, col, target_var)


def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    fig = sns.lmplot(data=df, x=col, y=target_var, ci=None) 
    plt.title(f"{col}", fontsize=20,y=1.05)
    st.pyplot(fig) 



def heatmap_corr(df,threshold, figsize=(20,12), font_annot = 8):
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True
        mask[abs(df) < threshold] = True

        fig, axes = plt.subplots(figsize=figsize)
        sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                mask=mask, cmap='viridis', annot_kws={"size": font_annot}, ax=axes,
                linewidth=0.5
                     )
        axes.set_yticklabels(df.columns, rotation = 0)
        plt.ylim(len(df.columns),0)
        st.pyplot(fig) 


def heatmap_pps(df,threshold, figsize=(20,12), font_annot = 8):
    if len(df.columns) > 1:

        mask = np.zeros_like(df, dtype=np.bool)
        mask[abs(df) < threshold] = True

        fig, ax = plt.subplots(figsize=figsize)
        ax = sns.heatmap(df, annot=True, xticklabels=True,yticklabels=True,
                       mask=mask,cmap='rocket_r', annot_kws={"size": font_annot},
                       linewidth=0.05,linecolor='grey')
      
        plt.ylim(len(df.columns),0)
        st.pyplot(fig) 



def CalculateCorrAndPPS(df):
    df_corr_spearman = df.corr(method="spearman")
    df_corr_pearson = df.corr(method="pearson")

    pps_matrix_raw = pps.matrix(df)
    pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(columns='x', index='y', values='ppscore')

    pps_score_stats = pps_matrix_raw.query("ppscore < 1").filter(['ppscore']).describe().T

    return df_corr_pearson, df_corr_spearman, pps_matrix


def DisplayCorrAndPPS(df_corr_pearson, df_corr_spearman, pps_matrix,CorrThreshold,PPS_Threshold,
                      figsize=(20,12), font_annot=8 ):

    st.write("*** Heatmap: Spearman Correlation ***")
    st.write("It evaluates monotonic relationship \n")
    heatmap_corr(df=df_corr_spearman, threshold=CorrThreshold, figsize=figsize, font_annot=font_annot)

    st.write("\n")
    st.write("*** Heatmap: Pearson Correlation ***")
    st.write("It evaluates the linear relationship between two continuous variables \n")
    heatmap_corr(df=df_corr_pearson, threshold=CorrThreshold, figsize=figsize, font_annot=font_annot)

    st.write("\n")
    st.write("*** Heatmap: Power Predictive Score (PPS) ***")
    st.write("PPS detects linear or non-linear relationships between two columns.\n")
    heatmap_pps(df=pps_matrix,threshold=PPS_Threshold, figsize=figsize, font_annot=font_annot)

