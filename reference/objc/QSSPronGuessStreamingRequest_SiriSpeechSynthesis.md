# `QSSPronGuessStreamingRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{PronGuessStreamingRequest=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) content_type;
@property (T@"QSSStartPronGuessRequest",R,N) contentAsQSSStartPronGuessRequest;
@property (T@"QSSAudioPacket",R,N) contentAsQSSAudioPacket;
@property (T@"QSSFinishAudio",R,N) contentAsQSSFinishAudio;
@property (T@"QSSCancelRequest",R,N) contentAsQSSCancelRequest;
```

## Instance methods

```
-[QSSPronGuessStreamingRequest copyWithZone:];
-[QSSPronGuessStreamingRequest addObjectToBuffer:];
-[QSSPronGuessStreamingRequest content_type];
-[QSSPronGuessStreamingRequest flatbuffData];
-[QSSPronGuessStreamingRequest initAndVerifyWithFlatbuffData:];
-[QSSPronGuessStreamingRequest initWithFlatbuffData:];
-[QSSPronGuessStreamingRequest initWithFlatbuffData:root:];
-[QSSPronGuessStreamingRequest initWithFlatbuffData:root:verify:];
-[QSSPronGuessStreamingRequest contentAsQSSAudioPacket];
-[QSSPronGuessStreamingRequest contentAsQSSCancelRequest];
-[QSSPronGuessStreamingRequest contentAsQSSFinishAudio];
-[QSSPronGuessStreamingRequest contentAsQSSStartPronGuessRequest];
```
