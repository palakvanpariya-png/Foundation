"""
User Profile Management System Template
Topic 1: Variables and Data Types Implementation Task

Fill in the methods marked with 'TODO' to complete the implementation.
This template demonstrates proper class structure and variable usage.
"""

from datetime import date
from typing import List, Dict, Any, Tuple, Optional


class UserProfile:
    # Class constants (proper naming convention)
    MIN_AGE = 13
    MAX_AGE = 120
    DEFAULT_BALANCE = 0.0
    
    def __init__(self):
        # TODO: Initialize all instance variables with appropriate data types
        # String variables
        self.full_name: str = ""
        self.email: str = ""
        
        # Numeric variables
        self.age: int = 0
        self.account_balance: float = self.DEFAULT_BALANCE
        
        # Boolean variable
        self.is_premium_member: bool = False
        
        # Collection variables
        self.interests: List[str] = []
        self.account_creation_date: Tuple[int, int, int] = (0, 0, 0)  # (year, month, day) {could use date.today() instead}
        # self.account_creation_date: date = date.today()
        self.profile_settings: Dict[str, Any] = {}
        
        # None type
        self.last_login: Optional[str] = None
    
    def create_profile(self, name: str, age: int, email: str) -> bool:
        # TODO: Implement profile creation
        # 1. Validate input parameters (check types and values)
        # 2. Set the instance variables
        # 3. Set account_creation_date to today's date
        # 4. Initialize default profile_settings
        # 5. Return True if successful, False if validation fails
        if not name or not email: # so name and email are required fields
            return False

        # validate input types
        if not isinstance(name, str) or not isinstance(age, int) or not isinstance(email, str):
            return False
        
        # Validate age
        if age < self.MIN_AGE or age > self.MAX_AGE:
            return False
        
        # Validate email format (basic check)
        if "@" not in email or "." not in email:
            return False
        
        self.full_name =name
        self.age = age
        self.email = email
        self.account_creation_date = (date.today().year, date.today().month, date.today().day)
        self.profile_settings = {
            "theme": "light",
            "notifications": False,
            "language": "en"}
        
        # If all validations pass, return True
        return True
    
    def display_profile(self) -> None:
        # TODO: Implement profile display
        # 1. Check if profile is created (has valid data)
        # 2. Format and print all profile information nicely
        # 3. Use f-strings for formatting
        # 4. Show validation status
        if not self.full_name:  # because full_name is a required field
            print("Profile not created yet.")
            return 
        
        print("=== USER PROFILE ===")
        # Your implementation here
        print(f"Name: {self.full_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Account Balance: {self.account_balance:.2f}")
        print(f"Premium Member: {'Yes' if self.is_premium_member else 'No'}")
        print(f"Interests: {', '.join(self.interests) if self.interests else 'None'}")
        print(f"Account Created: {self.account_creation_date[0]}-{self.account_creation_date[1]:02}-{self.account_creation_date[2]:02}") # :02 for zero padding {2025-09-01}
        print(f"Profile Settings: {self.profile_settings}")
        print("====================")
    
    def update_balance(self, amount) -> bool:
        # TODO: Implement balance update
        # 1. Validate amount is a number
        # 2. Check if new balance would be negative (optional business rule)
        # 3. Update the balance
        # 4. Return success status
        if not isinstance(amount, (int, float)) or amount == 0:
            return False
        if self.account_balance + amount < 0:
            return False
        
        self.account_balance += amount
        
        return True
    
    def add_interest(self, interest: str) -> bool:
        # TODO: Implement add interest
        # 1. Validate interest is a string and not empty
        # 2. Check if interest already exists (avoid duplicates)
        # 3. Add to interests list
        # 4. Return success status

        if not isinstance(interest, str) or not interest:
            return False
        
        if interest in self.interests:
            return False
        
        self.interests.append(interest)

        return True
    
    def update_profile_setting(self, key: str, value: Any) -> None:
        # TODO: Implement setting update
        # 1. Add or update the key-value pair in profile_settings
        # 2. Handle different data types for values
        if not isinstance(key, str) or not key:
            raise ValueError("Key must be a non-empty string")
        
        self.profile_settings[key] = value
        print(f"Setting '{key}' updated to '{value}'")

        return None
        

    def remove_all_interests(self) -> None:
        """
        Remove all interests from the user profile using a while loop.
        """
        # TODO: Implement this using a while loop
        # 1. Use a while loop to remove items one by one from self.interests
        # 2. Optionally print each removed item
        while self.interests:
            removed_interest = self.interests.pop() # Remove the last interest(pop removes the last item)
            print(f"Removed interest: {removed_interest}")


    def find_and_highlight_interest(self, keyword: str) -> None:
        """
        Search through interests using a for loop, and highlight matches.
        
        Demonstrates:
        - for loop
        - continue and break
        - case-insensitive matching
        - enumerate usage
        
        Args:
            keyword: A string to search for in interests
        """
        # TODO: Implement this function
        # 1. Validate keyword
        # 2. Use a for loop with enumerate to iterate over interests
        # 3. Use `continue` to skip empty or invalid items
        # 4. Use `break` if keyword is found (after printing it)
        # 5. Print a message if nothing found
        if not isinstance(keyword, str) or not keyword:
            return False
        
        keyword = keyword.lower()  # Case-insensitive search
        found = False
        for index, interest in enumerate(self.interests):
            if not interest:
                continue
            if keyword in interest.lower():
                print(f"Found interest '{interest}' at index {index}")
                found = True
                break

        if not found:
            print(f"No interest found containing '{keyword}'")
        else:
            print(f"Search completed for keyword '{keyword}'")


def main():
    user = UserProfile()

    # Test: create profile
    created = user.create_profile("Alice Smith", 28, "alice@example.com")
    print("Profile creation successful?" , created)
    print()

    # Display the profile
    user.display_profile()
    print()

    # Test: update balance
    success = user.update_balance(150.75)
    print("Balance update successful?", success)
    print(f"New Balance: {user.account_balance:.2f}")
    print()

    # Test: add interests
    print("Adding interest 'Reading':", user.add_interest("Reading"))
    print("Adding interest 'Traveling':", user.add_interest("Traveling"))
    print("Adding duplicate interest 'Reading':", user.add_interest("Reading"))  # Should fail
    print()

    # Display profile again
    user.display_profile()
    print()

    # Test: update settings
    user.update_profile_setting("theme", "dark")
    user.update_profile_setting("language", "fr")
    user.update_profile_setting("notifications", True)
    print()

    # Final profile display
    user.display_profile()

     # === Loop Function Tests ===
    print("\n--- Advanced For Loop Test: find_and_highlight_interest ---")
    user.find_and_highlight_interest("read")  # Should find "Reading"

    print("\n--- While Loop Test: remove_all_interests ---")
    user.remove_all_interests()  # Should remove "Reading" and "Traveling"

    print("\n--- Display Profile After Removing Interests ---")
    user.display_profile()

    print("\n--- Try Searching After Removal ---")
    user.find_and_highlight_interest("travel")  # Should now return "not found"


if __name__ == "__main__":
    main()
