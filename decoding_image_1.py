import subprocess

image_path = "pdf-417.png"
command = [
    "java", "-cp", "javase-3.5.0.jar:core-3.5.0.jar:jcommander-1.82.jar",
    "com.google.zxing.client.j2se.CommandLineRunner", image_path
]

result = subprocess.run(command, capture_output=True, text=True)

if result.returncode == 0:
    print(result.stdout)
else:
    print(f"Error: {result.stderr}")
