# `QSSTextToSpeechResource`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechResource=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) language;
@property (T@"NSString",R,N) version;
```

## Instance methods

```
-[QSSTextToSpeechResource language];
-[QSSTextToSpeechResource version];
-[QSSTextToSpeechResource copyWithZone:];
-[QSSTextToSpeechResource addObjectToBuffer:];
-[QSSTextToSpeechResource flatbuffData];
-[QSSTextToSpeechResource initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechResource initWithFlatbuffData:];
-[QSSTextToSpeechResource initWithFlatbuffData:root:];
-[QSSTextToSpeechResource initWithFlatbuffData:root:verify:];
```
