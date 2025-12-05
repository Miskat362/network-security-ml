from network_security.components.data_ingestion import DataIngestion
from network_security.components.data_validation import DataValidation
from network_security.components.data_transformation import DataTransformation
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from network_security.entity.config_entity import TrainingPipelineConfig
from network_security.components.model_trainer import ModelTrainer
from network_security.entity.config_entity import ModelTrainerConfig
import sys


if __name__=='__main__':
    try:
        trainingPipelineConfig = TrainingPipelineConfig()
        dataIngestionConfig = DataIngestionConfig(trainingPipelineConfig)
        data_ingestion = DataIngestion(dataIngestionConfig)
        logging.info("Initiate the data Ingestion")
        dataIngestionArtifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataIngestionArtifact)

        dataValidationConfig = DataValidationConfig(trainingPipelineConfig)
        data_validation = DataValidation(dataIngestionArtifact,dataValidationConfig)
        logging.info("Initiate the data Validation")
        dataValidationArtifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(dataValidationArtifact)

        dataTransformationConfig = DataTransformationConfig(trainingPipelineConfig)
        data_transformation = DataTransformation(dataValidationArtifact,dataTransformationConfig)
        logging.info("Data Transformation Started")
        dataTransformationArtifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation Completed")
        print(dataTransformationArtifact)

        logging.info("Model Training Stared")
        modelTrainerConfig = ModelTrainerConfig(trainingPipelineConfig)
        model_trainer = ModelTrainer(model_trainer_config=modelTrainerConfig,data_transformation_artifact=dataTransformationArtifact)
        modelTrainerArtifact = model_trainer.initiate_model_trainer()
        logging.info("Model Training artifact created")

    except Exception as e:
           raise NetworkSecurityException(e,sys)