# turtle_teleop_voice
- PCのマイクで録音された音声をGoogle Cloud Speech to Textで日本語文字列に変換します
- 変換した文字列の先頭一文字が「前後左右」のいずれかであれば、それぞれ前進、後退、左回転４５°、右回転45°の指示をTwist型のメッセージとして/turtle1/cmd_velのtopicにpublishします
- 認識された文字が「終」であればプログラムを終了します
- それ以外の文字は無視されます
