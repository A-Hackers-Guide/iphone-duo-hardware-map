# `SBPIPSplitPIPStagingTransitionAssistant`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`
- 11 instance variables, 8 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"UIViewController" _pictureInPictureViewController;
@"UIPanGestureRecognizer" _exitPanGestureRecognizer;
@"SBPIPInteractionController" _exitPanInteractionController;
B _hasPendingDrop;
B _isExitingForDrag;
B _cancelsPendingEnter;
B _invalidated;
B _staging;
B _interactionInFlight;
@"<SBPIPSplitPIPStagingTransitionAssistantDelegate>" _delegate;
@"SBLayoutStateTransitionCoordinator" _layoutStateTransitionCoordinator;
```

## Properties

```
@property (T@"<SBPIPSplitPIPStagingTransitionAssistantDelegate>",W,N,V_delegate) delegate;
@property (T@"SBLayoutStateTransitionCoordinator",W,N,V_layoutStateTransitionCoordinator) layoutStateTransitionCoordinator;
@property (TB,R,N,GisStaging,V_staging) staging;
@property (TB,R,N,GisInteractionInFlight,V_interactionInFlight) interactionInFlight;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPIPSplitPIPStagingTransitionAssistant gestureRecognizer:shouldReceiveTouch:];
-[SBPIPSplitPIPStagingTransitionAssistant layoutStateTransitionCoordinator];
-[SBPIPSplitPIPStagingTransitionAssistant invalidate];
-[SBPIPSplitPIPStagingTransitionAssistant setDelegate:];
-[SBPIPSplitPIPStagingTransitionAssistant gestureRecognizerShouldBegin:];
-[SBPIPSplitPIPStagingTransitionAssistant delegate];
-[SBPIPSplitPIPStagingTransitionAssistant setLayoutStateTransitionCoordinator:];
-[SBPIPSplitPIPStagingTransitionAssistant _removeExitPanGestureRecognizer];
-[SBPIPSplitPIPStagingTransitionAssistant resizeDidSettle];
-[SBPIPSplitPIPStagingTransitionAssistant _commitWhileInSplitPIP:];
-[SBPIPSplitPIPStagingTransitionAssistant _handleExitPanGesture:];
-[SBPIPSplitPIPStagingTransitionAssistant _leaveSplitPIP];
-[SBPIPSplitPIPStagingTransitionAssistant _requestExitForDrag];
-[SBPIPSplitPIPStagingTransitionAssistant _setInteractionInFlight:];
-[SBPIPSplitPIPStagingTransitionAssistant beginStaging];
-[SBPIPSplitPIPStagingTransitionAssistant consumeCancelledEnter];
-[SBPIPSplitPIPStagingTransitionAssistant consumePendingDrop];
-[SBPIPSplitPIPStagingTransitionAssistant endStagingWithCommit:];
-[SBPIPSplitPIPStagingTransitionAssistant exitCancelledEnter];
-[SBPIPSplitPIPStagingTransitionAssistant initWithPictureInPictureViewController:];
-[SBPIPSplitPIPStagingTransitionAssistant isInteractionInFlight];
-[SBPIPSplitPIPStagingTransitionAssistant isStaging];
-[SBPIPSplitPIPStagingTransitionAssistant layoutStateTransitionDidEnd];
-[SBPIPSplitPIPStagingTransitionAssistant updateExitDrag];
```
