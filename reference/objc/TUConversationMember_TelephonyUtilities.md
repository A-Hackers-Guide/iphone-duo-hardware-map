# `TUConversationMember`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 16 instance variables, 24 properties, 58 instance methods, 1 class methods

## Instance variables

```
B _isLightweightMember;
B _joinedFromLetMeIn;
B _isOtherInvitedHandle;
B _isAccessibilityInterpreter;
@"TUHandle" _handle;
@"NSString" _nickname;
q _validationSource;
@"NSDate" _dateReceivedLetMeIn;
@"NSDate" _dateInitiatedLetMeIn;
@"TUHandle" _lightweightPrimary;
Q _lightweightPrimaryParticipantIdentifier;
@"TUConversationMemberAssociation" _association;
@"TUVoucher" _associationVoucher;
@"NSString" _stableDeviceIdentifier;
@"TUConversationParticipantCluster" _proposedParticipantCluster;
@"TUConversationParticipantLinkAssociation" _linkAssociation;
```

## Properties

```
@property (TB,R,N) needsContactLookupForDisplayName;
@property (T@"NSString",R,C,N) idsFromID;
@property (T@"NSString",R,C,N) idsDestination;
@property (T@"NSString",C,N,V_nickname) nickname;
@property (TB,N,V_joinedFromLetMeIn) joinedFromLetMeIn;
@property (TB,N,V_isOtherInvitedHandle) isOtherInvitedHandle;
@property (Tq,N,V_validationSource) validationSource;
@property (T@"TUConversationMemberAssociation",C,N,V_association) association;
@property (T@"TUVoucher",&,N,V_associationVoucher) associationVoucher;
@property (T@"NSString",C,N,V_stableDeviceIdentifier) stableDeviceIdentifier;
@property (T@"TUConversationParticipantCluster",C,N,V_proposedParticipantCluster) proposedParticipantCluster;
@property (T@"TUConversationParticipantLinkAssociation",C,N,V_linkAssociation) linkAssociation;
@property (TB,N,V_isAccessibilityInterpreter) isAccessibilityInterpreter;
@property (T@"NSArray",R,C,N) idsDestinations;
@property (T@"TUHandle",R,N,V_handle) handle;
@property (TB,R,N,GisValidated) validated;
@property (TB,N) isSplitSessionMember;
@property (TB,N,V_isLightweightMember) isLightweightMember;
@property (T@"NSDate",&,N,V_dateReceivedLetMeIn) dateReceivedLetMeIn;
@property (T@"NSDate",&,N,V_dateInitiatedLetMeIn) dateInitiatedLetMeIn;
@property (T@"TUHandle",C,N) splitSessionPrimary;
@property (T@"TUHandle",C,N,V_lightweightPrimary) lightweightPrimary;
@property (TQ,N,V_lightweightPrimaryParticipantIdentifier) lightweightPrimaryParticipantIdentifier;
@property (T@"NSSet",R,C,N) handles;
```

## Class methods

```
+[TUConversationMember supportsSecureCoding];
```

## Instance methods

```
-[TUConversationMember validationSource];
-[TUConversationMember setJoinedFromLetMeIn:];
-[TUConversationMember initWithDestination:];
-[TUConversationMember setIsOtherInvitedHandle:];
-[TUConversationMember isValidated];
-[TUConversationMember initWithHandle:];
-[TUConversationMember initWithDestinations:];
-[TUConversationMember setStableDeviceIdentifier:];
-[TUConversationMember idsDestination];
-[TUConversationMember setAssociationVoucher:];
-[TUConversationMember dateInitiatedLetMeIn];
-[TUConversationMember dateReceivedLetMeIn];
-[TUConversationMember stableDeviceIdentifier];
-[TUConversationMember setLinkAssociation:];
-[TUConversationMember initWithHandles:];
-[TUConversationMember isLightweightMember];
-[TUConversationMember idsDestinations];
-[TUConversationMember associationVoucher];
-[TUConversationMember setLightweightPrimary:];
-[TUConversationMember initWithContact:additionalHandles:];
-[TUConversationMember setIsLightweightMember:];
-[TUConversationMember proposedParticipantCluster];
-[TUConversationMember idsFromID];
-[TUConversationMember pseudonym];
-[TUConversationMember setIsAccessibilityInterpreter:];
-[TUConversationMember initWithContact:];
-[TUConversationMember setSplitSessionPrimary:];
-[TUConversationMember setNickname:];
-[TUConversationMember needsContactLookupForDisplayName];
-[TUConversationMember setAssociation:];
-[TUConversationMember representsSameMemberAs:];
-[TUConversationMember handle];
-[TUConversationMember initWithHandle:nickname:joinedFromLetMeIn:];
-[TUConversationMember lightweightPrimary];
-[TUConversationMember association];
-[TUConversationMember nickname];
-[TUConversationMember setValidationSource:];
-[TUConversationMember setIsSplitSessionMember:];
-[TUConversationMember joinedFromLetMeIn];
-[TUConversationMember encodeWithCoder:];
-[TUConversationMember setDateInitiatedLetMeIn:];
-[TUConversationMember hash];
-[TUConversationMember description];
-[TUConversationMember handles];
-[TUConversationMember splitSessionPrimary];
-[TUConversationMember initWithCoder:];
-[TUConversationMember isSplitSessionMember];
-[TUConversationMember isEqualToMember:];
-[TUConversationMember setProposedParticipantCluster:];
-[TUConversationMember copyWithZone:];
-[TUConversationMember setDateReceivedLetMeIn:];
-[TUConversationMember lightweightPrimaryParticipantIdentifier];
-[TUConversationMember linkAssociation];
-[TUConversationMember isEqual:];
-[TUConversationMember initWithHandle:nickname:];
-[TUConversationMember setLightweightPrimaryParticipantIdentifier:];
-[TUConversationMember isOtherInvitedHandle];
-[TUConversationMember isAccessibilityInterpreter];
```
