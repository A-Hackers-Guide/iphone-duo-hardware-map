# `NanoPhoneVoicemailTranscript`

- Image: [`/System/Library/PrivateFrameworks/TelephonyRPC.framework/TelephonyRPC`](../userland/System__Library__PrivateFrameworks__TelephonyRPC.framework__TelephonyRPC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 2 instance variables, 3 properties, 15 instance methods, 0 class methods

## Instance variables

```
q _voicemailNumber;
@"NSString" _transcriptionString;
```

## Properties

```
@property (Tq,N,V_voicemailNumber) voicemailNumber;
@property (TB,R,N) hasTranscriptionString;
@property (T@"NSString",&,N,V_transcriptionString) transcriptionString;
```

## Instance methods

```
-[NanoPhoneVoicemailTranscript writeTo:];
-[NanoPhoneVoicemailTranscript mergeFrom:];
-[NanoPhoneVoicemailTranscript hash];
-[NanoPhoneVoicemailTranscript copyTo:];
-[NanoPhoneVoicemailTranscript description];
-[NanoPhoneVoicemailTranscript readFrom:];
-[NanoPhoneVoicemailTranscript copyWithZone:];
-[NanoPhoneVoicemailTranscript isEqual:];
-[NanoPhoneVoicemailTranscript dictionaryRepresentation];
-[NanoPhoneVoicemailTranscript transcriptionString];
-[NanoPhoneVoicemailTranscript voicemailNumber];
-[NanoPhoneVoicemailTranscript hasTranscriptionString];
-[NanoPhoneVoicemailTranscript initWithTranscriptMessage:voicemailNumber:];
-[NanoPhoneVoicemailTranscript setTranscriptionString:];
-[NanoPhoneVoicemailTranscript setVoicemailNumber:];
```
