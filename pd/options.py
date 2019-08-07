# pandas options
# pandas provides the api to change some aspects of its behaviour
# the api is composed of 5 relavent options

# get_option
# set_option
# reset_option
# describe_option
# option_context

# get_option takes a single parameter and returns the value as given in the output below

import pandas as pd

print(pd.get_option('display.max_rows'))

print(pd.get_option("display.max_columns"))

# set_option we can change the default number of rows and column

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns',10)

print(pd.get_option('display.max_rows'))
print(pd.get_option("display.max_columns"))

# reset_option  reset a particular option
pd.reset_option("display.max_rows")
print(pd.get_option("display.max_rows"))


# describe option prints the discription of arguments
pd.describe_option("display.max_rows")

print(pd.options['display.max_rows"'])

# option_context context manager is used to set the option in with statement temporarily. Option values are restored automatically when you exit the with block −

with pd.option_context("display.max_rows",10):
   print(pd.get_option("display.max_rows"))
   print(pd.get_option("display.max_rows"))



# display.max_rows
#
# Displays maximum number of rows to display
#
#
# display.max_columns
#
# Displays maximum number of columns to display
#
# display.expand_frame_repr
#
# Displays DataFrames to Stretch Pages
#
# display.max_colwidth
#
# Displays maximum column width
#
# display.precision
#
# Displays precision for decimal numbers