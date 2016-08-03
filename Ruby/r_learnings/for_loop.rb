=begin
Shows the use of For loop in ruby
=end

numbers = [1,2,3,4,5]

for n in numbers
	print "#{n} "
end	

groceries = ["apple", "ginger", "banana", "mango", "raddish", "potato"]
puts
groceries.each do |item|
	puts "get some : #{item}"
end	

(0..5).each do |n|
	puts "# #{n}"
end	