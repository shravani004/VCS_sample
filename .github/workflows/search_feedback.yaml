name: Test Search Feedback Script
on: [push]
jobs:
  test-search-feedback:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install expect
        run: sudo apt-get update && sudo apt-get install expect -y
      - name: Run Python script with expect
        run: |
          expect -c "
            spawn python search_feedback.py
            expect \"Enter name to search (leave blank for all): \"
            send \"John\r\"
            interact
          "
