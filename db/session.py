from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://ptjplqubrntdot:869c995e8c02bfda8f71d2c63eb361b105d7766a286ea9c27a871d3851b14c7a@ec2-52-209-185-5.eu-west-1.compute.amazonaws.com:5432/d1fsbmu87r2djb"


engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    # required for sqlite
    connect_args={"check_same_thread": False},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
