from fastapi import APIRouter, status, Header, Request, Form
from fastapi.exceptions import RequestValidationError
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from uuid import UUID

import services as GatewayService
import schemas.dto as schemas
from schemas.responses import ResponsesEnum
from config.config import get_settings

from validator import Validator

router = APIRouter(prefix='', tags=['Gateway API'])
settings = get_settings()


@router.get('/manage/health', status_code=status.HTTP_200_OK)
async def check_availability():
    return Response(status_code=status.HTTP_200_OK)


@router.get(f'{settings["prefix"]}/hotels', status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: ResponsesEnum.PaginationResponse.value
            })
async def get_all_hotels(page: int = 0, size: int = 0, credentials: str = Header(alias='Authorization', default="")):
    token = credentials.replace("Bearer ", "")
    print("access token: (", type(token), ") ", token)
    if not (await Validator.validate_token(token, leeway=0)):
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                            content=schemas.ErrorResponse(message='Unauthorized').model_dump())
    return await GatewayService.get_all_hotels(page, size, token)


@router.get(f'{settings["prefix"]}/me', status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: ResponsesEnum.UserInfoResponse.value
            })
async def get_user_info(credentials: str = Header(alias='Authorization', default="")):
    token = credentials.replace("Bearer ", "")
    if not (await Validator.validate_token(token, leeway=0)):
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                            content=schemas.ErrorResponse(message='Unauthorized').model_dump())
    return await GatewayService.get_user_info(token)


@router.get(f'{settings["prefix"]}/loyalty', status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: ResponsesEnum.LoyaltyInfoResponse.value
            })
async def get_loyalty(credentials: str = Header(alias='Authorization', default="")):
    token = credentials.replace("Bearer ", "")
    if not (await Validator.validate_token(token, leeway=0)):
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                            content=schemas.ErrorResponse(message='Unauthorized').model_dump())
    return await GatewayService.get_loyalty(token)


@router.get(f'{settings["prefix"]}/reservations', status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: ResponsesEnum.ReservationsResponse.value
            })
async def get_reservations(credentials: str = Header(alias='Authorization', default="")):
    token = credentials.replace("Bearer ", "")
    if not (await Validator.validate_token(token, leeway=0)):
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                            content=schemas.ErrorResponse(message='Unauthorized').model_dump())
    return await GatewayService.get_reservations(token)


@router.get(f'{settings["prefix"]}/reservations/' + '{reservationUid}', status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: ResponsesEnum.ReservationResponse.value,
                status.HTTP_404_NOT_FOUND: ResponsesEnum.ErrorResponse.value
            })
async def get_reservation_by_uid(reservationUid: UUID, credentials: str = Header(alias='Authorization', default="")):
    token = credentials.replace("Bearer ", "")
    if not (await Validator.validate_token(token, leeway=0)):
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                            content=schemas.ErrorResponse(message='Unauthorized').model_dump())
    reservation = await GatewayService.get_reservation_by_uid(reservationUid, token)
    if reservation is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=schemas.ErrorResponse().model_dump())
    return reservation


@router.post(f'{settings["prefix"]}/reservations', status_code=status.HTTP_200_OK,
             responses={
                 status.HTTP_200_OK: ResponsesEnum.CreateReservationResponse.value,
                 status.HTTP_400_BAD_REQUEST: ResponsesEnum.ValidationErrorResponse.value
             })
async def create_reservation(reservRequest: schemas.CreateReservationRequest,
                             credentials: str = Header(alias='Authorization', default="")):
    token = credentials.replace("Bearer ", "")
    if not (await Validator.validate_token(token, leeway=0)):
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                            content=schemas.ErrorResponse(message='Unauthorized').model_dump())
    try:
        reservation = await GatewayService.create_reservation(reservRequest, token)
    except RequestValidationError as exc:
        details = [schemas.ErrorDescription(
            field=e["field"],
            error=e["msg"]
        ) for e in jsonable_encoder(exc.errors())]

        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=schemas.ValidationErrorResponse(
            message='Invalid request',
            errors=list(details)
        ).model_dump())
    return reservation


@router.delete(f'{settings["prefix"]}/reservations/' + '{reservationUid}', status_code=status.HTTP_204_NO_CONTENT,
               responses={
                   status.HTTP_404_NOT_FOUND: ResponsesEnum.ErrorResponse.value
               })
async def delete_reservation(reservationUid: UUID, credentials: str = Header(alias='Authorization', default="")):
    token = credentials.replace("Bearer ", "")
    if not (await Validator.validate_token(token, leeway=0)):
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                            content=schemas.ErrorResponse(message='Unauthorized').model_dump())
    return await GatewayService.delete_reservation(reservationUid, token)


@router.post(f'{settings["prefix"]}/register', status_code=status.HTTP_200_OK, responses={})
async def register_user(data: Request):
    return await GatewayService.register_user(request=data)


@router.post(f'{settings["prefix"]}/oauth/token', status_code=status.HTTP_200_OK, responses={
    status.HTTP_200_OK: ResponsesEnum.CreateReservationResponse.value
})
async def auth_user(scope: str = Form(default=""),
                    grant_type: str = Form(default=""),
                    username: str = Form(default=""),
                    password: str = Form(default=""),
                    refresh_token: str = Header(alias='Authorization', default="")):
    """if req.headers['Content-Type'] == 'application/x-www-form-urlencoded':
        request = await req.form()"""
    return await GatewayService.auth_user(schemas.AuthenticationRequest(
        scope=scope,
        grant_type=grant_type,
        username=username,
        password=password,
        refresh_token=refresh_token
    ))


@router.post(f'{settings["prefix"]}/oauth/revoke', status_code=status.HTTP_200_OK, responses={})
async def logout(request: Request):
    await GatewayService.logout(request)
