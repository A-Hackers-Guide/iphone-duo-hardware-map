# `AVSpeechSynthesisProviderVoice`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 8 instance variables, 8 properties, 19 instance methods, 3 class methods

## Instance variables

```
@"NSString" _name;
@"NSString" _identifier;
@"NSArray" _primaryLanguages;
@"NSArray" _supportedLanguages;
q _voiceSize;
@"NSString" _version;
q _gender;
q _age;
```

## Properties

```
@property (T@"NSString",&,N,V_name) name;
@property (T@"NSString",&,N,V_identifier) identifier;
@property (T@"NSArray",&,N,V_supportedLanguages) supportedLanguages;
@property (T@"NSArray",R,N,V_primaryLanguages) primaryLanguages;
@property (Tq,N,V_voiceSize) voiceSize;
@property (T@"NSString",&,N,V_version) version;
@property (Tq,N,V_gender) gender;
@property (Tq,N,V_age) age;
```

## Class methods

```
+[AVSpeechSynthesisProviderVoice supportsSecureCoding];
+[AVSpeechSynthesisProviderVoice initialize];
+[AVSpeechSynthesisProviderVoice updateSpeechVoices];
```

## Instance methods

```
-[AVSpeechSynthesisProviderVoice supportedLanguages];
-[AVSpeechSynthesisProviderVoice identifier];
-[AVSpeechSynthesisProviderVoice age];
-[AVSpeechSynthesisProviderVoice version];
-[AVSpeechSynthesisProviderVoice setIdentifier:];
-[AVSpeechSynthesisProviderVoice encodeWithCoder:];
-[AVSpeechSynthesisProviderVoice setGender:];
-[AVSpeechSynthesisProviderVoice setSupportedLanguages:];
-[AVSpeechSynthesisProviderVoice setName:];
-[AVSpeechSynthesisProviderVoice initWithCoder:];
-[AVSpeechSynthesisProviderVoice setVersion:];
-[AVSpeechSynthesisProviderVoice copyWithZone:];
-[AVSpeechSynthesisProviderVoice name];
-[AVSpeechSynthesisProviderVoice gender];
-[AVSpeechSynthesisProviderVoice setAge:];
-[AVSpeechSynthesisProviderVoice initWithName:identifier:primaryLanguages:supportedLanguages:];
-[AVSpeechSynthesisProviderVoice primaryLanguages];
-[AVSpeechSynthesisProviderVoice setVoiceSize:];
-[AVSpeechSynthesisProviderVoice voiceSize];
```
