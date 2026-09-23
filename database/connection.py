#!/usr/bin/env python3
"""
Database Connection Module for Cook-Up Recipe App
Handles all database connections and basic operations
"""

import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self, host="localhost", user="connorsinger", database="fall2025_482cook"):
        self.host = host
        self.user = user
        self.database = database
        self.connection = None
        self.cursor = None
    
    def connect(self):
        """Establish database connection"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print(f"Successfully connected to {self.database} database")
            return True
        except Error as e:
            print(f"Error connecting to database: {e}")
            return False
    
    def close(self):
        """Close database connection"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Database connection closed")
    
    def execute_query(self, query, params=None):
        """Execute a query with optional parameters"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return True
        except Error as e:
            print(f"Error executing query: {e}")
            return False
    
    def fetch_all(self):
        """Fetch all results from last query"""
        return self.cursor.fetchall()
    
    def fetch_one(self):
        """Fetch one result from last query"""
        return self.cursor.fetchone()
    
    def commit(self):
        """Commit changes to database"""
        if self.connection:
            self.connection.commit()

# Usage example:
if __name__ == "__main__":
    db = DatabaseConnection()
    if db.connect():
        # Test query
        db.execute_query("SELECT COUNT(*) FROM recipes")
        result = db.fetch_one()
        print(f"Total recipes in database: {result[0]}")
        db.close()