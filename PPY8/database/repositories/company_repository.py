from typing import Sequence

from sqlalchemy import select, func, all_
from sqlalchemy.ext.asyncio import AsyncSession

from PPY8.database import Employee
from PPY8.database.models import Company


async def create_company(session: AsyncSession, name: str, address: str) -> Company:
    company = Company(name=name, address=address)
    session.add(company)
    await session.commit()
    await session.refresh(company)
    return company

async def get_companies(session: AsyncSession) -> Sequence[Company]:
    stmt = select(Company)
    result = await session.execute(stmt)
    return result.scalars().all()

async def get_companies_having_mt_employees(session: AsyncSession, threshold: int) -> Sequence[Company]:
    stmt = (
        select(Company)
        .join(Company.employees)
        .group_by(Company.id)
        .having(func.count(Employee.id) > threshold)
    )
    result = await session.execute(stmt)
    return result.scalars().all()

async def get_company_having_max_employees(session: AsyncSession) -> Company:
    subq_stmt = (
        select(func.count(Employee.id))
        .join(Company.employees)
        .group_by(Company.id)
    ).scalar_subquery()

    stmt = (
        select(Company)
        .join(Company.employees)
        .group_by(Company.id)
        .having(func.count(Employee.id) >= all_(subq_stmt))
    )

    result = await session.execute(stmt)
    return result.scalars().first()
