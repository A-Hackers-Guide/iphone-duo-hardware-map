# `SBDisplayCloneTransitionParticipantAction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
B _cloneBoundary;
q _identifier;
q _disposition;
@"UIView" _participantView;
```

## Properties

```
@property (Tq,R,N,V_identifier) identifier;
@property (Tq,R,N,V_disposition) disposition;
@property (T@"UIView",R,W,N,V_participantView) participantView;
@property (TB,R,N,GisCloneBoundary,V_cloneBoundary) cloneBoundary;
```

## Instance methods

```
-[SBDisplayCloneTransitionParticipantAction disposition];
-[SBDisplayCloneTransitionParticipantAction identifier];
-[SBDisplayCloneTransitionParticipantAction participantView];
-[SBDisplayCloneTransitionParticipantAction isCloneBoundary];
-[SBDisplayCloneTransitionParticipantAction initWithIdentifier:disposition:participantView:cloneBoundary:];
```
