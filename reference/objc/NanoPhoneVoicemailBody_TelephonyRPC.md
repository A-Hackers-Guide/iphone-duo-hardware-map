# `NanoPhoneVoicemailBody`

- Image: [`/System/Library/PrivateFrameworks/TelephonyRPC.framework/TelephonyRPC`](../userland/System__Library__PrivateFrameworks__TelephonyRPC.framework__TelephonyRPC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 2 instance variables, 3 properties, 15 instance methods, 0 class methods

## Instance variables

```
q _voicemailNumber;
@"NSData" _voicemailRecording;
```

## Properties

```
@property (Tq,N,V_voicemailNumber) voicemailNumber;
@property (TB,R,N) hasVoicemailRecording;
@property (T@"NSData",&,N,V_voicemailRecording) voicemailRecording;
```

## Instance methods

```
-[NanoPhoneVoicemailBody writeTo:];
-[NanoPhoneVoicemailBody mergeFrom:];
-[NanoPhoneVoicemailBody hash];
-[NanoPhoneVoicemailBody copyTo:];
-[NanoPhoneVoicemailBody description];
-[NanoPhoneVoicemailBody readFrom:];
-[NanoPhoneVoicemailBody copyWithZone:];
-[NanoPhoneVoicemailBody isEqual:];
-[NanoPhoneVoicemailBody dictionaryRepresentation];
-[NanoPhoneVoicemailBody voicemailNumber];
-[NanoPhoneVoicemailBody hasVoicemailRecording];
-[NanoPhoneVoicemailBody initWithAudioMessage:voicemailNumber:];
-[NanoPhoneVoicemailBody setVoicemailNumber:];
-[NanoPhoneVoicemailBody setVoicemailRecording:];
-[NanoPhoneVoicemailBody voicemailRecording];
```
