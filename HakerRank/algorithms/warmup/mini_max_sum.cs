//C#

static void Main(String[] args) 
        {
            string[] line_temp = Console.ReadLine().Split();
            long[] line = Array.ConvertAll(line_temp, long.Parse);
                     
            Array.Sort(line);
            
            long array_sum = line.Sum();
            long min_value = array_sum - line[4];
            long max_value = array_sum - line[0];

            Console.Write(min_value + " " + max_value);
            }
            
        }