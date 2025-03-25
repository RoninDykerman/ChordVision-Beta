"""
This script runs the Test application using a development server.
"""

from Test import app

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)