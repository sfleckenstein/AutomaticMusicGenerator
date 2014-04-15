from collections import defaultdict

def rank_songs(songs_data, tempo):
    # TODO make this work for multiple songs

    # Counts the total number of times that a sequence of length PREV_NOTES
    # occurs in each song
    total_results = {}

    # Counts the number of times that each sequence of length PREV_NOTES
    # is followed by each note
    # ex. number of times an A follows a DC
    positive_results = defaultdict(lambda: defaultdict(int))

    for song in songs_data:
        # TODO what set should I use here?
        for pitch_group in set(song.seg_pitches):
            (current_pitch, no_current_pitch) = current_pitch_data(pitch_group)
            total_results[no_current_pitch] = 0
            positive_results[no_current_pitch][current_pitch] = 0
  
    for song in songs_data:
        for pitch_group in song.seg_pitches:
            (current_pitch, no_current_pitch) = current_pitch_data(pitch_group)
            total_results[no_current_pitch] += 1
            positive_results[no_current_pitch][current_pitch] += 1

    sum_positive_ratio = 0.0
    for song in songs_data:
        for pitch_group in set(song.seg_pitches):
            (current_pitch, no_current_pitch) = current_pitch_data(pitch_group)
            max_index = get_pitch_count(positive_results[no_current_pitch])
            sum_positive_ratio += float(positive_results[no_current_pitch][max_index]) / total_results[no_current_pitch]

    positive_ratio = float(sum_positive_ratio) / float(len(set(song.seg_pitches)))

def current_pitch_data(pitch_group):
    current_note_index = pitch_group.find('|')
    return(pitch_group[0:current_note_index], pitch_group[current_note_index + 1:])


def get_pitch_count(positive_results):
    max_value = -1
    max_index = -1

    for pitch in positive_results:
        pitch_count = positive_results[pitch]
        if pitch_count > max_value:
            max_value = pitch_count
            max_index = pitch

    return max_index
