# `DSXPCParticipant`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DSParticipation`, `NSSecureCoding`
- 3 instance variables, 10 properties, 14 instance methods, 2 class methods

## Instance variables

```
@"NSNumber" _participationRole;
@"NSNumber" _participationPermission;
@"DSIdentity" _participantIdentity;
```

## Properties

```
@property (T@"NSNumber",N,V_participationRole) participationRole;
@property (T@"NSNumber",N,V_participationPermission) participationPermission;
@property (T@"DSIdentity",&,N,V_participantIdentity) participantIdentity;
@property (Tq,R,N) role;
@property (Tq,R,N) permission;
@property (T@"<DSIdentifiable>",R,N) identity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DSXPCParticipant supportsSecureCoding];
+[DSXPCParticipant participants:];
```

## Instance methods

```
-[DSXPCParticipant initWithParticipant:];
-[DSXPCParticipant encodeWithCoder:];
-[DSXPCParticipant role];
-[DSXPCParticipant identity];
-[DSXPCParticipant permission];
-[DSXPCParticipant initWithCoder:];
-[DSXPCParticipant isEqual:];
-[DSXPCParticipant participantIdentity];
-[DSXPCParticipant initWithIdentity:role:permission:];
-[DSXPCParticipant participationPermission];
-[DSXPCParticipant participationRole];
-[DSXPCParticipant setParticipantIdentity:];
-[DSXPCParticipant setParticipationPermission:];
-[DSXPCParticipant setParticipationRole:];
```
