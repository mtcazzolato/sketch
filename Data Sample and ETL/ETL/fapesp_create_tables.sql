/* ######################################################### */
/* Authors:                                                  */
/* - Mirela Teixeira Cazzolato - mirelac@usp.br              */
/* - Lucas Santiago Rodrigues - lucas_rodrigues@usp.br       */
/* ######################################################### */


/* ######################################################### */
/* Comando para criar esquema FAPESP-COVID                   */
/* ######################################################### */
CREATE SCHEMA FAPESP;


/* ######################################################### */
/* Comandos para ínserir todas as tabelas                    */
/* ######################################################### */
DROP TABLE IF EXISTS FAPESP.pacientes CASCADE;
CREATE TABLE FAPESP.pacientes
(
id_paciente           TEXT PRIMARY KEY,
ic_sexo               CHAR,
aa_nascimento         INTEGER, 
cd_pais               TEXT,
cd_uf                 CHAR(2),
cd_municipio          TEXT,
cd_cepreduzido        TEXT,
id_hospital           INTEGER 
);

DROP TABLE IF EXISTS FAPESP.exames CASCADE;
CREATE TABLE FAPESP.exames 
(
id_exame            SERIAL PRIMARY KEY ,
id_paciente         TEXT,
id_atendimento      TEXT,
dt_coleta           DATE,
de_origem           TEXT,
de_exame            TEXT,
de_analito          TEXT,
de_resultado        TEXT,
cd_unidade          TEXT,
de_valor_referencia TEXT,
id_hospital         INTEGER,
  
FOREIGN KEY (id_paciente) 
    REFERENCES FAPESP.pacientes(id_paciente) 
    ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS desfechos CASCADE;
CREATE TABLE FAPESP.desfechos
(
id_paciente             TEXT,
id_atendimento          TEXT,
dt_atendimento          DATE,
de_tipo_atendimento     TEXT,
id_clinica              INTEGER,
de_clinica              TEXT,
dt_desfecho             DATE,
de_desfecho             TEXT,
id_hospital             INTEGER,


PRIMARY KEY (id_paciente, id_atendimento),

FOREIGN KEY (id_paciente) 
    REFERENCES FAPESP.pacientes(id_paciente)
    ON UPDATE CASCADE ON DELETE CASCADE

);

/* REFERENCES ID_HOSPITAL

id_hospital = {0 : 'EINSTEINAgosto',
               1 : 'GrupoFleury_Janeiro2021',
               2 : 'HC_Janeiro2021',
               3 : 'HSL_Janeiro2021',
               4 : 'BPSP'}
*/


/* ######################################################### */
/* Comandos para inserir comentarios em cada atributo        */
/* ######################################################### */

COMMENT ON TABLE FAPESP.pacientes IS 'Tabela de pacientes Covid-19 FAPESP';
COMMENT ON COLUMN FAPESP.pacientes.ID_Paciente         IS 'Identificação única do paciente (correlaciona com o ID_PACIENTE de todos os arquivos onde aparece). 32 caracteres alfanuméricos';
COMMENT ON COLUMN FAPESP.pacientes.IC_Sexo             IS 'Sexo do Paciente. 1 caracter alfanumérico. F - Feminino; M - Masculino';
COMMENT ON COLUMN FAPESP.pacientes.AA_Nascimento       IS E'Ano de nascimento do Paciente. 4 caracteres alfanuméricos.\n Os 4 dígitos do ano do nascimento; ou\n AAAA - para ano de nascimento igual ou anterior a 1930 (visando anonimização);\n YYYY - quaisquer outros anos, em caso de anonimização do ano';
COMMENT ON COLUMN FAPESP.pacientes.CD_Pais             IS 'Pais de residencia do Paciente. 2 caracteres alfanuméricos. BR ou XX (país estrangeiro)';
COMMENT ON COLUMN FAPESP.pacientes.CD_UF               IS E'Unidade da Federacao de residencia do Paciente. 2 caracteres alfanumérico\n AC - Acre, AL - Alagoas, AM - Amazonas, AP - Amapá, BA - Bahia, CE - Ceará, DF - Distrito Federal, ES - Espírito Santo, GO - Goiás, MA - Maranhão, MG - Minas Gerais, MS - Mato Grosso do Sul, MT - Mato Grosso, PA - Pará, PB - Paraíba, PE - Pernambuco, PI - Piauí, PR - Paraná, RJ - Rio de Janeiro, RN - Rio Grande do Norte, RO - Rondônia, RR - Roraima, RS - Rio Grande do Sul, SC - Santa Catarina, SE - Sergipe, SP - São Paulo, TO - Tocantins, UU -  quando houver necessidade de  anonimização/estrangeiro';
COMMENT ON COLUMN FAPESP.pacientes.CD_Municipio        IS E'Municipio de residencia do Paciente. Alfanumérico.\n Nome do município por extenso,\n ou MMMM - quando houver necessidade de  anonimização ou estrangeiro';
COMMENT ON COLUMN FAPESP.pacientes.CD_CepReduzido      IS E'CEP parcial da residencia do Paciente. 5 caracteres alfanuméricos. Os primeiros cinco dígitos do CEP (Código de Endereçamento Postal Brasileiro).\n CCCC - quando houver necessidade de  anonimização ou estrangeiro';
COMMENT ON COLUMN FAPESP.pacientes.id_hospital         IS E'Identificação númerica do hospital 0 : EINSTEINAgosto,1 : GrupoFleury_Janeiro2021,2 : HC_Janeiro2021,3 : HSL_Janeiro2021,4 : BPSP';

COMMENT ON TABLE FAPESP.exames                         IS 'Tabela de exames Covid-19 FAPESP';
COMMENT ON COLUMN FAPESP.exames.ID_Paciente            IS 'Identificação única do paciente (correlaciona com o ID_PACIENTE de todos os arquivos onde aparece). 32 caracteres alfanuméricos';
COMMENT ON COLUMN FAPESP.exames.ID_Atendimento         IS 'Identificação única do atendimento. Correlaciona com o ID_ATENDIMENTO de todas as tabelas onde aparece. 32 caracteres alfanuméricos';
COMMENT ON COLUMN FAPESP.exames.DT_Coleta              IS 'Data em que o material foi coletado do paciente (DD/MM/AAAA)';
COMMENT ON COLUMN FAPESP.exames.DE_Origem              IS E'Local de Coleta do exame. 4 caracteres alfanuméricos:\n  LAB – Exame realizado por paciente em uma  unidade de atendimento laboratorial;\n  HOSP – Exame realizado por paciente dentro de uma Unidade Hospitalar;\n  UTI - exame realizado na UTI';
COMMENT ON COLUMN FAPESP.exames.DE_Exame               IS E'Descrição do exame realizado. Alfanumérico.\n  Exemplo: HEMOGRAMA, sangue total / GLICOSE, plasma / SODIO, soro / POTASSIO, soro.\n Um exame é composto por 1 ou mais analitos.';
COMMENT ON COLUMN FAPESP.exames.DE_Analito             IS E'Descrição do analito. Alfanumérico. Exemplo: Eritrócitos / Leucócitos / Glicose / Ureia / Creatinina.\n Para o exame Hemograma, tem o resultado de vários analitos: Eritrócitos, Hemoglobina, Leucócitos, Linfócitos, etc.\n A maioria dos exames tem somente 1 analito, por exemplo  Glicose, Colesterol Total, Uréia e Creatinina.';
COMMENT ON COLUMN FAPESP.exames.DE_Resultado           IS E'Resultado do exame, associado ao DE_ANALITO. Alfanumérico. Se DE_ANALITO exige valor numérico, NNNN se inteiro ou NNNN,NNN se casas decimais;\n  Se DE_ANALITO exige qualitativo, String com domínio restrito;\n  Se DE_ANALITO por observação microscópica, String conteúdo livre.\n Exemplo de dominio restrito - Positivo, Detectado, Reagente, nâo reagente, etc.\n Exemplo de conteúdo livre - ''não foram observados caracteres tóxico-degenerativos nos neutrófilos, não foram observadas atipias linfocitárias''';
COMMENT ON COLUMN FAPESP.exames.CD_Unidade             IS E'Unidade de Medida utilizada na Metodologia do laboratório específico para analisar o exame. Alfanumérico. \n Exemplo: g/dL (gramas por decilitro)';
COMMENT ON COLUMN FAPESP.exames.DE_Valor_Referencia    IS E'Faixa de valores de referência. Alfanumérico. Resultado ou faixa de resultados considerado normal para este analito.\n  Exemplo para Glicose: 75 a 99';
COMMENT ON COLUMN FAPESP.exames.id_hospital         IS E'Identificação númerica do hospital 0 : EINSTEINAgosto,1 : GrupoFleury_Janeiro2021,2 : HC_Janeiro2021,3 : HSL_Janeiro2021,4 : BPSP';


COMMENT ON TABLE FAPESP.desfechos                      IS E'Tabela de desfechos  Covid-19 FAPESP\n (só tem dados do Hospital São Luiz)';
COMMENT ON COLUMN FAPESP.desfechos.ID_Paciente         IS 'Identificação única do paciente (correlaciona com o ID_PACIENTE de todos os arquivos onde aparece. 32 caracteres alfanuméricos)';
COMMENT ON COLUMN FAPESP.desfechos.ID_Atendimento      IS 'Identificação única do atendimento. Cada atendimento tem um desfecho. Correlaciona com ID_ATENDIMENTO de todas as tabelas onde aparece';
COMMENT ON COLUMN FAPESP.desfechos.DT_Atendimento      IS 'Data de realização do atendimento - (DD/MM/AAAA)';
COMMENT ON COLUMN FAPESP.desfechos.DE_Tipo_Atendimento IS 'Descrição do tipo de atendimento realizado. Texto livre. Exemplo: Pronto atendimento.';
COMMENT ON COLUMN FAPESP.desfechos.ID_Clinica          IS 'Identificação da clínica onde o evento aconteceu. Numérico. Exemplo: 1013';
COMMENT ON COLUMN FAPESP.desfechos.DE_Clinica          IS 'Descrição da clínica onde o evento aconteceu. Texto livre. Exemplo: Cardiologia';
COMMENT ON COLUMN FAPESP.desfechos.DT_Desfecho         IS 'Data do desfecho - (DD/MM/YYYY) ou string DDMMAA se DE_DESFECHO for óbito';
COMMENT ON COLUMN FAPESP.desfechos.DE_Desfecho         IS 'Descriçao do desfecho. Texto livre. Exemplo: Alta médica melhorado';
COMMENT ON COLUMN FAPESP.desfechos.id_hospital         IS E'Identificação númerica do hospital 0 : EINSTEINAgosto,1 : GrupoFleury_Janeiro2021,2 : HC_Janeiro2021,3 : HSL_Janeiro2021,4 : BPSP';


