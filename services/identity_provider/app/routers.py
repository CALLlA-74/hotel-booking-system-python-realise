from fastapi import APIRouter, Depends, status, Header, Response, Request, Form
from sqlalchemy.orm import Session
from database.AppDatabase import AppDatabase
from config.config import get_settings

import services as IdentityService
from schemas.responses import ResponsesEnum
from schemas.dto import RegisterUserRequest, AuthenticationRequest

from validator import Validator

router = APIRouter(prefix='', tags=['Loyalty REST API operations'])
app_db = AppDatabase.app_db
settings = get_settings()


@router.get('/manage/health', status_code=status.HTTP_200_OK)
async def check_availability():
    return Response(status_code=status.HTTP_200_OK)


@router.get(f'/.well-known/jwks.json', status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: ResponsesEnum.JWKsResponse.value
            })
async def get_jwks(db: Session = Depends(app_db.get_db)):
    return await IdentityService.get_jwks(db)


@router.post(f'{settings["prefix"]}/register', status_code=status.HTTP_200_OK,
             responses={
                 status.HTTP_200_OK: ResponsesEnum.TokenResponse.value
             })
async def register_user(data: RegisterUserRequest,
                        db: Session = Depends(app_db.get_db)):
    return await IdentityService.register_user(user_info=data, db=db)


@router.post(f'{settings["prefix"]}/oauth/token', status_code=status.HTTP_200_OK,
             responses={
                 status.HTTP_200_OK: ResponsesEnum.TokenResponse.value
             })
async def auth_user(
                    request: AuthenticationRequest = None,
                    db: Session = Depends(app_db.get_db)):
    """if req.headers['Content-Type'] == 'application/x-www-form-urlencoded':
        request = await req.form()"""
    request.refresh_token = request.refresh_token.replace("Bearer ", "")
    return await IdentityService.auth_user(request, db)


@router.post(f'{settings["prefix"]}/oauth/revoke', status_code=status.HTTP_200_OK,
             responses={
                 status.HTTP_200_OK: ResponsesEnum.TokenResponse.value
             })
async def logout(refresh_token: str = Header(alias='Authorization'),
                 db: Session = Depends(app_db.get_db)):
    await IdentityService.logout(refresh_token.replace("Bearer ", ""), db)
