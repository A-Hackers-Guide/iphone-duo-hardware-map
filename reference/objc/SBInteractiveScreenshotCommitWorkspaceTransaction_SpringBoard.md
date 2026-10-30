# `SBInteractiveScreenshotCommitWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBMainWorkspaceTransaction`
- Protocols: `SBTransientOverlayPresentWorkspaceTransactionObserver`
- 11 instance variables, 9 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _hasBeganPresentation;
B _hasFinishedPresentation;
B _hasQueuedPresentationTransaction;
B _hasRequestedPlaceholderChromeRemoval;
B _hasWatchdogExpired;
@"NSTimer" _watchdogTimeoutTimer;
B _hasFinishedFlashAnimation;
B _hasFinishedSettlingAnimation;
@"NSUUID" _gestureSessionID;
@"SBTransientOverlayViewController" _screenshotMarkupTransientOverlayViewController;
@"<SBInteractiveScreenshotCommitWorkspaceTransactionDelegate>" _interactiveScreenshotCommitDelegate;
```

## Properties

```
@property (T@"NSUUID",R,C,N,V_gestureSessionID) gestureSessionID;
@property (TB,N,V_hasFinishedFlashAnimation) hasFinishedFlashAnimation;
@property (TB,N,V_hasFinishedSettlingAnimation) hasFinishedSettlingAnimation;
@property (T@"SBTransientOverlayViewController",&,N,V_screenshotMarkupTransientOverlayViewController) screenshotMarkupTransientOverlayViewController;
@property (T@"<SBInteractiveScreenshotCommitWorkspaceTransactionDelegate>",W,N,V_interactiveScreenshotCommitDelegate) interactiveScreenshotCommitDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBInteractiveScreenshotCommitWorkspaceTransaction _updateState];
-[SBInteractiveScreenshotCommitWorkspaceTransaction _begin];
-[SBInteractiveScreenshotCommitWorkspaceTransaction _handleWatchdogTimeout];
-[SBInteractiveScreenshotCommitWorkspaceTransaction gestureSessionID];
-[SBInteractiveScreenshotCommitWorkspaceTransaction hasFinishedFlashAnimation];
-[SBInteractiveScreenshotCommitWorkspaceTransaction hasFinishedSettlingAnimation];
-[SBInteractiveScreenshotCommitWorkspaceTransaction initWithTransitionRequest:gestureSessionID:];
-[SBInteractiveScreenshotCommitWorkspaceTransaction interactiveScreenshotCommitDelegate];
-[SBInteractiveScreenshotCommitWorkspaceTransaction screenshotMarkupTransientOverlayViewController];
-[SBInteractiveScreenshotCommitWorkspaceTransaction setHasFinishedFlashAnimation:];
-[SBInteractiveScreenshotCommitWorkspaceTransaction setHasFinishedSettlingAnimation:];
-[SBInteractiveScreenshotCommitWorkspaceTransaction setInteractiveScreenshotCommitDelegate:];
-[SBInteractiveScreenshotCommitWorkspaceTransaction setScreenshotMarkupTransientOverlayViewController:];
-[SBInteractiveScreenshotCommitWorkspaceTransaction transientOverlayPresentWorkspaceTransactionDidPerformPresentation:];
```
