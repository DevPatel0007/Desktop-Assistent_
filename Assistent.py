# Importing the libraries 
#pip install pyttsx3 speechrecognition datetime wikipedia google-api-python-client google-auth-httplib2 google-auth-oauthlib
import pyttsx3 # For text-to-speech conversion
import speech_recognition as sr # For speech recognition
import datetime # For date and time
import wikipedia # For accessing Wikipedia
import webbrowser # For opening web pages
import google.generativeai as genai



genai.configure(api_key="your_api_kye ")



    # Create a speech recognition object
recognizer = sr.Recognizer()

# Create a text-to-speech engine
engine = pyttsx3.init()

# Set the voice of the engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 0.95,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": "Explain deadlocks and solutions to remove deadlocks."
  },
  {
    "role": "model",
    "parts": "**Deadlocks:**\n\nA deadlock occurs when two or more processes are waiting for each other to release resources, resulting in a situation where none of the processes can proceed. This can happen when multiple processes are competing for the same limited resources, such as memory, CPU time, or I/O devices.\n\n**Solutions to Remove Deadlocks:**\n\n1. **Deadlock Prevention:**\n\n   - Avoid assigning resources to processes that may lead to potential deadlocks.\n   - Keep track of resource utilization and prevent processes from acquiring additional resources if it could result in a deadlock.\n\n2. **Deadlock Avoidance:**\n\n   - Utilize algorithms like Banker's Algorithm to determine whether assigning a resource to a process will lead to a deadlock.\n   - Only grant resources if it can be ensured that the process will be able to complete its execution without causing a deadlock.\n\n3. **Deadlock Detection:**\n\n   - Continuously monitor the system for deadlocks using algorithms like Floyd's cycle detection algorithm or path-finding algorithms.\n   - If a deadlock is detected, identify the processes involved and take appropriate actions to resolve the deadlock.\n\n4. **Deadlock Recovery:**\n\n   - Abort one or more processes involved in the deadlock to release resources and allow the remaining processes to continue.\n   - Rollback the processes involved in the deadlock to a previous state where they were not deadlocked.\n\n5. **Design for Deadlock Avoidance:**\n\n   - Organize resources in a hierarchical manner, with processes requesting resources in the same order.\n   - Allow processes to acquire resources in a non-preemptible manner, where resources cannot be forcibly taken away from a process once granted.\n\n6. **Mutual Exclusion:**\n\n   - Ensure that only one process can access a shared resource at a time.\n   - Use mechanisms like semaphores, locks, or mutexes to enforce mutual exclusion.\n\n7. **Hold and Wait:**\n\n   - Avoid situations where a process holds one resource while waiting for another resource that is held by a different process.\n\n8. **Circular Wait:**\n\n   - Break the circular wait condition by ensuring that processes request resources in a specific order.\n\n9. **Resource Ordering:**\n\n   - Assign unique priorities to resources and processes, and enforce a resource allocation order based on these priorities.\n\n10. **Timeouts:**\n\n   - Set timeouts for resource acquisition and release to prevent processes from holding resources indefinitely.\n\nBy implementing these solutions, system designers and developers can minimize the risk of deadlocks and ensure the smooth execution of processes in a multiprogramming environment."
  },
  {
    "role": "user",
    "parts": "UNIT: 2-Process Management\n1. What is the process? Compare CPU bound process and I/O bound process.\n2. Explain process life cycle.\n3. List types of scheduler. Explain Long term schedulers.\n4. Explain necessary conditions for deadlocks to occur.\n5. Explain deadlocks and solutions to remove deadlocks.\n6. Explain Round Robin scheduling (time slice scheduling) algorithm with\nexample.\n7. Explain FCFS (first come first served)\n8. Explain SRTN (shortest remaining time next) algorithm.\n9. Explain priority scheduling.\n10.Define following :-\n(A) Race condition (B) IPC\n(C) Semaphore (D) Mutual exclusion\n(E) Scheduler (F) Scheduling\n11.Draw diagram of PCB. Explain each component of PCB."
  },
  {
    "role": "model",
    "parts": "**1. Process:**\n\nA process is an instance of a computer program that is being executed. It consists of the program code, its data, and its execution context.\n\n**CPU-bound process:**\n\n- Spends most of its time executing instructions and performs minimal I/O operations.\n- Examples: Scientific simulations, video rendering, mathematical calculations.\n\n**I/O-bound process:**\n\n- Spends most of its time performing input/output operations and performs minimal CPU processing.\n- Examples: Database queries, file transfers, web browsing.\n\n**2. Process Life Cycle:**\n\n- **New:** Process is created by the operating system.\n- **Running:** Process is executing instructions.\n- **Waiting:** Process is waiting for a resource (e.g., CPU, I/O device) to become available.\n- **Ready:** Process is ready to execute but is waiting for the CPU to become available.\n- **Terminated:** Process has completed execution or has been terminated by the operating system.\n\n**3. Types of Schedulers:**\n\n- **Long-term scheduler:** Decides which processes to admit into the system and allocates memory to them.\n- **Short-term scheduler (CPU scheduler):** Decides which process to execute next from the set of ready processes.\n\n**Long-term schedulers:**\n\n- **First-Come-First-Served (FCFS):** Admits processes in the order they arrive.\n- **Shortest Job First (SJF):** Admits processes with the shortest estimated execution time first.\n- **Priority Scheduling:** Admits processes based on their priority, with higher priority processes admitted first.\n\n**4. Necessary Conditions for Deadlocks to Occur:**\n\n- **Mutual exclusion:** Only one process can use a resource at a time.\n- **Hold and wait:** A process holding a resource is waiting for another resource held by another process.\n- **No preemption:** Resources cannot be forcibly taken away from a process once granted.\n- **Circular wait:** A circular chain of processes is waiting for each other to release resources.\n\n**5. Deadlocks and Solutions to Remove Deadlocks:**\n\n- **Deadlock prevention:** Avoid assigning resources to processes that may lead to potential deadlocks.\n- **Deadlock avoidance:** Use algorithms like Banker's Algorithm to determine whether assigning a resource to a process will lead to a deadlock.\n- **Deadlock detection:** Continuously monitor the system for deadlocks and take appropriate actions to resolve them.\n- **Deadlock recovery:** Abort one or more processes involved in the deadlock to release resources and allow the remaining processes to continue.\n\n**6. Round Robin Scheduling (Time Slice Scheduling) Algorithm:**\n\n- Each process is allocated a time slice (quantum) to execute.\n- If a process does not complete within its time slice, it is preempted and placed at the end of the ready queue.\n- The scheduler then selects the next process from the ready queue and allocates it a time slice.\n\n**Example:**\n\n- Time slice = 5 milliseconds\n- Process A: 10 milliseconds of execution time\n- Process B: 15 milliseconds of execution time\n\n- Time 0-5 ms: Process A executes\n- Time 5-10 ms: Process B executes\n- Time 10-15 ms: Process A executes again\n\n**7. FCFS (First Come First Served):**\n\n- The simplest scheduling algorithm.\n- Processes are executed in the order they arrive.\n- No preemption.\n\n**8. SRTN (Shortest Remaining Time Next) Algorithm:**\n\n- Selects the process with the shortest remaining execution time to execute next.\n- Preemption is allowed.\n\n**9. Priority Scheduling:**\n\n- Each process is assigned a priority.\n- Processes with higher priorities are executed before processes with lower priorities.\n- Preemption is allowed.\n\n**10. Definitions:**\n\n- **Race condition:** A situation where the outcome of a program depends on the relative timing of multiple events.\n- **IPC:** Inter-process communication, a mechanism that allows processes to communicate with each other.\n- **Semaphore:** A synchronization primitive used to control access to shared resources.\n- **Mutual exclusion:** Ensuring that only one process can access a shared resource at a time.\n- **Scheduler:** The part of the operating system that decides which process to execute next.\n- **Scheduling:** The process of selecting the next process to execute from the set of ready processes.\n\n**11. PCB (Process Control Block) Diagram:**\n\n[Image of a PCB diagram]\n\n**Components of PCB:**\n\n- **Process ID:** A unique identifier for the process.\n- **Process State:** The current state of the process (e.g., running, waiting, ready).\n- **Program Counter:** The address of the next instruction to be executed.\n- **Stack Pointer:** The address of the top of the process's stack.\n- **Memory Management Information:** Information about the process's memory usage.\n- **Registers:** The values of the process's registers.\n- **I/O Information:** Information about the process's I/O devices and their status."
  },
  {
    "role": "user",
    "parts": "UNIT: 4- File Management System\n1 Explain File Operation in detail.\n2 Explain directory structure of OS\n3 Write and explain Contiguous file allocation method.\n4.Write and explain Linked file allocation method.\n4 Write and explain the Disk Scheduling Algorithm in detail.\n5 Write a short note on : Physical structure of disk with Addressing."
  },
  {
    "role": "model",
    "parts": "**1. File Operations:**\n\n- **Creating a File:** Allocates space on the disk for the file and initializes its metadata (e.g., file name, size, permissions).\n- **Opening a File:** Locates the file on the disk and prepares it for reading or writing.\n- **Reading from a File:** Retrieves data from the file and returns it to the user program.\n- **Writing to a File:** Stores data in the file from the user program.\n- **Closing a File:** Releases the resources associated with the file and updates its metadata.\n- **Deleting a File:** Removes the file from the disk and deallocates its space.\n- **Renaming a File:** Changes the name of the file.\n- **Copying a File:** Creates a new file and copies the contents of an existing file into it.\n\n**2. Directory Structure of OS:**\n\nA directory structure is a hierarchical organization of files and directories on a storage device. It allows users to organize and access files efficiently.\n\n- **Root Directory:** The top-level directory in the hierarchy.\n- **Subdirectories:** Directories within other directories.\n- **Files:** Data stored on the storage device.\n\n**3. Contiguous File Allocation Method:**\n\n- Stores a file as a contiguous block of disk space.\n- Simple to implement and manage.\n- Fast access time for sequential reads and writes.\n- Internal fragmentation: Unused space at the end of the file.\n- External fragmentation: Unused disk space between files.\n\n**4. Linked File Allocation Method:**\n\n- Stores a file as a linked list of disk blocks.\n- Each block contains a pointer to the next block in the list.\n- No internal fragmentation.\n- External fragmentation can still occur.\n\n**5. Disk Scheduling Algorithms:**\n\nDisk scheduling algorithms determine the order in which disk I/O requests are serviced.\n\n- **First-Come-First-Served (FCFS):** Requests are serviced in the order they arrive.\n- **Shortest Seek Time First (SSTF):** The request with the shortest seek time is serviced next.\n- **SCAN:** The disk head moves in one direction, servicing requests along the way, until it reaches the end of the disk. It then reverses direction and services requests in the opposite direction.\n- **C-SCAN:** Similar to SCAN, but the disk head only moves in one direction, servicing requests along the way. Once it reaches the end of the disk, it immediately returns to the beginning and continues servicing requests.\n\n**6. Physical Structure of Disk with Addressing:**\n\n- **Disk Platters:** Data is stored on magnetic disks called platters.\n- **Tracks:** Each platter is divided into concentric circles called tracks.\n- **Sectors:** Tracks are further divided into smaller segments called sectors.\n- **Clusters:** A cluster is a group of sectors that is the smallest unit of data that can be read or written to the disk.\n- **Disk Addressing:** Each sector on a disk is identified by a unique address, which consists of the platter number, track number, and sector number."
  },
  {
    "role": "user",
    "parts": "UNIT: 4- File Management System1 Explain File Operation in detail.2 Explain directory structure of OS3 Write and explain Contiguous file allocation method.4.Write and explain Linked file allocation method.4 Write and explain the Disk Scheduling Algorithm in detail.5 Write a short note on : Physical structure of disk with Addressing."
  },
  {
    "role": "model",
    "parts": "**1. File Operations:**\n\n- **Creating a File:** Allocates space on the disk for the file and initializes its metadata (e.g., file name, size, permissions).\n- **Opening a File:** Locates the file on the disk and prepares it for reading or writing.\n- **Reading from a File:** Retrieves data from the file and returns it to the user program.\n- **Writing to a File:** Stores data in the file from the user program.\n- **Closing a File:** Releases the resources associated with the file and updates its metadata.\n- **Deleting a File:** Removes the file from the disk and deallocates its space.\n- **Renaming a File:** Changes the name of the file.\n- **Copying a File:** Creates a new file and copies the contents of an existing file into it.\n\n**2. Directory Structure of OS:**\n\nA directory structure is a hierarchical organization of files and directories on a storage device. It allows users to organize and access files efficiently.\n\n- **Root Directory:** The top-level directory in the hierarchy.\n- **Subdirectories:** Directories within other directories.\n- **Files:** Data stored on the storage device.\n\n**3. Contiguous File Allocation Method:**\n\n- Stores a file as a contiguous block of disk space.\n- Simple to implement and manage.\n- Fast access time for sequential reads and writes.\n- Internal fragmentation: Unused space at the end of the file.\n- External fragmentation: Unused disk space between files.\n\n**4. Linked File Allocation Method:**\n\n- Stores a file as a linked list of disk blocks.\n- Each block contains a pointer to the next block in the list.\n- No internal fragmentation.\n- External fragmentation can still occur.\n\n**5. Disk Scheduling Algorithms:**\n\nDisk scheduling algorithms determine the order in which disk I/O requests are serviced.\n\n- **First-Come-First-Served (FCFS):** Requests are serviced in the order they arrive.\n- **Shortest Seek Time First (SSTF):** The request with the shortest seek time is serviced next.\n- **SCAN:** The disk head moves in one direction, servicing requests along the way, until it reaches the end of the disk. It then reverses direction and services requests in the opposite direction.\n- **C-SCAN:** Similar to SCAN, but the disk head only moves in one direction, servicing requests along the way. Once it reaches the end of the disk, it immediately returns to the beginning and continues servicing requests.\n\n**6. Physical Structure of Disk with Addressing:**\n\n- **Disk Platters:** Data is stored on magnetic disks called platters.\n- **Tracks:** Each platter is divided into concentric circles called tracks.\n- **Sectors:** Tracks are further divided into smaller segments called sectors.\n- **Clusters:** A cluster is a group of sectors that is the smallest unit of data that can be read or written to the disk.\n- **Disk Addressing:** Each sector on a disk is identified by a unique address, which consists of the platter number, track number, and sector number."
  }
])

