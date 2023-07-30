import cloudinary.uploader
import os
from urllib.parse import urlparse
from ai_tools.models import AITool

# Your Cloudinary setup
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
    secure=True
)

# Get all AI tools and prepare for counting
tools = AITool.objects.all()
total_tools = len(tools)
success_counter = 0
failure_counter = 0
unchanged_counter = 0

# Create a list to store names of tools for which favicon upload failed
failed_tools = []

# Iterate through all AI tools
for i, tool in enumerate(tools):
    # The public_id will be the tool's name
    public_id = tool.name

    # If the tool's favicon_url is not set, not "None", or not stored on Cloudinary, attempt to re-upload
    if not tool.favicon_url or tool.favicon_url == "None" or 'res.cloudinary.com' not in tool.favicon_url:
        if not tool.favicon_url or tool.favicon_url == "None":
            print(f"Favicon for tool ({i+1}/{total_tools}): {tool.name} is not set or 'None'. Attempting to upload...")
        else:
            print(f"Favicon for tool ({i+1}/{total_tools}): {tool.name} is not stored on Cloudinary. Attempting to replace...")

        # Use faviconkit.com to get favicon URL
        favicon_url = f"https://api.faviconkit.com/{urlparse(tool.website).netloc}/144"

        print(f"Attempting to upload favicon for tool ({i+1}/{total_tools}): {tool.name}")

        try:
            # Upload the favicon to Cloudinary
            response = cloudinary.uploader.upload(
                favicon_url,
                public_id=public_id,
                overwrite=True,
                resource_type="image",
                folder=os.getenv('CLOUDINARY_FOLDER')
            )

            # Update the tool's favicon_url with the URL from the upload response
            tool.favicon_url = response['url']

            # Save the tool
            tool.save()

            print(f"Successfully uploaded and updated favicon for tool: {tool.name}")
            success_counter += 1
        except Exception as e:
            # Here you may want to do something if an error happens during upload
            print(f"An error occurred while uploading favicon for tool {tool.name}: {str(e)}")
            tool.favicon_url = "faviconkit.com failed"
            tool.save()
            failure_counter += 1
            failed_tools.append(tool.name)
    else:
        print(f"Favicon for tool ({i+1}/{total_tools}): {tool.name} is already stored on Cloudinary, no need to replace.")
        unchanged_counter += 1

# Print out final results
print(f"\nSuccessfully uploaded favicons for {success_counter} tools. Failed to upload favicons for {failure_counter} tools. {unchanged_counter} tools already had favicons stored on Cloudinary.\n")
