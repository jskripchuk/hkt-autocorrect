import hkt_generator
import random
import os

script_dir = os.path.dirname(__file__)
harmony_hkt = hkt_generator.HKTObject(os.path.join(script_dir,"harmony.hkt"))
melody_hkt = hkt_generator.HKTObject(os.path.join(script_dir,"melody.hkt"))
prob = float(input("Autocorrect Probability [0-1]: "))



#harmony_path = "data-files/autocorrect/autocorrect_harmony.hkt"
#melody_path = "data-files/autocorrect/autocorrect_melody.hkt"

#harmony_hkt = hkt_generator.HKTObject(harmony_path)
harmony = harmony_hkt.segments[0].chords
#melody_hkt = hkt_generator.HKTObject(melody_path)
melody = melody_hkt.segments[0].melody

#DOES NOT ACCOUNT FOR BORROWED CHORDS
for chord in harmony:
    zero_root = int(chord.scale_degree)-1
    third = ((zero_root+2)%7)+1
    fifth = ((zero_root+4)%7)+1
    #third = ((int(chord.scale_degree)+2)%8)
    #print(str(chord.scale_degree)+", "+str(third)+", "+str(fifth))

    chord.tones = [int(chord.scale_degree),third,fifth]

#for chord in harmony:
    #print(str(chord.tones)+", "+str(int(chord.start_beat_abs)+int(chord.chord_duration)))

def pick_closest(tones, note_degree):
    smallest_diff = 99999
    smallest_note = note_degree
    current_index = 0

    while current_index < len(tones):

        #print()
        diff = min(abs(note_degree-(tones[current_index]+7)), abs(note_degree-tones[current_index]))
        #diff = abs(note_degree-tones[current_index])
        #print(diff)
        if diff < smallest_diff:
            smallest_diff = diff
            smallest_note = tones[current_index]
        current_index+=1

    #print(smallest_note)
    return smallest_note


#pick_closest([1,3,5],6)

#for note in melody:
    #print(note.start_beat_abs)
def autocorrect(chord,note,prob):
    #print(str(chord.tones) +", "+str(note.scale_degree))

    if int(note.scale_degree) not in chord.tones and prob >= random.uniform(0, 1):
        #print(str(chord.tones) +", "+str(note.scale_degree))
        #print("AUTOCORRECTED")
        return "["+note.scale_degree+"->"+str(pick_closest(chord.tones,int(note.scale_degree)))+"]"
        #return 999
    else:
        return note.scale_degree

current_note_num = 0
current_note = melody[current_note_num]
for chord in harmony:
    #print(chord.tones)
    chord_end = int(chord.start_beat_abs)+int(chord.chord_duration)
    #print("CHORD END: "+str(chord_end))

    while(int(current_note.start_beat_abs) < chord_end and current_note_num+1 < len(melody)):
        #print("CURRENT NOTE: "+str(current_note_num))
        #print("NOTE START: "+str(current_note.start_beat_abs))

        #print(current_note.scale_degree)
        current_note.scale_degree = autocorrect(chord,current_note,prob)
        current_note_num+=1
        current_note = melody[current_note_num]

        if(current_note_num == len(melody)-1):
            current_note.scale_degree = autocorrect(chord,current_note,prob)


    #print(current_note.scale_degree)
    #while(current_note.start_beat_abs < )
cat = ""
for note in melody:
    cat+=note.scale_degree+', '
    #print(note.scale_degree)

print(cat)

    #print(note.scale_degree)
#print(harmony.segments[0].chords)
