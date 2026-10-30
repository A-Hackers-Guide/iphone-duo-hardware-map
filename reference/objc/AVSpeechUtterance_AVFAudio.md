# `AVSpeechUtterance`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 9 instance variables, 9 properties, 24 instance methods, 5 class methods

## Instance variables

```
@"AVSpeechSynthesisVoice" _voice;
B _prefersAssistiveTechnologySettings;
f _rate;
f _pitchMultiplier;
f _volume;
@"NSString" _speechString;
@"NSAttributedString" _attributedSpeechString;
d _preUtteranceDelay;
d _postUtteranceDelay;
```

## Properties

```
@property (T@"NSString",&,N,V_speechString) speechString;
@property (T@"NSAttributedString",&,N,V_attributedSpeechString) attributedSpeechString;
@property (T@"AVSpeechSynthesisVoice",&,N,V_voice) voice;
@property (Tf,N,V_rate) rate;
@property (Tf,N,V_pitchMultiplier) pitchMultiplier;
@property (Tf,N,V_volume) volume;
@property (TB,N,V_prefersAssistiveTechnologySettings) prefersAssistiveTechnologySettings;
@property (Td,N,V_preUtteranceDelay) preUtteranceDelay;
@property (Td,N,V_postUtteranceDelay) postUtteranceDelay;
```

## Class methods

```
+[AVSpeechUtterance supportsSecureCoding];
+[AVSpeechUtterance initialize];
+[AVSpeechUtterance speechUtteranceWithAttributedString:];
+[AVSpeechUtterance speechUtteranceWithString:];
+[AVSpeechUtterance speechUtteranceWithSSMLRepresentation:];
```

## Instance methods

```
-[AVSpeechUtterance initWithAttributedString:];
-[AVSpeechUtterance rate];
-[AVSpeechUtterance initWithString:];
-[AVSpeechUtterance voice];
-[AVSpeechUtterance volume];
-[AVSpeechUtterance setVolume:];
-[AVSpeechUtterance setRate:];
-[AVSpeechUtterance encodeWithCoder:];
-[AVSpeechUtterance setVoice:];
-[AVSpeechUtterance initWithCoder:];
-[AVSpeechUtterance copyWithZone:];
-[AVSpeechUtterance setPitchMultiplier:];
-[AVSpeechUtterance pitchMultiplier];
-[AVSpeechUtterance attributedSpeechString];
-[AVSpeechUtterance initWithSSMLRepresentation:];
-[AVSpeechUtterance postUtteranceDelay];
-[AVSpeechUtterance preUtteranceDelay];
-[AVSpeechUtterance prefersAssistiveTechnologySettings];
-[AVSpeechUtterance setAttributedSpeechString:];
-[AVSpeechUtterance setSpeechString:];
-[AVSpeechUtterance speechString];
-[AVSpeechUtterance setPostUtteranceDelay:];
-[AVSpeechUtterance setPreUtteranceDelay:];
-[AVSpeechUtterance setPrefersAssistiveTechnologySettings:];
```
