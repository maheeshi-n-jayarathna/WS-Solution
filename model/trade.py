from sqlalchemy import Column, Integer, Float, ForeignKey, String, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
import enum


# Define ENUMs for trade types and currency types
class TradeType(enum.Enum):
    BUY = 'buy'
    SELL = 'sell'


class CurrencyType(enum.Enum):
    BTC = 'BTC'
    USD = 'USD'


class Trade(Base):
    __tablename__ = 'trades'

    trade_id = Column(Integer, primary_key=True, index=True)
    usd_amount = Column(Float, nullable=False)
    btc_amount = Column(Float, nullable=False)
    currency = Column(Enum(CurrencyType), nullable=False)
    trade_type = Column(Enum(TradeType), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
