# `SBFDisplayContentModeTransitionContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`
- 22 instance variables, 24 properties, 55 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _initialContentModes;
@"NSMutableDictionary" _finalContentModes;
B _interactive;
B _continuousFoldBeganFromHingeEndpoint;
B _progressLockedForApplicationOfDisplayContentModeChanges;
B _hingeAtAnEndpoint;
@"SBFDisplayContentModeResolver" _resolver;
q _phase;
q _transitionStyle;
@"NSArray" _hardwareIdentifiersOfTransitioningDisplays;
d _interactiveProgress;
d _progressToSwap;
d _progressFromSwap;
d _continuousFoldPosition;
d _continuousFoldVelocity;
d _mechanicalHingeAngleDegrees;
d _continuousFoldEffectProgress;
@"NSArray" _displays;
@"NSSet" _swappingHardwareIdentifiers;
d _interactiveProgressIgnoringLock;
d _progressToSwapIgnoringLock;
d _progressFromSwapIgnoringLock;
```

## Properties

```
@property (TB,N,GisInteractive,V_interactive) interactive;
@property (Td,N,V_interactiveProgress) interactiveProgress;
@property (TB,N,GisProgressLockedForApplicationOfDisplayContentModeChanges,V_progressLockedForApplicationOfDisplayContentModeChanges) progressLockedForApplicationOfDisplayContentModeChanges;
@property (Td,N,V_progressToSwap) progressToSwap;
@property (Td,N,V_progressFromSwap) progressFromSwap;
@property (Tq,N,V_phase) phase;
@property (T@"NSArray",C,N,V_displays) displays;
@property (T@"NSSet",C,N,V_swappingHardwareIdentifiers) swappingHardwareIdentifiers;
@property (Td,N,V_interactiveProgressIgnoringLock) interactiveProgressIgnoringLock;
@property (Td,N,V_progressToSwapIgnoringLock) progressToSwapIgnoringLock;
@property (Td,N,V_progressFromSwapIgnoringLock) progressFromSwapIgnoringLock;
@property (Td,N,V_continuousFoldPosition) continuousFoldPosition;
@property (Td,N,V_continuousFoldVelocity) continuousFoldVelocity;
@property (Td,N,V_mechanicalHingeAngleDegrees) mechanicalHingeAngleDegrees;
@property (Td,N,V_continuousFoldEffectProgress) continuousFoldEffectProgress;
@property (TB,N,V_continuousFoldBeganFromHingeEndpoint) continuousFoldBeganFromHingeEndpoint;
@property (TB,N,GisHingeAtAnEndpoint,V_hingeAtAnEndpoint) hingeAtAnEndpoint;
@property (T@"SBFDisplayContentModeResolver",W,N,V_resolver) resolver;
@property (Tq,R,N,V_transitionStyle) transitionStyle;
@property (T@"NSArray",R,N,V_hardwareIdentifiersOfTransitioningDisplays) hardwareIdentifiersOfTransitioningDisplays;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFDisplayContentModeTransitionContext resolver];
-[SBFDisplayContentModeTransitionContext debugDescription];
-[SBFDisplayContentModeTransitionContext setResolver:];
-[SBFDisplayContentModeTransitionContext phase];
-[SBFDisplayContentModeTransitionContext isInteractive];
-[SBFDisplayContentModeTransitionContext succinctDescription];
-[SBFDisplayContentModeTransitionContext transitionStyle];
-[SBFDisplayContentModeTransitionContext setDisplays:];
-[SBFDisplayContentModeTransitionContext displays];
-[SBFDisplayContentModeTransitionContext description];
-[SBFDisplayContentModeTransitionContext setPhase:];
-[SBFDisplayContentModeTransitionContext appendDescriptionToStream:];
-[SBFDisplayContentModeTransitionContext setInteractive:];
-[SBFDisplayContentModeTransitionContext interactiveProgress];
-[SBFDisplayContentModeTransitionContext interactiveProgressIgnoringLock];
-[SBFDisplayContentModeTransitionContext setMechanicalHingeAngleDegrees:];
-[SBFDisplayContentModeTransitionContext setSwappingHardwareIdentifiers:];
-[SBFDisplayContentModeTransitionContext _finalContentModeOfDisplay:];
-[SBFDisplayContentModeTransitionContext _finalContentModeOfDisplayWithIdentifier:];
-[SBFDisplayContentModeTransitionContext _initialContentModeOfDisplay:];
-[SBFDisplayContentModeTransitionContext _initialContentModeOfDisplayWithIdentifier:];
-[SBFDisplayContentModeTransitionContext _otherHardwareIdentifierForSwappingWithIdentifier:];
-[SBFDisplayContentModeTransitionContext _updateFinalContentModeForDisplay:newMode:];
-[SBFDisplayContentModeTransitionContext _updateInitialContentModeForDisplay:newMode:];
-[SBFDisplayContentModeTransitionContext continuousFoldBeganFromHingeEndpoint];
-[SBFDisplayContentModeTransitionContext continuousFoldEffectProgress];
-[SBFDisplayContentModeTransitionContext continuousFoldPosition];
-[SBFDisplayContentModeTransitionContext continuousFoldVelocity];
-[SBFDisplayContentModeTransitionContext finalContentModeOfDisplayForWindowScene:];
-[SBFDisplayContentModeTransitionContext hardwareIdentifiersOfTransitioningDisplays];
-[SBFDisplayContentModeTransitionContext initWithResolver:initialContentModes:finalContentModes:transitionStyle:];
-[SBFDisplayContentModeTransitionContext initialContentModeOfDisplayForWindowScene:];
-[SBFDisplayContentModeTransitionContext isHingeAtAnEndpoint];
-[SBFDisplayContentModeTransitionContext isModeSwapTransition];
-[SBFDisplayContentModeTransitionContext isProgressLockedForApplicationOfDisplayContentModeChanges];
-[SBFDisplayContentModeTransitionContext isTransitionInvolvingWindowScene:];
-[SBFDisplayContentModeTransitionContext mechanicalHingeAngleDegrees];
-[SBFDisplayContentModeTransitionContext otherHardwareIdentifierForSwappingWithWindowScene:];
-[SBFDisplayContentModeTransitionContext progressFromSwap];
-[SBFDisplayContentModeTransitionContext progressFromSwapIgnoringLock];
-[SBFDisplayContentModeTransitionContext progressToSwap];
-[SBFDisplayContentModeTransitionContext progressToSwapIgnoringLock];
-[SBFDisplayContentModeTransitionContext setContinuousFoldBeganFromHingeEndpoint:];
-[SBFDisplayContentModeTransitionContext setContinuousFoldEffectProgress:];
-[SBFDisplayContentModeTransitionContext setContinuousFoldPosition:];
-[SBFDisplayContentModeTransitionContext setContinuousFoldVelocity:];
-[SBFDisplayContentModeTransitionContext setHingeAtAnEndpoint:];
-[SBFDisplayContentModeTransitionContext setInteractiveProgress:];
-[SBFDisplayContentModeTransitionContext setInteractiveProgressIgnoringLock:];
-[SBFDisplayContentModeTransitionContext setProgressFromSwap:];
-[SBFDisplayContentModeTransitionContext setProgressFromSwapIgnoringLock:];
-[SBFDisplayContentModeTransitionContext setProgressLockedForApplicationOfDisplayContentModeChanges:];
-[SBFDisplayContentModeTransitionContext setProgressToSwap:];
-[SBFDisplayContentModeTransitionContext setProgressToSwapIgnoringLock:];
-[SBFDisplayContentModeTransitionContext swappingHardwareIdentifiers];
```
