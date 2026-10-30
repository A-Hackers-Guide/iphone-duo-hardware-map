# `QSSMultilingualStreamingRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{MultilingualStreamingRequest=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) content_type;
@property (T@"QSSStartMultilingualSpeechRequest",R,N) contentAsQSSStartMultilingualSpeechRequest;
@property (T@"QSSUpdateAudioInfo",R,N) contentAsQSSUpdateAudioInfo;
@property (T@"QSSSetRequestOrigin",R,N) contentAsQSSSetRequestOrigin;
@property (T@"QSSSetSpeechContext",R,N) contentAsQSSSetSpeechContext;
@property (T@"QSSSetSpeechProfile",R,N) contentAsQSSSetSpeechProfile;
@property (T@"QSSAudioPacket",R,N) contentAsQSSAudioPacket;
@property (T@"QSSFinishAudio",R,N) contentAsQSSFinishAudio;
@property (T@"QSSLanguageDetected",R,N) contentAsQSSLanguageDetected;
```

## Instance methods

```
-[QSSMultilingualStreamingRequest copyWithZone:];
-[QSSMultilingualStreamingRequest addObjectToBuffer:];
-[QSSMultilingualStreamingRequest content_type];
-[QSSMultilingualStreamingRequest flatbuffData];
-[QSSMultilingualStreamingRequest initAndVerifyWithFlatbuffData:];
-[QSSMultilingualStreamingRequest initWithFlatbuffData:];
-[QSSMultilingualStreamingRequest initWithFlatbuffData:root:];
-[QSSMultilingualStreamingRequest initWithFlatbuffData:root:verify:];
-[QSSMultilingualStreamingRequest contentAsQSSAudioPacket];
-[QSSMultilingualStreamingRequest contentAsQSSFinishAudio];
-[QSSMultilingualStreamingRequest contentAsQSSLanguageDetected];
-[QSSMultilingualStreamingRequest contentAsQSSSetRequestOrigin];
-[QSSMultilingualStreamingRequest contentAsQSSSetSpeechContext];
-[QSSMultilingualStreamingRequest contentAsQSSSetSpeechProfile];
-[QSSMultilingualStreamingRequest contentAsQSSStartMultilingualSpeechRequest];
-[QSSMultilingualStreamingRequest contentAsQSSUpdateAudioInfo];
```
