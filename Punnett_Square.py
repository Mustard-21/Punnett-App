import marimo

__generated_with = "0.2.1"
app = marimo.App(width="full")


@app.cell
def __(mo):
    mo.md("#Punnett Square App &ndash; <strong> Genotype </strong>").center()
    return


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import altair as alt
    return alt, mo, pd


@app.cell
def __(pd):
    #Use index to reflect rownames of punnett squares
    Aa_Aa = pd.DataFrame(
        {
            'A': [1/4,2/4],
            'a': [2/4,1/4]
        }, 
            index=['A', 'a']
    )

    aa_aa = pd.DataFrame(
        {
            'a': [4/4, 4/4],
            'a': [4/4, 4/4]
        },
        index=['a', 'a']
    )

    AA_AA = pd.DataFrame(
        {
            'A': [4/4,4/4],
            'A': [4/4,4/4]
        }, 
            index = ['A','A']
    )  

    Aa_Bb = pd.DataFrame(
        {
            'AB': [1/16,2/16,2/16,4/16],
            'Ab': [2/16,1/16,4/16,2/16],
            'aB': [2/16,4/16,1/16,2/16],
            'ab': [4/16,2/16,2/16,1/16]
        }, 
            index = ['AB','Ab','aB','ab']
    )

    AA_BB = pd.DataFrame(
        {
            'AB': [8/16,8/16,8/16,8/16],
            'AB': [8/16,8/16,8/16,8/16],
            'AB': [8/16,8/16,8/16,8/16],
            'AB': [8/16,8/16,8/16,8/16]
        },
            index = ['aB','ab','aB','ab']
    ) 

    Ab_Ba = pd.DataFrame(
        {
            'Ab':[4/16,4/16,4/16,4/16],
            'Ab':[4/16,4/16,4/16,4/16],
            'bb':[4/16,4/16,4/16,4/16],
            'bb':[4/16,4/16,4/16,4/16]
        },
            index = ['BA','BA','aA','aA']
    )
    return AA_AA, AA_BB, Aa_Aa, Aa_Bb, Ab_Ba, aa_aa


@app.cell
def __(AA_AA, AA_BB, Aa_Aa, Aa_Bb, Ab_Ba, aa_aa):
    Punnett_Options = {
        'AaxAa':Aa_Aa,
        'AAxAA':AA_AA,
        'aaxaa':aa_aa,
        'AaBbxAaBb':Aa_Bb,
        'AABBxaaBb':AA_BB,
        'AbbbxBaAA':Ab_Ba
    }
    return Punnett_Options,


@app.cell
def __(mo):
    Punnett_Square_Chooser = mo.ui.dropdown(
        options = [
            'AaxAa',
            'AAxAA',
            'aaxaa',
            'AaBbxAaBb',
            'AABBxaaBb',
            'AbbbxBaAA'
        ],value='AaxAa'
    )
    Punnett_Square_Chooser
    return Punnett_Square_Chooser,


@app.cell
def __(Punnett_Options, Punnett_Square_Chooser, mo):
    Punnett_Square = Punnett_Options[Punnett_Square_Chooser.value]
    mo.ui.table(Punnett_Square).center()
    return Punnett_Square,


@app.cell
def __(Most_Probable_Offspring, mo):
    mo.stat(
        value=str(Most_Probable_Offspring),
        label='Most probable outcome(s):',
        caption='Trait',
        bordered=True
    ).style({'border-width':'4px','background-color':'navy','border-color':'maroon'})
    return


@app.cell
def __(alt, pd):
    #Restructure the punnett squares to turn them into either bar plots or pie charts, I'm not sure yet. 

    #AaxAa
    Heterozygous_Aa = pd.DataFrame(
        {
            'Genotype':['Aa','AA','aa'],
            'Probability':[2/4,1/4,1/4]
        }
    ) 
    Aa_Bar = alt.Chart(Heterozygous_Aa).mark_bar().encode(
        x='Genotype',
        y='Probability'
    )

    #AAxAA 
    Homozygous_AA = pd.DataFrame(
        {
            'Genotype':['AA'],
            'Probability':[4/4]
        }
    )
    AA_Bar = alt.Chart(Homozygous_AA).mark_bar().encode(
        x='Genotype',
        y='Probability'
    )

    ##aaxaa
    Homozygous_aa = pd.DataFrame(
        {
            'Genotype':['aa'],
            'Probability':[4/4]
        }
    )
    aa_Bar = alt.Chart(Homozygous_aa).mark_bar().encode(
        x='Genotype',
        y='Probability'
    )

    #AaxBb 
    Heterozygous_Aa_Bb = pd.DataFrame(
        {
            'Genotype': ['AaBb','AABb','AaBB','Aabb','aaBb','AABB','AAbb','aaBB','aabb'],
            'Probability': [4/16,2/16,2/16,2/16,2/16,1/16,1/16,1/16,1/16]
        }  
    )
    Aa_Bb_Bar = alt.Chart(Heterozygous_Aa_Bb).mark_bar().encode(
        x='Genotype',
        y='Probability'
    )
    #AABBxaaBb
    Heterozygous_AA_BB = pd.DataFrame(
        {
            'Genotype': ['AaBB','AaBb'],
            'Probability': [8/16,8/16]
        }
    )
    AA_BB_Bar = alt.Chart(Heterozygous_AA_BB).mark_bar().encode(
        x='Genotype',
        y='Probability'
    )
    #AbbbxBaAA
    Heterozygous_Ab_Ba = pd.DataFrame(
        {
            'Genotype':['AbbA','bBbA','AabA','babA'],
            'Probability':[1/4,1/4,1/4,1/4]
        }
    )
    Ab_Ba_Bar = alt.Chart(Heterozygous_Ab_Ba).mark_bar().encode(
        x='Genotype',
        y='Probability'
    )
    return (
        AA_BB_Bar,
        AA_Bar,
        Aa_Bar,
        Aa_Bb_Bar,
        Ab_Ba_Bar,
        Heterozygous_AA_BB,
        Heterozygous_Aa,
        Heterozygous_Aa_Bb,
        Heterozygous_Ab_Ba,
        Homozygous_AA,
        Homozygous_aa,
        aa_Bar,
    )


