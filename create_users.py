import selenium
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import regex as re
import time
import requests

def run_shit():
	temp_email_path = 'https://tempmail.email/'

	skool_signup = 'https://www.skool.com/'

	first_names = [
    "Liam", "Noah", "William", "James", "Oliver", "Benjamin", "Elijah", "Lucas", "Mason", "Logan",
    "Alexander", "Ethan", "Jacob", "Michael", "Daniel", "Henry", "Jackson", "Sebastian", "Aiden", "Matthew",
    "Samuel", "David", "Joseph", "Carter", "Owen", "Wyatt", "John", "Jack", "Luke", "Dylan",
    "Grayson", "Levi", "Isaac", "Gabriel", "Julian", "Mateo", "Anthony", "Jaxon", "Lincoln", "Joshua",
    "Christopher", "Andrew", "Theodore", "Caleb", "Ryan", "Asher", "Nathan", "Thomas", "Leo", "Isaiah",
    "Charles", "Josiah", "Hudson", "Christian", "Hunter", "Connor", "Eli", "Ezra", "Aaron", "Landon",
    "Adrian", "Jonathan", "Nolan", "Jeremiah", "Easton", "Elias", "Colton", "Cameron", "Carson", "Robert",
    "Angel", "Maverick", "Nicholas", "Dominic", "Jaxson", "Greyson", "Adam", "Ian", "Austin", "Santiago",
    "Jordan", "Cooper", "Brayden", "Roman", "Evan", "Ezekiel", "Xavier", "Jose", "Jace", "Jameson",
    "Leonardo", "Bryson", "Axel", "Everett", "Parker", "Kayden", "Miles", "Sawyer", "Jason", "Declan",
    "Weston", "Micah", "Ayden", "Wesley", "Luca", "Vincent", "Damian", "Zachary", "Silas", "Gavin",
    "Chase", "Kai", "Emmett", "Harrison", "Nathaniel", "Kingston", "Cole", "Tyler", "Bennett", "Bentley",
    "Ryker", "Tristan", "Brandon", "Kevin", "Luis", "George", "Ashton", "Rowan", "Braxton", "Ryder",
    "Gael", "Ivan", "Diego", "Maxwell", "Max", "Carlos", "Kaiden", "Juan", "Maddox", "Justin",
    "Waylon", "Calvin", "Giovanni", "Jonah", "Abel", "Jayce", "Jesus", "Amir", "King", "Beau",
    "Camden", "Alex", "Jasper", "Malachi", "Brody", "Jude", "Blake", "Emmanuel", "Eric", "Brooks",
    "Elliot", "Antonio", "Abraham", "Timothy", "Finn", "Rhett", "Elliott", "Edward", "August", "Xander",
    "Alan", "Dean", "Lorenzo", "Bryce", "Karter", "Victor", "Milo", "Miguel", "Hayden", "Graham",
    "Grant", "Zion", "Tucker", "Jesse", "Zayden", "Joel", "Richard", "Patrick", "Emiliano", "Avery",
    "Nicolas", "Brantley", "Dawson", "Myles", "Matteo", "River", "Steven", "Thiago", "Zane", "Matias",
    "Judah", "Messiah", "Jeremy", "Preston", "Oscar", "Kaleb", "Alec", "Kaden", "Paul", "Raul",
    "Colt", "Reid", "Jax", "Caden", "Javier", "Zander", "Andre", "Cayden", "Keegan", "Dominick",
    "Leighton", "Walker", "Kyrie", "Maddux", "Alexis", "Iker", "Jayson", "Roberto", "Lawson", "Broderick",
    "Malik", "Payton", "Mario", "Adriel", "Davis", "Landen", "Phoenix", "Seth", "Enzo", "Desmond",
    "Garrett", "Jared", "Knox", "Gage", "Simon", "Randy", "Edwin", "Teagan", "Riley", "Augustus",
    "Israel", "Adonis", "Cristian", "Jaiden", "Grady", "Jaime", "Sutton", "Sergio", "Marshal", "Marshall",
    "Ronin", "Leonel", "Armando", "Troy", "Nehemiah", "Daxton", "Dexter", "Fabian", "Elian", "Brock",
    "Leland", "Kamden", "Mohamed", "Derrick", "Ali", "Remy", "Dante", "Gerardo", "Joaquin", "Jonas",
    "Kasen", "Sullivan", "Davis", "Albert", "Russell", "Karson", "Royal", "Conor", "Ari", "Dalton",
    "Gunnar", "Sage", "Frank", "Keaton", "Reed", "Dillon", "Morgan", "Rhys", "Rocco", "Emanuel",
    "Zaiden", "Cohen", "Ace", "Arturo", "Nico", "Kieran", "Dennis", "Charlie", "Kian", "Tate",
    "Jaime", "Zayn", "Curtis", "Luka", "Mauricio", "Mathias", "Nash", "Ahmed", "Emery", "Archer",
    "Kyler", "Theo", "Orlando", "Kellan", "Milan", "Jeffrey", "Raphael", "Callum", "Hugo", "Issac",
    "Marvin", "Chandler", "Dorian", "Enrique", "Keith", "Soren", "Jonathon", "Quinn", "Gunner", "Solomon",
    "Ezequiel", "Nasir", "Nico", "Jaxen", "Kylan", "Luigi", "Gannon", "Gary", "Wilson", "Nikolas",
    "Brooklyn", "Fletcher", "Santino", "Trace", "Memphis", "Edgar", "Nelson", "Romeo", "Baker", "Hamza",
    "Devin", "Santana", "Adan", "Harvey", "Harley", "Emmitt", "Cullen", "Rohan", "Rhett", "Deacon",
    "Casen", "London", "Lucian", "Baylor", "Casey", "Dax", "Lawrence", "Braylon", "Omari", "Nico",
    "Pierce", "Billy", "Aaden", "Brendan", "Cairo", "Kingsley", "Valentino", "Marcel", "Jamie", "Kace",
    "Reece", "Nikolai", "Moshe", "Rodrigo", "Makai", "Harlan", "Keagan", "Korbin", "Franco", "Boston",
    "Irving", "Merlin", "Shaun", "Crosby", "Dariel", "Ulysses", "Rodney", "Sampson", "Yahir", "Kye",
    "Emory", "Yousef", "Jaziel", "Makhi", "Mathew", "Drew", "Terry", "Eddie", "Rayan", "Zayne",
    "Terrance", "Chaim", "Dakari", "Jon", "Kareem", "Mordechai", "Arian", "Jagger", "Keanu", "Konnor",
    "Randall", "Zain", "Bentlee", "Benton", "Willie", "Jonael", "Maxim", "Brett", "Fox", "Leandro",
    "Joziah", "Morris", "Rene", "Denver", "Ayan", "Darian", "Gianluca", "Kamari", "Yusuf", "Dimitri",
    "Jamir", "Van", "Aarav", "Clinton", "Horacio", "Kody", "Robin", "Aron", "Maxton", "Salvador",
    "Will", "Brycen", "Cristopher", "Kace", "Dereon", "Vicente", "Kamryn", "Konnor", "Rayden", "Bear",
    "Isaias", "Jefferson", "Tomas", "Harold", "Harper", "Zahir", "Kamdyn", "Mike", "Orion", "Reginald",
    "Nixon", "Louie", "Raylan", "Ernesto", "Neil", "Bodie", "Vincenzo", "Ishaan", "Ameer", "Anton",
    "Aron", "Layton", "Leighton", "Maison", "Brixton", "Branson", "Rocky", "Kenny", "Maximilian", "Alaric",
    "Yosef", "Aryan", "Dario", "Roland", "Alfonso", "Davion", "Bobby", "Joey", "Shaurya", "Konner",
    "Markus", "Harlem", "Gatlin", "Jair", "Reign", "Aron", "Payton", "Rayyan", "Reagan", "Dangelo",
    "Sonny", "Rudy", "Van", "Azariah", "Tru", "Westin", "Blaze", "Gerald", "Terrence", "Bentley",
    "Vance", "Giovanny", "Olivia", "Alfredo", "Kolton", "Ralph", "Reuben", "Westley", "Blaise", "Aldo",
    "Jerome", "Kylen", "London", "Mack", "Jeremias", "Rex", "Deandre", "Fisher", "Harry", "Pierre",
    "Khalid", "Lyric", "Marlon", "Samir", "Zeke", "Denzel", "Broderick", "Ares", "Blaine", "Coen",
    "Grey", "Kyson", "Aarush", "Elisha", "Kamryn", "Lian", "Arjun", "Kyran", "Zackary", "Aaden",
    "Callan", "Tristian", "Eugene", "Jovanni", "Kingsley", "Orlando", "Alvin", "Madden", "Santos", "Alistair",
    "Eugene", "Vivaan", "Bishop", "Brenden", "Talon", "Briggs", "Chad", "Ernest", "Javion", "Lyle",
    "Simeon", "Ridge", "Santos", "Rylen", "Willis", "Jaxxon", "Kace", "Darnell", "Franco", "Jean",
    "Stefan", "Watson", "Sutton", "Brysen", "Niklaus", "Cale", "Kelvin", "Houston", "Leif", "Allan",
    "Colten", "Jamar", "Jovani", "Mikael", "Kenny", "Hassan", "Leroy", "Khalil", "Freddy", "Agustin",
    "Brentley", "Gaige", "Gibson", "Kase", "Augustine", "Darwin", "Yehuda", "Cain", "Camron", "Jamie",
    "Yadiel", "Dangelo", "Trystan", "Alfred", "Huxley", "Marley", "Kamdyn", "Kye", "Rashad", "Lennon",
    "Thaddeus", "Xzavier", "Daxtyn", "Donte", "Edison", "Jabari", "Lian", "Franco", "Sheldon", "Shiloh",
    "Benicio", "Blaise", "Bronson", "Emir", "Jovanny", "Juelz", "Kasey", "Masen", "Hakeem", "Krish",
    "Kymani", "Maison", "Maximo", "Gian", "Jaydon", "Franco", "Jovani", "Kamron", "Rayan", "Todd",
    "Bjorn", "Anson", "Brecken", "Jovanny", "Kalvin", "Kyron", "Riggs", "Austyn", "Franco", "Immanuel",
    "Jovany", "Wesson", "Dov", "Jovani", "Khai", "Ramiro", "Bryar", "Kymani", "Makai", "Percy",
    "Gavyn", "Jovany", "Kaidyn", "Yisroel", "Blayne", "Franco", "Jovani", "Keyon", "Jovanny", "Zackery",
    "Auston", "Franco", "Jovanny", "Zaki", "Jovanny", "Kaine", "Kyden", "Rigoberto", "Bjorn", "Jovanny",
    "Kaison", "Khyree", "Franco", "Jovani", "Kanoa", "Kayan", "Zaki", "Franco", "Jovani", "Brogan",
    "Jov"]

	last_names = [
	    "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson",
	    "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore", "Martin", "Jackson", "Thompson", "White",
	    "Lopez", "Lee", "Gonzalez", "Harris", "Clark", "Lewis", "Robinson", "Walker", "Perez", "Hall",
	    "Young", "Allen", "Sanchez", "Wright", "King", "Scott", "Green", "Baker", "Adams", "Nelson",
	    "Hill", "Ramirez", "Campbell", "Mitchell", "Roberts", "Carter", "Phillips", "Evans", "Turner", "Torres",
	    "Parker", "Collins", "Edwards", "Stewart", "Flores", "Morris", "Nguyen", "Murphy", "Rivera", "Cook",
	    "Rogers", "Morgan", "Peterson", "Cooper", "Reed", "Bailey", "Bell", "Gomez", "Kelly", "Howard",
	    "Ward", "Cox", "Diaz", "Richardson", "Wood", "Watson", "Brooks", "Bennett", "Gray", "James",
	    "Reyes", "Cruz", "Hughes", "Price", "Myers", "Long", "Foster", "Sanders", "Ross", "Morales",
	    "Powell", "Sullivan", "Russell", "Ortiz", "Jenkins", "Gutierrez", "Perry", "Butler", "Barnes", "Fisher",
	    "Henderson", "Coleman", "Simmons", "Patterson", "Jordan", "Reynolds", "Hamilton", "Graham", "Kim", "Gonzales",
	    "Alexander", "Ramos", "Wallace", "Griffin", "West", "Cole", "Hayes", "Chavez", "Gibson", "Bryant",
	    "Ellis", "Stevens", "Murray", "Ford", "Marshall", "Owens", "Mcdonald", "Harrison", "Ruiz", "Kennedy",
	    "Wells", "Alvarez", "Woods", "Mendoza", "Castillo", "Olson", "Webb", "Washington", "Tucker", "Freeman",
	    "Burns", "Henry", "Vasquez", "Snyder", "Simpson", "Crawford", "Jimenez", "Porter", "Mason", "Shaw",
	    "Gordon", "Wagner", "Hunter", "Romero", "Hicks", "Dixon", "Hunt", "Palmer", "Robertson", "Black",
	    "Holmes", "Stone", "Meyer", "Boyd", "Mills", "Warren", "Fox", "Rose", "Rice", "Moreno",
	    "Schmidt", "Patel", "Ferguson", "Nichols", "Herrera", "Medina", "Ryan", "Fernandez", "Weaver", "Daniels",
	    "Stephens", "Gardner", "Payne", "Kelley", "Dunn", "Pierce", "Arnold", "Tran", "Spencer", "Peters",
	    "Hawkins", "Grant", "Hansen", "Castro", "Hoffman", "Hart", "Elliott", "Cunningham", "Knight", "Bradley",
	    "Carroll", "Hudson", "Duncan", "Armstrong", "Berry", "Andrews", "Johnston", "Ray", "Lane", "Riley",
	    "Carpenter", "Perkins", "Aguilar", "Silva", "Richards", "Willis", "Matthews", "Chapman", "Lawrence", "Garza",
	    "Vargas", "Watkins", "Wheeler", "Larson", "Carlson", "Harper", "George", "Greene", "Burke", "Guzman",
	    "Morrison", "Munoz", "Jacobs", "Obrien", "Lawson", "Franklin", "Lynch", "Bishop", "Carr", "Salazar",
	    "Austin", "Mendez", "Gilbert", "Jensen", "Williamson", "Montgomery", "Harvey", "Oliver", "Howell", "Dean",
	    "Hanson", "Weber", "Garrett", "Sims", "Burton", "Fuller", "Soto", "Mccoy", "Welch", "Chen",
	    "Schultz", "Walters", "Reid", "Fields", "Walsh", "Little", "Fowler", "Bowman", "Davidson", "May",
	    "Day", "Schneider", "Newman", "Brewer", "Lucas", "Holland", "Wong", "Banks", "Santos", "Curtis",
	    "Pearson", "Delgado", "Valdez", "Pena", "Rios", "Douglas", "Sandoval", "Barrett", "Hopkins", "Keller",
	    "Guerrero", "Stanley", "Bates", "Alvarado", "Beck", "Ortega", "Wade", "Estrada", "Contreras", "Barnett",
	    "Caldwell", "Santiago", "Lambert", "Powers", "Chambers", "Nunez", "Craig", "Leonard", "Lowe", "Rhodes",
	    "Byrd", "Gregory", "Shelton", "Frazier", "Becker", "Maldonado", "Fleming", "Vega", "Sutton", "Cohen",
	    "Jennings", "Parks", "Mcdaniel", "Watts", "Barker", "Norris", "Vaughn", "Vazquez", "Holt", "Schwartz",
	    "Steele", "Benson", "Neal", "Dominguez", "Horton", "Terry", "Wolfe", "Hale", "Lyons", "Graves",
	    "Haynes", "Miles", "Park", "Warner", "Padilla", "Bush", "Thornton", "Mccarthy", "Mann", "Zimmerman",
	    "Erickson", "Fletcher", "Mckinney", "Page", "Dawson", "Joseph", "Marquez", "Reeves", "Klein", "Espinoza",
	    "Baldwin", "Moran", "Love", "Robbins", "Higgins", "Ball", "Cortez", "Le", "Griffith", "Bowen",
	    "Sharp", "Cummings", "Ramsey", "Hardy", "Swanson", "Barber", "Acosta", "Luna", "Chandler", "Blair",
	    "Daniel", "Cross", "Simon", "Dennis", "Oconnor", "Quinn", "Gross", "Navarro", "Moss", "Fitzgerald",
	    "Doyle", "Mclaughlin", "Rojas", "Rodgers", "Stevenson", "Singh", "Yang", "Figueroa", "Harmon", "Newton",
	    "Paul", "Manning", "Garner", "Mcgee", "Reese", "Francis", "Burgess", "Adkins", "Goodman", "Curry",
	    "Brady", "Christensen", "Potter", "Walton", "Goodwin", "Mullins", "Molina", "Webster", "Fischer", "Campos",
	    "Avila", "Sherman", "Todd", "Chang", "Blake", "Malone", "Wolf", "Hodges", "Juarez", "Gill",
	    "Farmer", "Hines", "Gallagher", "Duran", "Hubbard", "Cannon", "Miranda", "Wang", "Saunders", "Tate",
	    "Mack", "Hammond", "Carrillo", "Townsend", "Wise", "Ingram", "Barton", "Mejia", "Ayala", "Schroeder",
	    "Hampton", "Rowe", "Parsons", "Frank", "Waters", "Strickland", "Osborne", "Maxwell", "Chan", "Deleon",
	    "Norman", "Harrington", "Casey", "Patton", "Logan", "Bowers", "Mueller", "Glover", "Floyd", "Hartman",
	    "Buchanan", "Cobb", "French", "Kramer", "Mccormick", "Clarke", "Tyler", "Gibbs", "Moody", "Conner",
	    "Sparks", "Mcguire", "Leon", "Bauer", "Norton", "Pope", "Flynn", "Hogan", "Robles", "Salinas",
	    "Yates", "Lindsey", "Lloyd", "Marsh", "Mcbride", "Owen", "Solis", "Pham", "Lang", "Pratt",
	    "Lara", "Brock", "Ballard", "Trujillo", "Shaffer", "Drake", "Roman", "Aguirre", "Morton", "Stokes",
	    "Lamb", "Pacheco", "Patrick", "Cochran", "Shepherd", "Cain", "Burnett", "Hess", "Li", "Cervantes",
	    "Olsen", "Briggs", "Ochoa", "Cabrera", "Velasquez", "Montoya", "Roth", "Meyers", "Cardenas", "Fuentes",
	    "Weiss", "Hoover", "Wilkins", "Nicholson", "Underwood", "Short", "Carson", "Morrow", "Colon", "Holloway",
	    "Summers", "Bryan", "Petersen", "Mckenzie", "Serrano", "Wilcox", "Carey", "Clayton", "Poole", "Calderon",
	    "Gallegos", "Greer", "Rivas", "Guerra", "Decker", "Collier", "Wall", "Whitaker", "Bass", "Flowers",
	    "Davenport", "Conley", "Houston", "Huff", "Copeland", "Hood", "Monroe", "Massey", "Roberson", "Combs",
	    "Franco", "Larsen", "Pittman", "Randall", "Skinner", "Wilkinson", "Kirby", "Cameron", "Bridges", "Anthony",
	    "Richard", "Kirk", "Bruce", "Singleton", "Mathis", "Bradford", "Boone", "Abbott", "Charles", "Allison",
	    "Sweeney", "Atkinson", "Horn", "Jefferson", "Rosales", "York", "Christian", "Phelps", "Farrell", "Castaneda",
	    "Nash", "Dickerson", "Bond", "Wyatt", "Foley", "Chase", "Gates", "Vincent", "Mathews", "Hodge",
	    "Garrison", "Trevino", "Villarreal", "Heath", "Dalton", "Valencia", "Callahan", "Hensley", "Atkins", "Huffman",
	    "Roy", "Boyer", "Shields", "Lin", "Hancock", "Grimes", "Glenn", "Cline", "Delacruz", "Camacho",
	    "Dillon", "Parrish", "Oneill", "Melton", "Booth", "Kane", "Berg", "Harrell", "Pitts", "Savage",
	    "Wiggins", "Brennan", "Salas", "Marks", "Russo", "Sawyer", "Baxter", "Golden", "Hutchinson", "Liu",
	    "Walter", "Mcdowell", "Wiley", "Rich", "Humphrey", "Johns", "Koch", "Suarez", "Hobbs", "Beard",
	    "Gilmore", "Ibarra", "Keith", "Macias", "Khan", "Andrade", "Ware", "Stephenson", "Henson", "Wilkerson",
	    "Dyer", "Mcclure", "Blackwell", "Mercado", "Tanner", "Eaton", "Clay", "Barron", "Beasley", "Oneal",
	    "Preston", "Small", "Wu", "Zamora", "Macdonald", "Vance", "Snow", "Mcclain", "Stafford", "Orozco",
	    "Barry", "English", "Shannon", "Kline", "Jacobson", "Woodard", "Huang", "Kemp", "Mosley", "Prince",
	    "Merritt", "Hurst", "Villanueva", "Roach", "Nolan", "Lam", "Yoder", "Mccullough", "Lester", "Santana",
	    "Valenzuela", "Winters", "Barrera", "Orr", "Leach", "Berger", "Mckee", "Strong", "Conway", "Stein",
	    "Whitehead", "Bullock", "Escobar", "Knox", "Meadows", "Solomon", "Velez", "Odonnell", "Kerr", "Stout",
	    "Blankenship", "Browning", "Kent"]

	print('init chrome incognito...')
	chrome_options = Options()
	chrome_options.add_argument("--incognito")  # This line enables incognito mode
	chrome_options.add_argument("--enable-chrome-browser-cloud-management")

	# Path to your ChromeDriver executable
	chromedriver_path = 'chromedriver-win64/chromedriver-win64/chromedriver.exe'

	# Initialize Chrome driver with Chrome options
	driver = webdriver.Chrome(options=chrome_options)
	try:

		first_name = random.choice(first_names)
		last_name = random.choice(last_names)

		print(f'generating user for {first_name} {last_name}')

		driver.execute_script(f"window.open('{temp_email_path}','email_tab');")
		driver.switch_to.window("email_tab")
		wait = WebDriverWait(driver, 10)
		div_element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div[3]/div/div[2]')))
		temp_email = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/div[2]").text

		print(temp_email)


		driver.execute_script(f"window.open('{skool_signup}','skool_tab');")
		driver.switch_to.window("skool_tab")

		init_signup_btn = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/div/div/div[3]/div/button[1]")
		init_signup_btn.click()

		time.sleep(2)

		fn_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/form/div/div[1]/div/input")
		fn_input.send_keys(first_name)

		ln_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/form/div/div[2]/div/input")
		ln_input.send_keys(last_name)

		email_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/form/div/div[3]/div/input")
		email_input.send_keys(temp_email)


		pw_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/form/div/div[4]/div/input")
		driver.execute_script("arguments[0].scrollIntoView();", pw_input)
		pw_input.send_keys('password12345')


		signup_btn = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/form/button")
		driver.execute_script("arguments[0].scrollIntoView();", signup_btn)
		driver.implicitly_wait(10)
		signup_btn.click()

		time.sleep(3)

		driver.switch_to.window("email_tab")
		driver.switch_to.window("skool_tab")
		time.sleep(3)
		driver.switch_to.window("email_tab")
		time.sleep(75)
		# driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/img').click()
		# wait = WebDriverWait(driver, 20)
		# div_element = wait.until(EC.visibility_of_element_located((By.XPATH, '/div/div[3]/div[2]')))
		# verification_code = driver.find_element(By.XPATH, '/div/div[3]/div[2]').text

		all_page = driver.page_source
		verification_code = re.findall(r'\d{4} is your Skool verification code', all_page)
		print(verification_code)
		verification_code_cut = verification_code[0][:4]
		print(verification_code_cut)
		driver.switch_to.window("skool_tab")

		driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[2]/form/div[1]/div/input').send_keys(verification_code_cut)


		driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[2]/form/button').click()

		time.sleep(1)
		with open('emails.txt', 'a') as f:
			f.write(f'{temp_email}\n')
		driver.quit()
		return
	except:
		driver.quit()

for i in range(5000):
	try:
		print('attempting...')
		run_shit()
		print('success!')
		time.sleep(30)
	except:
		print('failure!')
		time.sleep(30)
