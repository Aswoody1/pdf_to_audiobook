from pypdf import PdfReader
from google.cloud import texttospeech

#Reading PDF File - choose a pdf to read
reader = PdfReader("Input_File.pdf")
# Converting PDF file to text variable
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"



# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=text)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender
voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Standard-A",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')

