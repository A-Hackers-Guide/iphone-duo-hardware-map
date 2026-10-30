# `QSSTextToSpeechRouterStreamingStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechRouterStreamingStreamingResponse=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) content_type;
@property (T@"QSSBeginTextToSpeechStreamingResponse",R,N) contentAsQSSBeginTextToSpeechStreamingResponse;
@property (T@"QSSPartialTextToSpeechStreamingResponse",R,N) contentAsQSSPartialTextToSpeechStreamingResponse;
@property (T@"QSSFinalTextToSpeechStreamingResponse",R,N) contentAsQSSFinalTextToSpeechStreamingResponse;
```

## Instance methods

```
-[QSSTextToSpeechRouterStreamingStreamingResponse copyWithZone:];
-[QSSTextToSpeechRouterStreamingStreamingResponse addObjectToBuffer:];
-[QSSTextToSpeechRouterStreamingStreamingResponse content_type];
-[QSSTextToSpeechRouterStreamingStreamingResponse flatbuffData];
-[QSSTextToSpeechRouterStreamingStreamingResponse initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechRouterStreamingStreamingResponse initWithFlatbuffData:];
-[QSSTextToSpeechRouterStreamingStreamingResponse initWithFlatbuffData:root:];
-[QSSTextToSpeechRouterStreamingStreamingResponse initWithFlatbuffData:root:verify:];
-[QSSTextToSpeechRouterStreamingStreamingResponse contentAsQSSBeginTextToSpeechStreamingResponse];
-[QSSTextToSpeechRouterStreamingStreamingResponse contentAsQSSFinalTextToSpeechStreamingResponse];
-[QSSTextToSpeechRouterStreamingStreamingResponse contentAsQSSPartialTextToSpeechStreamingResponse];
```
