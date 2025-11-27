from network_security.components.data_ingestion import DataIngestion
from network_security.components.data_validation import DataValidation
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.entity.config_entity import DataIngestionConfig, DataValidationConfig
from network_security.entity.config_entity import TrainingPipelineConfig
import sys


if __name__=='__main__':
    try:
        trainingPipelineConfig = TrainingPipelineConfig()
        dataIngestionConfig = DataIngestionConfig(trainingPipelineConfig)
        data_ingestion = DataIngestion(dataIngestionConfig)
        logging.info("Initiate the data ingestion")
        dataIngestionArtifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataIngestionArtifact)

        dataValidationConfig = DataValidationConfig(trainingPipelineConfig)
        data_validation = DataValidation(dataIngestionArtifact,dataValidationConfig)
        logging.info("Initiate the data Validation")
        dataValidationArtifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(dataValidationArtifact)

    except Exception as e:
           raise NetworkSecurityException(e,sys)