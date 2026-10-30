# `AVSpeechSynthesisMarker`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 20 instance methods, 2 class methods

## Instance variables

```
q _mark;
Q _byteSampleOffset;
@"NSString" _bookmarkName;
@"NSString" _phoneme;
{_NSRange="location"Q"length"Q} _textRange;
```

## Properties

```
@property (Tq,N,V_mark) mark;
@property (TQ,N,V_byteSampleOffset) byteSampleOffset;
@property (T{_NSRange=QQ},N,V_textRange) textRange;
@property (T@"NSString",C,N,V_bookmarkName) bookmarkName;
@property (T@"NSString",C,N,V_phoneme) phoneme;
```

## Class methods

```
+[AVSpeechSynthesisMarker supportsSecureCoding];
+[AVSpeechSynthesisMarker initialize];
```

## Instance methods

```
-[AVSpeechSynthesisMarker mark];
-[AVSpeechSynthesisMarker textRange];
-[AVSpeechSynthesisMarker setTextRange:];
-[AVSpeechSynthesisMarker encodeWithCoder:];
-[AVSpeechSynthesisMarker initWithCoder:];
-[AVSpeechSynthesisMarker copyWithZone:];
-[AVSpeechSynthesisMarker phoneme];
-[AVSpeechSynthesisMarker bookmarkName];
-[AVSpeechSynthesisMarker byteSampleOffset];
-[AVSpeechSynthesisMarker initWithBookmarkName:atByteSampleOffset:];
-[AVSpeechSynthesisMarker initWithMarkerType:forTextRange:atByteSampleOffset:];
-[AVSpeechSynthesisMarker initWithParagraphRange:atByteSampleOffset:];
-[AVSpeechSynthesisMarker initWithPhonemeString:atByteSampleOffset:];
-[AVSpeechSynthesisMarker initWithSentenceRange:atByteSampleOffset:];
-[AVSpeechSynthesisMarker initWithWordRange:atByteSampleOffset:];
-[AVSpeechSynthesisMarker setBookmarkName:];
-[AVSpeechSynthesisMarker setByteSampleOffset:];
-[AVSpeechSynthesisMarker setMark:];
-[AVSpeechSynthesisMarker setPhoneme:];
-[AVSpeechSynthesisMarker initWithMarkerType:name:forTextRange:atByteSampleOffset:];
```
