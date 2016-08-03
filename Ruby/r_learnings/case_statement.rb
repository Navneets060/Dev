=begin
	
uses case statement demonstration
	
=end

print "Enter Greetings :"
greeting = gets.chomp

case greeting
when "French", "french"
	puts "Bojour"
	exit
when "Spanish", "spanish"
	puts "hola"
	exit
else
	puts "hello"
end		
		
