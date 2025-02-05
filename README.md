# 🤖 Automated Metadata Extraction and Reporting Tool (AMERT)

<div style="font-family: 'Segoe UI', Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 40px; background: linear-gradient(135deg, #ffffff, #f8f9fa); box-shadow: 0 8px 32px rgba(0,0,0,0.1); border-radius: 20px;">

<div style="text-align: center; margin-bottom: 40px;">
<h1 style="color: #2d3436; font-size: 3.5em; margin-bottom: 20px; text-shadow: 2px 2px 4px rgba(0,0,0,0.2); background: linear-gradient(to right, #6c5ce7, #a55eea); -webkit-background-clip: text; -webkit-text-fill-color: transparent; padding: 20px;">🚀 AMERT 🤖</h1>
<p style="color: #636e72; font-size: 1.5em; font-weight: bold; text-transform: uppercase; letter-spacing: 2px;">Your friendly neighborhood metadata extractor!</p>
</div>

<div style="background: linear-gradient(145deg, #6c5ce7, #a55eea); padding: 30px; border-radius: 15px; color: white; margin: 20px 0;">
<h2 style="font-size: 1.8em; margin-bottom: 15px;">What's This All About? 🤔</h2>
<p style="font-size: 1.1em; line-height: 1.6;">AMERT is your trusty Python-powered sidekick, designed to dive deep into those PDF and DOCX files lurking in your folder labyrinths. Perfect for when you're drowning in coursework submissions or battling an avalanche of research docs!</p>
</div>

<div style="background: linear-gradient(145deg, #00b894, #00cec9); padding: 30px; border-radius: 15px; color: white; margin: 20px 0;">
<h2 style="font-size: 1.8em; margin-bottom: 15px;">Super Powers ✨</h2>
<ul style="list-style-type: none; padding: 0;">
    <li style="margin: 10px 0; font-size: 1.1em;">🔍 <strong>Metadata Mining</strong>: Excavates juicy details like author, title, creation date, and more from PDF/DOCX files</li>
    <li style="margin: 10px 0; font-size: 1.1em;">📁 <strong>Folder Deep Diving</strong>: Fearlessly ventures into the deepest, darkest corners of your directory structures</li>
    <li style="margin: 10px 0; font-size: 1.1em;">📊 <strong>Excel Wizardry</strong>: Conjures up beautiful spreadsheet reports faster than you can say "metadata"</li>
    <li style="margin: 10px 0; font-size: 1.1em;">🚨 <strong>Error Detective</strong>: Keeps a watchful eye on everything, logging any sneaky issues that try to slip by</li>
    <li style="margin: 10px 0; font-size: 1.1em;">🌐 <strong>Platform Ninja</strong>: Gracefully performs its magic on Windows, macOS, or Linux - no discrimination here!</li>
</ul>
</div>

<div style="background: linear-gradient(145deg, #0984e3, #74b9ff); padding: 30px; border-radius: 15px; color: white; margin: 20px 0;">
<h2 style="font-size: 1.8em; margin-bottom: 15px;">Getting Started 🚀</h2>
<pre style="background: rgba(0,0,0,0.2); padding: 20px; border-radius: 10px; overflow-x: auto;">
# Clone this bad boy
git clone https://github.com/yourusername/amert.git
cd amert

# Create your magical environment

python -m venv venv
source venv/bin/activate # Windows wizards use: venv\Scripts\activate

# Summon the dependencies

pip install -r requirements.txt

# Let it rip!

python main.py</pre>

</div>

<div style="background: linear-gradient(145deg, #fd79a8, #e84393); padding: 30px; border-radius: 15px; color: white; margin: 20px 0;">
<h2 style="font-size: 1.8em; margin-bottom: 15px;">How to Use This Beast 🎮</h2>
<ol style="font-size: 1.1em; line-height: 1.6;">
    <li>📦 Drop your zipped submissions into the `submissions` folder</li>
    <li>🏃‍♂️ Run the script</li>
    <li>✨ Watch as `metadata.xlsx` materializes in your root directory</li>
</ol>
</div>

<div style="background: linear-gradient(145deg, #00b894, #55efc4); padding: 30px; border-radius: 15px; color: white; margin: 20px 0;">
<h2 style="font-size: 1.8em; margin-bottom: 15px;">The Magic Behind the Scenes 🎭</h2>
<p style="font-size: 1.1em; line-height: 1.6;"><strong>Input</strong>: Your chaotic folder of zipped files</p>
<p style="font-size: 1.1em; line-height: 1.6;"><strong>Processing</strong>:</p>
<ul style="list-style-type: none; padding: 0;">
    <li style="margin: 10px 0;">🤐 Unzips all the things</li>
    <li style="margin: 10px 0;">🕵️‍♂️ Hunts down supported files</li>
    <li style="margin: 10px 0;">🎯 Extracts all the metadata goodness</li>
</ul>
<p style="font-size: 1.1em; line-height: 1.6;"><strong>Output</strong>: A beautiful Excel file containing all your organized data!</p>
</div>

<div style="background: linear-gradient(145deg, #fdcb6e, #ffeaa7); padding: 30px; border-radius: 15px; color: #2d3436; margin: 20px 0;">
<h2 style="font-size: 1.8em; margin-bottom: 15px;">Known Quirks 🐛</h2>
<ul style="list-style-type: none; padding: 0;">
    <li style="margin: 10px 0; font-size: 1.1em;">• Some PDFs might throw a tantrum (looking at you, corrupted files!)</li>
    <li style="margin: 10px 0; font-size: 1.1em;">• Occasionally, dates might get a bit confused about what century they're in</li>
</ul>
</div>

<div style="background: linear-gradient(145deg, #0984e3, #74b9ff); padding: 30px; border-radius: 15px; color: white; margin: 20px 0;">
<h2 style="font-size: 1.8em; margin-bottom: 15px;">Want to Help? 🤝</h2>
<ol style="font-size: 1.1em; line-height: 1.6;">
    <li>🍴 Fork it</li>
    <li>🌱 Create your feature branch</li>
    <li>💾 Commit your changes</li>
    <li>🚀 Push to the branch</li>
    <li>🎉 Open a PR and celebrate!</li>
</ol>
</div>

<div style="background: linear-gradient(145deg, #e17055, #fab1a0); padding: 30px; border-radius: 15px; color: white; margin: 20px 0;">
<h2 style="font-size: 1.8em; margin-bottom: 15px;">Need to Chat? 📬</h2>
<ul style="list-style-type: none; padding: 0;">
    <li style="margin: 10px 0; font-size: 1.1em;">📧 Email: koiralavinay@gmail.com</li>
    <li style="margin: 10px 0; font-size: 1.1em;">🐙 GitHub: @v-eenay</li>
</ul>
</div>
<div style="text-align: center; color: #e84393; font-style: italic; margin-top: 20px;">
<p style="font-size: 1.2em;">Made with 💻 and ☕ by Vinay Koirala</p>
<p style="font-size: 1em;">(Because sleep is for the weak!)</p>
</div>

</div>
