# `AVSpeechSynthesisVoice`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 7 properties, 3 instance methods, 6 class methods

## Instance variables

```
@"NSDictionary" _audioFileSettings;
```

## Properties

```
@property (T@"NSString",C,D,N) language;
@property (T@"NSString",&,D,N) identifier;
@property (T@"NSString",&,D,N) name;
@property (Tq,D,N) quality;
@property (Tq,D,N) gender;
@property (TQ,D,N) voiceTraits;
@property (T@"NSDictionary",R,N,V_audioFileSettings) audioFileSettings;
```

## Class methods

```
+[AVSpeechSynthesisVoice supportsSecureCoding];
+[AVSpeechSynthesisVoice initialize];
+[AVSpeechSynthesisVoice currentLanguageCode];
+[AVSpeechSynthesisVoice voiceWithIdentifier:];
+[AVSpeechSynthesisVoice speechVoices];
+[AVSpeechSynthesisVoice voiceWithLanguage:];
```

## Instance methods

```
-[AVSpeechSynthesisVoice encodeWithCoder:];
-[AVSpeechSynthesisVoice initWithCoder:];
-[AVSpeechSynthesisVoice audioFileSettings];
```
