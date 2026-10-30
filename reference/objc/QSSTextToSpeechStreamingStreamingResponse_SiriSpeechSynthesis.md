# `QSSTextToSpeechStreamingStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechStreamingStreamingResponse=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) content_type;
@property (T@"QSSQssAckResponse",R,N) contentAsQSSQssAckResponse;
@property (T@"QSSBeginTextToSpeechStreamingResponse",R,N) contentAsQSSBeginTextToSpeechStreamingResponse;
@property (T@"QSSPartialTextToSpeechStreamingResponse",R,N) contentAsQSSPartialTextToSpeechStreamingResponse;
@property (T@"QSSFinalTextToSpeechStreamingResponse",R,N) contentAsQSSFinalTextToSpeechStreamingResponse;
```

## Instance methods

```
-[QSSTextToSpeechStreamingStreamingResponse copyWithZone:];
-[QSSTextToSpeechStreamingStreamingResponse addObjectToBuffer:];
-[QSSTextToSpeechStreamingStreamingResponse content_type];
-[QSSTextToSpeechStreamingStreamingResponse flatbuffData];
-[QSSTextToSpeechStreamingStreamingResponse initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechStreamingStreamingResponse initWithFlatbuffData:];
-[QSSTextToSpeechStreamingStreamingResponse initWithFlatbuffData:root:];
-[QSSTextToSpeechStreamingStreamingResponse initWithFlatbuffData:root:verify:];
-[QSSTextToSpeechStreamingStreamingResponse contentAsQSSBeginTextToSpeechStreamingResponse];
-[QSSTextToSpeechStreamingStreamingResponse contentAsQSSFinalTextToSpeechStreamingResponse];
-[QSSTextToSpeechStreamingStreamingResponse contentAsQSSPartialTextToSpeechStreamingResponse];
-[QSSTextToSpeechStreamingStreamingResponse contentAsQSSQssAckResponse];
```
