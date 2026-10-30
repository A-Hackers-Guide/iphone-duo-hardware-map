# `SBTransientOverlayPresentWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBMainWorkspaceTransaction`
- Protocols: `SBUIAnimationControllerObserver`
- 3 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"SBUIAnimationController" _animation;
@"<BSInvalidatable>" _displayLayoutTransitionAssertion;
@"<BSInvalidatable>" _eventBufferingAssertion;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBTransientOverlayPresentWorkspaceTransaction canInterruptForTransitionRequest:];
-[SBTransientOverlayPresentWorkspaceTransaction _willBegin];
-[SBTransientOverlayPresentWorkspaceTransaction _canBeInterrupted];
-[SBTransientOverlayPresentWorkspaceTransaction _didComplete];
-[SBTransientOverlayPresentWorkspaceTransaction _begin];
-[SBTransientOverlayPresentWorkspaceTransaction _performStandardPresentationAnimated:];
-[SBTransientOverlayPresentWorkspaceTransaction _logForInterruptAttemptReason:];
-[SBTransientOverlayPresentWorkspaceTransaction _willInterruptWithReason:];
-[SBTransientOverlayPresentWorkspaceTransaction initWithTransitionRequest:];
-[SBTransientOverlayPresentWorkspaceTransaction animationControllerDidFinishAnimation:];
```
