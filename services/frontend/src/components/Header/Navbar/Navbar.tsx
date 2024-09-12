import React from "react";
import { Box, Center, Text } from "@chakra-ui/react";

import AuthActions from "./AuthActions";

export interface NavbarProps {}
const Navbar: React.FC<NavbarProps> = () => {
    let username = (localStorage.getItem('username') !== null ? localStorage.getItem('username') : '')!;

    return (
    <Box>
        <Box as='b' fontFamily='Courier New'>
                <Center>
                <Text mb='2' fontSize='3xl'>WILD WEST HOTELS</Text>
                </Center>
        </Box>
        { username !== '' && <AuthActions login={username.slice(0, 10)} />}
    </Box>
    )
}

export default React.memo(Navbar);
