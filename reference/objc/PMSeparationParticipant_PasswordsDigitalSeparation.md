# `PMSeparationParticipant`

- Image: [`/System/Library/DigitalSeparation/SharingSources/PasswordsDigitalSeparation.bundle/PasswordsDigitalSeparation`](../userland/System__Library__DigitalSeparation__SharingSources__PasswordsDigitalSeparation.bundle__PasswordsDigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DSParticipation`
- 2 instance variables, 8 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"<DSIdentifiable>" _identity;
@"KCSharingParticipant" _participant;
```

## Properties

```
@property (T@"KCSharingParticipant",R,N,V_participant) participant;
@property (Tq,R,N) role;
@property (Tq,R,N) permission;
@property (T@"<DSIdentifiable>",R,N,V_identity) identity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PMSeparationParticipant participant];
-[PMSeparationParticipant role];
-[PMSeparationParticipant identity];
-[PMSeparationParticipant permission];
-[PMSeparationParticipant description];
-[PMSeparationParticipant initWithParticipant:identity:];
```
