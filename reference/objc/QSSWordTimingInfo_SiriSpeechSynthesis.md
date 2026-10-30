# `QSSWordTimingInfo`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{WordTimingInfo=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) word;
@property (TI,R,N) sample_idx;
@property (TI,R,N) offset;
@property (TI,R,N) length;
@property (Tf,R,N) timestamp;
```

## Instance methods

```
-[QSSWordTimingInfo timestamp];
-[QSSWordTimingInfo length];
-[QSSWordTimingInfo word];
-[QSSWordTimingInfo copyWithZone:];
-[QSSWordTimingInfo offset];
-[QSSWordTimingInfo addObjectToBuffer:];
-[QSSWordTimingInfo flatbuffData];
-[QSSWordTimingInfo initAndVerifyWithFlatbuffData:];
-[QSSWordTimingInfo initWithFlatbuffData:];
-[QSSWordTimingInfo initWithFlatbuffData:root:];
-[QSSWordTimingInfo initWithFlatbuffData:root:verify:];
-[QSSWordTimingInfo sample_idx];
```
