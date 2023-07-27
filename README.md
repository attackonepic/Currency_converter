# Currency Converter GUI

This repository contains a simple currency converter graphical user interface (GUI) built using the Tkinter library in Python. The program allows users to convert an amount from one currency to another based on the latest exchange rates obtained from the exchangeratesapi.io API.

## Requirements

To run this program, you need to have Python installed on your system. The program uses the following Python libraries, which are generally included in the standard library:

- Tkinter: Provides the GUI functionality.
- ttk: Contains themed widget elements for Tkinter.
- requests: Used to fetch data from the exchangeratesapi.io API.
- json: Used to handle JSON data.

## Usage

1. Clone the repository to your local machine using Git or download the code as a ZIP file and extract it.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the `currency_converter.py` script using Python:

```
python currency_converter.py
```

4. The GUI window will open, displaying a currency converter application.

## Functionality

- The application fetches the latest exchange rates from the exchangeratesapi.io API on startup.
- The user can select the source currency from the "From" dropdown (currently set to "Euros").
- The user can select the target currency from the "To" dropdown (a list of currencies is provided).
- The user can enter the amount to be converted in the provided entry field.
- After entering the amount and selecting the source and target currencies, clicking the "Convert" button will display the converted amount in the result box.
- The result is calculated based on the latest exchange rates fetched from the API.

## Notes

- The exchange rates data is fetched from the exchangeratesapi.io API using a free access key. Make sure you have a stable internet connection to access the API.
- The provided `moneda.ico` file is used as the application's icon. You can replace it with your desired icon file or use the default Tkinter icon.

## License

This project is open-source and available under the [MIT License](LICENSE).

Feel free to use, modify, and distribute the code as you see fit. If you find any issues or want to contribute to the project, please feel free to create a pull request or open an issue on the repository.

Enjoy using the currency converter GUI!
