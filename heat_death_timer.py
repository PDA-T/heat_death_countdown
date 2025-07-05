from datetime import datetime, timezone

# 1. 定义年数
heat_death_years = 10 ** 100
# 平年、闰年平均
seconds_per_year = 365.25 * 24 * 60 * 60

# 2. 总秒数
heat_death_seconds = int(heat_death_years * seconds_per_year)

# 3. 年龄
universe_age_years = 13_800_000_000

# 4. 年龄秒数
universe_age_seconds = int(universe_age_years * seconds_per_year)

# 5. 年龄截至时间
start_time = datetime(1970, 1, 1, tzinfo=timezone.utc)

# 6. 距离现在已经过去的秒数
now_time = datetime.now(timezone.utc)
elapsed_seconds_since_1970 = int((now_time - start_time).total_seconds())

# 7. 剩余秒数
remaining_seconds = heat_death_seconds - universe_age_seconds - elapsed_seconds_since_1970


def get_heat_death_seconds():
    # 只返回剩余秒数，每次调用刷新当前秒
    now_time = datetime.now(timezone.utc)
    elapsed_seconds_since_1970 = int((now_time - start_time).total_seconds())
    remaining_seconds = heat_death_seconds - universe_age_seconds - elapsed_seconds_since_1970
    return max(remaining_seconds, 0)
