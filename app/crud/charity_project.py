from typing import Dict, List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectUpdate)


class CRUDCharityProject(CRUDBase[
    CharityProject,
    CharityProjectCreate,
    CharityProjectUpdate
]):
    async def get_chairty_project_id_by_name(
        self,
        room_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        db_room_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == room_name
            )
        )
        return db_room_id.scalars().first()

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> List[Dict[str, int]]:
        charity_projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested
            )
        )
        charity_projects = charity_projects.scalars().all()
        projects = []
        for project in charity_projects:
            projects.append({
                'name': project.name,
                'collection_time': project.close_date - project.create_date,
                'description': project.description
            })
        return sorted(projects, key=lambda x: x['collection_time'])


charityproject_crud = CRUDCharityProject(CharityProject)
