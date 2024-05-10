#!/usr/bin/env ruby
# This project is done by me

if ARGV[0]
    puts ARGV[0].scan(/School/).join
else
    puts "Please provide a string to search for occurrences of 'School'."
end
