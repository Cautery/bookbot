# bookbot
A simple Python CLI application built for Boot.dev

Reads book text from a file (in this case Mary Shelley's *Frankenstein*) and outputs a report. The report shows a total word count and a sorted list of letters in the text.

Functionality was added to send output to `./reports/report.txt`, in addition to standard output. The contents of the file are shown below:

    *** Begin report of ./books/frankenstein.txt ***

    There were 77986 words found in the document.

    Letter  |  Frequency
    -------------------------
       e    |    46043
       t    |    30365
       a    |    26743
       o    |    25225
       i    |    24613
       n    |    24367
       s    |    21155
       r    |    20818
       h    |    19725
       d    |    16863
       l    |    12739
       m    |    10604
       u    |    10407
       c    |    9243
       f    |    8731
       y    |    7914
       w    |    7638
       p    |    6121
       g    |    5974
       b    |    5026
       v    |    3833
       k    |    1755
       x    |    677
       j    |    504
       q    |    324
       z    |    243


