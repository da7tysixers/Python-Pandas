#from msgraph import GraphServiceClient
#from azure.identity import InteractiveBrowserCredential

# This handles the auth popup seamlessly locally
#credential = InteractiveBrowserCredential()
#client = GraphServiceClient(credentials=credential)

#print("Microsoft Graph SDK for Python loaded successfully!")


import asyncio
from msgraph import GraphServiceClient
from azure.identity import InteractiveBrowserCredential

async def main():
    print("Initializing connection to Microsoft Graph...")
    
    # 1. Setup modern interactive browser login
    credential = InteractiveBrowserCredential()
    
    # Use 'credentials=' to match the official SDK requirement
    client = GraphServiceClient(credentials=credential)
    
    try:
        print("\n[Action Needed] Please sign in using the web browser window that just opened.")
        
        # 2. Fetch your profile data dynamically from Entra ID
        user = await client.me.get()
        
        # 3. Print out your successful connection results
        print("\n" + "="*40)
        print("🎉 SUCCESS: Connected to Microsoft Graph in VS Code!")
        print(f"Display Name:         {user.display_name}")
        print(f"User Principal Name:  {user.user_principal_name}")
        print(f"User ID:              {user.id}")
        print("="*40)
        
    except Exception as e:
        print(f"\n❌ Error connecting to Graph: {e}")

# Securely handle the asynchronous event loop execution
# Windows: Press Windows Key + . (period) or Windows Key + ; (semicolon) to open the emoji picker.
# Type "cross mark" or "x" to find it.
if __name__ == "__main__":
    asyncio.run(main())
