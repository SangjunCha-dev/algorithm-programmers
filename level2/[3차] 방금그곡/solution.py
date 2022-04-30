def solution(m, musicinfos):
    answer = ''
    musics = {
        'title': None,
        'play_time': 0,
    }

    m = m.replace('C#', 'H')\
         .replace('D#', 'I')\
         .replace('F#', 'J')\
         .replace('G#', 'K')\
         .replace('A#', 'L')

    for info in musicinfos:
        # 전처리
        music = info.split(',')

        hours = (int(music[1][:2]) - int(music[0][:2]))
        minutes = int(music[1][3:]) - int(music[0][3:])
        play_time = hours*60 + minutes

        title = music[2]

        # C#, D#, F#, G#, A# 문자 변환
        origin_melody = music[3].replace('C#', 'H')\
                                .replace('D#', 'I')\
                                .replace('F#', 'J')\
                                .replace('G#', 'K')\
                                .replace('A#', 'L')

        share, remainder = play_time//len(origin_melody), play_time%len(origin_melody)
        melody = origin_melody*share + origin_melody[:remainder]

        # 멜로디 찾기
        result = melody.find(m)
        if -1 != result:
            if musics['play_time'] < play_time:
                musics['title'] = title
                musics['play_time'] = play_time

    answer = musics['title'] if musics['title'] else '(None)'
    return answer