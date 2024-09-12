import React from "react";
import {
  Box,
  Container, HStack, Center, VStack
} from "@chakra-ui/react";

//import styles from "./Header.module.scss";

import Navbar from "./Navbar"
import Titles, { TitlesProps } from "components/Header/Titles/Titles";

export interface HeaderProps extends TitlesProps {
    role?: string
    addField?: JSX.Element
}

const Header: React.FC<HeaderProps> = (props) => {
    return (
    <Box>
    <Center>
    <Box bg='#D2691E' borderRadius='15' width='80%' mt='3' py='2'>
    <Center>
            <Navbar />
    </Center>
    </Box>
    </Center>
    <Center mt='5' fontFamily='Courier New'>
    <Titles {...props}/>
    {props.addField && props.addField}
    </Center>
    </Box>
    );
}

export default React.memo(Header);
