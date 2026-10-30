# `SBSAShakeRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `SBSARequestRepresenting`
- 2 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
@ _participantIdentifier;
@? _triggeredBlock;
```

## Properties

```
@property (T@,R,C,N,V_participantIdentifier) participantIdentifier;
@property (T@?,R,C,N,V_triggeredBlock) triggeredBlock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSAShakeRequest initialize];
```

## Instance methods

```
-[SBSAShakeRequest participantIdentifier];
-[SBSAShakeRequest encodeWithCoder:];
-[SBSAShakeRequest hash];
-[SBSAShakeRequest description];
-[SBSAShakeRequest copyWithZone:];
-[SBSAShakeRequest isEqual:];
-[SBSAShakeRequest membersForCoder];
-[SBSAShakeRequest initWithParticipantIdentifier:triggeredBlock:];
-[SBSAShakeRequest triggeredBlock];
```
