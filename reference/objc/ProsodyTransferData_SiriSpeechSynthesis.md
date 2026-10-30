# `ProsodyTransferData`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSData" _waveData;
@"UserVoiceProfile" _userVoiceProfile;
@"NSString" _userVoiceProfileUrl;
{AudioStreamBasicDescription="mSampleRate"d"mFormatID"I"mFormatFlags"I"mBytesPerPacket"I"mFramesPerPacket"I"mBytesPerFrame"I"mChannelsPerFrame"I"mBitsPerChannel"I"mReserved"I} _asbd;
```

## Properties

```
@property (T{AudioStreamBasicDescription=dIIIIIIII},N,V_asbd) asbd;
@property (T@"NSData",C,N,V_waveData) waveData;
@property (T@"UserVoiceProfile",&,N,V_userVoiceProfile) userVoiceProfile;
@property (T@"NSString",C,N,V_userVoiceProfileUrl) userVoiceProfileUrl;
```

## Instance methods

```
-[ProsodyTransferData init];
-[ProsodyTransferData asbd];
-[ProsodyTransferData setAsbd:];
-[ProsodyTransferData setUserVoiceProfile:];
-[ProsodyTransferData setUserVoiceProfileUrl:];
-[ProsodyTransferData setWaveData:];
-[ProsodyTransferData userVoiceProfile];
-[ProsodyTransferData userVoiceProfileUrl];
-[ProsodyTransferData waveData];
```
