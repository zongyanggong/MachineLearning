import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# Page title
image = Image.open('dna-logo.jpg')
st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA!
***
""")

# Input text box
st.sidebar.header("Enter DNA sequence")
# st.header("Enter DNA sequence")
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\n" \
                 "ATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\n" \
                 "TGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
# sequence = st.text_area("Sequence input", sequence_input, height=250)
# Splitting text in textarea by new lines (including empty lines) into array
sequence = sequence.splitlines()
# Skips the sequence name (first line: DNA Query 2)
sequence = sequence[1:]
# Concatenates list to string
sequence = ''.join(sequence)

# display split line
# st.write("""
# ***
# """)

# Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

# 1. Print dictionary
st.subheader('1. Print dictionary')

def DNA_nucleotide_count(seq):
    d = dict([
            ('A', seq.count('A')),
            ('T', seq.count('T')),
            ('G', seq.count('G')),
            ('C', seq.count('C'))
            ])
    return d

X = DNA_nucleotide_count(sequence)
# X_label = list(X)
# X_values = list(X.values())
X

# 2. Print text
st.subheader('2. Print text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

# 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
print(df)
df = df.rename({0: 'count'}, axis='columns')
print(df)
df.reset_index(inplace=True)
print(df)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)
# st.dataframe(df)

#4. Display Bar Chart using Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)







