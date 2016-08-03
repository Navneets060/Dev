=begin
Exception Handling Example	
=end

print " Enter a Number : "
num1 = gets.chomp.to_i
print "Enter second Number: "
num2 = gets.chomp.to_i

begin
	ans = num1/num2
 	
 rescue Exception => e
 	puts "Exception occured: please provide non zero dividend;"
 	exit
end 

puts "#{num1}/#{num2} equals : #{ans}"