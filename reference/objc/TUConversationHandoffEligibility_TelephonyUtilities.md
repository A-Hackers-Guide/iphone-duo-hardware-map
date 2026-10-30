# `TUConversationHandoffEligibility`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 7 properties, 21 instance methods, 1 class methods

## Instance variables

```
B _eligible;
B _uplinkMuted;
B _sendingVideo;
@"NSUUID" _conversationGroupUUID;
@"TUConversationParticipantAssociation" _association;
@"NSString" _originatingDeviceType;
```

## Properties

```
@property (TB,N,GisEligible,V_eligible) eligible;
@property (TB,N,GisUplinkMuted,V_uplinkMuted) uplinkMuted;
@property (TB,N,GisSendingVideo,V_sendingVideo) sendingVideo;
@property (T@"NSUUID",&,N,V_conversationGroupUUID) conversationGroupUUID;
@property (T@"TUConversationParticipantAssociation",&,N,V_association) association;
@property (T@"NSString",&,N,V_originatingDeviceType) originatingDeviceType;
@property (T@"NSString",R,N) localizedDeviceCategory;
```

## Class methods

```
+[TUConversationHandoffEligibility supportsSecureCoding];
```

## Instance methods

```
-[TUConversationHandoffEligibility isSendingVideo];
-[TUConversationHandoffEligibility isUplinkMuted];
-[TUConversationHandoffEligibility setSendingVideo:];
-[TUConversationHandoffEligibility setAssociation:];
-[TUConversationHandoffEligibility association];
-[TUConversationHandoffEligibility conversationGroupUUID];
-[TUConversationHandoffEligibility encodeWithCoder:];
-[TUConversationHandoffEligibility setUplinkMuted:];
-[TUConversationHandoffEligibility hash];
-[TUConversationHandoffEligibility description];
-[TUConversationHandoffEligibility initWithCoder:];
-[TUConversationHandoffEligibility copyWithZone:];
-[TUConversationHandoffEligibility isEqual:];
-[TUConversationHandoffEligibility isEligible];
-[TUConversationHandoffEligibility originatingDeviceType];
-[TUConversationHandoffEligibility initWithHandoffEligibility:];
-[TUConversationHandoffEligibility isEqualToHandoffEligibility:];
-[TUConversationHandoffEligibility localizedDeviceCategory];
-[TUConversationHandoffEligibility setConversationGroupUUID:];
-[TUConversationHandoffEligibility setEligible:];
-[TUConversationHandoffEligibility setOriginatingDeviceType:];
```
