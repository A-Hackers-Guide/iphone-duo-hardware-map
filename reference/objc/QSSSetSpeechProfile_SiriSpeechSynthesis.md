# `QSSSetSpeechProfile`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{SetSpeechProfile=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"QSSUserLanguageProfile",R,N) user_language_profile;
@property (T@"QSSUserAcousticProfile",R,N) user_acoustic_profile;
@property (T@"NSString",R,N) language;
```

## Instance methods

```
-[QSSSetSpeechProfile language];
-[QSSSetSpeechProfile copyWithZone:];
-[QSSSetSpeechProfile addObjectToBuffer:];
-[QSSSetSpeechProfile flatbuffData];
-[QSSSetSpeechProfile initAndVerifyWithFlatbuffData:];
-[QSSSetSpeechProfile initWithFlatbuffData:];
-[QSSSetSpeechProfile initWithFlatbuffData:root:];
-[QSSSetSpeechProfile initWithFlatbuffData:root:verify:];
-[QSSSetSpeechProfile session_id];
-[QSSSetSpeechProfile speech_id];
-[QSSSetSpeechProfile user_acoustic_profile];
-[QSSSetSpeechProfile user_language_profile];
```
