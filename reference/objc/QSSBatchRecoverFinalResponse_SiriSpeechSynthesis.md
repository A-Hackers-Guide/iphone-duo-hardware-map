# `QSSBatchRecoverFinalResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{BatchRecoverFinalResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) error_code;
@property (T@"NSString",R,N) error_str;
@property (Ti,R,N) num_of_requested;
@property (Ti,R,N) num_of_processed;
@property (Ti,R,N) num_of_succeeded;
```

## Instance methods

```
-[QSSBatchRecoverFinalResponse copyWithZone:];
-[QSSBatchRecoverFinalResponse addObjectToBuffer:];
-[QSSBatchRecoverFinalResponse error_code];
-[QSSBatchRecoverFinalResponse error_str];
-[QSSBatchRecoverFinalResponse flatbuffData];
-[QSSBatchRecoverFinalResponse initAndVerifyWithFlatbuffData:];
-[QSSBatchRecoverFinalResponse initWithFlatbuffData:];
-[QSSBatchRecoverFinalResponse initWithFlatbuffData:root:];
-[QSSBatchRecoverFinalResponse initWithFlatbuffData:root:verify:];
-[QSSBatchRecoverFinalResponse session_id];
-[QSSBatchRecoverFinalResponse speech_id];
-[QSSBatchRecoverFinalResponse num_of_processed];
-[QSSBatchRecoverFinalResponse num_of_requested];
-[QSSBatchRecoverFinalResponse num_of_succeeded];
```
