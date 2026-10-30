# `SBInteractiveScreenshotGestureManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSTransactionObserver`, `SBInteractiveScreenshotCommitWorkspaceTransactionDelegate`, `SBInteractiveScreenshotGestureRootViewControllerDelegate`, `SBAppInteractionEventSourceObserving`, `SBSystemGestureRecognizerDelegate`
- 22 instance variables, 5 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _activeGestureSessionID;
@"SBDisplayAppInteractionEventSource" _appInteractionEventSource;
@"SBAsynchronousRenderingAssertion" _asynchronousRenderingAssertion;
@"SBCornerPencilPanGestureRecognizer" _bottomLeftPencilGestureRecognizer;
@"SBCornerFingerPanGestureRecognizer" _bottomLeftFingerGestureRecognizer;
@"SBCornerPencilPanGestureRecognizer" _bottomRightPencilGestureRecognizer;
@"SBCornerFingerPanGestureRecognizer" _bottomRightFingerGestureRecognizer;
@"SBInteractiveScreenshotCommitWorkspaceTransaction" _commitTransaction;
@"<BSInvalidatable>" _commitTransactionDisableGestureAssertion;
@"NSMutableSet" _disableGestureAssertions;
B _hasInitiatedCommit;
B _isCapturingScreenshot;
d _lastApplicationTouchTime;
@"NSMutableArray" _pendingCommitWorkspaceTransactionBlocks;
@"UIScreen" _screen;
@"NSMutableDictionary" _sessionIDToSession;
@"SBInteractiveScreenshotSettings" _settings;
@"SBSystemGestureManager" _systemGestureManager;
@"NSHashTable" _weakReusableGestureRootWindows;
@"SBMainWorkspace" _workspace;
@"SBWindowScene" _windowScene;
@"<SBInteractiveScreenshotGestureManagerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBInteractiveScreenshotGestureManagerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBInteractiveScreenshotGestureManager eventSource:userTouchedApplication:];
-[SBInteractiveScreenshotGestureManager gestureRecognizer:shouldReceiveTouch:];
-[SBInteractiveScreenshotGestureManager transactionDidComplete:];
-[SBInteractiveScreenshotGestureManager dealloc];
-[SBInteractiveScreenshotGestureManager viewForSystemGestureRecognizer:];
-[SBInteractiveScreenshotGestureManager setDelegate:];
-[SBInteractiveScreenshotGestureManager gestureRecognizerShouldBegin:];
-[SBInteractiveScreenshotGestureManager delegate];
-[SBInteractiveScreenshotGestureManager _invalidateSessionID:];
-[SBInteractiveScreenshotGestureManager _performPendingCommitWorkspaceTransactionBlocksWithTransaction:];
-[SBInteractiveScreenshotGestureManager _touchTypeForGestureRecognizer:];
-[SBInteractiveScreenshotGestureManager _handleInteractiveScreenshotGesture:];
-[SBInteractiveScreenshotGestureManager _performCommitWorkspaceTransactionBlock:];
-[SBInteractiveScreenshotGestureManager _screenshotPresentationOptions];
-[SBInteractiveScreenshotGestureManager _springBoardBootCompleted:];
-[SBInteractiveScreenshotGestureManager _updateFailureRequirements];
-[SBInteractiveScreenshotGestureManager acquireDisableGestureAssertionWithReason:];
-[SBInteractiveScreenshotGestureManager handleRemoteTransientOverlayPresentationRequest:forSession:];
-[SBInteractiveScreenshotGestureManager initWithWindowScene:workspace:appInteractionEventSource:];
-[SBInteractiveScreenshotGestureManager interactiveScreenshotCommitWorkspaceTransactionRequestsGestureWindowInvalidation:];
-[SBInteractiveScreenshotGestureManager interactiveScreenshotCommitWorkspaceTransactionRequestsPlaceholderChromeRemoval:];
-[SBInteractiveScreenshotGestureManager interactiveScreenshotGestureRootViewController:gestureDidCompleteWithIntent:];
-[SBInteractiveScreenshotGestureManager interactiveScreenshotGestureRootViewControllerRequestsGestureRecognizerCancellation:];
```
