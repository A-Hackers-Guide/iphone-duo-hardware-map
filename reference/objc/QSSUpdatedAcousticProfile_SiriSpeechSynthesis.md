# `QSSUpdatedAcousticProfile`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{UpdatedAcousticProfile=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_str;
@property (T@"QSSUserAcousticProfile",R,N) updated_acoustic_profile;
```

## Instance methods

```
-[QSSUpdatedAcousticProfile copyWithZone:];
-[QSSUpdatedAcousticProfile addObjectToBuffer:];
-[QSSUpdatedAcousticProfile flatbuffData];
-[QSSUpdatedAcousticProfile initAndVerifyWithFlatbuffData:];
-[QSSUpdatedAcousticProfile initWithFlatbuffData:];
-[QSSUpdatedAcousticProfile initWithFlatbuffData:root:];
-[QSSUpdatedAcousticProfile initWithFlatbuffData:root:verify:];
-[QSSUpdatedAcousticProfile session_id];
-[QSSUpdatedAcousticProfile speech_id];
-[QSSUpdatedAcousticProfile return_code];
-[QSSUpdatedAcousticProfile return_str];
-[QSSUpdatedAcousticProfile updated_acoustic_profile];
```
