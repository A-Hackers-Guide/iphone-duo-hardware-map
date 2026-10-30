# `QSSSpan`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{Span=[1C]} _root;
```

## Properties

```
@property (Ti,R,N) start_index;
@property (Ti,R,N) end_index;
@property (TB,R,N) do_not_translate;
@property (T@"NSString",R,N) meta_info;
```

## Instance methods

```
-[QSSSpan copyWithZone:];
-[QSSSpan addObjectToBuffer:];
-[QSSSpan flatbuffData];
-[QSSSpan initAndVerifyWithFlatbuffData:];
-[QSSSpan initWithFlatbuffData:];
-[QSSSpan initWithFlatbuffData:root:];
-[QSSSpan initWithFlatbuffData:root:verify:];
-[QSSSpan meta_info];
-[QSSSpan do_not_translate];
-[QSSSpan end_index];
-[QSSSpan start_index];
```
