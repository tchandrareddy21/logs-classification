from pipeline.regex_classifier import classify_with_regex
from pipeline.ml_classifier import classify_with_ml
from pipeline.llm_classifier import classify_with_llm


if __name__ == "__main__":
    # print(classify_with_regex("Backup completed successfully."))
    # print(classify_with_regex("Account with ID 1234 created by User1."))
    # print(classify_with_regex("Hey Bro, chill ya!"))

    # logs = [
    #     "alpha.osapi_compute.wsgi.server - 12.10.11.1 - API returned 404 not found error",
    #     "GET /v2/3454/servers/detail HTTP/1.1 RCODE   404 len: 1583 time: 0.1878400",
    #     "System crashed due to drivers errors when restarting the server",
    #     "Hey bro, chill ya!",
    #     "Multiple login failures occurred on user 6454 account",
    #     "Server A790 was restarted unexpectedly during the process of data transfer"
    # ]
    # for log in logs:
    #     label = classify_with_ml(log)
    #     print(log, "->", label)

    print(classify_with_llm(
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classify_with_llm(
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
    print(classify_with_llm("System reboot initiated by user 12345."))