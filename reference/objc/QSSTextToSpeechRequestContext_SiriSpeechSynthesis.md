# `QSSTextToSpeechRequestContext`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechRequestContext=[1C]} _root;
```

## Properties

```
@property (T@"NSArray",R,N) context_info;
@property (T@"NSString",R,N) dialog_identifier;
```

## Instance methods

```
-[QSSTextToSpeechRequestContext copyWithZone:];
-[QSSTextToSpeechRequestContext addObjectToBuffer:];
-[QSSTextToSpeechRequestContext context_info];
-[QSSTextToSpeechRequestContext dialog_identifier];
-[QSSTextToSpeechRequestContext flatbuffData];
-[QSSTextToSpeechRequestContext initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechRequestContext initWithFlatbuffData:];
-[QSSTextToSpeechRequestContext initWithFlatbuffData:root:];
-[QSSTextToSpeechRequestContext initWithFlatbuffData:root:verify:];
```
