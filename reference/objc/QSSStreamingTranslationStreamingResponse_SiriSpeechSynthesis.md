# `QSSStreamingTranslationStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{StreamingTranslationStreamingResponse=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) content_type;
@property (T@"QSSTranslationResponse",R,N) contentAsQSSTranslationResponse;
```

## Instance methods

```
-[QSSStreamingTranslationStreamingResponse copyWithZone:];
-[QSSStreamingTranslationStreamingResponse addObjectToBuffer:];
-[QSSStreamingTranslationStreamingResponse content_type];
-[QSSStreamingTranslationStreamingResponse flatbuffData];
-[QSSStreamingTranslationStreamingResponse initAndVerifyWithFlatbuffData:];
-[QSSStreamingTranslationStreamingResponse initWithFlatbuffData:];
-[QSSStreamingTranslationStreamingResponse initWithFlatbuffData:root:];
-[QSSStreamingTranslationStreamingResponse initWithFlatbuffData:root:verify:];
-[QSSStreamingTranslationStreamingResponse contentAsQSSTranslationResponse];
```
