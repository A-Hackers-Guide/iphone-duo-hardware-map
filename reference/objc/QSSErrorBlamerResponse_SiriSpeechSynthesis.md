# `QSSErrorBlamerResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{ErrorBlamerResponse=[1C]} _root;
```

## Properties

```
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_str;
@property (T@"NSString",R,N) blamer_report;
```

## Instance methods

```
-[QSSErrorBlamerResponse copyWithZone:];
-[QSSErrorBlamerResponse addObjectToBuffer:];
-[QSSErrorBlamerResponse flatbuffData];
-[QSSErrorBlamerResponse initAndVerifyWithFlatbuffData:];
-[QSSErrorBlamerResponse initWithFlatbuffData:];
-[QSSErrorBlamerResponse initWithFlatbuffData:root:];
-[QSSErrorBlamerResponse initWithFlatbuffData:root:verify:];
-[QSSErrorBlamerResponse blamer_report];
-[QSSErrorBlamerResponse return_code];
-[QSSErrorBlamerResponse return_str];
```
