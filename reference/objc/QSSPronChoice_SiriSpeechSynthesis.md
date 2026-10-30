# `QSSPronChoice`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{PronChoice=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) pron_sequence;
@property (Tf,R,N) log_weight;
```

## Instance methods

```
-[QSSPronChoice copyWithZone:];
-[QSSPronChoice addObjectToBuffer:];
-[QSSPronChoice flatbuffData];
-[QSSPronChoice initAndVerifyWithFlatbuffData:];
-[QSSPronChoice initWithFlatbuffData:];
-[QSSPronChoice initWithFlatbuffData:root:];
-[QSSPronChoice initWithFlatbuffData:root:verify:];
-[QSSPronChoice log_weight];
-[QSSPronChoice pron_sequence];
```
