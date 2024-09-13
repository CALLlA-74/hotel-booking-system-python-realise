--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: hotels; Type: TABLE; Schema: public; Owner: program
--

CREATE TABLE public.hotels (
    id integer NOT NULL PRIMARY KEY,
    hotel_uid uuid NOT NULL UNIQUE,
    name varchar(255) NOT NULL,
    country varchar(80) NOT NULL,
    city varchar(80) NOT NULL,
    adress varchar(255) NOT NULL,
    stars integer,
    price integer NOT NULL
);

ALTER TABLE public.hotels OWNER TO program;

--
-- Name: hotels_id_seq; Type: SEQUENCE; Schema: public; Owner: program
--

CREATE SEQUENCE public.hotels_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.hotels_id_seq OWNER TO program;

--
-- Name: hotels_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: program
--

ALTER SEQUENCE public.hotels_id_seq OWNED BY public.hotels.id;


--
-- Name: hotels id; Type: DEFAULT; Schema: public; Owner: program
--

ALTER TABLE ONLY public.hotels ALTER COLUMN id SET DEFAULT nextval('public.hotels_id_seq'::regclass);


--
-- Data for Name: hotels; Type: TABLE DATA; Schema: public; Owner: program
--

COPY public.hotels (id, hotel_uid, name, country, city, adress, stars, price) FROM stdin;
1	049161bb-badd-4fa8-9d90-87c9a82b0668	South Shore Resort	USA	Salina	Victoria Heights Ter, 738	3	12500
2	049161bb-badd-4fa8-9d90-87c9a82b0667	One-night stand	USA	Winfield	142nd Rd, 17382	4	34000
3	049161bb-badd-4fa8-9d90-87c9a82b0666	Galactic Hotel	USA	El Dorado	Rr 5, 74	3	14000
4	049161bb-badd-4fa8-9d90-87c9a82b0665	Blue Moon	USA	Silver Lake	NW 35th St., 8942	5	46000
5	049161bb-badd-4fa8-9d90-87c9a82b0664	Olympus Hotel	USA	New Town	1806th Hwy E, 3911	5	72500
6	049161bb-badd-4fa8-9d90-87c9a82b0663	Obsidian Sky	USA	Bismarck	Deer Valley Ln., 2131	5	55500
7	99619f07-5e7e-42fa-bc25-7ba5df639534	Galactic Hotel	USA	Oakes	13th St N., 214	4	37200
8	2e721544-6e53-4a55-aaed-d0ad048ccab8	Treebones Resort	USA	Ranger	Vitalious St., 1023	2	4900
9	63ea23c8-04e8-43f3-a817-e77fac3bd78c	Obsidian Sky	USA	New Braunfels	Twin Oaks Dr., 891	5	52000
10	910d222d-a88c-4617-8fb2-89fefde8ad99	The Park Lane	USA	Hemphill	Pontiac Dr., 2312	4	44000
\.


--
-- Name: ticket_id_seq; Type: SEQUENCE SET; Schema: public; Owner: program
--

SELECT pg_catalog.setval('public.hotels_id_seq', 1, false);


--
-- Name: hotels hotels_pkey; Type: CONSTRAINT; Schema: public; Owner: program
--

ALTER TABLE ONLY public.hotels
    ADD CONSTRAINT hotels_pkey PRIMARY KEY (id);


--
-- Name: hotels hotels_hotel_uid_key; Type: CONSTRAINT; Schema: public; Owner: program
--

ALTER TABLE ONLY public.hotels
    ADD CONSTRAINT hotels_hotel_uid_key UNIQUE (hotel_uid);


--
-- Name: ix_hotel_id; Type: INDEX; Schema: public; Owner: program
--

CREATE INDEX ix_hotel_id ON public.hotels USING btree (id);


--
-- PostgreSQL database dump complete
--