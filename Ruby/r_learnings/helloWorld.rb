#SAMPLE PROGRAMS FOR RUBY

class HelloWorld

  @@count	= 0

  def initialize(name, id, ph_no)
    @hworld_name = name
	@hworld_id = id
	@hworld_ph_no = ph_no
  end

  def show_values
	puts "name = #{@hworld_name} \nId = #{@hworld_id} \nPh_no = #{@hworld_ph_no}"
  end

  $a = %W[nav neet san gyal]

  def recur
    $a.each do |name|
	  puts "#{@@count} : #{name}\n"
	  @@count += 1
    end
  end
end

H1 = HelloWorld.new('Navneet', 'I324519', '7795605568')
H1.show_values
H1.recur
