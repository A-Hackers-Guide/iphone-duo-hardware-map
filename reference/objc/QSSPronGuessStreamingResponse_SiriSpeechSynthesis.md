# `QSSPronGuessStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{PronGuessStreamingResponse=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) content_type;
@property (T@"QSSPronGuessResponse",R,N) contentAsQSSPronGuessResponse;
```

## Instance methods

```
-[QSSPronGuessStreamingResponse copyWithZone:];
-[QSSPronGuessStreamingResponse addObjectToBuffer:];
-[QSSPronGuessStreamingResponse content_type];
-[QSSPronGuessStreamingResponse flatbuffData];
-[QSSPronGuessStreamingResponse initAndVerifyWithFlatbuffData:];
-[QSSPronGuessStreamingResponse initWithFlatbuffData:];
-[QSSPronGuessStreamingResponse initWithFlatbuffData:root:];
-[QSSPronGuessStreamingResponse initWithFlatbuffData:root:verify:];
-[QSSPronGuessStreamingResponse contentAsQSSPronGuessResponse];
```