# Defining a function that takes text as input and converts it to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Defining a function that takes audio as input and converts it to text
def recognize(audio):
    try:
        text = recognize.recognize_google(audio)
        print("You said: " + text)
        return text
    except:
        print("Sorry, I could not understand what you said.")
        return None

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    speak("I am your desktop assistant. Please tell me how may I help you") 

# Defining a function that listens to the microphone input and returns the audio data

def listen():
    with sr.Microphone() as source:
      print("Listening...")
      audio = recognizer.listen(source)
      return audio

# Defining a function that executes the commands given by the user
def execute(text):
    # If the user says "hello" or "hi", greet them back
    if "hello" in text.lower() or "hi" in text.lower():
        speak("Hello, I am your desktop assistant. How can I help you?")
    
    # If the user says "time" or "date", tell them the current time and date
    elif "time" in text.lower() or "date" in text.lower():
        now = datetime.datetime.now()
        speak("The current time is " + now.strftime("%H:%M") + " and the current date is " + now.strftime("%d %B %Y"))
    
    # If the user says "wikipedia" or "wiki", search Wikipedia for the query after these words
    elif "wikipedia" in text.lower() or "wiki" in text.lower():
       
        query = text.split("Wikipedia ")[-1] or text.split("wiki ")[-1]
        speak("Searching Wikipedia for " + query)
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia, " + result)
        speak("for more information see this page")
        webbrowser.open("https://www.wikipedia.org/wiki/" +query.replace(" ", "_"))
    
    # If the user says "google" or "search", open Google in the default browser with the query after these words
    elif "google" in text.lower() or "search" in text.lower():
        query = text.split("google")[-1] or text.split("search")[-1]
        speak("Opening Google for " + query)
        webbrowser.open("https://www.google.com/search?q=" + query) 
    
    elif 'youtube' in text.lower():
        query = text.split("youtube")[-1]
        speak("Opening Youtub for " + query)
        webbrowser.open("https://www.youtube.com/results?search_query=" + query)
        speak("you can see video of"+ query) 
        
    elif 'open Whatsapp' in text.lower():
        webbrowser.open("https://web.whatsapp.com/")

    elif 'open drive' in text.lower():
        webbrowser.open("https://drive.google.com/drive/my-drive")

    elif 'hay gamini' in text.lower()  :
        query = text.split("hay gamini")[-1] 
        convo.send_message(query)
        print(convo.last.text)
        speak(convo.last.text)
    # If the user says "bye" or "quit", exit the program

    elif "bye" in text.lower() or "quit" in text.lower():
        speak("Goodbye, have a nice day!")
        exit()        
    
    # If none of the above commands match, say that the command is not valid
    else:
        speak("Sorry, I did not recognize that command. Please try again.")

# Writing the main loop that listens to the user's voice input and calls the appropriate functions
if __name__ == "__main__":
 wishMe()
while True:
   
    audio = listen() # Listen to the microphone input
    text = recognize(audio) # Convert the audio to text
    if text: # If the text is not None, execute the command
        execute(text)
