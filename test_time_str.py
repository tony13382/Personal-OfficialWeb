#!/usr/bin/env python3
"""測試 time_str 邏輯"""

def old_logic(startdate, enddate):
    """原本的邏輯"""
    time_str = ""
    if startdate is None and enddate is None:
        time_str = ""
    elif enddate is None:
        time_str = f"{startdate} ~ Present"
    else:
        time_str = f"{startdate} ~ {enddate}"
    return time_str

def new_logic(startdate, enddate):
    """新的邏輯"""
    time_str = ""
    if startdate is None and enddate is None:
        time_str = ""
    elif startdate and enddate:
        time_str = f"{startdate} ~ {enddate}"
    elif startdate:
        time_str = f"{startdate} ~ Present"
    elif enddate:
        time_str = f"~ {enddate}"
    return time_str

# 測試案例
test_cases = [
    (None, None, "都是 None"),
    ("2024/08", "Present", "正常日期範圍"),
    ("2024/08", None, "只有開始日期"),
    (None, "2024/12", "只有結束日期"),
    ("", "", "空字串"),
    ("", None, "開始是空字串，結束是 None"),
    (None, "", "開始是 None，結束是空字串"),
]

print("=" * 60)
print("測試結果對比")
print("=" * 60)
for startdate, enddate, desc in test_cases:
    old = old_logic(startdate, enddate)
    new = new_logic(startdate, enddate)
    print(f"\n{desc}:")
    print(f"  startdate={repr(startdate)}, enddate={repr(enddate)}")
    print(f"  舊邏輯: '{old}'")
    print(f"  新邏輯: '{new}'")
    if old != new:
        print(f"  ⚠️  結果不同！")
