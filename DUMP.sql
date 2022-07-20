PGDMP     ;    2                z            tarea3    14.4    14.4                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    33564    tarea3    DATABASE     b   CREATE DATABASE tarea3 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Chile.1252';
    DROP DATABASE tarea3;
                postgres    false            �            1259    33566 	   canciones    TABLE     �   CREATE TABLE public.canciones (
    id_cancion integer NOT NULL,
    nombre character varying NOT NULL,
    letra character varying,
    fecha_composicion date
);
    DROP TABLE public.canciones;
       public         heap    postgres    false            �            1259    33565    canciones_id_cancion_seq    SEQUENCE     �   CREATE SEQUENCE public.canciones_id_cancion_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.canciones_id_cancion_seq;
       public          postgres    false    210                       0    0    canciones_id_cancion_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.canciones_id_cancion_seq OWNED BY public.canciones.id_cancion;
          public          postgres    false    209            �            1259    33597    facturas    TABLE       CREATE TABLE public.facturas (
    id_factura integer NOT NULL,
    monto_facturado integer,
    fecha_facturacion date,
    fecha_vencimiento date,
    estado boolean,
    metodo_de_pago character varying(100),
    fecha_hora_pago timestamp without time zone,
    id_usuario integer
);
    DROP TABLE public.facturas;
       public         heap    postgres    false            �            1259    33596    facturas_id_factura_seq    SEQUENCE     �   CREATE SEQUENCE public.facturas_id_factura_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.facturas_id_factura_seq;
       public          postgres    false    215                       0    0    facturas_id_factura_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.facturas_id_factura_seq OWNED BY public.facturas.id_factura;
          public          postgres    false    214            �            1259    33575    personas    TABLE     �  CREATE TABLE public.personas (
    id_usuario integer NOT NULL,
    nombre character varying(100) NOT NULL,
    apellido character varying(80),
    email character varying(100) NOT NULL,
    password character varying(100) NOT NULL,
    usuario_suscripcion_activa boolean,
    artista_nombre_artistico character varying(100),
    artista_verificado boolean,
    tipo_de_persona boolean NOT NULL
);
    DROP TABLE public.personas;
       public         heap    postgres    false            �            1259    33574    personas_id_usuario_seq    SEQUENCE     �   CREATE SEQUENCE public.personas_id_usuario_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.personas_id_usuario_seq;
       public          postgres    false    212                       0    0    personas_id_usuario_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.personas_id_usuario_seq OWNED BY public.personas.id_usuario;
          public          postgres    false    211            �            1259    33581    reproducciones    TABLE     �   CREATE TABLE public.reproducciones (
    id_cancion integer NOT NULL,
    id_usuario integer NOT NULL,
    cantidad_reproducciones integer,
    ultima_reproduccion timestamp without time zone
);
 "   DROP TABLE public.reproducciones;
       public         heap    postgres    false            j           2604    33569    canciones id_cancion    DEFAULT     |   ALTER TABLE ONLY public.canciones ALTER COLUMN id_cancion SET DEFAULT nextval('public.canciones_id_cancion_seq'::regclass);
 C   ALTER TABLE public.canciones ALTER COLUMN id_cancion DROP DEFAULT;
       public          postgres    false    209    210    210            l           2604    33600    facturas id_factura    DEFAULT     z   ALTER TABLE ONLY public.facturas ALTER COLUMN id_factura SET DEFAULT nextval('public.facturas_id_factura_seq'::regclass);
 B   ALTER TABLE public.facturas ALTER COLUMN id_factura DROP DEFAULT;
       public          postgres    false    215    214    215            k           2604    33578    personas id_usuario    DEFAULT     z   ALTER TABLE ONLY public.personas ALTER COLUMN id_usuario SET DEFAULT nextval('public.personas_id_usuario_seq'::regclass);
 B   ALTER TABLE public.personas ALTER COLUMN id_usuario DROP DEFAULT;
       public          postgres    false    211    212    212                      0    33566 	   canciones 
   TABLE DATA           Q   COPY public.canciones (id_cancion, nombre, letra, fecha_composicion) FROM stdin;
    public          postgres    false    210   �%       	          0    33597    facturas 
   TABLE DATA           �   COPY public.facturas (id_factura, monto_facturado, fecha_facturacion, fecha_vencimiento, estado, metodo_de_pago, fecha_hora_pago, id_usuario) FROM stdin;
    public          postgres    false    215   �&                 0    33575    personas 
   TABLE DATA           �   COPY public.personas (id_usuario, nombre, apellido, email, password, usuario_suscripcion_activa, artista_nombre_artistico, artista_verificado, tipo_de_persona) FROM stdin;
    public          postgres    false    212   �'                 0    33581    reproducciones 
   TABLE DATA           n   COPY public.reproducciones (id_cancion, id_usuario, cantidad_reproducciones, ultima_reproduccion) FROM stdin;
    public          postgres    false    213   �(                  0    0    canciones_id_cancion_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.canciones_id_cancion_seq', 15, true);
          public          postgres    false    209                       0    0    facturas_id_factura_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.facturas_id_factura_seq', 10, true);
          public          postgres    false    214                       0    0    personas_id_usuario_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.personas_id_usuario_seq', 9, true);
          public          postgres    false    211            n           2606    33573    canciones canciones_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.canciones
    ADD CONSTRAINT canciones_pkey PRIMARY KEY (id_cancion);
 B   ALTER TABLE ONLY public.canciones DROP CONSTRAINT canciones_pkey;
       public            postgres    false    210            t           2606    33602    facturas facturas_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.facturas
    ADD CONSTRAINT facturas_pkey PRIMARY KEY (id_factura);
 @   ALTER TABLE ONLY public.facturas DROP CONSTRAINT facturas_pkey;
       public            postgres    false    215            p           2606    33580    personas personas_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.personas
    ADD CONSTRAINT personas_pkey PRIMARY KEY (id_usuario);
 @   ALTER TABLE ONLY public.personas DROP CONSTRAINT personas_pkey;
       public            postgres    false    212            r           2606    33585 "   reproducciones reproducciones_pkey 
   CONSTRAINT     t   ALTER TABLE ONLY public.reproducciones
    ADD CONSTRAINT reproducciones_pkey PRIMARY KEY (id_cancion, id_usuario);
 L   ALTER TABLE ONLY public.reproducciones DROP CONSTRAINT reproducciones_pkey;
       public            postgres    false    213    213            w           2606    33603 !   facturas facturas_id_usuario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.facturas
    ADD CONSTRAINT facturas_id_usuario_fkey FOREIGN KEY (id_usuario) REFERENCES public.personas(id_usuario);
 K   ALTER TABLE ONLY public.facturas DROP CONSTRAINT facturas_id_usuario_fkey;
       public          postgres    false    212    3184    215            u           2606    33586 -   reproducciones reproducciones_id_cancion_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.reproducciones
    ADD CONSTRAINT reproducciones_id_cancion_fkey FOREIGN KEY (id_cancion) REFERENCES public.canciones(id_cancion);
 W   ALTER TABLE ONLY public.reproducciones DROP CONSTRAINT reproducciones_id_cancion_fkey;
       public          postgres    false    213    3182    210            v           2606    33591 -   reproducciones reproducciones_id_usuario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.reproducciones
    ADD CONSTRAINT reproducciones_id_usuario_fkey FOREIGN KEY (id_usuario) REFERENCES public.personas(id_usuario);
 W   ALTER TABLE ONLY public.reproducciones DROP CONSTRAINT reproducciones_id_usuario_fkey;
       public          postgres    false    213    212    3184                 x����j�0E�㯘��H���!�U
����I��"~���~}��I[H�fg8W ��\An]	�)�DA��+������V-���-z�9�c]�\�i�!()� )��Ζ��❫�<�vøI��F(
}�~��Ɩ��j־a<ٯ>QO�	L�DuA@ZMjR��\Cr�t[)�ٌV]ǑV�ir��_ߑ�ꯋ�y<����@Ó�2k�n�����<��^�؀���4K��x�4@�<nV��r{�_� �Z`�?      	   �   x���A
�@�ur�^�%�$ө�z�n*��n�2��V�����_|��6"!��ښݫ:��a��4TǸ�rM��Ԋ��0
��pԼ�Nm�L�7�����j�{��(���RS)IA�7i�fɡ�"���W
xn���Q         �   x�e��J�0��ӧ�'�n]��Y]
����m�M3���o�4� �&�7����}#0]��Y�E�6�U�͞;�)�H�j1��}Q�	~6��̈́`A�4� �rO�eFB�	����Ɋ�kr�#aD�-u�!���L:��N���̕�T�*�R�>L ���F����!f����k���:^�/���t����;�����Y���^_8Ĥ�ٺ�[���{:��95v=��F�:�ޯv��y�:�1osVEQ��8y�         ~   x�}һ�0К�"8�G$�̒����.t�=�t �d䤬zp2_̟�N��AvST�t��J�V�T�tbn-K�$�ƴ1ö:
��eP�Ƥ�	4oLj���NT�&WWr!�����c� �|n�     