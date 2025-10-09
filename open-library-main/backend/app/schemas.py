from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

class Token(BaseModel)
    access_token: str
    token_type: str = "bearer"


class TokenData(Basemodel):
    user_id : Optional[int] = None

class UserCreate(BaseMdoel):
    username: Optional[str] = None
    email: str
    password: str

class UserRead(BaseModel):
    id: int
    email: str
    username: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime


class FileRead(BaseModel):
    id: int
    title: Optional[str]
    original_filename: str
    stored_filename: str
    mime_type: str
    size_bytes: Optional[int]
    uploader_id: Optional[int]
    upload_date: datetime
    public: bool

class ChatRoomCreate(BaseModel):
    Title: str
    description: Optional[str] = None
    is_group: Optional[bool] = False
    member_ids: List[int]  # List of user IDs to be added to the chat room

class MessageCreate(BaseModel):
    content: str
    

class MessageRead(BaseModel):
    id: int
    room_id: int
    sender_id: int
    content: str
    timestamp: datetime
    read_by_ids: List[int] = []
    
    '''attachment_ids: List[int] = []
    reply_to_id: Optional[int] = None
    forwarded_from_id: Optional[int] = None
    edited: bool = False
    edited_at: Optional[datetime] = None
    deleted: bool = False
    deleted_at: Optional[datetime] = None
    reactions: Optional[dict] = {}
    mentions: List[int] = []
    tags: List[str] = []
    location: Optional[str] = None
    priority: Optional[int] = None
    scheduled_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    is_pinned: bool = False
    is_starred: bool = False
    is_important: bool = False
    is_private: bool = False
    is_broadcast: bool = False
    is_encrypted: bool = False
    is_system: bool = False
    is_ephemeral: bool = False
    is_silent: bool = False
    is_auto_deleted: bool = False
    is_highlighted: bool = False
    is_flagged: bool = False
    is_reported: bool = False
    is_archived: bool = False
    is_muted: bool = False
    is_blocked: bool = False
    is_followed: bool = False
    is_liked: bool = False
    is_shared: bool = False
    is_saved: bool = False
    is_published: bool = False
    is_draft: bool = False
    is_template: bool = False
    is_scheduled: bool = False
    is_recurring: bool = False'''