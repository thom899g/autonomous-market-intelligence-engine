from typing import Dict, Any

class ConfigurationManager:
    def __init__(self):
        self.config = {
            'max_allowed_risk': 0.3,
            'quantum_instance_name': 'primary',
            'ai_model_version': 'v1'
        }
        
    def get(self, key: str) -> Any:
        """
        Retrieves a configuration value.
        
        Args:
            key: Configuration key
            
        Returns:
            Value of the configuration key
        """
        return self.config.get(key)

    def set(self, key: str, value: Any) -> None:
        """
        Sets a configuration value.
        
        Args:
            key: Configuration key
            value: Value to set
        """
        self.config[key] = value

    def update(self, new_config: Dict[str, Any]) -> None:
        """
        Updates multiple configuration values.
        
        Args:
            new_config: Dictionary of new configuration values
        """
        self.config.update(new_config)