#
#  Sort integer arguments (ascending) 
#
###

sorted_numbers = []
ARGV.each do |arg|
    # skip if not an integer
    next if arg !~ /^-?[0-9]+$/

    # convert to integer
    integer_value = arg.to_i
    
    # insert integer_value at the right position
    inserted = false
    index = 0
    length = sorted_numbers.size
    while !inserted && index < length do
        if sorted_numbers[index] < integer_value
            index += 1
        else
            sorted_numbers.insert(index , integer_value)
            inserted = true
            break
        end
    end
    sorted_numbers << integer_value if !inserted
end

puts sorted_numbers
