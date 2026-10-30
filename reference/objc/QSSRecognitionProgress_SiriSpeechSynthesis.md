# `QSSRecognitionProgress`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{RecognitionProgress=[1C]} _root;
```

## Properties

```
@property (Ti,R,N) processed_audio_duration_ms;
@property (T@"NSString",R,N) speech_id;
```

## Instance methods

```
-[QSSRecognitionProgress copyWithZone:];
-[QSSRecognitionProgress addObjectToBuffer:];
-[QSSRecognitionProgress flatbuffData];
-[QSSRecognitionProgress initAndVerifyWithFlatbuffData:];
-[QSSRecognitionProgress initWithFlatbuffData:];
-[QSSRecognitionProgress initWithFlatbuffData:root:];
-[QSSRecognitionProgress initWithFlatbuffData:root:verify:];
-[QSSRecognitionProgress speech_id];
-[QSSRecognitionProgress processed_audio_duration_ms];
```
