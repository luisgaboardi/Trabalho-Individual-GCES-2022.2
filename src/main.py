import json
import os

from parser.YAML_parser import YAMLParser
from parser.feature_engineering_parser import FeatureEngineeringParser
from parser.model_parser import ModelParser

if __name__ != "__main__":
    exit()   

def get_config():
    initialParser = YAMLParser
    featureEngineringParser = FeatureEngineeringParser
    modelParser = ModelParser

    for file in os.listdir('src/yamls'):
        filepath = os.path.join('src/yamls', file)
        config = initialParser(filepath).parse()
    
        features_configs, columns_set_alias = featureEngineringParser(filepath).parse(config['feature_engineering'])
        del config['feature_engineering']
        json_features_config = json.dumps(json.loads(features_configs), indent=2)
        
        model_configs = modelParser(columns_set_alias).parse(config['model'])
        del config['model']
        json_model_configs = json.dumps(json.loads(model_configs), indent=2)

        
        print("FEATURES")
        print(json_features_config)
        print(2*'\n')
        print(20*'-')
        print(2*'\n')
        print(json_model_configs)
         
get_config()
