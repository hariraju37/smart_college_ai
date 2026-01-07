# smart_college_ai

CHECKPOINT 1
smart_college_ai/
│
├── app.py                  # main server
├── config.py               # API keys
├── requirements.txt
│
├── agent/
│   ├── planner.py          # task planning (agentic brain)
│   ├── memory.py           # student behavior memory
│   └── decision.py         # priority & actions
│
├── tools/
│   ├── notice_reader.py    # PDF/notice reading
│   ├── calendar_tool.py    # add deadlines
│   └── reminder.py         # notifications
│
├── data/
│   ├── students.db
│   └── notices/
│
└── logs/
