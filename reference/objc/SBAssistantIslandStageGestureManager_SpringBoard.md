# `SBAssistantIslandStageGestureManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `SBSystemGestureRecognizerDelegate`, `AIRemoteGestureHostComponentDelegate`, `SBFZStackParticipantDelegate`, `SBAssistantIslandHomeGestureAssertionDelegate`, `SBPanSystemGestureRecognizerDelegate`, `SBReachabilityObserver`, `PTSettingsKeyObserver`, `BSInvalidatable`
- 13 instance variables, 10 properties, 48 instance methods, 0 class methods

## Instance variables

```
@"SBScreenEdgePanGestureRecognizer" _presentScreenEdgeGestureRecognizer;
@"SBPanSystemGestureRecognizer" _presentScreenEdgeGestureRecognizerFromStatusBar;
@"SBScreenEdgePanGestureRecognizer" _dismissScreenEdgeGestureRecognizer;
@"UIPanGestureRecognizer" _transientCanvasDragGestureRecognizer;
@"SBPanSystemGestureRecognizer" _activityDragGestureRecognizer;
@"AIRemoteGesture" _activeGesture;
@"SBFZStackParticipant" _zStackParticipant;
@"NSMutableSet" _homeGestureAssertions;
@"SBSystemGesturesSettings" _settings;
d _defaultPresentGestureEdgeRegionSize;
B _systemApertureIsEmpty;
@"SBWindowScene" _windowScene;
@"<SBAssistantIslandStageGestureManagerDelegate>" _delegate;
```

## Properties

```
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (T@"<SBAssistantIslandStageGestureManagerDelegate>",R,W,N,V_delegate) delegate;
@property (T@"UIGestureRecognizer",R,N) presentGestureRecognizer;
@property (T@"UIGestureRecognizer",R,N) dismissGestureRecognizer;
@property (T@"UIGestureRecognizer",R,N) transientCanvasDragGestureRecognizer;
@property (T@"UIGestureRecognizer",R,N) activityDragGestureRecognizer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAssistantIslandStageGestureManager handleReachabilityModeActivated];
-[SBAssistantIslandStageGestureManager _updatePresentGestureEdgeRegionSize];
-[SBAssistantIslandStageGestureManager handleReachabilityModeDeactivated];
-[SBAssistantIslandStageGestureManager gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[SBAssistantIslandStageGestureManager _systemGestureManager];
-[SBAssistantIslandStageGestureManager _edgeOccludingCaseStatusDidChange:];
-[SBAssistantIslandStageGestureManager _handleGestureRecognizer:];
-[SBAssistantIslandStageGestureManager gestureRecognizer:shouldReceiveTouch:];
-[SBAssistantIslandStageGestureManager zStackParticipant:updatePreferences:];
-[SBAssistantIslandStageGestureManager _stageSpaceViewForGestureRecognizer:];
-[SBAssistantIslandStageGestureManager _captureGestureStateFromGestureRecognizer:];
-[SBAssistantIslandStageGestureManager dismissGestureRecognizer];
-[SBAssistantIslandStageGestureManager _removeGestureRecognizers];
-[SBAssistantIslandStageGestureManager dealloc];
-[SBAssistantIslandStageGestureManager _isPoint:containedWithinPreferredDragRegionForTransientCanvasFrame:];
-[SBAssistantIslandStageGestureManager _systemApertureLayoutDidChange:];
-[SBAssistantIslandStageGestureManager acquireHomeGestureAssertionWithReason:];
-[SBAssistantIslandStageGestureManager zStackParticipantDidChange:];
-[SBAssistantIslandStageGestureManager _isSystemApertureGestureRecognizer:];
-[SBAssistantIslandStageGestureManager _frameForDraggableActivity];
-[SBAssistantIslandStageGestureManager settings:changedValueForKey:];
-[SBAssistantIslandStageGestureManager _updateGestureRecognizers];
-[SBAssistantIslandStageGestureManager viewForSystemGestureRecognizer:];
-[SBAssistantIslandStageGestureManager _addGestureRecognizers];
-[SBAssistantIslandStageGestureManager _isTouchOverBanner:];
-[SBAssistantIslandStageGestureManager homeGestureAssertionDidAcquire:];
-[SBAssistantIslandStageGestureManager invalidate];
-[SBAssistantIslandStageGestureManager _shouldActivityDragGesture:receiveTouch:];
-[SBAssistantIslandStageGestureManager gestureRecognizerShouldBegin:];
-[SBAssistantIslandStageGestureManager _windowSceneDidUpdateReachabilityController:];
-[SBAssistantIslandStageGestureManager gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[SBAssistantIslandStageGestureManager delegate];
-[SBAssistantIslandStageGestureManager _shouldBeginActivityDragGesture:];
-[SBAssistantIslandStageGestureManager _shouldDismissEdgeGesture:receiveTouch:];
-[SBAssistantIslandStageGestureManager homeGestureAssertionDidInvalidate:];
-[SBAssistantIslandStageGestureManager setNeedsSystemAperturePreferencesUpdate];
-[SBAssistantIslandStageGestureManager _frameForTransientCanvas];
-[SBAssistantIslandStageGestureManager transientCanvasDragGestureRecognizer];
-[SBAssistantIslandStageGestureManager remoteGestureComponentDidInvalidate:];
-[SBAssistantIslandStageGestureManager presentGestureRecognizer];
-[SBAssistantIslandStageGestureManager initWithWindowScene:delegate:];
-[SBAssistantIslandStageGestureManager _shouldTransientCanvasDragGesture:receiveTouch:];
-[SBAssistantIslandStageGestureManager _updateHomeGestureRequirement];
-[SBAssistantIslandStageGestureManager windowScene];
-[SBAssistantIslandStageGestureManager activityDragGestureRecognizer];
-[SBAssistantIslandStageGestureManager _enablementDidChange:];
-[SBAssistantIslandStageGestureManager _shouldPresentEdgeGesture:receiveTouch:];
-[SBAssistantIslandStageGestureManager _topHitTestRectForFrame:];
```
