=begin
File Operations Hndled here
=end

finput = File.new("hello.txt", "w")
finput.puts("hello navneet... welcome to file !!!").to_s
finput.close

fout = File.read("hello.txt")
puts "from file : " + fout
