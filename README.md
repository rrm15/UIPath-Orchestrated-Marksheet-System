# Automated Marksheet Generation System

## 📋 Project Overview

A comprehensive automation solution for generating professional student marksheets using UiPath REFramework, Python, and cloud orchestration. This system processes student data from CSV files, calculates grades and GPA, generates PDF marksheets, and delivers them via email - all in a fully automated, queue-based workflow.

---

## 🎯 Problem Statement

Educational institutions face significant challenges in manual marksheet generation:
- Time-consuming manual data entry and PDF creation
- High error rates in grade calculations
- Inconsistent formatting and branding
- Delayed delivery to students
- Lack of audit trails and processing logs
- Difficulty scaling during peak examination periods

---

## 💡 Solution Architecture

This project implements a **Dispatcher-Performer** architecture using **UiPath REFramework**, providing:

### Key Components

```
┌─────────────────────────────────────────────────────────────┐
│                    ORCHESTRATOR QUEUE                        │
│                    (MarksheetQueue)                          │
└─────────────────────────────────────────────────────────────┘
         ↑                                          ↓
         │                                          │
    DISPATCHER                                 PERFORMER
┌─────────────────┐                      ┌──────────────────┐
│ Read CSV File   │                      │  REFramework     │
│ Parse Student   │                      │  Main.xaml       │
│ Data            │                      │                  │
│ Populate Queue  │                      │  ├── Initialize  │
│ (10 students)   │                      │  ├── Get Trans.  │
└─────────────────┘                      │  ├── Process     │
                                         │  │   ├── Validate│
                                         │  │   ├── Calculate│
                                         │  │   ├── Generate│
                                         │  │   └── Verify  │
                                         │  └── End Process │
                                         │      └── Email   │
                                         └──────────────────┘
                                                   ↓
                                         ┌──────────────────┐
                                         │  OUTPUT          │
                                         │  ├── PDFs (10)   │
                                         │  └── Email       │
                                         └──────────────────┘
```

---

## ✨ Features

### 🔄 Automated Processing
- **Queue-based architecture** for scalable transaction processing
- **REFramework implementation** ensuring robustness and error handling
- **Retry mechanism** for transient failures
- **Business exception handling** for data validation errors

### 📊 Grade Calculation
- **Alphabetic grading system:** A, B, C, D, E, F
- **Automatic mark-to-grade conversion:**
  - A: 90-100
  - B: 80-89
  - C: 70-79
  - D: 60-69
  - E: 50-59
  - F: Below 50
- **GPA calculation:** Overall GPA on a 10-point scale
- **Data validation:** Marks range (0-100), required fields

### 📄 PDF Generation
- **Professional layout** with institutional branding
- **Student details section:** Name, Roll Number, DOB, Semester, Year, Department
- **Marks table:** 5 subjects with marks and grades
- **GPA display:** Overall GPA with visual formatting
- **Grade scale reference** for transparency
- **Automated signatures:** Controller of Examinations placeholder
- **Timestamps:** Generation date included

### 📧 Email Automation
- **Batch email notification** after all PDFs are generated
- **SMTP integration** with Gmail
- **Multiple PDF attachments** (all 10 marksheets)
- **Professional email body** with summary statistics
- **Configurable recipients** and branding

### 🔐 Error Handling
- **Business Rule Exceptions:** Invalid marks, missing data
- **Application Exceptions:** Python errors, file system issues
- **System Exceptions:** Network failures, SMTP errors
- **Comprehensive logging** at every step
- **Queue status tracking** in Orchestrator

---

## 🏗️ Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Automation Platform** | UiPath Studio 2026.x | Workflow orchestration |
| **Framework** | REFramework | Transactional processing |
| **Queue Management** | UiPath Orchestrator | Transaction queue, logging |
| **PDF Generation** | Python 3.14 + ReportLab | Professional PDF creation |
| **Data Source** | CSV (Excel compatible) | Student records |
| **Email** | SMTP (Gmail) | Notification delivery |
| **Configuration** | Excel (Config.xlsx) | Centralized settings |

