# `QSSLanguageDetectionStreamingRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{LanguageDetectionStreamingRequest=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) content_type;
@property (T@"QSSStartLanguageDetectionRequest",R,N) contentAsQSSStartLanguageDetectionRequest;
@property (T@"QSSAudioPacket",R,N) contentAsQSSAudioPacket;
@property (T@"QSSFinishAudio",R,N) contentAsQSSFinishAudio;
```

## Instance methods

```
-[QSSLanguageDetectionStreamingRequest copyWithZone:];
-[QSSLanguageDetectionStreamingRequest addObjectToBuffer:];
-[QSSLanguageDetectionStreamingRequest content_type];
-[QSSLanguageDetectionStreamingRequest flatbuffData];
-[QSSLanguageDetectionStreamingRequest initAndVerifyWithFlatbuffData:];
-[QSSLanguageDetectionStreamingRequest initWithFlatbuffData:];
-[QSSLanguageDetectionStreamingRequest initWithFlatbuffData:root:];
-[QSSLanguageDetectionStreamingRequest initWithFlatbuffData:root:verify:];
-[QSSLanguageDetectionStreamingRequest contentAsQSSAudioPacket];
-[QSSLanguageDetectionStreamingRequest contentAsQSSFinishAudio];
-[QSSLanguageDetectionStreamingRequest contentAsQSSStartLanguageDetectionRequest];
```
