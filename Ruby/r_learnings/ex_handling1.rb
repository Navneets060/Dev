age = 12

def age_check(age)
	raise ArgumentError, "Enter Positive age" unless age >0
end

begin
	age_check(-1)	
	rescue ArgumentError
		puts "This is an Impossible age"		
end	