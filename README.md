
# Spotify Charts Analyzer

This project allows you to analyze and visualize Spotify charts using Streamlit for the web interface. The project uses Spotify's API to fetch data, perform analysis, and present insights in an interactive way.

## Prerequisites

Before running the project, ensure you have the following:

- Python 3.11.5 (the project has been tested with this version)
- Spotify API credentials (Client ID and Client Secret)

## Setup

1. Obtain your Spotify API credentials by following these steps:
   - Go to https://developer.spotify.com/dashboard/login.
   - Log in with your Spotify account.
   - Click on "Create an App" and fill in the details.
   - After creating the app, you’ll receive your Client ID and Client Secret.

2. Set up your Spotify API credentials as environment variables by creating a `.env` file in the root directory of your project:

   ```
   SPOTIFY_CLIENT_ID=<YOUR_CLIENT_ID>
   SPOTIFY_CLIENT_SECRET=<YOUR_CLIENT_SECRET>
   ```

   Replace `<YOUR_CLIENT_ID>` and `<YOUR_CLIENT_SECRET>` with your actual Spotify API credentials.

3. Create a virtual environment:

   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   ```
   source venv/bin/activate
   ```

5. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the application locally, use the following command:

```
streamlit run main.py --server.port 8080 --server.address 0.0.0.0
```

This command starts the Streamlit application and makes it accessible at `http://localhost:8080`.

## Usage

1. Launch the application by accessing `http://localhost:8080` in your web browser.
2. Enter your Spotify Client ID and Client Secret, select a country or global chart, and analyze the top tracks or artists.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository, explaining your changes and their benefits.

## Contact

If you have any questions or suggestions regarding this project, please feel free to contact the project maintainer at neillakshmi@gmail.com
