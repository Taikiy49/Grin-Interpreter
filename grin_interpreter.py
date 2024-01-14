import read
import grin


def main() -> None:
    """The main function that executes the Grin interpreter."""
    try:
        read.run_program()
    except grin.GrinParseError:
        print("Parsing error occurred...")
    except grin.GrinLexError:
        print("Lexing error occurred...")
    except ZeroDivisionError:
        print('Cannot divide integers or floats by 0.')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
