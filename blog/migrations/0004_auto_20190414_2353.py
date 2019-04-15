# Generated by Django 2.2 on 2019-04-15 03:53

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190414_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='colegioadv',
            field=models.CharField(blank=True, choices=[('', 'Escoge un colegio...'), ('Arica', 'Colegio Adventista de Arica'), ('Iquique', 'Colegio Adventista de Iquique'), ('Calama', 'Colegio Adventista de Calama'), ('Antofagasta', 'Colegio Adventista de Antofagasta'), ('Copiapó', 'Colegio Adventista de Copiapó'), ('La Serena', 'Colegio Adventista de La Serena'), ('Quilpué', 'Colegio Adventista de Quilpué'), ('Buenaventura', 'Colegio Adventista de Buenaventura'), ('Porvenir', 'Colegio Adventista Porvenir'), ('La Cisterna', 'Colegio Adventista La Cisterna'), ('Las Condes', 'Colegio Adventista Las Condes'), ('Santiago Norte', 'Colegio Adventista Santiago Norte'), ('Santiago Sur', 'Colegio Adventista Santiago Sur'), ('Santiago Poniente', 'Colegio Adventista Santiago Poniente'), ('Molina', 'Colegio Adventista de Molina'), ('Talca', 'Colegio Adventista de Talca'), ('Chillan', 'Colegio Adventista de Chile'), ('Lota', 'Colegio Adventista de Lota'), ('Talcahuano Centro', 'Colegio Adventista Talcahuano Centro'), ('Talcahuano', 'Colegio Adventista de Talcahuano'), ('Concepción', 'Colegio Adventista de Concepción'), ('Los Angeles', 'Centro Educacional Adventista Los Angeles'), ('Angol', 'Colegio Adventista de Angol'), ('Temuco', 'Colegio Adventista de Temuco'), ('Pitrufquén', 'Colegio Adventista de Pitrufquén'), ('Villarrica', 'Colegio Adventista de Villarrica'), ('Valdivia', 'Colegio Adventista de Valdivia'), ('Punta Arenas', 'Colegio Adventista de Punta Arenas')], max_length=40),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='aniopost',
            field=models.CharField(choices=[('', 'Escoge un curso...'), ('PRIMERO', '1° medio'), ('SEGUNDO', '2° medio'), ('TERCERO', '3° medio'), ('CUARTO', '4° medio'), ('OTRO', 'Ya egresé')], max_length=15),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='carrera_post_1',
            field=models.CharField(choices=[('', 'Escoge una carrera...'), ('AGRO', 'Agronomía'), ('CON_AUD', 'Contador Auditor'), ('ED_PARV', 'Educación Parvularia'), ('ENF', 'Enfermería'), ('ING_COM', 'Ingeniería Comercial'), ('ING_INF', 'Ingeniería Informática'), ('ING_ELEC', 'Ingeniería en Electrónica y Telecomunicaciones'), ('ING_CIV_IND', 'Ingeniería Civil Industrial'), ('ING_CIV_INF', 'Ingeniería Civil Informática'), ('NUT', 'Nutrición y Dietética'), ('OBS', 'Obstetricia y Puericultura'), ('PED_BIO', 'Pedagogía en Biología'), ('PED_ED_DIF', 'Pedagogía en Educación Diferencial'), ('PED_ED_FIS', 'Pedagogía en Educación Física'), ('PED_ED_GEN_BAS', 'Pedagogía en Educación General Básica'), ('PED_HIS', 'Pedagogía en Historia y Geografia'), ('PED_ING', 'Pedagogía en Inglés'), ('PED_LENG', 'Pedagogía en Lengua Castellana y Comunicacion'), ('PED_MAT', 'Pedagogía en Matemática y Computacion'), ('PED_MUS', 'Pedagogía en Música'), ('PSICO', 'Psicología'), ('TEO', 'Teología'), ('TNS_ENF', 'TENS en Enfermería'), ('TRAB_SOC', 'Trabajo Social')], max_length=50),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='carrera_post_2',
            field=models.CharField(blank=True, choices=[('', 'Escoge una carrera...'), ('AGRO', 'Agronomía'), ('CON_AUD', 'Contador Auditor'), ('ED_PARV', 'Educación Parvularia'), ('ENF', 'Enfermería'), ('ING_COM', 'Ingeniería Comercial'), ('ING_INF', 'Ingeniería Informática'), ('ING_ELEC', 'Ingeniería en Electrónica y Telecomunicaciones'), ('ING_CIV_IND', 'Ingeniería Civil Industrial'), ('ING_CIV_INF', 'Ingeniería Civil Informática'), ('NUT', 'Nutrición y Dietética'), ('OBS', 'Obstetricia y Puericultura'), ('PED_BIO', 'Pedagogía en Biología'), ('PED_ED_DIF', 'Pedagogía en Educación Diferencial'), ('PED_ED_FIS', 'Pedagogía en Educación Física'), ('PED_ED_GEN_BAS', 'Pedagogía en Educación General Básica'), ('PED_HIS', 'Pedagogía en Historia y Geografia'), ('PED_ING', 'Pedagogía en Inglés'), ('PED_LENG', 'Pedagogía en Lengua Castellana y Comunicacion'), ('PED_MAT', 'Pedagogía en Matemática y Computacion'), ('PED_MUS', 'Pedagogía en Música'), ('PSICO', 'Psicología'), ('TEO', 'Teología'), ('TNS_ENF', 'TENS en Enfermería'), ('TRAB_SOC', 'Trabajo Social')], max_length=50),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='carrera_post_3',
            field=models.CharField(blank=True, choices=[('', 'Escoge una carrera...'), ('AGRO', 'Agronomía'), ('CON_AUD', 'Contador Auditor'), ('ED_PARV', 'Educación Parvularia'), ('ENF', 'Enfermería'), ('ING_COM', 'Ingeniería Comercial'), ('ING_INF', 'Ingeniería Informática'), ('ING_ELEC', 'Ingeniería en Electrónica y Telecomunicaciones'), ('ING_CIV_IND', 'Ingeniería Civil Industrial'), ('ING_CIV_INF', 'Ingeniería Civil Informática'), ('NUT', 'Nutrición y Dietética'), ('OBS', 'Obstetricia y Puericultura'), ('PED_BIO', 'Pedagogía en Biología'), ('PED_ED_DIF', 'Pedagogía en Educación Diferencial'), ('PED_ED_FIS', 'Pedagogía en Educación Física'), ('PED_ED_GEN_BAS', 'Pedagogía en Educación General Básica'), ('PED_HIS', 'Pedagogía en Historia y Geografia'), ('PED_ING', 'Pedagogía en Inglés'), ('PED_LENG', 'Pedagogía en Lengua Castellana y Comunicacion'), ('PED_MAT', 'Pedagogía en Matemática y Computacion'), ('PED_MUS', 'Pedagogía en Música'), ('PSICO', 'Psicología'), ('TEO', 'Teología'), ('TNS_ENF', 'TENS en Enfermería'), ('TRAB_SOC', 'Trabajo Social')], max_length=50),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='ciudad',
            field=models.CharField(choices=[('', 'Escoge una ciudad...'), ('Arica', 'Arica'), ('Iquique', 'Iquique'), ('Chillan', 'Chillán'), ('Santiago', 'Santiago'), ('Concepcion', 'Concepción'), ('Otra', 'Otra ciudad')], max_length=20),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='colegio',
            field=models.CharField(blank=True, choices=[('', 'Escoge un colegio...'), ('Colegio San Vicente de Paul', 'Colegio San Vicente de Paul'), ('Colegio Purísima Concepción', 'Colegio Purísima Concepción'), ('Colegio San Buenaventura', 'Colegio San Buenaventura'), ('Colegio San Esteban', 'Colegio San Esteban'), ('Colegio Chillán', 'Colegio Chillán'), ('Colegio Creación', 'Colegio Creación'), ('Liceo Bicentenario E.P.', 'Liceo Bicentenario E.P.'), ('Colegio Sagrado Corazón de J.', 'Colegio Sagrado Corazón de J.'), ('CESB-Colegio Tecnico Profesional P. Enrique', 'CESB-Colegio Tecnico Profesional P. Enrique'), ('Colegio Sydney College', 'Colegio Sydney College'), ('Colegio Tecnológico Darío Salas', 'Colegio Tecnológico Darío Salas'), ('Colegio Da Vinci', 'Colegio Da Vinci'), ('Colegio San Fernando', 'Colegio San Fernando'), ('Dinabec College', 'Dinabec College'), ('Colegio San Agustín', 'Colegio San Agustín'), ('C. Polivalente Padre A. Hurtado', 'C. Polivalente Padre A. Hurtado'), ('Colegio Alcázares de Ñuble', 'Colegio Alcázares de Ñuble'), ('Liceo Narciso Tondreau', 'Liceo Narciso Tondreau'), ('Liceo Diego Portales Palazuelos', 'Liceo Diego Portales Palazuelos'), ('Colegio Ciudad Educativa', 'Colegio Ciudad Educativa'), ('Liceo Bicentenario Marta Brunet', 'Liceo Bicentenario Marta Brunet'), ('Comewealth School', 'Comewealth School'), ('Colegio Francisco de Asis', 'Colegio Francisco de Asis'), ('Liceo Jorge Alessandri Rodríguez', 'Liceo Jorge Alessandri Rodríguez'), ('Liceo Polivalente Carlos Montane C.', 'Liceo Polivalente Carlos Montane C.'), ('Liceo Polivalente Juvenal Hernández Jaque', 'Liceo Polivalente Juvenal Hernández Jaque'), ('Colegio Coyam', 'Colegio Coyam'), ('INSUCO- Instituto Superior de Comercio Insuco', 'INSUCO- Instituto Superior de Comercio Insuco'), ('Liceo Arturo Prat Chacón', 'Liceo Arturo Prat Chacón'), ('Liceo Santa Cruz de Larqui', 'Liceo Santa Cruz de Larqui'), ('Liceo A-17 Yungay', 'Liceo A-17 Yungay'), ('Liceo Politécnico José Manuel P.', 'Liceo Politécnico José Manuel P.'), ('Liceo Técnico Puente Ñuble', 'Liceo Técnico Puente Ñuble'), ('Colegio Polivalente Darío Salas', 'Colegio Polivalente Darío Salas'), ('Liceo Agrícola de Chillán A-8', 'Liceo Agrícola de Chillán A-8'), ('Liceo Pueblo Seco', 'Liceo Pueblo Seco'), ('Liceo Politécnico C. Ignacio C.', 'Liceo Politécnico C. Ignacio C.'), ('Colegio Nuestra Señora del Carmen', 'Colegio Nuestra Señora del Carmen'), ('Liceo Claudio Arrau Leon', 'Liceo Claudio Arrau Leon'), ('Liceo Técnico Mabel Condemarín', 'Liceo Técnico Mabel Condemarín'), ('Colegio Altazor', 'Colegio Altazor'), ('Liceo Politécnico Yiré', 'Liceo Politécnico Yiré'), ('Colegio Hispanoamericano Río Viejo', 'Colegio Hispanoamericano Río Viejo'), ('Intech', 'Intech'), ('Colegio El Árbol de la Vida', 'Colegio El Árbol de la Vida'), ('Liceo República de Italia', 'Liceo República de Italia'), ('Centro de Estudios la Araucana', 'Centro de Estudios la Araucana'), ('Liceo Nuestra Señora de la Merced', 'Liceo Nuestra Señora de la Merced'), ('Sebastian School', 'Sebastian School'), ('Liceo Arturo Pacheco Altamirano', 'Liceo Arturo Pacheco Altamirano'), ('Colegio Concepción', 'Colegio Concepción'), ('Colegio Cholguán', 'Colegio Cholguán'), ('Instituto Santa María', 'Instituto Santa María'), ('Colegio Santa Teresa de los Andes', 'Colegio Santa Teresa de los Andes'), ('Colegio Seminario Padre Alberto Hurtado', 'Colegio Seminario Padre Alberto Hurtado')], max_length=40),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='nrofono',
            field=phonenumber_field.modelfields.PhoneNumberField(default='9', help_text='Los 8 dígitos luego del +56', max_length=128, region=None),
        ),
    ]