---

## 📁 Project Structure

```
F:\UiPath\Final Project\
│
├── Main.xaml                          # REFramework performer (core automation)
├── AddTestQueueItem.xaml              # Dispatcher workflow
├── project.json                       # UiPath project configuration
│
├── Data/
│   ├── Config.xlsx                    # Configuration settings
│   ├── Input/
│   │   └── Sample_Student_Data.csv    # Student records (10 test students)
│   └── Output/                        # Generated PDFs (auto-created)
│       └── Marksheet_*.pdf            # Individual student marksheets
│
├── Framework/                         # REFramework components
│   ├── InitAllApplications.xaml       # Initialization + folder check
│   ├── GetTransactionData.xaml        # Queue item retrieval
│   ├── Process.xaml                   # Core business logic
│   ├── SetTransactionStatus.xaml      # Status update
│   └── KillAllProcesses.xaml          # Cleanup
│
├── Scripts/
│   └── generate_marksheet.py          # Python PDF generation
│
└── README.md                          # This file
```

---

## ⚙️ Configuration

### Config.xlsx Settings

The `Data/Config.xlsx` file contains all system configurations:

| Setting | Value | Description |
|---------|-------|-------------|
| **OrchestratorQueueName** | MarksheetQueue | Name of the queue in Orchestrator |
| **PythonScriptPath** | Scripts\generate_marksheet.py | Relative path to Python script |
| **OutputFolderPath** | Data\Output | PDF output directory (relative) |
| **InstitutionName** | ABC University | Institution name on marksheets |
| **LogF_BusinessProcessName** | MarksheetGeneration | Process name for logging |
| **MaxRetryNumber** | 2 | Maximum retry attempts for failures |
| **RetryNumberGetTransactionItem** | 3 | Queue fetch retry count |
| **LogToConsole** | True | Enable console logging |
| **MinimumLogLevel** | Information | Minimum log level (Info/Debug/Trace) |

**Email Configuration (hardcoded in Main.xaml):**
- SMTP Server: smtp.gmail.com
- Port: 587
- EnableSSL: True
- Gmail App Password required

---

## 🚀 Installation & Setup

### Prerequisites

1. **UiPath Studio** 2024.x or later
2. **Python 3.x** installed on system
3. **Python ReportLab library:**
   ```powershell
   pip install reportlab
   ```
4. **UiPath Orchestrator** access (Community or Enterprise)
5. **Gmail account** with App Password (for email notifications)

### Installation Steps

1. **Clone/Extract Project**
   ```
   Extract to: F:\UiPath\Final Project\
   ```

2. **Open in UiPath Studio**
   - File → Open → Select `project.json`

3. **Update Config.xlsx**
   - Navigate to `Data\Config.xlsx`
   - Verify all 9 settings (see Configuration table above)
   - Save changes

4. **Verify Python**
   ```powershell
   python --version          # Should show Python 3.x
   pip show reportlab        # Should show installed
   ```

5. **Test Python Script**
   ```powershell
   cd F:\UiPath\Final Project
   python Scripts\generate_marksheet.py
   # Should generate test_marksheet.pdf
   ```

6. **Create Orchestrator Queue**
   - Login to Orchestrator
   - Queues → Add Queue
   - Name: `MarksheetQueue`
   - Max retries: 2
   - Enable "Unique Reference"
   - Save

7. **Update Email Credentials**
   - Open `Main.xaml`
   - Navigate to End Process state
   - Find "Send SMTP Mail Message" activity
   - Update:
     - From: your_email@gmail.com
     - To: recipient@gmail.com
     - Username: your_email@gmail.com
     - Password: your_16_char_app_password

---

## 🎮 Usage

### Running Locally (Development/Testing)

**Step 1: Run Dispatcher**
```
1. Open AddTestQueueItem.xaml in Studio
2. Press F5 (Debug) or Click Run
3. Verify: Output shows "Rows read: 10"
4. Check Orchestrator → MarksheetQueue → 10 items with Status: New
```

