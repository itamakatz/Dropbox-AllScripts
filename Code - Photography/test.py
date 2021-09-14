import os
import msvcrt

cwd = os.getcwd()
print(os.path.basename(cwd))

def wait_input_to_exit():
    msvcrt.getch()

print("\nPlease press any key to exit");
wait_input_to_exit();
