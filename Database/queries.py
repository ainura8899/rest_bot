class Queries:
    CREATE_REVIEW_RESULTS_TABLE = '''
    CREATE TABLE IF NOT EXISTS restauran_review(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    instagram_username TEXT,
    visit_date DATE,
    food_rating INTEGER,
    cleanliness_rating INTEGER,
    extra_comments TEXT
    )
    '''


    INSERT_INTO_RESTAURANT_REVIEW = '''
    insert into restauran_review  values(?, ?, ?, ?, ?, ?, ?)
    '''

    CREATE_TABLE_CATEGORIES = '''
    CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (255),
    UNIQUE (name))'''


    CREATE_TABLE_DISHES = '''
    CREATE TABLE IF NOT EXISTS dishes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR (255),
    price INTEGER,
    photo TEXT,
    category_id INTEGER,
    UNIQUE (title),
    FOREIGN KEY (category_id) REFERENCES categories(id))'''

    INSERT_INTO_CAT = '''
    INSERT OR IGNORE INTO categories (name) VALUES ('Напитки'), ('Блюда'), ('Салаты')'''

    INSERT_INTO_DISHES = '''
    INSERT OR IGNORE INTO dishes (title, price, photo, category_id) VALUES 
    ('Плов', 365, 'images/plov.jpg', 2), ('Шашлык', 415, 'images/shashlyk.jpg', 2),
    ('Греческий салат', 390, 'images/greek salad.jpg', 3), ('Салат цезарь', 485, 'images/tsezar.jpeg', 3),
     ('Лимонад', 350, 'images/lemonade.jpg', 1), ('Чай', 300, 'images/tea.jpg', 1)
    '''
