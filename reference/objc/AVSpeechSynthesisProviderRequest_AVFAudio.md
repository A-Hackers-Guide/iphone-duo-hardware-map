# `AVSpeechSynthesisProviderRequest`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"NSString" _ssmlRepresentation;
@"AVSpeechSynthesisProviderVoice" _voice;
```

## Properties

```
@property (T@"NSString",&,N,V_ssmlRepresentation) ssmlRepresentation;
@property (T@"AVSpeechSynthesisProviderVoice",&,N,V_voice) voice;
```

## Class methods

```
+[AVSpeechSynthesisProviderRequest supportsSecureCoding];
+[AVSpeechSynthesisProviderRequest initialize];
```

## Instance methods

```
-[AVSpeechSynthesisProviderRequest voice];
-[AVSpeechSynthesisProviderRequest encodeWithCoder:];
-[AVSpeechSynthesisProviderRequest setVoice:];
-[AVSpeechSynthesisProviderRequest initWithCoder:];
-[AVSpeechSynthesisProviderRequest copyWithZone:];
-[AVSpeechSynthesisProviderRequest initWithSSMLRepresentation:voice:];
-[AVSpeechSynthesisProviderRequest setSsmlRepresentation:];
-[AVSpeechSynthesisProviderRequest ssmlRepresentation];
```
