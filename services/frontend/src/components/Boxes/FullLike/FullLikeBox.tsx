import React from "react";
import {
    InputProps as IProps, Text, HStack
} from "@chakra-ui/react";

interface InputProps extends IProps {
    price?: number | string
}

const FullLikeBox: React.FC<InputProps> = (props) => {
    return (
    <HStack>
        <Text fontFamily='Courier New' color='#800000' fontSize='25'>(₽) {props.price} </Text>
    </HStack>
    )
}

export default FullLikeBox;