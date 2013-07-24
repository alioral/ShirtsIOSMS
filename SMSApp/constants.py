SUCCESS_MESSAGE = 'You have successfully submitted your shirt request'
SUCCESS_MESSAGE_CANCELLATION = 'You have successfully canceled your shirt request'


ERROR_MESSAGE_ALREADY_HAVE_SHIRT_REQUEST = 'You already have a pending shirt request'
ERROR_MESSAGE_SERVER = 'An error occured on server. Please try again later.'


DB_URL = 'mongodb://ali:1234@ds037488.mongolab.com:37488/heroku_app17085708'

YES_ARRAY = ["yes", "YES", "Yes"]
NO_ARRAY = ["no", "NO", "No"]
YES_NO_ARRAY = YES_ARRAY + NO_ARRAY

APPLICATION_IMAGE_LINK = 'http://guarded-caverns-8300.herokuapp.com/image/'

ORDER_API_MAPPINGS = {'api_key': '63aae231cdab277428c0c4e73ee2e9f3ccbe6c42',
         'test':'True', 'design':'True', 'price':'18.41', 
         'garment[0][product_id]': '3',
         'garment[0][color]':'White',
         'garment[0][sizes][lrg]': '1',
         'print[front][color_count]':'1',
         'print[front][artwork]':'http://i488.photobucket.com/albums/rr249/STACIA_GIRL_2009/ANIMALES/koala.png',
         'print[front][proof]':'http://www.stanford.edu/~jay/koalas/Koala450j.jpg',
         'addresses[0][name]':'John Doe',
         'addresses[0][address]':'123 Hope Ln.',
         'addresses[0][city]':'Las Vegas',
         'addresses[0][state]':'Nevada',
         'addresses[0][zipcode]':'12345'}