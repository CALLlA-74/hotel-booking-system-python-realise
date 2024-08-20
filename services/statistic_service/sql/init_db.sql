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
-- Name: statistics; Type: TABLE; Schema: public; Owner: program
--

CREATE TABLE public.statistics (
    id integer NOT NULL,
	username varchar(80) NOT NULL,
	reservation_count integer NOT NULL,
	status varchar(80) NOT NULL CHECK (status IN ('BRONZE', 'SILVER', 'GOLD')),
	discount integer NOT NULL
);


ALTER TABLE public.statistics OWNER TO program;

--
-- Name: statistics_id_seq; Type: SEQUENCE; Schema: public; Owner: program
--

CREATE SEQUENCE public.statistics_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.statistics_id_seq OWNER TO program;

--
-- Name: statistics_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: program
--

ALTER SEQUENCE public.statistics_id_seq OWNED BY public.statistics.id;


--
-- Name: statistics id; Type: DEFAULT; Schema: public; Owner: program
--

ALTER TABLE ONLY public.statistics ALTER COLUMN id SET DEFAULT nextval('public.statistics_id_seq'::regclass);


--
-- Data for Name: statistics; Type: TABLE DATA; Schema: public; Owner: program
--

/*COPY public.statistics (id, username, reservation_count, status, discount) FROM stdin;
1	Test Max	25	GOLD	10
2	test-max@yaml.com	25	GOLD	10
\.*/


--
-- Name: statistics_id_seq; Type: SEQUENCE SET; Schema: public; Owner: program
--

SELECT pg_catalog.setval('public.statistics_id_seq', 1, false);


--
-- Name: statistics statistics_pkey; Type: CONSTRAINT; Schema: public; Owner: program
--

ALTER TABLE ONLY public.statistics
    ADD CONSTRAINT statistics_pkey PRIMARY KEY (id);

--
-- PostgreSQL database dump complete
--