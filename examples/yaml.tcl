# NOTE: 
#      I recoment to set up shebang for tclsh or xtclsh and setting chmod u+x on this file for faster iterations 

# Ingest YAML
# Note: YAML reader exist in most tcl based systems including Mentor and Xilinx tools.
#       the -file option makes YAML the most attractive option for file ingest as it becomes a one(two) liner.
package require yaml
set data [::yaml::yaml2dict -file [file join [file dirname [info script]] show.yml]]

# Print Raw YAML interpetation
puts "\n\nRAW data: $data"
puts [string repeat - 50 ]

# NOTE: Loop 2 Objects per iter as i know the input data are in dict format
foreach {key value} $data {
    puts [string repeat - 50 ]
    # Note: Order in the yaml file set president for ingest order!
    # Note: File normalizer could go here in an non nested usage, as all values are files.
    switch -regexp $key {
        vhdl(-\d+)? { 
            switch -regexp $key {
                vhdl-(20)?08 {
                    puts "read_vhdl -vhdl_2008 $value"
                }
                vhdl-(20)?02 {
                    puts "read_vhdl -vhdl-2002 $value"
                }
                default {
                    puts "Sadness!! 93 is such an old standard..."
                    puts "read_vhdl $value"
                }
            }
        }
        vlog|verilog {
            puts "read_verilog $value"
        }
        constraint {
            puts "Handle them with care, otherwise you will make some one loose their hair"
        }
        default {
            error "Unknown Format"
        }

    }
}
puts [string repeat - 50 ]

# Conclutions, thought about feature expantion:
#   * This will scale quite well to if vhdl library support or other nesting feature would be added.
#   * [ dict get $object $key ] will make a loot of the segmentet structures manageble. 
#   * procs will become usefull to not clutter the main data flow. 
#   * File relativity is always an issue. I sugest never defining files of a project wit .. in their paths. 
#     This will always make the end result clutterd and will be prone to errors. 
#       * Place the list in the root folder. You will only have the path to this file as a relative ".."
#         (this can be managed with ease)
#
# Recursion could probably be handled some thing like this to enable a system of systems (SoS) approach.
#   Would require the most outer foreach and everything inside to be packaged as a proc.
#   Library namespace does not got reqursive depth to my knowledge. This might be a problem. As large 
#   SoS should be prone to have namespace collisions. 
# Note: need to read up on TCL Recursion, vhdl library constructs and best practices of other types of 
#       name collisions (.xdc or other)
# 
# CASE in switch above, wrapper is proc aroud foreach above
# yaml { 
#     foreach file $value {
#         set d [::yaml::yaml2dict -file $value]
#         wrapper $d
#     }
# }
