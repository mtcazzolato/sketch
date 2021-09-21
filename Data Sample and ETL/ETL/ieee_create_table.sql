/* ######################################################### */
/* Authors:                                                  */
/* - Mirela Teixeira Cazzolato - mirelac@usp.br              */
/* - Lucas Santiago Rodrigues - lucas_rodrigues@usp.br       */
/* ######################################################### */

/* ######################################################### */
/* Comando para criar o esquema IEEE                         */
/* ######################################################### */
CREATE SCHEMA IEEE;

/* ######################################################### */
/* Comandos para ínserir todas as tabelas                    */
/* ######################################################### */
DROP TABLE IF EXISTS IEEE.casesCovid;

CREATE TABLE IEEE.casesCovid
(
patientid 					TEXT, 
offset_at    			 	NUMERIC, 
sex							CHAR, 
age							NUMERIC,
finding						TEXT,
RT_PCR_positive				TEXT,
survival					CHAR,
intubated					CHAR, 
intubation_present			CHAR,
went_icu					CHAR,
in_icu						TEXT,
needed_supplemental_O2		CHAR,
extubated					CHAR,
temperature					NUMERIC,
pO2_saturation				NUMERIC,
leukocyte_count				NUMERIC,
neutrophil_count			NUMERIC, 
lymphocyte_count			NUMERIC,
view						TEXT,
modality					TEXT, 
date_exam					TEXT, 
location					TEXT,
clinical_notes				TEXT,
other_notes					TEXT,
NCH32 						NUMERIC[],
NCH128 						NUMERIC[],
TS 							NUMERIC[],
NCH256						NUMERIC[],
EH							NUMERIC[],
TCH 						NUMERIC[],
SC							NUMERIC[],
BIC							NUMERIC[],
MH							NUMERIC[],
NCH8 						NUMERIC[],
CT 							NUMERIC[], 
CS 							NUMERIC[],
CL 							NUMERIC[],
LBP							NUMERIC[],
NCH16 						NUMERIC[],
Hr							NUMERIC[],
NCH64						NUMERIC[]
);
