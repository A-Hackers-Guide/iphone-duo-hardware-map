# `QSSTextToSpeechUserVoiceProfile`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechUserVoiceProfile=[1C]} _root;
```

## Properties

```
@property (Tf,R,N) pitch_mean;
@property (Tf,R,N) pitch_std;
@property (Tf,R,N) energy_mean;
@property (Tf,R,N) energy_std;
@property (Tf,R,N) duration_mean;
@property (Tf,R,N) duration_std;
```

## Instance methods

```
-[QSSTextToSpeechUserVoiceProfile copyWithZone:];
-[QSSTextToSpeechUserVoiceProfile addObjectToBuffer:];
-[QSSTextToSpeechUserVoiceProfile duration_mean];
-[QSSTextToSpeechUserVoiceProfile duration_std];
-[QSSTextToSpeechUserVoiceProfile energy_mean];
-[QSSTextToSpeechUserVoiceProfile energy_std];
-[QSSTextToSpeechUserVoiceProfile flatbuffData];
-[QSSTextToSpeechUserVoiceProfile initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechUserVoiceProfile initWithFlatbuffData:];
-[QSSTextToSpeechUserVoiceProfile initWithFlatbuffData:root:];
-[QSSTextToSpeechUserVoiceProfile initWithFlatbuffData:root:verify:];
-[QSSTextToSpeechUserVoiceProfile pitch_mean];
-[QSSTextToSpeechUserVoiceProfile pitch_std];
```
