# `SBSAAnimatedTransitionResultDescribing` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `NSCopying`
- 0 instance variables, 6 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"NSUUID",R,C,N) animatedTransitionIdentifier;
@property (T@"<SBSAInterfaceElementPropertyIdentifying>",R,C,N) associatedInterfaceElementPropertyIdentity;
@property (Td,R,N) targetedMilestone;
@property (TB,R,N,GisTransitionEndTargeted) transitionEndTargeted;
@property (TB,R,N) finished;
@property (TB,R,N) retargeted;
```

## Instance methods

```
-[SBSAAnimatedTransitionResultDescribing finished];
-[SBSAAnimatedTransitionResultDescribing animatedTransitionIdentifier];
-[SBSAAnimatedTransitionResultDescribing associatedInterfaceElementPropertyIdentity];
-[SBSAAnimatedTransitionResultDescribing isTransitionEndTargeted];
-[SBSAAnimatedTransitionResultDescribing retargeted];
-[SBSAAnimatedTransitionResultDescribing targetedMilestone];
```
