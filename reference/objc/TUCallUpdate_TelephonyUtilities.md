# `TUCallUpdate`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 15 instance variables, 15 properties, 37 instance methods, 1 class methods

## Instance variables

```
B _hasVideo;
B _conversation;
B _answeringMachineAvailable;
B _eligibleForScreening;
@"TUCallProvider" _provider;
@"TUHandle" _handle;
Q _remoteParticipantCount;
@"NSUUID" _UUID;
@"NSUUID" _callUUID;
@"<TUFeatureFlags>" _featureFlags;
@"TUCallServicesInterface" _callServicesInterface;
@? _contactsCountBlock;
@? _clarityEnabledBlock;
q _priority;
q _junkConfidence;
```

## Properties

```
@property (T@"<TUFeatureFlags>",&,N,V_featureFlags) featureFlags;
@property (T@"TUCallServicesInterface",&,N,V_callServicesInterface) callServicesInterface;
@property (T@?,C,N,V_contactsCountBlock) contactsCountBlock;
@property (T@?,C,N,V_clarityEnabledBlock) clarityEnabledBlock;
@property (Tq,N,V_priority) priority;
@property (Tq,N,V_junkConfidence) junkConfidence;
@property (T@"TUCallProvider",&,N,V_provider) provider;
@property (T@"TUHandle",&,N,V_handle) handle;
@property (TQ,N,V_remoteParticipantCount) remoteParticipantCount;
@property (TB,N,V_hasVideo) hasVideo;
@property (TB,N,GisConversation,V_conversation) conversation;
@property (T@"NSUUID",&,N,V_UUID) UUID;
@property (T@"NSUUID",&,N,V_callUUID) callUUID;
@property (TB,N,GisAnsweringMachineAvailable,V_answeringMachineAvailable) answeringMachineAvailable;
@property (TB,N,GisEligibleForScreening,V_eligibleForScreening) eligibleForScreening;
```

## Class methods

```
+[TUCallUpdate supportsSecureCoding];
```

## Instance methods

```
-[TUCallUpdate priority];
-[TUCallUpdate setHasVideo:];
-[TUCallUpdate init];
-[TUCallUpdate setUUID:];
-[TUCallUpdate callServicesInterface];
-[TUCallUpdate hasVideo];
-[TUCallUpdate UUID];
-[TUCallUpdate setPriority:];
-[TUCallUpdate junkConfidence];
-[TUCallUpdate setCallUUID:];
-[TUCallUpdate isAnsweringMachineAvailable];
-[TUCallUpdate provider];
-[TUCallUpdate clarityEnabledBlock];
-[TUCallUpdate setCallServicesInterface:];
-[TUCallUpdate callUUID];
-[TUCallUpdate isEligibleForScreening];
-[TUCallUpdate handle];
-[TUCallUpdate setConversation:];
-[TUCallUpdate encodeWithCoder:];
-[TUCallUpdate setClarityEnabledBlock:];
-[TUCallUpdate isConversation];
-[TUCallUpdate initWithProvider:];
-[TUCallUpdate description];
-[TUCallUpdate initWithCoder:];
-[TUCallUpdate setHandle:];
-[TUCallUpdate copyWithZone:];
-[TUCallUpdate setProvider:];
-[TUCallUpdate setFeatureFlags:];
-[TUCallUpdate featureFlags];
-[TUCallUpdate contactsCountBlock];
-[TUCallUpdate isHostEligibleForScreening];
-[TUCallUpdate remoteParticipantCount];
-[TUCallUpdate setAnsweringMachineAvailable:];
-[TUCallUpdate setContactsCountBlock:];
-[TUCallUpdate setEligibleForScreening:];
-[TUCallUpdate setJunkConfidence:];
-[TUCallUpdate setRemoteParticipantCount:];
```
