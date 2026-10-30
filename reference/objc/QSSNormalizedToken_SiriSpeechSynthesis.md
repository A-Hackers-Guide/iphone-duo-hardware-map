# `QSSNormalizedToken`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{NormalizedToken=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) original_token;
@property (T@"NSArray",R,N) nbest_variants;
```

## Instance methods

```
-[QSSNormalizedToken copyWithZone:];
-[QSSNormalizedToken addObjectToBuffer:];
-[QSSNormalizedToken flatbuffData];
-[QSSNormalizedToken initAndVerifyWithFlatbuffData:];
-[QSSNormalizedToken initWithFlatbuffData:];
-[QSSNormalizedToken initWithFlatbuffData:root:];
-[QSSNormalizedToken initWithFlatbuffData:root:verify:];
-[QSSNormalizedToken nbest_variants];
-[QSSNormalizedToken original_token];
```
