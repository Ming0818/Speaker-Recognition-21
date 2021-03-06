import pyaudio
import wave
import configs
import sys

def recordAudio(time, output_filename):
    FORMAT = pyaudio.paInt16

    p = pyaudio.PyAudio()

    stream = p.open(format = FORMAT,
                    channels = configs.channels,
                    rate = configs.rate,
                    input = True,
                    frames_per_buffer = configs.chunk)

    str = input('Press Enter to begin recording.')

    print("* recording")

    frames = []

    for i in range(0, int(configs.rate / configs.chunk * time)):
        data = stream.read(configs.chunk, exception_on_overflow = False)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(output_filename, 'wb')
    wf.setnchannels(configs.channels)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(configs.rate)
    wf.writeframes(b''.join(frames))
    wf.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Error arguments! Please used as "python record.py TIME OUTPUT_FILE"')
        exit()
    recordAudio(int(sys.argv[1]), sys.argv[2])
    