**Step 2: Run Performer**
```
1. Open Main.xaml in Studio
2. Press F5 (Debug) or Click Run
3. Watch execution:
   - Initialization → Load Config
   - Get Transaction Data → Fetch queue item
   - Process Transaction → Generate PDF
   - Set Transaction Status → Mark Successful
   - (Repeats for all 10 students)
   - End Process → Send email with PDFs
4. Verify results:
   - Data\Output\ → 10 PDF files
   - Orchestrator Queue → All items "Successful"
   - Email inbox → 1 email with 10 attachments
```

### Running in Production (Orchestrator)

**Step 1: Publish Processes**
```
Dispatcher:
  - Open AddTestQueueItem.xaml
  - Publish → Publish to Orchestrator
  - Version: 1.0.0
  - Package Name: Dispatcher_MarksheetQueue

Performer:
  - Open Main.xaml
  - Publish → Publish to Orchestrator
  - Version: 1.0.0
  - Package Name: Performer_MarksheetGeneration
```

**Step 2: Create Processes in Orchestrator**
```
1. Automations → Processes → Add Process
2. Select: Dispatcher_MarksheetQueue package
3. Name: Dispatcher_MarksheetQueue
4. Create

5. Add Process again
6. Select: Performer_MarksheetGeneration package
7. Name: Performer_MarksheetGeneration
8. Create
```

**Step 3: Execute**
```
Option A: Manual Execution
  1. Start Job → Dispatcher_MarksheetQueue
  2. Wait for completion (30 seconds)
  3. Start Job → Performer_MarksheetGeneration
  4. Monitor in Jobs section

Option B: UiPath Assistant
  1. Open UiPath Assistant (system tray)
  2. Run → Dispatcher_MarksheetQueue
  3. Run → Performer_MarksheetGeneration
```

---

## 📊 Sample Data Format

The `Data/Input/Sample_Student_Data.csv` file should have these columns:

```csv
Name,RollNumber,DOB,Semester,Year,Department,Subject1,Mark1,Subject2,Mark2,Subject3,Mark3,Subject4,Mark4,Subject5,Mark5
Alice Johnson,2024001,15-Jan-2000,Fall 2024,2024,Computer Science,Mathematics,95,Physics,88,Chemistry,82,English,75,Programming,92
Bob Smith,2024002,20-Feb-2000,Fall 2024,2024,Electrical Engineering,Mathematics,78,Physics,85,Electronics,90,English,70,Programming,88
...
```

**10 test students are included** with varying marks to demonstrate all grade levels.

---

## 🔍 Workflow Details

### Dispatcher Workflow (AddTestQueueItem.xaml)

**Purpose:** Load student data from CSV and populate Orchestrator queue

**Steps:**
1. **Read CSV** → Load student records into DataTable
2. **Log Count** → Display number of students found
3. **For Each Row** → Iterate through student records
   - **Add Queue Item** → Create transaction with 16 fields:
     - Student info: Name, Roll Number, DOB, Semester, Year, Department
     - Subjects 1-5: Subject name, Mark (Int32)
   - **Reference:** Roll Number (unique identifier)
4. **Log Success** → Confirm queue population

**Variables:**
- `dtStudents` (DataTable): Student records
- `csvPath` (String): "Data\Input\Sample_Student_Data.csv"
- `queueName` (String): "MarksheetQueue"

---

### Performer Workflow (Process.xaml)

**Purpose:** Process each queue item to generate and verify PDF

**Steps:**

**1. Data Extraction (16 Assign activities)**
```vb
varName = in_TransactionItem.SpecificContent("Name").ToString
varRollNumber = in_TransactionItem.SpecificContent("RollNumber").ToString
... (14 more fields)
varMark1 = Convert.ToInt32(in_TransactionItem.SpecificContent("Mark1"))
... (4 more marks)
```

