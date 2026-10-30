# `QSSContextWithPronHints`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{ContextWithPronHints=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) contextual_text;
@property (T@"NSArray",R,N) pron_hints;
```

## Instance methods

```
-[QSSContextWithPronHints copyWithZone:];
-[QSSContextWithPronHints addObjectToBuffer:];
-[QSSContextWithPronHints flatbuffData];
-[QSSContextWithPronHints initAndVerifyWithFlatbuffData:];
-[QSSContextWithPronHints initWithFlatbuffData:];
-[QSSContextWithPronHints initWithFlatbuffData:root:];
-[QSSContextWithPronHints initWithFlatbuffData:root:verify:];
-[QSSContextWithPronHints contextual_text];
-[QSSContextWithPronHints pron_hints];
```