@app.cell
def __(AA_BB_Bar, AA_Bar, Aa_Bar, Aa_Bb_Bar, Ab_Ba_Bar, aa_Bar, mo):
    #Return bar charts to corresponding crosses 
    def Allele_Bar_Plot(Zygosity):
        if Zygosity == 'AaxAa':
            return mo.ui.altair_chart(Aa_Bar)
        if Zygosity == 'AAxAA':
            return mo.ui.altair_chart(AA_Bar)
        if Zygosity == 'aaxaa':
            return mo.ui.altair_chart(aa_Bar)
        if Zygosity == 'AaBbxAaBb':
            return mo.ui.altair_chart(Aa_Bb_Bar)
        if Zygosity == 'AABBxaaBb':
            return mo.ui.altair_chart(AA_BB_Bar)
        if Zygosity == 'AbbbxBaAA':
            return mo.ui.altair_chart(Ab_Ba_Bar)
    return Allele_Bar_Plot,


@app.cell
def __(Allele_Bar_Plot, Punnett_Square_Chooser):
    Zygosity = Punnett_Square_Chooser.value
    Allele_Bar_Chart = Allele_Bar_Plot(Zygosity)
    return Allele_Bar_Chart, Zygosity


@app.cell
def __(Allele_Bar_Chart, Punnett_Heat_Map, mo):
    mo.md(
        f"""
        {mo.hstack([Allele_Bar_Chart,Punnett_Heat_Map])}
        """
    ).style({'background-color':'#981b1e'}).center()
    return


@app.cell
def __():
    import duckdb as db
    return db,


@app.cell
def __(db):
    Aa_Max = db.sql("SELECT Genotype,MAX(Probability) FROM Heterozygous_Aa GROUP BY Genotype").df()
    AA_Max = db.sql("SELECT Genotype,MAX(Probability) FROM Homozygous_AA GROUP BY Genotype").df()
    aa_Max = db.sql("SELECT Genotype,MAX(Probability) FROM Homozygous_aa GROUP BY Genotype").df()
    Aa_Bb_Max = db.sql("SELECT Genotype,MAX(Probability) FROM Heterozygous_Aa_Bb GROUP BY Genotype").df()
    AA_BB_Max = db.sql("SELECT Genotype,MAX(Probability) FROM Heterozygous_AA_BB GROUP BY Genotype").df()
    Ab_Ba_Max = db.sql("SELECT Genotype,MAX(Probability) FROM Heterozygous_Ab_Ba GROUP BY Genotype").df()
    return AA_BB_Max, AA_Max, Aa_Bb_Max, Aa_Max, Ab_Ba_Max, aa_Max


@app.cell
def __(AA_BB_Max, AA_Max, Aa_Bb_Max, Aa_Max, Ab_Ba_Max, aa_Max):
    def Likely_Offspring(Zygosity):
        if Zygosity == 'AaxAa':
            return Aa_Max.Genotype[0]
        if Zygosity == 'AAxAA':
            return AA_Max.Genotype[0]
        if Zygosity == 'aaxaa':
            return aa_Max.Genotype[0]
        if Zygosity == 'AaBbxAaBb':
            return Aa_Bb_Max.Genotype[0]
        if Zygosity == 'AABBxaaBb':
            return [AA_BB_Max.Genotype[0],AA_BB_Max.Genotype[1]]
        if Zygosity =='AbbbxBaAA':
            return [Ab_Ba_Max.Genotype[0],Ab_Ba_Max.Genotype[1],Ab_Ba_Max.Genotype[2],Ab_Ba_Max.Genotype[3]]
    return Likely_Offspring,


@app.cell
def __(Likely_Offspring, Zygosity):
    Most_Probable_Offspring = Likely_Offspring(Zygosity)
    return Most_Probable_Offspring,


@app.cell
def __():
    import plotly.express as px
    return px,


@app.cell
def __(Punnett_Square, px):
    Punnett_Heat_Map = px.imshow(Punnett_Square,text_auto=True)
    return Punnett_Heat_Map,


if __name__ == "__main__":
    app.run()
