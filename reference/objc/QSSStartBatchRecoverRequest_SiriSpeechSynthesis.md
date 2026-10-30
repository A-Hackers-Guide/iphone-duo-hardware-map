# `QSSStartBatchRecoverRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{StartBatchRecoverRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) language;
@property (T@"NSArray",R,N) apg_ids;
```

## Instance methods

```
-[QSSStartBatchRecoverRequest language];
-[QSSStartBatchRecoverRequest copyWithZone:];
-[QSSStartBatchRecoverRequest addObjectToBuffer:];
-[QSSStartBatchRecoverRequest flatbuffData];
-[QSSStartBatchRecoverRequest initAndVerifyWithFlatbuffData:];
-[QSSStartBatchRecoverRequest initWithFlatbuffData:];
-[QSSStartBatchRecoverRequest initWithFlatbuffData:root:];
-[QSSStartBatchRecoverRequest initWithFlatbuffData:root:verify:];
-[QSSStartBatchRecoverRequest session_id];
-[QSSStartBatchRecoverRequest speech_id];
-[QSSStartBatchRecoverRequest apg_ids];
```
