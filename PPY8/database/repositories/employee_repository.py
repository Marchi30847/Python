from typing import Sequence

from sqlalchemy import select, update, delete, func, and_
from sqlalchemy.ext.asyncio import AsyncSession

from PPY8.database import Employee, Company


async def create_employee(session: AsyncSession, first_name: str, last_name: str, salary: float, company_id: int) -> Employee:
    employee = Employee(first_name=first_name, last_name=last_name, salary=salary, company_id=company_id)
    session.add(employee)
    await session.commit()
    await session.refresh(employee)
    return employee

async def get_employees(session: AsyncSession) -> Sequence[Employee]:
    stmt = select(Employee)
    result = await session.execute(stmt)
    return result.scalars().all()

async def get_employees_by_company_id(session: AsyncSession, company_id: int) -> Sequence[Employee]:
    stmt = (
        select(Employee)
        .where(Employee.company_id == company_id)
    )
    result = await session.execute(stmt)
    return result.scalars().all()

async def get_employee_by_id(session: AsyncSession, employee_id: int) -> Employee:
    stmt = (
        select(Employee)
        .where(Employee.id == employee_id)
    )
    result = await session.execute(stmt)
    return result.scalars().first()

async def update_salary_by_id(session: AsyncSession, employee_id: int, salary: float) -> None:
    stmt = (
        update(Employee)
        .where(Employee.id == employee_id)
        .values(salary=salary)
    )
    await session.execute(stmt)
    await session.commit()

async def delete_employee_by_id(session: AsyncSession, employee_id: int) -> None:
    stmt = (
        delete(Employee)
        .where(Employee.id == employee_id)
    )
    await session.execute(stmt)
    await session.commit()

async def get_employees_by_last_name_pattern(session: AsyncSession, last_name_pattern: str) -> Sequence[Employee]:
    stmt = (
        select(Employee)
        .where(Employee.last_name.ilike(f"%{last_name_pattern}%"))
    )
    result = await session.execute(stmt)
    return result.scalars().all()

async def get_employees_having_salary_gt_avg_in_their_company(session: AsyncSession) -> Sequence[Employee]:
    subq_stmt = (
        select(Employee.company_id, func.avg(Employee.salary).label("avg"))
        .group_by(Employee.company_id)
    ).subquery()
    stmt = (
        select(Employee)
        .where(and_(
            Employee.company_id == subq_stmt.c.company_id,
            Employee.salary > subq_stmt.c.avg,
        ))
    )
    result = await session.execute(stmt)
    return result.scalars().all()