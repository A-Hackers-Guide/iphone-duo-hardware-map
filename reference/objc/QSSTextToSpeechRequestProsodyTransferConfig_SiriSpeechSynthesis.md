# `QSSTextToSpeechRequestProsodyTransferConfig`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechRequestProsodyTransferConfig=[1C]} _root;
```

## Properties

```
@property (T@"QSSTextToSpeechSpeechFeatureInputWave",R,N) wave_data;
@property (T@"QSSTextToSpeechUserVoiceProfile",R,N) user_voice_profile;
@property (T@"NSString",R,N) user_voice_profile_url;
```

## Instance methods

```
-[QSSTextToSpeechRequestProsodyTransferConfig copyWithZone:];
-[QSSTextToSpeechRequestProsodyTransferConfig addObjectToBuffer:];
-[QSSTextToSpeechRequestProsodyTransferConfig flatbuffData];
-[QSSTextToSpeechRequestProsodyTransferConfig initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechRequestProsodyTransferConfig initWithFlatbuffData:];
-[QSSTextToSpeechRequestProsodyTransferConfig initWithFlatbuffData:root:];
-[QSSTextToSpeechRequestProsodyTransferConfig initWithFlatbuffData:root:verify:];
-[QSSTextToSpeechRequestProsodyTransferConfig user_voice_profile];
-[QSSTextToSpeechRequestProsodyTransferConfig user_voice_profile_url];
-[QSSTextToSpeechRequestProsodyTransferConfig wave_data];
```
