from dotenv import load_dotenv
from pydantic import BaseSettings, Field
from typing import List, Optional

load_dotenv()

class Settings(BaseSettings):
    # Basic app config
    PROJECT_NAME: str = Field("Open Library", env="PROJECT_NAME")


    # B used env parsing; keep as bool with sensible defaults
    DEBUG: bool = Field(True, decription="Enable Debug (use False in Prod)", env="DEBUG")
    TESTING: bool = Field(False, description="Enable Testing", env="TESTING")

    #JWT config -TODO change defaults
    SECRET_KEY: str = Field(...,env = "SECRET_KEY", description="Secret key for JWT")
    ALGORITHM: str = Field("HS256", env="ALGORITHM", description="Algorithm for JWT")
    
    # access token expiry time in minutes
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(
        60*24*8, # 8 days
        env="ACCESS_TOKEN_EXPIRE_MINUTES",
        description="Access token expiry time in minutes"
    )
    # refresh token expiry time in minutes
    REFRESH_TOKEN_EXPIRE_MINUTES: int = Field(
        60*24*30, # 30 days
        env="REFRESH_TOKEN_EXPIRE_MINUTES",
        description="Refresh token expiry time in minutes"
    )

    #DATABASE URL
    #B Used simple os.getenv; using pydantic Field + env ensures validation and type safety
    DATABASE_URL: str = Field(..., env="DATABASE_URL", description="Database URL")
    #Keep DB test but keep it optional
    TEST_DATABASE_URL: Optional[str] = Field(None, env="TEST_DATABASE_URL", description="Test Database URL")


    # Upload config
    UPLOAD_DIR: str = Field("data/uploads", env="UPLOAD_DIR", description="Upload directory")
    
    # allowed file extensions for later use
    '''ALLOWED_FILE_EXTENSIONS: List[str] = Field(
        default=[".pdf", ".epub", ".mobi", ".azw3", ".txt"],
        env="ALLOWED_FILE_EXTENSIONS",
        description="Allowed file extensions for uploads"
    )
    '''
    #MAX_FILE_SIZE_MB: int = Field(100, env="MAX_FILE_SIZE_MB", description="Max file size for uploads in MB")
    MAX_FILE_SIZE_BYTES: int = Field(30*1024*1024, env="MAX_FILE_SIZE_BYTES", description="Max file size for uploads in bytes")

    #CORS origins

    BACKEND_CORS_ORIGINS: List[str] = Field(
        deafult_facctory=lambda: ["*"],
        env="BACKEND_CORS_ORIGINS",
        description="Allowed CORS origins, comma separated"
    )
    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"
#add validation methods if needed make sure UPLOAD_DIR exists, etc.

settings = Settings()