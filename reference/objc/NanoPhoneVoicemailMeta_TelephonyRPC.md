# `NanoPhoneVoicemailMeta`

- Image: [`/System/Library/PrivateFrameworks/TelephonyRPC.framework/TelephonyRPC`](../userland/System__Library__PrivateFrameworks__TelephonyRPC.framework__TelephonyRPC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `SYObject`, `NSCopying`
- 18 instance variables, 37 properties, 72 instance methods, 1 class methods

## Instance variables

```
d _date;
q _identifier;
q _remoteUID;
q _voicemailNumber;
@"NSString" _callUUIDString;
@"NSString" _callbackNumber;
@"NSString" _conversationIDString;
@"NSString" _dataPath;
i _duration;
i _flags;
@"NSString" _nphReceiverISOCountryCode;
@"NSString" _providerID;
@"NSString" _receiverDestinationID;
@"NSString" _sender;
@"NSString" _simID;
@"NanoPhoneVoicemailBody" _voicemailBody;
@"NanoPhoneVoicemailTranscript" _voicemailTranscript;
{?="date"b1"identifier"b1"remoteUID"b1"duration"b1"flags"b1} _has;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,N,V_voicemailNumber) voicemailNumber;
@property (TB,N) hasIdentifier;
@property (Tq,N,V_identifier) identifier;
@property (TB,N) hasRemoteUID;
@property (Tq,N,V_remoteUID) remoteUID;
@property (TB,N) hasDate;
@property (Td,N,V_date) date;
@property (TB,R,N) hasSender;
@property (T@"NSString",&,N,V_sender) sender;
@property (TB,R,N) hasCallbackNumber;
@property (T@"NSString",&,N,V_callbackNumber) callbackNumber;
@property (TB,N) hasDuration;
@property (Ti,N,V_duration) duration;
@property (TB,R,N) hasDataPath;
@property (T@"NSString",&,N,V_dataPath) dataPath;
@property (TB,N) hasFlags;
@property (Ti,N,V_flags) flags;
@property (TB,R,N) hasVoicemailBody;
@property (T@"NanoPhoneVoicemailBody",&,N,V_voicemailBody) voicemailBody;
@property (TB,R,N) hasVoicemailTranscript;
@property (T@"NanoPhoneVoicemailTranscript",&,N,V_voicemailTranscript) voicemailTranscript;
@property (TB,R,N) hasReceiverDestinationID;
@property (T@"NSString",&,N,V_receiverDestinationID) receiverDestinationID;
@property (TB,R,N) hasNphReceiverISOCountryCode;
@property (T@"NSString",&,N,V_nphReceiverISOCountryCode) nphReceiverISOCountryCode;
@property (TB,R,N) hasProviderID;
@property (T@"NSString",&,N,V_providerID) providerID;
@property (TB,R,N) hasConversationIDString;
@property (T@"NSString",&,N,V_conversationIDString) conversationIDString;
@property (TB,R,N) hasCallUUIDString;
@property (T@"NSString",&,N,V_callUUIDString) callUUIDString;
@property (TB,R,N) hasSimID;
@property (T@"NSString",&,N,V_simID) simID;
```

## Class methods

```
+[NanoPhoneVoicemailMeta voicemailWithMessage:];
```

## Instance methods

```
-[NanoPhoneVoicemailMeta providerID];
-[NanoPhoneVoicemailMeta setHasIdentifier:];
-[NanoPhoneVoicemailMeta writeTo:];
-[NanoPhoneVoicemailMeta setFlags:];
-[NanoPhoneVoicemailMeta flags];
-[NanoPhoneVoicemailMeta identifier];
-[NanoPhoneVoicemailMeta setDate:];
-[NanoPhoneVoicemailMeta hasIdentifier];
-[NanoPhoneVoicemailMeta mergeFrom:];
-[NanoPhoneVoicemailMeta hasDuration];
-[NanoPhoneVoicemailMeta hasSender];
-[NanoPhoneVoicemailMeta date];
-[NanoPhoneVoicemailMeta duration];
-[NanoPhoneVoicemailMeta setHasDuration:];
-[NanoPhoneVoicemailMeta setSimID:];
-[NanoPhoneVoicemailMeta sender];
-[NanoPhoneVoicemailMeta setIdentifier:];
-[NanoPhoneVoicemailMeta hasDate];
-[NanoPhoneVoicemailMeta setDataPath:];
-[NanoPhoneVoicemailMeta hash];
-[NanoPhoneVoicemailMeta copyTo:];
-[NanoPhoneVoicemailMeta description];
-[NanoPhoneVoicemailMeta setSender:];
-[NanoPhoneVoicemailMeta setDuration:];
-[NanoPhoneVoicemailMeta simID];
-[NanoPhoneVoicemailMeta readFrom:];
-[NanoPhoneVoicemailMeta copyWithZone:];
-[NanoPhoneVoicemailMeta hasProviderID];
-[NanoPhoneVoicemailMeta isEqual:];
-[NanoPhoneVoicemailMeta setProviderID:];
-[NanoPhoneVoicemailMeta dictionaryRepresentation];
-[NanoPhoneVoicemailMeta dictionaryRepresentation];
-[NanoPhoneVoicemailMeta hasFlags];
-[NanoPhoneVoicemailMeta setHasFlags:];
-[NanoPhoneVoicemailMeta setHasDate:];
-[NanoPhoneVoicemailMeta syncId];
-[NanoPhoneVoicemailMeta dataPath];
-[NanoPhoneVoicemailMeta receiverDestinationID];
-[NanoPhoneVoicemailMeta setReceiverDestinationID:];
-[NanoPhoneVoicemailMeta setRemoteUID:];
-[NanoPhoneVoicemailMeta voicemailNumber];
-[NanoPhoneVoicemailMeta amrDataPath];
-[NanoPhoneVoicemailMeta asXpcObject];
-[NanoPhoneVoicemailMeta callUUIDString];
-[NanoPhoneVoicemailMeta callbackNumber];
-[NanoPhoneVoicemailMeta clearVoicemailBody];
-[NanoPhoneVoicemailMeta conversationIDString];
-[NanoPhoneVoicemailMeta hasCallUUIDString];
-[NanoPhoneVoicemailMeta hasCallbackNumber];
-[NanoPhoneVoicemailMeta hasConversationIDString];
-[NanoPhoneVoicemailMeta hasDataPath];
-[NanoPhoneVoicemailMeta hasNphReceiverISOCountryCode];
-[NanoPhoneVoicemailMeta hasReceiverDestinationID];
-[NanoPhoneVoicemailMeta hasRemoteUID];
-[NanoPhoneVoicemailMeta hasSimID];
-[NanoPhoneVoicemailMeta hasVoicemailBody];
-[NanoPhoneVoicemailMeta hasVoicemailTranscript];
-[NanoPhoneVoicemailMeta initWithVoicemailMessage:];
-[NanoPhoneVoicemailMeta loadVoicemailBodyIfNeeded];
-[NanoPhoneVoicemailMeta nphReceiverISOCountryCode];
-[NanoPhoneVoicemailMeta remoteUID];
-[NanoPhoneVoicemailMeta setCallUUIDString:];
-[NanoPhoneVoicemailMeta setCallbackNumber:];
-[NanoPhoneVoicemailMeta setConversationIDString:];
-[NanoPhoneVoicemailMeta setHasRemoteUID:];
-[NanoPhoneVoicemailMeta setNphReceiverISOCountryCode:];
-[NanoPhoneVoicemailMeta setVoicemailBody:];
-[NanoPhoneVoicemailMeta setVoicemailNumber:];
-[NanoPhoneVoicemailMeta setVoicemailTranscript:];
-[NanoPhoneVoicemailMeta voicemailBody];
-[NanoPhoneVoicemailMeta voicemailDescription];
-[NanoPhoneVoicemailMeta voicemailTranscript];
```
