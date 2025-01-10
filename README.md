# Instagram Follower Difference Checker

This script identifies the differences between your Instagram followers and followings.

## How to Use

### 1. Request Your Instagram Data
Follow these steps to request your data from Instagram:
- Go to *More > Your activity > Download your information*.
- Hit the *[Continue]* button.
- Under *Download or transfer information, select your Instagram account and hit *[Next]**.
- Select *"Some of your information"*.
- Under *Connections, check *"Followers and following"* and hit *[Next]**.
- Select *"Download to device"*.
- In the new window:
  - Select *"All Time"* for *Date Range*.
  - Choose *"Format"* as *JSON*.
  - Hit the *[Create files]* button.

Instagram will take a few hours to prepare files under the *Download your information* page you previously visited under *Your activity*.

### 2. Download Your Data
Once your files are ready:
- Go back to the *Download your information* page.
- Download the zip file.

### 3. Prepare the Files for the Script
Unzip the downloaded zip file under the InstaFollowerDiff directory.

### 4. Run the Script
Make sure you have Python 3 installed. Then, run the script as follows:
bash
python3 diff.py

### 5. Results
Results will be viewed in result.html in the same directory.

