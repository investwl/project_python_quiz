--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

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
-- Name: experiment_1; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.experiment_1 (
    house_number integer NOT NULL,
    road_name character varying(50) NOT NULL,
    owner_id integer NOT NULL
);


ALTER TABLE public.experiment_1 OWNER TO postgres;

--
-- Name: experiment_1_house_number_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.experiment_1_house_number_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.experiment_1_house_number_seq OWNER TO postgres;

--
-- Name: experiment_1_house_number_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.experiment_1_house_number_seq OWNED BY public.experiment_1.house_number;


--
-- Name: trial_and_error; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.trial_and_error (
    name_id integer NOT NULL,
    name character varying(30) NOT NULL,
    job character varying(30) NOT NULL
);


ALTER TABLE public.trial_and_error OWNER TO postgres;

--
-- Name: trial_and_error_name_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.trial_and_error_name_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.trial_and_error_name_id_seq OWNER TO postgres;

--
-- Name: trial_and_error_name_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.trial_and_error_name_id_seq OWNED BY public.trial_and_error.name_id;


--
-- Name: experiment_1 house_number; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.experiment_1 ALTER COLUMN house_number SET DEFAULT nextval('public.experiment_1_house_number_seq'::regclass);


--
-- Name: trial_and_error name_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trial_and_error ALTER COLUMN name_id SET DEFAULT nextval('public.trial_and_error_name_id_seq'::regclass);


--
-- Data for Name: experiment_1; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.experiment_1 (house_number, road_name, owner_id) FROM stdin;
2	Silicon Valley	7
\.


--
-- Data for Name: trial_and_error; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.trial_and_error (name_id, name, job) FROM stdin;
7	Brock	Dentist
\.


--
-- Name: experiment_1_house_number_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.experiment_1_house_number_seq', 2, true);


--
-- Name: trial_and_error_name_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.trial_and_error_name_id_seq', 7, true);


--
-- Name: trial_and_error trial_and_error_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trial_and_error
    ADD CONSTRAINT trial_and_error_name_key UNIQUE (name);


--
-- PostgreSQL database dump complete
--

