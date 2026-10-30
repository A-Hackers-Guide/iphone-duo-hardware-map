# `QSSUserAcousticProfile`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{UserAcousticProfile=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) acoustic_profile_version;
@property (T@"NSData",R,N) acoustic_profile_blob;
@property (T@"NSString",R,N) profile_checksum;
```

## Instance methods

```
-[QSSUserAcousticProfile copyWithZone:];
-[QSSUserAcousticProfile addObjectToBuffer:];
-[QSSUserAcousticProfile flatbuffData];
-[QSSUserAcousticProfile initAndVerifyWithFlatbuffData:];
-[QSSUserAcousticProfile initWithFlatbuffData:];
-[QSSUserAcousticProfile initWithFlatbuffData:root:];
-[QSSUserAcousticProfile initWithFlatbuffData:root:verify:];
-[QSSUserAcousticProfile acoustic_profile_blob];
-[QSSUserAcousticProfile acoustic_profile_blob:];
-[QSSUserAcousticProfile acoustic_profile_version];
-[QSSUserAcousticProfile profile_checksum];
```
