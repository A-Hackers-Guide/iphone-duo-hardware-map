# `QSSSanitizedPronToken`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{SanitizedPronToken=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) token;
@property (T@"NSString",R,N) pron_source;
```

## Instance methods

```
-[QSSSanitizedPronToken token];
-[QSSSanitizedPronToken copyWithZone:];
-[QSSSanitizedPronToken addObjectToBuffer:];
-[QSSSanitizedPronToken flatbuffData];
-[QSSSanitizedPronToken initAndVerifyWithFlatbuffData:];
-[QSSSanitizedPronToken initWithFlatbuffData:];
-[QSSSanitizedPronToken initWithFlatbuffData:root:];
-[QSSSanitizedPronToken initWithFlatbuffData:root:verify:];
-[QSSSanitizedPronToken pron_source];
```
