# `QSSBatchRecoverStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{BatchRecoverStreamingResponse=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) content_type;
@property (T@"QSSPronGuessResponse",R,N) contentAsQSSPronGuessResponse;
@property (T@"QSSBatchRecoverFinalResponse",R,N) contentAsQSSBatchRecoverFinalResponse;
```

## Instance methods

```
-[QSSBatchRecoverStreamingResponse copyWithZone:];
-[QSSBatchRecoverStreamingResponse addObjectToBuffer:];
-[QSSBatchRecoverStreamingResponse content_type];
-[QSSBatchRecoverStreamingResponse flatbuffData];
-[QSSBatchRecoverStreamingResponse initAndVerifyWithFlatbuffData:];
-[QSSBatchRecoverStreamingResponse initWithFlatbuffData:];
-[QSSBatchRecoverStreamingResponse initWithFlatbuffData:root:];
-[QSSBatchRecoverStreamingResponse initWithFlatbuffData:root:verify:];
-[QSSBatchRecoverStreamingResponse contentAsQSSBatchRecoverFinalResponse];
-[QSSBatchRecoverStreamingResponse contentAsQSSPronGuessResponse];
```