**2. Validation & Calculation (Invoke Code)**
```vb
' Validate marks (0-100)
' Calculate grades (A/B/C/D/E/F)
' Calculate GPA (average grade points)
' Outputs: varGrade1-5, varGPA
```

**3. Build PDF Path (Assign)**
```vb
varPDFPath = Path.Combine(
    in_Config("OutputFolderPath").ToString,
    "Marksheet_" + varRollNumber + "_" + DateTime.Now.ToString("yyyyMMddHHmmss") + ".pdf"
)
```

**4. Generate PDF (Invoke Code - Python)**
```vb
' Calls Python script with 24 parameters
' System.Diagnostics.Process to execute python.exe
' Arguments: student data, grades, GPA, output path
' Wait for completion
```

**5. Verify PDF (Path Exists + If)**
```vb
If pdfExists Then
    Log "PDF generated successfully"
Else
    Throw New BusinessRuleException("PDF generation failed")
End If
```

**Variables (23 total):**
- String: varName, varRollNumber, varDOB, varSemester, varYear, varDepartment, varSubject1-5, varGrade1-5, varPDFPath
- Int32: varMark1-5
- Double: varGPA

---

### Email Notification (Main.xaml - End Process)

**Purpose:** Send batch email with all generated PDFs after processing completes

**Implementation:**
```vb
' Get all PDF files
emailAttachments = Directory.GetFiles("Data\Output", "*.pdf")

' Send SMTP email
To: configured_recipient@gmail.com
Subject: "Marksheet Generation Complete - [Date]"
Body: Summary with PDF count and timestamp
Attachments: All PDFs in Output folder
```

---

## 🧪 Testing

### Unit Testing

**Test Python Script Independently:**
```powershell
cd F:\UiPath\Final Project
python Scripts\generate_marksheet.py

# Expected: test_marksheet.pdf created
# Verify: PDF opens, shows test student data
```

**Test Config Loading:**
```
1. Run Main.xaml with Debug
2. Check Output panel for "Config loaded successfully"
3. Verify in_Config dictionary populated
```

### Integration Testing

**Test with 1 Student:**
```
1. Manually add 1 queue item in Orchestrator
2. Run Main.xaml
3. Verify single PDF generated
4. Check queue item status: Successful
```

**Test with All 10 Students:**
```
1. Run Dispatcher → Queue populated
2. Run Performer → All processed
3. Verify:
   - 10 PDFs in Data\Output\
   - 10 queue items "Successful"
   - Email received with 10 attachments
```

### Error Testing

**Invalid Marks:**
```
Test case: Mark > 100 or Mark < 0
Expected: BusinessRuleException
Queue Status: Failed
Log: "Invalid marks for Subject X"
```

**Missing Python:**
```
Test case: Python not installed
Expected: Application Exception
Retry: 2 attempts
Queue Status: Failed after retries
```

**SMTP Failure:**
```
Test case: Wrong email password
Expected: Error logged in End Process
Result: PDFs still generated (email is bonus feature)
```

---

## 📈 Performance Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| **Processing Time** | ~5-8 seconds/student | Depends on system performance |
| **Throughput** | 10 students in ~60 seconds | Sequential processing |
| **Success Rate** | 100% (with valid data) | Robust error handling |
| **PDF Size** | ~15-20 KB each | Lightweight, optimized |
| **Queue Capacity** | Unlimited | Orchestrator queue scales |
| **Concurrent Execution** | Scalable | Can run multiple performers |

**Scalability:** 
- 100 students: ~10 minutes
- 1000 students: ~100 minutes (1.6 hours)
- Can be parallelized with multiple robot licenses

---

## 🛠️ Troubleshooting

### Common Issues & Solutions

**❌ Python Script Error: "reportlab not found"**
```
Solution:
  pip install reportlab
  Verify: pip show reportlab
```

**❌ Queue Error: "Queue not found"**
```
Solution:
  - Check queue name matches Config.xlsx: "MarksheetQueue"
  - Verify queue created in Orchestrator
  - Check case sensitivity
```

