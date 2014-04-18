from collections import defaultdict

def rank_songs(songs_data, tempo):
    """ This calculates how well each song fits our data model.
        Abandoned when we realized that songs didn't fit our model at all. """
    positive_ratios = []

    for song in songs_data:
        # Counts the total number of times that a sequence of length PREV_NOTES
        # occurs in each song
        total_results = {}
    
        # Counts the number of times that each sequence of length PREV_NOTES
        # is followed by each note
        # ex. number of times an A follows a DC
        positive_results = defaultdict(lambda: defaultdict(int))

        for pitch_group in set(song.seg_pitches):
            (current_pitch, no_current_pitch) = current_pitch_data(pitch_group)
            total_results[no_current_pitch] = 0
            positive_results[no_current_pitch][current_pitch] = 0

        # Count the number of times each SongData.PREV_NOTES note sequence occurs
        # Count the number of times each pitch follows each SongData.PREV_PITCHES note sequence  
        for pitch_group in song.seg_pitches:
            (current_pitch, no_current_pitch) = current_pitch_data(pitch_group)
            total_results[no_current_pitch] += 1
            positive_results[no_current_pitch][current_pitch] += 1
    
        # Find the note that followed each SongData.PREV_PITCHES sequence the most times
        # Incremement the ratio of positive occurances to total occurences by the count for that note
        sum_positive_ratio = 0.0
        for pitch_group in set(song.seg_pitches):
            (current_pitch, no_current_pitch) = current_pitch_data(pitch_group)
            max_index = get_pitch_count(positive_results[no_current_pitch])
            sum_positive_ratio += float(positive_results[no_current_pitch][max_index]) / total_results[no_current_pitch]
    
        positive_ratios.append(sum_positive_ratio / float(len(set(song.seg_pitches))))


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
