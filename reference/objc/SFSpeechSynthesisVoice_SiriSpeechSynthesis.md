# `SFSpeechSynthesisVoice`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 16 instance methods, 5 class methods

## Instance variables

```
B _isDefault;
@"NSLocale" _locale;
@"NSString" _gender;
@"NSString" _name;
q _voiceType;
q _voiceReleaseType;
@"SFSSVoiceAsset" _voiceAsset;
@"SFSSResourceAsset" _resourceAsset;
@"SFSpeechSynthesisServerVoiceConfig" _serverVoiceConfig;
```

## Properties

```
@property (TB,R,N,V_isDefault) isDefault;
@property (Tq,N,V_voiceType) voiceType;
@property (Tq,N,V_voiceReleaseType) voiceReleaseType;
@property (T@"SFSSVoiceAsset",&,N,V_voiceAsset) voiceAsset;
@property (T@"SFSSResourceAsset",&,N,V_resourceAsset) resourceAsset;
@property (T@"SFSpeechSynthesisServerVoiceConfig",&,N,V_serverVoiceConfig) serverVoiceConfig;
@property (T@"NSLocale",R,N,V_locale) locale;
@property (T@"NSString",R,N,V_gender) gender;
@property (T@"NSString",R,N,V_name) name;
```

## Class methods

```
+[SFSpeechSynthesisVoice initialize];
+[SFSpeechSynthesisVoice supportedLocales];
+[SFSpeechSynthesisVoice getVoiceByName:];
+[SFSpeechSynthesisVoice getDefaultVoiceByLocale:];
+[SFSpeechSynthesisVoice supportedVoicesByLocale:];
```

## Instance methods

```
-[SFSpeechSynthesisVoice locale];
-[SFSpeechSynthesisVoice isDefault];
-[SFSpeechSynthesisVoice name];
-[SFSpeechSynthesisVoice gender];
-[SFSpeechSynthesisVoice setVoiceType:];
-[SFSpeechSynthesisVoice voiceType];
-[SFSpeechSynthesisVoice initWithVoiceAsset:resourceAsset:];
-[SFSpeechSynthesisVoice init:gender:name:isDefault:];
-[SFSpeechSynthesisVoice resourceAsset];
-[SFSpeechSynthesisVoice serverVoiceConfig];
-[SFSpeechSynthesisVoice setResourceAsset:];
-[SFSpeechSynthesisVoice setServerVoiceConfig:];
-[SFSpeechSynthesisVoice setVoiceAsset:];
-[SFSpeechSynthesisVoice setVoiceReleaseType:];
-[SFSpeechSynthesisVoice voiceAsset];
-[SFSpeechSynthesisVoice voiceReleaseType];
```
