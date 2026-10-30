# `QSSTokenProns_SanitizedSequence`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{SanitizedSequence=[1C]} _root;
```

## Properties

```
@property (T@"NSArray",R,N) sanitized_tokens;
```

## Instance methods

```
-[QSSTokenProns_SanitizedSequence copyWithZone:];
-[QSSTokenProns_SanitizedSequence addObjectToBuffer:];
-[QSSTokenProns_SanitizedSequence flatbuffData];
-[QSSTokenProns_SanitizedSequence initAndVerifyWithFlatbuffData:];
-[QSSTokenProns_SanitizedSequence initWithFlatbuffData:];
-[QSSTokenProns_SanitizedSequence initWithFlatbuffData:root:];
-[QSSTokenProns_SanitizedSequence initWithFlatbuffData:root:verify:];
-[QSSTokenProns_SanitizedSequence sanitized_tokens];
```
