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
-- Name: users; Type: TABLE; Schema: public; Owner: program
--

CREATE TABLE public.users (
    id integer NOT NULL,
	username varchar(80) NOT NULL,
	password_hash varchar() NOT NULL,
	role varchar(80) NOT NULL CHECK (role IN ('User', 'Admin')),
	first_name varchar(80) NOT NULL,
	last_name varchar(80) NOT NULL,
	patronymic varchar(80),
	phone_number varchar(15) NOT NULL,
	email varchar(), NOT NULL
);


ALTER TABLE public.users OWNER TO program;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: program
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO program;

--
-- Name: ticket_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: program
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: ticket id; Type: DEFAULT; Schema: public; Owner: program
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: program
--

/*COPY public.users (id, username, password_hash, role, first_name, last_name, patronymic, phone_number, email) FROM stdin;
1	username	passw	Admin	name	surname	patronymic	82222222222	username@domain.ru
\. */


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: program
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: program
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);

--
-- PostgreSQL database dump complete
--