# `QSSUserLanguageProfile`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{UserLanguageProfile=[1C]} _root;
```

## Properties

```
@property (T@"NSData",R,N) profile_blob;
@property (T@"NSString",R,N) profile_blob_version;
@property (T@"NSString",R,N) profile_checksum;
```

## Instance methods

```
-[QSSUserLanguageProfile copyWithZone:];
-[QSSUserLanguageProfile addObjectToBuffer:];
-[QSSUserLanguageProfile flatbuffData];
-[QSSUserLanguageProfile initAndVerifyWithFlatbuffData:];
-[QSSUserLanguageProfile initWithFlatbuffData:];
-[QSSUserLanguageProfile initWithFlatbuffData:root:];
-[QSSUserLanguageProfile initWithFlatbuffData:root:verify:];
-[QSSUserLanguageProfile profile_blob];
-[QSSUserLanguageProfile profile_blob:];
-[QSSUserLanguageProfile profile_blob_version];
-[QSSUserLanguageProfile profile_checksum];
```
