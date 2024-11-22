import mysql.connector
import socket
from datetime import datetime, timedelta
import secrets
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class DatabaseConnection:
    def __init__(self):
        self.conn = None
        self.SECRET_KEY = secrets.token_hex(32)
        logger.info("DatabaseConnection initialized with ed25519 authentication")

    def connect(self):
        """Establish database connection if not already connected."""
        try:
            if not self.conn or not self.conn.is_connected():
                self.conn = mysql.connector.connect(
                    host='73.171.45.18',
                    user='remote_user',
                    password='sqlhokies',
                    database='wildlife_call_database',
                    auth_plugin='client_ed25519'
                )
                logger.info("Database connection established with ed25519 authentication")
            return self.conn
        except Exception as e:
            logger.error(f"Database connection error: {str(e)}")
            raise

    def get_cursor(self):
        """Get a prepared cursor for database operations."""
        try:
            return self.connect().cursor(prepared=True)
        except Exception as e:
            logger.error(f"Error getting cursor: {str(e)}")
            raise

    def verify_user_credentials(self, username: str, password: str) -> tuple:
        """Verify user credentials using ed25519."""
        cursor = self.get_cursor()
        try:
            # Get user information
            cursor.execute("""
                SELECT 'user' as type, user_id as id, is_certified 
                FROM User WHERE username = %s
                UNION
                SELECT 'admin' as type, admin_id as id, 1 as is_certified 
                FROM Admin WHERE username = %s
            """, (username, username))
            
            result = cursor.fetchone()
            
            if not result:
                logger.warning(f"No user found: {username}")
                return False, "Invalid username or password", None

            # Verify password using ed25519
            cursor.execute("SELECT ed25519_password(%s) = password FROM User WHERE username = %s", 
                         (password, username))
            is_valid = cursor.fetchone()
            
            if is_valid and is_valid[0]:
                logger.info(f"Successful login: {username}")
                return True, "Login successful", result
            else:
                logger.warning(f"Invalid password for user: {username}")
                return False, "Invalid username or password", None

        except Exception as e:
            logger.error(f"Login verification error: {str(e)}")
            return False, f"Login error: {str(e)}", None
        finally:
            cursor.close()

    def create_session(self, user_id: int, user_type: str) -> str:
        """Create a new session for a user."""
        cursor = self.get_cursor()
        try:
            session_id = secrets.token_hex(32)
            ip_address = socket.gethostbyname(socket.gethostname())
            expiry_time = datetime.now() + timedelta(hours=24)
            
            cursor.execute("""
                INSERT INTO Sessions (session_id, user_id, user_type, expiry_time, ip_address)
                VALUES (%s, %s, %s, %s, %s)
            """, (session_id, user_id, user_type, expiry_time, ip_address))
            
            self.conn.commit()
            logger.info(f"Created session for user {user_id}")
            return session_id
        except Exception as e:
            logger.error(f"Session creation error: {str(e)}")
            raise
        finally:
            cursor.close()

    def verify_session(self, session_id: str) -> tuple:
        """Verify if a session is valid and not expired."""
        cursor = self.get_cursor()
        try:
            cursor.execute("""
                SELECT user_id, user_type FROM Sessions 
                WHERE session_id = %s AND expiry_time > NOW()
            """, (session_id,))
            result = cursor.fetchone()
            return result if result else (None, None)
        finally:
            cursor.close()

    def log_activity(self, user_id: int, action: str, table_name: str = None, record_id: int = None):
        """Log user activity for audit purposes."""
        cursor = self.get_cursor()
        try:
            ip_address = socket.gethostbyname(socket.gethostname())
            cursor.execute("""
                INSERT INTO AuditLog (user_id, action, table_name, record_id, ip_address)
                VALUES (%s, %s, %s, %s, %s)
            """, (user_id, action, table_name, record_id, ip_address))
            self.conn.commit()
            logger.info(f"Logged activity: {action} for user {user_id}")
        finally:
            cursor.close()

    def create_user(self, first_name: str, last_name: str, username: str, password: str) -> tuple:
        """Create new user with secure password."""
        cursor = self.get_cursor()
        try:
            # Check if username exists
            cursor.execute("SELECT COUNT(*) FROM User WHERE username = %s", (username,))
            if cursor.fetchone()[0] > 0:
                return False, "Username already exists"
                
            # Create user with ed25519 password
            cursor.execute("""
                INSERT INTO User (first_name, last_name, username, password, is_certified)
                VALUES (%s, %s, %s, ed25519_password(%s), 0)
            """, (first_name, last_name, username, password))
            
            self.conn.commit()
            return True, "User created successfully"
        except Exception as e:
            logger.error(f"User creation error: {str(e)}")
            return False, f"Error creating user: {str(e)}"
        finally:
            cursor.close()
    def change_password(self, user_id: str, current_password: str, new_password: str) -> tuple:
        """Change user password with verification."""
        cursor = self.get_cursor()
        try:
            # Verify current password
            cursor.execute("""
                SELECT username FROM User 
                WHERE user_id = %s AND password = ed25519_password(%s)
            """, (user_id, current_password))
            
            if not cursor.fetchone():
                return False, "Current password is incorrect"
            
            # Update to new password
            cursor.execute("""
                UPDATE User 
                SET password = ed25519_password(%s) 
                WHERE user_id = %s
            """, (new_password, user_id))
            
            self.conn.commit()
            return True, "Password changed successfully"
        except Exception as e:
            logger.error(f"Password change error: {str(e)}")
            return False, f"Error changing password: {str(e)}"
        finally:
            cursor.close()

# Create a global instance
db = DatabaseConnection()
