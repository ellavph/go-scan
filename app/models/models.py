from sqlalchemy import DateTime, func, Boolean, Column


class Log:
    dat_insercao = Column(DateTime(timezone=True), server_default=func.now())
    dat_edicao = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    status = Column(Boolean(), nullable=True, server_default='true')
