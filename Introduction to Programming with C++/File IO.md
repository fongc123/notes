# File Input & Output (IO)
A <span style = "color:lightblue">stream</span> is a sequence of characters. A <span style = "color:lightblue">stream object</span> is used to convert **input and output data** into **a sequence of data**.

The library `iostream` combines the `istream` (*dealing with input*) and `ostream` (*dealing with output*) <span style = "color:lightblue">header files</span>.
- `istream cin`: standard input
- `ostream cout`: standard output
- `ostream cerr`: standard error output

The library `fstream` containts `ifstream` and `ofstream` for input and output from a file.

An <span style = "color:lightblue">input file</span> must exist before any input can be read. An <span style = "color:lightblue">output file</span> will be automatically created and **will erase and overwrite** any pre-existing output file with the same filename.

