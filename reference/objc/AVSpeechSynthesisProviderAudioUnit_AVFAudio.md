# `AVSpeechSynthesisProviderAudioUnit`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AUAudioUnit`
- 2 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _speechVoices;
@? _speechSynthesisOutputMetadataBlock;
```

## Properties

```
@property (T@"NSArray",&,N,V_speechVoices) speechVoices;
@property (T@?,C,N,V_speechSynthesisOutputMetadataBlock) speechSynthesisOutputMetadataBlock;
```

## Class methods

```
+[AVSpeechSynthesisProviderAudioUnit initialize];
```

## Instance methods

```
-[AVSpeechSynthesisProviderAudioUnit speechSynthesisOutputMetadataBlock];
-[AVSpeechSynthesisProviderAudioUnit setSpeechSynthesisOutputMetadataBlock:];
-[AVSpeechSynthesisProviderAudioUnit cancelSpeechRequest];
-[AVSpeechSynthesisProviderAudioUnit speechVoices];
-[AVSpeechSynthesisProviderAudioUnit synthesizeSpeechRequest:];
-[AVSpeechSynthesisProviderAudioUnit setSpeechVoices:];
```
