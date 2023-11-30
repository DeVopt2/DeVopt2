from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Numeric, Integer, String, DATETIME,UniqueConstraint, ForeignKey
from sqlalchemy.orm  import declarative_base

# Create engine
engine = create_engine('sqlite:///finance.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Portfolio(Base):
    __tablename__ = 'portfolio'
    id = Column(Integer, primary_key=True, autoincrement=True)
    /*ignore = Column(Integer, ForeignKey('users.id'),nullable=True)*/
    name = Column(String(30))
    sequence = Column(String(30))
    deposit = Column(Numeric(precision=13, scale=2), nullable=False, default=10000.00)
    symbol = Column(String(30), nullable=False)
    shares = Column(Integer, nullable=False)
    price = Column(Numeric(precision=13, scale=2), nullable=False)
    fname = Column(String(30), nullable=False)
    lname = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    phone = Column(String, nullable=False)
    country = Column(String(30), nullable=False)
    address = Column(String(30), nullable=False)
    city = Column(String(30), nullable=False)
    state = Column(String(30), nullable=False)
    zip = Column(Integer, nullable=False)
    creditcardno = Column(Integer, nullable=False)
    creditcardexp = Column(Integer, nullable=False)
    creditcardsecuritycode = Column(Integer, nullable=False)
    DATE=Column(DATETIME, nullable=False)
    buy_symbol = Column(String(30), nullable=False)
    buy_shares = Column(Integer, nullable=False)
    buy_price = Column(Numeric(precision=13, scale=2), nullable=False)
    buy_currentprice = Column(Numeric(precision=13, scale=2), nullable=False)
    buy_DATE = Column(DATETIME,nullable=False)
    sell_fname = Column(String(30), nullable=False)
    sell_lname = Column(String(30), nullable=False)
    sell_email = Column(String(30), nullable=False)
    sell_phone = Column(String, nullable=False)
    sell_country = Column(String(30), nullable=False)
    sell_address = Column(String(30), nullable=False)
    sell_city = Column(String(30), nullable=False)
    sell_state = Column(String(30), nullable=False)
    sell_zip = Column(Integer, nullable=False)
    sell_symbol = Column(String(30), nullable=False)
    sell_share = Column(Integer, nullable=False)
    sell_price = Column(Numeric(precision=13, scale=2), nullable=False)
    sell_DATE=Column(DATETIME,nullable=False)

    # Define the unique index
    __table_args__ = (
        UniqueConstraint('id', 'sequence', name='uq_name_sequence'),
    )

# Create an instance of the Portfolio class
portfolio = Portfolio(id=1,/*ignore='Example',*/ name='Example', sequence='ABC',
	deposit=10000.00,
    symbol='NFLX',
    shares=1.00,
    price=1.00,
    fname='Doe',
    lname='Remi',
    email='user@example.com',
    phone='123-456-7899',
    country='USA',
    address='12345 Main St',
    city='Cambridge',
    state=' Massachusetts',
    zip='10001',
    creditcardno='1234567890123',
    creditcardexp='01-29',
    creditcardsecuritycode='345',
    DATE=DATETIME,
    buy_symbol='KROG',
    buy_shares=1.00,
    buy_price=1.00,
    buy_currentprice=1.00,
    buy_DATE = DATETIME,
    sell_fname='Doe',
	sell_lname='Remi',
	sell_email='user@example.com',
    sell_phone='986-674-3202',
    sell_country='USA',
	sell_address='12345 Main St',
    sell_city='Cambridge',
	sell_state='Massachusetts',
    sell_zip='10001',
    sell_symbol='CLOX',
    sell_share =1.00,
    sell_price=234.00,
    sell_DATE=DATETIME),

# Create the table
Base.metadata.create_all(engine)



#Exception and error handling 
try:
        # Retrieve user's account try:
    # Perform database operations
    # ...
    # Add an object to the session
    session.add(portfolio)
    # ...
 # Commit the changes to the database
    session.commit()
except Exception as e:
    # Handle the exception
    print(f"An error occurred: {str(e)}")
    # Rollback the session to undo any changes
    session.rollback()
finally:
    # Close the session
    session.close()
