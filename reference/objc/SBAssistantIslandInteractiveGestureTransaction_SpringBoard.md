# `SBAssistantIslandInteractiveGestureTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSpotlightInteractiveGestureTransaction`
- Protocols: `AIRemoteGestureHostComponentDelegate`
- 6 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _gestureFinishedBeforeTransactionBegan;
@"SBAssistantIslandStageController" _controller;
@"AIRemoteGesture" _remoteGesture;
d _translation;
@"SBWindowScene" _windowScene;
@"SBAssistantIslandSettings" _assistantIslandSettings;
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
-[SBAssistantIslandInteractiveGestureTransaction canInterruptForTransitionRequest:];
-[SBAssistantIslandInteractiveGestureTransaction _didComplete];
-[SBAssistantIslandInteractiveGestureTransaction _begin];
-[SBAssistantIslandInteractiveGestureTransaction _homeScreenAnimator];
-[SBAssistantIslandInteractiveGestureTransaction remoteGestureComponentDidInvalidate:];
-[SBAssistantIslandInteractiveGestureTransaction initWithTransitionRequest:];
-[SBAssistantIslandInteractiveGestureTransaction endPresentation:];
-[SBAssistantIslandInteractiveGestureTransaction updatePresentationWithProgress:translation:];
-[SBAssistantIslandInteractiveGestureTransaction _captureGestureStateFromProgress:translation:end:];
-[SBAssistantIslandInteractiveGestureTransaction _setLockScreenScale:withDuration:behaviorMode:completion:];
-[SBAssistantIslandInteractiveGestureTransaction noteGestureFinishedBeforeTransactionBegan];
```
