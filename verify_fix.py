import sys
import os
import io

# Redirect stdout to a file
sys.stdout = open("debug_output_3.txt", "w", encoding="utf-8")
sys.stderr = sys.stdout

sys.path.append(os.path.join(os.getcwd(), 'backend'))

try:
    print("Starting verification with NEW token...")
    from generator import ImageGenerator
    print("Successfully imported ImageGenerator")
    
    gen = ImageGenerator()
    print("Initialised ImageGenerator")
    
    # Try a simple generation
    print("Attempting generation...")
    img, error = gen.generate("a small red apple")
    
    if error:
        print(f"FAILED: {error}")
        sys.exit(1)
        
    if img:
        print("SUCCESS: Image generated yay!")
    else:
        print("FAILED: No image and no error?")
        sys.exit(1)

except ImportError as e:
    print(f"Import Error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Exception: {e}")
    sys.exit(1)
