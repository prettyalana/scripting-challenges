#!/usr/bin/env python3

from datetime import datetime, timezone

start_time = "2021-05-30 12:22:00"
end_time = "2021-05-30 12:33:12"

start_date_object = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S").replace(
    tzinfo=timezone.utc
)
end_date_object = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S").replace(
    tzinfo=timezone.utc
)


def find_all_requests():
    matching_requests = []
    with open(
        "apache_access", "r"
    ) as file:  # Context manager that opens the file and assigns it to the variable file. Closes once the code in the block ends.
        for line in file:
            open_bracket = line.find("[")
            closed_bracket = line.find("]")
            line_date = line[open_bracket + 1 : closed_bracket]
            line_date_object = datetime.strptime(line_date, "%d/%b/%Y:%H:%M:%S %z")

            if start_date_object <= line_date_object <= end_date_object:
                open_quote = line.find('"')
                closed_quote = line.find('"', open_quote + 1)
                requests = line[open_quote + 1 : closed_quote]
                matching_requests.append(requests)
    return len(matching_requests)


result = find_all_requests()
print(f"Requests: {result}")
