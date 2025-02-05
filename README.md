# 🤖 Automated Metadata Extraction and Reporting Tool (AMERT)

# 🚀 AMERT 🤖
Your friendly neighborhood metadata extractor!

## What's This All About? 🤔
AMERT is your trusty Python-powered sidekick, designed to dive deep into those PDF and DOCX files lurking in your folder labyrinths. Perfect for when you're drowning in coursework submissions or battling an avalanche of research docs!

## Super Powers ✨
- 🔍 **Metadata Mining**: Excavates juicy details like author, title, creation date, and more from PDF/DOCX files
- 📁 **Folder Deep Diving**: Fearlessly ventures into the deepest, darkest corners of your directory structures
- 📊 **Excel Wizardry**: Conjures up beautiful spreadsheet reports faster than you can say "metadata"
- 🚨 **Error Detective**: Keeps a watchful eye on everything, logging any sneaky issues that try to slip by
- 🌐 **Platform Ninja**: Gracefully performs its magic on Windows, macOS, or Linux - no discrimination here!

## Getting Started 🚀

# Clone this bad boy
git clone https://github.com/v-eenay/Automated-Metadata-Extraction-and-Reporting-Tool-AMERT-.git
<br>
cd Automated-Metadata-Extraction-and-Reporting-Tool-AMERT-

# Create your magical environment
python -m venv venv
source venv/bin/activate 

# Windows wizards use: venv\Scripts\activate

# Summon the dependencies
pip install -r requirements.txt

# Let it rip!
python main.py


## How to Use This Beast 🎮
1. 📦 Drop your zipped submissions into the `submissions` folder
2. 🏃‍♂️ Run the script
3. ✨ Watch as `metadata.xlsx` materializes in your root directory

## The Magic Behind the Scenes 🎭
**Input**: Your chaotic folder of zipped files

**Processing**:
- 🤐 Unzips all the things
- 🕵️‍♂️ Hunts down supported files
- 🎯 Extracts all the metadata goodness

**Output**: A beautiful Excel file containing all your organized data!

## Known Quirks 🐛
- Some PDFs might throw a tantrum (looking at you, corrupted files!)
- Occasionally, dates might get a bit confused about what century they're in

## Want to Help? 🤝
1. 🍴 Fork it
2. 🌱 Create your feature branch
3. 💾 Commit your changes
4. 🚀 Push to the branch
5. 🎉 Open a PR and celebrate!

## Need to Chat? 📬
- 📧 Email: koiralavinay@gmail.com
- 🐙 GitHub: @v-eenay

Made with 💻 and ☕ by Vinay Koirala
