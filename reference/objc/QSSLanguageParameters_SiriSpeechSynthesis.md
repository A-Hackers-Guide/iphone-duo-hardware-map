# `QSSLanguageParameters`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{LanguageParameters=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) language;
@property (T@"NSString",R,N) request_locale;
@property (T@"NSString",R,N) fork_id;
```

## Instance methods

```
-[QSSLanguageParameters language];
-[QSSLanguageParameters copyWithZone:];
-[QSSLanguageParameters addObjectToBuffer:];
-[QSSLanguageParameters flatbuffData];
-[QSSLanguageParameters initAndVerifyWithFlatbuffData:];
-[QSSLanguageParameters initWithFlatbuffData:];
-[QSSLanguageParameters initWithFlatbuffData:root:];
-[QSSLanguageParameters initWithFlatbuffData:root:verify:];
-[QSSLanguageParameters fork_id];
-[QSSLanguageParameters request_locale];
```
