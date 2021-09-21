/* ######################################################### */
/* Authors:                                                  */
/* - Mirela Teixeira Cazzolato - mirelac@usp.br              */
/* - Lucas Santiago Rodrigues - lucas_rodrigues@usp.br       */
/* ######################################################### */


/* ######################################################### */
/* Comandos para ínserir carga                               */
/* ######################################################### */
COPY FAPESP.pacientes FROM 'D:\tmp\patients.csv' DELIMITER ';' CSV HEADER NULL '' ENCODING 'UTF-8'; 

COPY FAPESP.exames (id_paciente, id_atendimento, dt_coleta, de_origem, de_exame, de_analito, de_resultado, cd_unidade, de_valor_referencia, id_hospital)  FROM 'D:\tmp\exams-1.csv' DELIMITER ';' CSV HEADER  NULL '' ENCODING 'UTF8'; /* OK */
COPY FAPESP.exames (id_paciente, id_atendimento, dt_coleta, de_origem, de_exame, de_analito, de_resultado, cd_unidade, de_valor_referencia, id_hospital)  FROM 'D:\tmp\exams-2.csv' DELIMITER ';' CSV HEADER  NULL '' ENCODING 'UTF8'; /* OK */
COPY FAPESP.exames (id_paciente, id_atendimento, dt_coleta, de_origem, de_exame, de_analito, de_resultado, cd_unidade, de_valor_referencia, id_hospital)  FROM 'D:\tmp\exams-3.csv' DELIMITER ';' CSV HEADER  NULL '' ENCODING 'UTF8'; /* OK */
COPY FAPESP.exames (id_paciente, id_atendimento, dt_coleta, de_origem, de_exame, de_analito, de_resultado, cd_unidade, de_valor_referencia, id_hospital)  FROM 'D:\tmp\exams-4.csv' DELIMITER ';' CSV HEADER  NULL '' ENCODING 'UTF8'; /* OK */


COPY FAPESP.desfechos FROM 'D:\tmp\desfechos.csv'  DELIMITER ';' CSV HEADER  NULL '' ENCODING 'UTF8'; /* OK */


/* ################################################################# */
/* Comandos para padronizar termos em exames (DE_EXAME. DE_ANALITO)      */
/* ################################################################ */
UPDATE FAPESP.exames    -- in 5 min 28 secs
    SET DE_Exame=
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(DE_Exame, '.*', lower(DE_Exame))
           , '(atico|ático|actico|áctico)', 'ático', 'g')
           , '(erica)', 'érica', 'g')
           , '(urica)', 'úrica', 'g')
           , '(erico)', 'érico', 'g')
           , '(urico)', 'úrico', 'g')
           , '(anico)', 'ânico', 'g')
           , '(alico)', 'álico', 'g')
           , '(elico)', 'élico', 'g')
           , '(ilico)', 'ílico', 'g')
           , '(olico)', 'ólico', 'g')
           , '(onica)\M', 'ônica', 'g')
           , '(onico)', 'ônico', 'g')
           , '(proico)', 'próico', 'g')
           , '(virus)', 'vírus', 'g')
           , '(proteina)', 'proteína', 'g')
           , '(minio)', 'mínio', 'g')
           , '(monia)\M', 'mônia', 'g')
           , '(acteria)', 'actéria', 'g')
           , '(acido)', 'ácido', 'g')
           , '(rapid)', 'rápid', 'g'),
    DE_Analito=       
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(
       regexp_replace(DE_Exame, '.*', lower(DE_Exame))
           , '(atico|ático|actico|áctico)', 'ático', 'g')
           , '(erica)', 'érica', 'g')
           , '(urica)', 'úrica', 'g')
           , '(erico)', 'érico', 'g')
           , '(urico)', 'úrico', 'g')
           , '(anico)', 'ânico', 'g')
           , '(alico)', 'álico', 'g')
           , '(elico)', 'élico', 'g')
           , '(ilico)', 'ílico', 'g')
           , '(olico)', 'ólico', 'g')
           , '(onica)\M', 'ônica', 'g')
           , '(onico)', 'ônico', 'g')
           , '(proico)', 'próico', 'g')
           , '(virus)', 'vírus', 'g')
           , '(proteina)', 'proteína', 'g')
           , '(minio)', 'mínio', 'g')
           , '(monia)\M', 'mônia', 'g')
           , '(acteria)', 'actéria', 'g')
           , '(acido)', 'ácido', 'g')
           , '(rapid)', 'rápid', 'g');


/* ######################################################### */
/* Comandos para recuperar estatisticas de inserts           */
/* ######################################################### */
SELECT 'pacientes',COUNT(*) FROM FAPESP.pacientes AS p
UNION ALL
SELECT 'exames'   ,COUNT(*) FROM FAPESP.exames    AS ex
UNION ALL
SELECT 'desfechos',COUNT(*) FROM FAPESP.desfechos AS at;

/* ######################################################### */
/* Comandos para criar indices em exames                     */
/* Execution time -- 1 min 57 secs.                          */
/* ######################################################### */

CREATE INDEX deExamIndex ON FAPESP.exames (de_exame);
CREATE INDEX deAnalitoIndex ON FAPESP.exames (de_analito);
CREATE INDEX deExamAnalitoIndex ON FAPESP.exames (de_exame, de_analito);
