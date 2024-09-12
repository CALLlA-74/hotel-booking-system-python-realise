import { Box, HStack, Image, Text, Badge, Center} from "@chakra-ui/react";
import React from "react";

import { Hotel as HotelI } from "types/Hotel";

import StarBox from "components/Boxes/Star";
import FullLikeBox from "components/Boxes/FullLike";

//import styles from "./HotelCard.module.scss";
import GetImageUrl from "postAPI/likes/Get";

import CalendarWidget from "components/DateInput";
import {DateReservation as DateReservationT} from "types/DateReservation";
import {ReservationRequest as ReservationRequestT} from "types/ReservationRequest";
import PostReservation from "postAPI/likes/Post";


interface HotelProps extends HotelI {}

const HotelCard: React.FC<HotelProps> = (props) => {
  const [imageUrl, setImageUrl] = React.useState("https://media.discordapp.net/attachments/791290400086032437/1112498073478889502/default-fallback-image.png?width=720&height=480");

  async function getImageUrl() {
    var data = await GetImageUrl(props.hotelUid);
    if (data.status === 200) {
      setImageUrl(data.content);
    }
  }

  async function putDateReservation(dataInfo: DateReservationT) {
    const reservationRequest: ReservationRequestT = { 
      hotelUid: props.hotelUid, 
      startDate: dataInfo.startDate.toLocaleDateString("en-CA"),
      endDate: dataInfo.endDate.toLocaleDateString("en-CA") 
    };

    await PostReservation(reservationRequest);
  }

  getImageUrl();

  return (
    <Box mb='5' bg='#D2691E' p='3' borderRadius='' borderWidth='1px'>

      <Box p='3' borderWidth='1px' borderColor='#800000' borderRadius=''>
          <Badge py='2' fontFamily='Berlin Sans FB' borderRadius='full' px='65' bg='#800000' color='white' fontSize='3xl' width='100%'>
            <Center>{props.name}</Center>
          </Badge>

          <Center>
          <Image src='https://i.pinimg.com/736x/5d/8a/ac/5d8aacf58f7d14f91fbe9e35a2c1f157.jpg' 
          borderRadius='full' my='2'>
          </Image>
          </Center>
          
          <Center>
          <HStack>
            <Text fontSize='xl' fontFamily='Courier New' color='#800000'>{props.country}</Text>
            <Text as='u' color='#800000' fontFamily='Courier New'>{props.city}</Text>
            <Text as='u' color='#800000' fontFamily='Courier New'>{props.address}</Text>
          </HStack>
          </Center>

        <Center>
        <HStack>
          <StarBox duration={props.stars} />
          <FullLikeBox price={props.price} />
        </HStack>
        </Center>

        <CalendarWidget putCallback={(data: DateReservationT) => putDateReservation(data)}/>

      </Box>
    </Box>
  );
};

export default HotelCard;
