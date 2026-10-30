# `SBSAPulseRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSARequestRepresenting`
- 2 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"<NSCopying><SAElementIdentifying>" _participantIdentifier;
q _pulseStyle;
```

## Properties

```
@property (T@"<NSCopying><SAElementIdentifying>",R,C,N,V_participantIdentifier) participantIdentifier;
@property (Tq,R,N,V_pulseStyle) pulseStyle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSAPulseRequest initialize];
```

## Instance methods

```
-[SBSAPulseRequest participantIdentifier];
-[SBSAPulseRequest encodeWithCoder:];
-[SBSAPulseRequest hash];
-[SBSAPulseRequest description];
-[SBSAPulseRequest copyWithZone:];
-[SBSAPulseRequest isEqual:];
-[SBSAPulseRequest membersForCoder];
-[SBSAPulseRequest initWithParticipantIdentifier:pulseStyle:];
-[SBSAPulseRequest pulseStyle];
```
