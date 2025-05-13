import asyncio

from PPY8.database import get_company_having_max_employees, get_companies_having_mt_employees
from PPY8.database.data import init_db, AsyncSessionLocal
from PPY8.database.repositories.company_repository import create_company, get_companies
from PPY8.database.repositories.employee_repository import (
    create_employee,
    get_employees,
    get_employee_by_id,
    get_employees_by_company_id,
    update_salary_by_id,
    delete_employee_by_id,
    get_employees_by_last_name_pattern, get_employees_having_salary_gt_avg_in_their_company
)


async def main():
    await init_db()

    async with AsyncSessionLocal() as session:
        companies = [
            await create_company(session, name="TechCorp", address="Silicon Valley"),
            await create_company(session, name="EduLabs", address="Berlin"),
            await create_company(session, name="HealthPlus", address="London"),
            await create_company(session, name="AgroTech", address="Kyiv"),
            await create_company(session, name="GreenEnergy", address="Oslo")
        ]

        first_names = ["Alice", "Bob", "Charlie", "Diana", "Eve",
                       "Frank", "Grace", "Henry", "Ivy", "Jack",
                       "Kara", "Leo", "Mona", "Nate", "Olivia",
                       "Paul", "Quinn", "Rita", "Steve", "Tina"]

        last_names = ["Smith", "Brown", "Doe", "Lee", "White",
                      "Black", "Wong", "Davis", "Moore", "King",
                      "Clark", "Young", "Scott", "Hall", "Green",
                      "Hill", "Baker", "Nelson", "Cruz", "Reed"]

        for i in range(20):
            await create_employee(
                session,
                first_name=first_names[i],
                last_name=last_names[i],
                salary=40000 + i * 1000,
                company_id=companies[i % 5].id
            )

        all_employees = await get_employees(session)
        print("All employees:")
        for e in all_employees:
            print(f"{e.first_name} {e.last_name} | Company ID: {e.company_id} | Salary: {e.salary}")

        print("\nEmployees at TechCorp:")
        techcorp_emps = await get_employees_by_company_id(session, companies[0].id)
        for e in techcorp_emps:
            print(f"{e.first_name} {e.last_name}")

        await update_salary_by_id(session, employee_id=techcorp_emps[0].id, salary=99999)

        updated_emp = await get_employee_by_id(session, techcorp_emps[0].id)
        print(f"\nUpdated: {updated_emp.first_name} now earns {updated_emp.salary}")

        if len(techcorp_emps) > 1:
            await delete_employee_by_id(session, employee_id=techcorp_emps[1].id)

        print("\nSearch employees with 'doe' in last name:")
        matches = await get_employees_by_last_name_pattern(session, "doe")
        for e in matches:
            print(f"{e.first_name} {e.last_name}")

        print("\nCompanies in DB:")
        companies1 = await get_companies(session)
        for c in companies1:
            print(f"{c.id}: {c.name} - {c.address}")

        print("\nSearch companies having more employees than 3:")
        companies2 = await get_companies_having_mt_employees(session, 3)
        for c in companies2:
            print(f"{c.id}: {c.name} - {c.address}")

        print("\nSearch company with the max employees:")
        company = await get_company_having_max_employees(session)
        print(f"{company.id}: {company.name} - {company.address}")

        print("\nSearch for employees with salary greater than average in their company:")
        employees = await get_employees_having_salary_gt_avg_in_their_company(session)
        for e in employees:
            print(f"{e.id}: {e.first_name} {e.last_name} {e.salary} {e.company.name}")


if __name__ == "__main__":
    asyncio.run(main())