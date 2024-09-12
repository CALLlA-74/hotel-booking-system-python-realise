import React from "react";

import { Box, Link, Input, Button, Text, Center } from "@chakra-ui/react";
import { NavigateFunction } from "react-router-dom";

import { Create as CreateQuery } from "postAPI/accounts/Create";

import { RegistrationCard } from "types/RegistrationCard";

type SignUpProps = {
    navigate: NavigateFunction
}


class SignUpPage extends React.Component<SignUpProps> {
    registrationCard: RegistrationCard = {
        scope: "openid profile",
        username: "",
        first_name:	"",
        last_name:	"",
        patronymic: "",
        phone_number: "",
        password: "",
        email: ""
    }

    repPassword: string = ""

    setFirstName(val: string) {
        this.registrationCard.first_name = val
    }
    setLastName(val: string) {
        this.registrationCard.last_name = val
    }
    setPatronymic(val: string) {
        this.registrationCard.patronymic = val
    }
    setEmail(val: string) {
        this.registrationCard.email = val
    }
    setLogin(val: string) {
        this.registrationCard.username = val
    }
    setMobilePhone(val: string) {
        this.registrationCard.phone_number = val
    }
    setPassword(val: string) {
        this.registrationCard.password = val
    }
    setRepPassword(val: string) {
        this.repPassword = val
    }

    highlightNotMatch() {
        var title = document.getElementById("undertitle")
        if (title)
            title.innerText = "Пароли не совпадают!"
    }

    valueError(){
        var title = document.getElementById("undertitle")
        if (title)
            title.innerText = "Ошибка ввода данных! (Обнаружены пустые поля)"
    }

    async submit(e: React.MouseEvent<HTMLButtonElement, MouseEvent>) {
        if (this.registrationCard.password !== this.repPassword)
            return this.highlightNotMatch()

        if (this.registrationCard.first_name === '' || 
            this.registrationCard.last_name === '' ||
            this.registrationCard.phone_number === '' ||
            this.registrationCard.email === '' ||
            this.registrationCard.username === '')
            return this.valueError()

        //e.currentTarget.disabled = true
        var data = await CreateQuery(this.registrationCard)
        if (data.status === 200) {
            /*let acc: Account = {
                scope: "openid",
                grant_type: "password",
                username: this.registrationCard.username,
                password: this.registrationCard.password
            }

            await LoginQuery(acc);*/
            /*localStorage.setItem("token", response.data.access_token);
            localStorage.setItem("refresh-token", response.data.refresh_token);
            localStorage.setItem("scope", response.data.scope);
            localStorage.setItem("expires_in", response.data.expires_in);*/
            window.location.href = '/';
        } else {
            //e.currentTarget.disabled = false
            var title = document.getElementById("undertitle")
            if (title)
                title.innerText = "Ошибка создания аккаунта!"
        };
    }

    render() {
        return <Box fontFamily='Courier New' bg='#D2691E' borderRadius='' width='50%'>
            <Box p='3'>
                <Center>
                <Text fontSize='2xl'>Регистрация</Text>
                </Center>
            </Box>
            
            <Box p='3'>
                <Input bg='#8B4513' variant='' name="name" placeholder="Имя" 
                onInput={event => this.setFirstName(event.currentTarget.value)}/>
            </Box>
            <Box p='3'>
                <Input  bg='#8B4513' variant='' name="surname" placeholder="Фамилия" 
                onInput={event => this.setLastName(event.currentTarget.value)}/>
            </Box>
            <Box p='3'>
                <Input bg='#8B4513' variant='' name="patron" placeholder="Отчество" 
                onInput={event => this.setPatronymic(event.currentTarget.value)}/>
            </Box>
            <Box p='3'>
                <Input bg='#8B4513' variant='' name="mail" placeholder="E-mail" 
                onInput={event => this.setEmail(event.currentTarget.value)}/>
            </Box>
            <Box p='3'>
                <Input bg='#8B4513' variant='' name="login" placeholder="Логин" 
                onInput={event => this.setLogin(event.currentTarget.value)}/>
            </Box>
            <Box p='3'>
                <Input bg='#8B4513' variant='' name="number" placeholder="Номер телефона" 
                onInput={event => this.setMobilePhone(event.currentTarget.value)}/>
            </Box>
            <Box p='3' pt='10'>
                <Input bg='#8B4513' variant='' name="password" type="password" placeholder="Придумайте пароль"
                onInput={event => this.setPassword(event.currentTarget.value)}/>
            </Box>    
            <Box p='3'>
                <Input bg='#8B4513' variant='' name="rep-password" type="password" placeholder="Повторите пароль"
                onInput={event => this.setRepPassword(event.currentTarget.value)}/>
            </Box>

            <Box p='3'>
                <Button width='100%' bg='maroon' color='white' type="submit" onClick={event => this.submit(event)}>
                    Создать аккаунт
                </Button>
            </Box>
            <Box p='3'>
                <Text>Уже есть аккаунт?  
                    <Link color='#800000' href="/authorize">Войти</Link>
                </Text>
            </Box>
        </Box>
    }
}

export default SignUpPage;