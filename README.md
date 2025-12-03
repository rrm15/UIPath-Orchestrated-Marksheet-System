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
┌─────────────────┐                      ┌────────────────── ┐
│ Read CSV File   │                      │  REFramework      │
│ Parse Student   │                      │  Main.xaml        │
│ Data            │                      │                   │
│ Populate Queue  │                      │  ├── Initialize   │
|                 │                      │  ├── Get Trans.   │
└─────────────────┘                      │  ├── Process      │
                                         │  │   ├── Validate │
                                         │  │   ├── Calculate│
                                         │  │   ├── Generate │
                                         │  │   └── Verify   │
                                         │  └── End Process  │
                                         │      └── Email    │
                                         └────────────────── ┘
                                                   ↓
                                         ┌──────────────────┐
                                         │  OUTPUT          │
                                         │  ├── PDFs        │
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
- **Dual email modes:**
  - **Individual emails:** Personalized emails to each student with their marksheet
  - **Bulk admin email:** Single email to administrator with all marksheets
- **Custom Input Dialog:** Interactive checkbox UI at runtime for email configuration
- **Dynamic Orchestrator Assets:** Email preferences stored and retrieved from Orchestrator
- **Conditional logic:** Workflows adapt based on user selection (individual/bulk/both)
- **Personalized content:**
  - Student-specific email addresses (`rollnumber@rajalakshmi.edu.in`)
  - Custom subject lines with roll numbers
  - Detailed grade summaries in email body
- **SMTP integration** with Outlook/Gmail
- **Professional plain-text formatting** (email-client compatible)
- **Configurable recipients** and institutional branding

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
   - PDFs in Data\Output\
   - queue items "Successful"
   - Email received with attachments
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
Issue: Unattended robot not configured or setup primarily due to license constraints or windows permissions
Solution: Run from UiPath Studio or UiPath Assistant 
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

**1. Database Integration**
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
**Attribution:** Please credit original creator (me) if modified/redistributed

---



## 🙏 Acknowledgments

- **UiPath Community** - For REFramework template and documentation
- **ReportLab** - For excellent Python PDF library
- **Python Community** - For robust ecosystem and libraries

---


