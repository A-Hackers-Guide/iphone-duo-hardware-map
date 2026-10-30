# `QSSLatnnMitigatorResult`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{LatnnMitigatorResult=[1C]} _root;
```

## Properties

```
@property (TB,R,N) processed;
@property (T@"NSString",R,N) version;
@property (Td,R,N) threshold;
@property (Td,R,N) score;
```

## Instance methods

```
-[QSSLatnnMitigatorResult version];
-[QSSLatnnMitigatorResult score];
-[QSSLatnnMitigatorResult threshold];
-[QSSLatnnMitigatorResult copyWithZone:];
-[QSSLatnnMitigatorResult processed];
-[QSSLatnnMitigatorResult addObjectToBuffer:];
-[QSSLatnnMitigatorResult flatbuffData];
-[QSSLatnnMitigatorResult initAndVerifyWithFlatbuffData:];
-[QSSLatnnMitigatorResult initWithFlatbuffData:];
-[QSSLatnnMitigatorResult initWithFlatbuffData:root:];
-[QSSLatnnMitigatorResult initWithFlatbuffData:root:verify:];
```