**❌ Email Error: "Username and Password not accepted"**
```
Solution:
  - For Gmail: Use App Password, not regular password
  - Steps:
    1. Enable 2-Factor Authentication
    2. Generate App Password: myaccount.google.com/apppasswords
    3. Use 16-character password (no spaces) in workflow
```

**❌ PDF Not Generated**
```
Solution:
  - Check Output folder exists: Data\Output\
  - Verify Python script path in Config.xlsx
  - Test Python script manually
  - Check file permissions
```

**❌ "in_Config not declared" Error**
```
Issue: Using in_Config in wrong scope (Main.xaml End Process)
Solution: Use hardcoded values in Main.xaml, in_Config only works in Framework workflows
```

**❌ Orchestrator Robot Error (#1230)**
```
Issue: Unattended robot not configured
Solution: Run from UiPath Studio or UiPath Assistant for degree project demo
```

---

## 📚 Key Learnings & Best Practices

### REFramework Patterns
- ✅ **Queue-based processing** for scalability and resume capability
- ✅ **Transaction isolation** - each student processed independently
- ✅ **Retry mechanism** - automatic handling of transient failures
- ✅ **Status tracking** - comprehensive logging in Orchestrator

### Python Integration
- ✅ **Command-line arguments** for parameter passing
- ✅ **Process execution** via System.Diagnostics.Process
- ✅ **Wait for exit** to ensure PDF completion
- ✅ **Error handling** with try-catch in Python script

### Data Validation
- ✅ **BusinessRuleException** for invalid data (skip item, continue processing)
- ✅ **ApplicationException** for system errors (retry, then fail)
- ✅ **Type conversion** with error handling (String to Int32)

### Configuration Management
- ✅ **Centralized config** in Config.xlsx
- ✅ **Relative paths** for portability
- ✅ **Environment-specific settings** easily configurable

---

## 🎓 Educational Value

This project demonstrates:

**UiPath Skills:**
- REFramework implementation and customization
- Queue-based transaction processing
- Orchestrator integration (queues, assets, logging)
- Error handling patterns (Business vs Application exceptions)
- Email automation with SMTP
- File system operations
- External application integration (Python)

**Programming Skills:**
- Python (ReportLab PDF generation)
- VB.NET (grade calculation, GPA logic)
- Data structures (dictionaries, arrays, DataTables)
- Process execution and inter-process communication

**Automation Design:**
- Dispatcher-Performer architecture
- Scalable queue processing
- Modular design (separation of concerns)
- Configuration-driven development
- Comprehensive error handling

---

## 🔮 Future Enhancements

### Potential Improvements

**1. Individual Student Emails**
- Send each student their own marksheet via email
- Requires email column in CSV
- Personalized subject and body

**2. Database Integration**
- Replace CSV with SQL Server/MySQL
- Real-time data sync with student information system
- Historical grade tracking

**3. Digital Signatures**
- Sign PDFs with digital certificates
- Integrate with institutional PKI
- QR code for verification

**4. Barcode/QR Code**
- Add unique QR code to each marksheet
- Enables online verification portal
- Anti-forgery measure

**5. Multi-Language Support**
- Generate marksheets in multiple languages
- Configurable language templates
- Unicode font support

**6. Dashboard & Analytics**
- Power BI integration for grade analytics
- Pass/fail statistics
- Department-wise performance metrics

**7. Watermarking**
- Add "PROVISIONAL" watermark
- Institutional logo overlay
- Security features

**8. Parallel Processing**
- Multi-robot execution for faster throughput
- Load balancing across robots
- Optimized for high-volume processing

---

## 📄 License

This project is created for educational purposes as part of a degree program.

**Usage:** Free for educational and non-commercial use  
**Restrictions:** Commercial use requires permission  
**Attribution:** Please credit original creator if modified/redistributed

---



## 🙏 Acknowledgments

- **UiPath Community** - For REFramework template and documentation
- **ReportLab** - For excellent Python PDF library
- **Python Community** - For robust ecosystem and libraries

---


