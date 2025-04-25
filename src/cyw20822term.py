import serial
import threading
import sys
import time

def read_from_port(ser, stop_event):
    while not stop_event.is_set():
        try:
            if ser.is_open and ser.in_waiting:
                print(ser.readline().decode(), end='')
            time.sleep(0.01)  # Small delay to prevent CPU hogging
        except:
            break

def main():
    if len(sys.argv) != 2:
        print("Usage: python cyw20822term.py <COM_PORT>")
        print("Example: python cyw20822term.py COM14")
        sys.exit(1)

    port = sys.argv[1].upper()  # Convert to uppercase for consistency
    if not port.startswith("COM"):
        port = "COM" + port.strip("com")  # Handle both formats: 14 or COM14
    
    try:
        ser = serial.Serial(port, 115200, timeout=1)
    except serial.SerialException as e:
        print(f"Error opening port {port}: {e}")
        sys.exit(1)

    stop_event = threading.Event()
    
    # Start reading thread
    thread = threading.Thread(target=read_from_port, args=(ser, stop_event))
    thread.daemon = True
    thread.start()
    
    # Main loop for sending
    try:
        while True:
            cmd = input()
            if cmd:
                ser.write((cmd + '\r\n').encode())
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        stop_event.set()  # Signal the thread to stop
        time.sleep(0.1)   # Give thread time to finish
        if ser.is_open:
            ser.close()    # Close the serial port
        print("Port closed")

if __name__ == '__main__':
    main()