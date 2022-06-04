from barcode.base import Barcode
import barcode


def generate_barcode(card_number, filename):
    try:
        Barcode.default_writer_options["write_text"] = False

        CODE128 = barcode.get_barcode_class("code128")
        my_code = CODE128(card_number)
        my_code.save(filename)
        return True
    except:
        print(f"generate_barcode: {card_number}, {filename}")
        return False


def _find_which_barcode_class():
    barcodes = barcode.PROVIDED_BARCODES

    n = "980193539660062734010074546419"
    n2 = n[-17:]

    for code in barcodes:
        try:
            classname = barcode.get_barcode_class(code)
            my = classname(n)
            my2 = classname(n2)
            my.save(f"barcode_{code}_n")
            my2.save(f"barcode_{code}_n2")
        except:
            pass
