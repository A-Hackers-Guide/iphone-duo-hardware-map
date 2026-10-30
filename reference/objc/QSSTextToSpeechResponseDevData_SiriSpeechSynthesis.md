# `QSSTextToSpeechResponseDevData`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechResponseDevData=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) log;
@property (T@"QSSQSSVersionInfo",R,N) server_info;
@property (TB,R,N) has_click;
@property (T@"NSString",R,N) worker_process_type;
```

## Instance methods

```
-[QSSTextToSpeechResponseDevData log];
-[QSSTextToSpeechResponseDevData copyWithZone:];
-[QSSTextToSpeechResponseDevData addObjectToBuffer:];
-[QSSTextToSpeechResponseDevData flatbuffData];
-[QSSTextToSpeechResponseDevData initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechResponseDevData initWithFlatbuffData:];
-[QSSTextToSpeechResponseDevData initWithFlatbuffData:root:];
-[QSSTextToSpeechResponseDevData initWithFlatbuffData:root:verify:];
-[QSSTextToSpeechResponseDevData has_click];
-[QSSTextToSpeechResponseDevData server_info];
-[QSSTextToSpeechResponseDevData worker_process_type];
```
