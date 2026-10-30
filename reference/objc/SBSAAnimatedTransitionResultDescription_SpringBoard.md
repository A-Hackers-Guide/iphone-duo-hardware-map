# `SBSAAnimatedTransitionResultDescription`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `SBSAAnimatedTransitionResultDescribing`, `SBSABlockMutating`
- 6 instance variables, 10 properties, 20 instance methods, 3 class methods

## Instance variables

```
B _finished;
B _retargeted;
B _transitionEndTargeted;
@"NSUUID" _animatedTransitionIdentifier;
@"<SBSAInterfaceElementPropertyIdentifying>" _associatedInterfaceElementPropertyIdentity;
d _targetedMilestone;
```

## Properties

```
@property (T@"NSUUID",C,N,S_setAnimatedTransitionIdentifier:,V_animatedTransitionIdentifier) animatedTransitionIdentifier;
@property (T@"<SBSAInterfaceElementPropertyIdentifying>",C,N,S_setAssociatedInterfaceElementPropertyIdentityIdentity:,V_associatedInterfaceElementPropertyIdentity) associatedInterfaceElementPropertyIdentity;
@property (Td,N,S_setTargetedMilestone:,V_targetedMilestone) targetedMilestone;
@property (TB,N,GisTransitionEndTargeted,S_setTransitionEndTargeted:,V_transitionEndTargeted) transitionEndTargeted;
@property (TB,N,S_setFinished:,V_finished) finished;
@property (TB,N,S_setRetargeted:,V_retargeted) retargeted;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSAAnimatedTransitionResultDescription initialize];
+[SBSAAnimatedTransitionResultDescription instanceWithBlock:];
+[SBSAAnimatedTransitionResultDescription mutatorClass];
```

## Instance methods

```
-[SBSAAnimatedTransitionResultDescription finished];
-[SBSAAnimatedTransitionResultDescription encodeWithCoder:];
-[SBSAAnimatedTransitionResultDescription hash];
-[SBSAAnimatedTransitionResultDescription description];
-[SBSAAnimatedTransitionResultDescription copyWithZone:];
-[SBSAAnimatedTransitionResultDescription isEqual:];
-[SBSAAnimatedTransitionResultDescription copyWithBlock:];
-[SBSAAnimatedTransitionResultDescription membersForCoder];
-[SBSAAnimatedTransitionResultDescription _setFinished:];
-[SBSAAnimatedTransitionResultDescription _setRetargeted:];
-[SBSAAnimatedTransitionResultDescription _setAnimatedTransitionIdentifier:];
-[SBSAAnimatedTransitionResultDescription _setAssociatedInterfaceElementPropertyIdentityIdentity:];
-[SBSAAnimatedTransitionResultDescription _setTargetedMilestone:];
-[SBSAAnimatedTransitionResultDescription _setTransitionEndTargeted:];
-[SBSAAnimatedTransitionResultDescription animatedTransitionIdentifier];
-[SBSAAnimatedTransitionResultDescription associatedInterfaceElementPropertyIdentity];
-[SBSAAnimatedTransitionResultDescription initWithAnimatedTransitionResultDescription:];
-[SBSAAnimatedTransitionResultDescription isTransitionEndTargeted];
-[SBSAAnimatedTransitionResultDescription retargeted];
-[SBSAAnimatedTransitionResultDescription targetedMilestone];
```
