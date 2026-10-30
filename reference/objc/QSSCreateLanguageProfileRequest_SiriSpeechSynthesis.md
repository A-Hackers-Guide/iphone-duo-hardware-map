# `QSSCreateLanguageProfileRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{CreateLanguageProfileRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) language;
@property (T@"NSArray",R,N) user_data;
@property (T@"QSSUserLanguageProfile",R,N) user_language_profile;
```

## Instance methods

```
-[QSSCreateLanguageProfileRequest language];
-[QSSCreateLanguageProfileRequest copyWithZone:];
-[QSSCreateLanguageProfileRequest addObjectToBuffer:];
-[QSSCreateLanguageProfileRequest flatbuffData];
-[QSSCreateLanguageProfileRequest initAndVerifyWithFlatbuffData:];
-[QSSCreateLanguageProfileRequest initWithFlatbuffData:];
-[QSSCreateLanguageProfileRequest initWithFlatbuffData:root:];
-[QSSCreateLanguageProfileRequest initWithFlatbuffData:root:verify:];
-[QSSCreateLanguageProfileRequest session_id];
-[QSSCreateLanguageProfileRequest speech_id];
-[QSSCreateLanguageProfileRequest user_data];
-[QSSCreateLanguageProfileRequest user_language_profile];
```
