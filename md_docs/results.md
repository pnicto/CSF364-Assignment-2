# Comparison With RNAcentral

## Results

Our calculated results are shown in the following table along with RNAcentral's actual results. The table has the following columns:

1.  **S.No**: Serial Number
2.  **No. of Nucleotides**: Number of nucleotides in the RNA sequence
3.  **Actual No. of Pairs**: Number of base pairs in the RNA sequence present in RNAcentral
4.  **Our Calculated Result**: Number of base pairs in the RNA sequence as calculated by our algorithm
5.  **Percentage Match**: Percentage of base pairs in the RNA sequence that match with RNAcentral's results

Percentage Match is calculated as the ratio of the number of base pairs in the RNA sequence that match with RNAcentral's results to the total number of base pairs in the RNA sequence.

| S.No | No. of Nucleotides | Actual No. of Pairs | Our Calculated Result | Percentage Match |
| :--: | :----------------: | :-----------------: | :-------------------: | :--------------: |
|  1   |        451         |         61          |          163          |     28.1596      |
|  2   |        270         |         39          |          95           |     13.7037      |
|  3   |        954         |         118         |          330          |     29.0356      |
|  4   |        1903        |         296         |          692          |     21.1771      |
|  5   |        2488        |         443         |          899          |     23.3521      |
|  6   |        2466        |         441         |          881          |     21.2084      |

## Observations

As it is very clear from the above table that the number of base pairs calculated by our algorithm is very off to the actual value. This can be easily explained with the fact that RNA base pairing in living organisms is a very complex process and is not just limited to the Watson-Crick base pairing. There are many other factors that come into play like the tertiary structure of the RNA, stability of the RNA (minimum free energy), mutations, the presence of non-canonical base pairs, etc. which are not considered in our algorithm. This is the reason why the percentage match is very low for all the RNA sequences.

## Samples

1.  https://rnacentral.org/rna/URS00004A7003/9606
2.  https://rnacentral.org/rna/URS000014FF3E/9606
3.  https://rnacentral.org/rna/URS000044DFF6/9606
4.  https://rnacentral.org/rna/URS0001BBA686/9606
5.  https://rnacentral.org/rna/URS000215EBDC/7227
6.  https://rnacentral.org/rna/URS00021443C9/3702
