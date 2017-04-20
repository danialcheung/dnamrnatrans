# DNA-mRNA Protein-Translator/Transcriber
Takes a DNA or mRNA sequence and outputs the proteins. Will only translate up from the first Start Sequence to the first Stop Sequence for now. May work on a another build that separates the different start and stop sequences later.

## Operations: ##

### DNA->mRNA->Proteins ###
This operation takes in a DNA sequence that is in all capital letters and has no spaces. Returns the equivalent mRNA sequence and the proteins. This will also return the proteins up to the last grouping if no ending sequence is found.

#### Example 1 ####
##### Input: #####
`TACGGCAAAGTATATCCAUGA`

##### Output: #####
```
mRNA Sequence is: AUGCCGUUUCAUAUAGGU
WARNING! No ending Sequence found!
Proteins are: Met-Pro-Phe-His-Ile-Gly
```

#### Example 2 ####
##### Input: #####
`ACCAACCTCCATACCATCATCATCACACTATCCTTAAA`
##### Output: #####
```
mRNA Sequence is: UGGUUGGAGGUAUGGUAGUAGUAGUGUGAUAGGAAUUU
Proteins are: Met-Val-Val-Val-Val
```

### mRNA->Proteins ###
Takes an mRNA sequence that is in all capital letters and has no spaces. Only returns the proteins. 

#### Example 1 ####
##### Input: #####
`AUGCCGUUUCAUAUAGGU`

##### Output: #####
```
WARNING! No ending Sequence found!

Proteins are: Met-Pro-Phe-His-Ile-Gly
```

#### Example 2 ####
##### Input: #####
`UGGUUGGAGGUAUGGUAGUAGUAGUGUGAUAGGAAUUU`
##### Output: #####
`Proteins are: Met-Val-Val-Val-Val`