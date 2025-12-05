import os
import sys
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging

from network_security.components.data_ingestion import DataIngestion
from network_security.components.data_validation import DataValidation
from network_security.components.data_transformation import DataTransformation
from network_security.components.model_trainer import ModelTrainer
from network_security.entity.config_entity import(
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
)
from network_security.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact,
)


class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self):
        try:
            self.dataIngestionConfig = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Start data Ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.dataIngestionConfig)
            dataIngestionArtifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data Ingestion completed and artifact: {dataIngestionArtifact}")
            return dataIngestionArtifact        
        except Exception as e:
            raise NetworkSecurityException(e,sys)       
        
    def start_data_validation(self,dataIngestionArtifact:DataIngestionArtifact):
        try:
            dataValidationConfig = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_ingestion_artifact=dataIngestionArtifact,data_validation_config=dataValidationConfig)
            logging.info("Initiate the data Validation")
            dataValidationArtifact = data_validation.initiate_data_validation()
            logging.info("Data Validation Completed")
            return dataValidationArtifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_data_transformation(self,dataValidationArtifact:DataValidationArtifact):
        try:
            dataTransformationConfig = DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            data_transformation = DataTransformation(data_validation_artifact=dataValidationArtifact,data_transformation_config=dataTransformationConfig)
            logging.info("Data Transformation Started")
            dataTransformationArtifact = data_transformation.initiate_data_transformation()
            logging.info("Data Transformation Completed")
            return dataTransformationArtifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_model_trainer(self,dataTransformationArtifact:DataTransformationArtifact)->ModelTrainerArtifact:
        try:
            self.modelTrainerConfig: ModelTrainerConfig = ModelTrainerConfig(training_pipeline_config=self.training_pipeline_config)
            model_trainer = ModelTrainer(data_transformation_artifact=dataTransformationArtifact,model_trainer_config=self.modelTrainerConfig)
            logging.info("Model Training Stared")
            modelTrainerArtifact = model_trainer.initiate_model_trainer()
            logging.info("Model Training artifact created")
            return modelTrainerArtifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def run_pipeline(self):
        try:
            logging.info("Pipeline Started")
            dataIngestionArtifact=self.start_data_ingestion()
            dataValidationArtifact=self.start_data_validation(dataIngestionArtifact=dataIngestionArtifact)
            dataTransformationArtifact=self.start_data_transformation(dataValidationArtifact=dataValidationArtifact)
            modelTrainerArtifact=self.start_model_trainer(dataTransformationArtifact=dataTransformationArtifact)
            logging.info("Pipeline Completed")
            return modelTrainerArtifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)