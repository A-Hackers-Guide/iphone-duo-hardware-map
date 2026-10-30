# `SBSystemNotesContentViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBWorkspaceApplicationSceneTransitionContextDelegate`, `SBFSystemPointerInteractionDelegate`, `SBTransientUITapToDismissParticipant`, `SBDeviceApplicationSceneHandleObserver`, `SBSceneHandleActionConsuming`, `SBPIPSceneContentProviding`
- 25 instance variables, 9 properties, 48 instance methods, 0 class methods

## Instance variables

```
@"SBSystemNotesInteractionSettings" _notesInteractionSettings;
@"SBDeviceApplicationSceneViewController" _sceneViewController;
@"SBNubView" _nubView;
@"SBApplicationBlurContentView" _blurView;
@"SBMainWorkspace" _workspace;
@"UITapGestureRecognizer" _thumbnailTapGestureRecognizer;
@"UIView" _thumbnailView;
@"SBSystemNotesPlaceholderContentProvider" _placeholderProvider;
@"SBSceneViewStatusBarAssertion" _statusBarAssertion;
@"<BSInvalidatable>" _hostingAssertion;
@"SBTransientUIInteractionManager" _transientUIInteractionManager;
@"SBSystemPointerInteractionManager" _systemPointerInteractionManager;
{CGSize="width"d"height"d} _preferredSceneContentSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastKnownSceneFrame;
@"SBSSystemNotesPresentationConfiguration" _currentConfiguration;
@"SBSystemNotesContentPresentationContext" _presentationContext;
@"BSAbsoluteMachTimer" _thumbnailCooldownTimer;
B _thumbnailCooldownTimerFired;
B _haveBeenForeground;
@"NSString" _pendingAnalyticsString;
@"TRAArbiter" _arbiter;
@"SBWindowScene" _lastKnownWindowScene;
@"TRAParticipant" _traitsParticipant;
@"SBTraitsSceneParticipantDelegate" _traitsParticipantDelegate;
@"<SBSystemNotesContentViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"SBDeviceApplicationSceneHandle",R,N) sceneHandle;
@property (T@"SBSSystemNotesPresentationConfiguration",R,N) currentConfiguration;
@property (Tq,N) presentationMode;
@property (T@"NSString",R,C,N) bundleIdentifier;
@property (T@"<SBSystemNotesContentViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemNotesContentViewController sceneHandle:didDestroyScene:];
-[SBSystemNotesContentViewController sceneHandle:clientConnectedForScene:];
-[SBSystemNotesContentViewController presentationMode];
-[SBSystemNotesContentViewController styleForRegion:forView:];
-[SBSystemNotesContentViewController setPresentationMode:];
-[SBSystemNotesContentViewController sceneHandle];
-[SBSystemNotesContentViewController viewWillDisappear:];
-[SBSystemNotesContentViewController currentConfiguration];
-[SBSystemNotesContentViewController dealloc];
-[SBSystemNotesContentViewController applicationTransitionContext:frameForApplicationSceneEntity:];
-[SBSystemNotesContentViewController bundleIdentifier];
-[SBSystemNotesContentViewController viewDidLoad];
-[SBSystemNotesContentViewController layoutStateForApplicationTransitionContext:];
-[SBSystemNotesContentViewController shouldAutorotate];
-[SBSystemNotesContentViewController shouldBeginPointerInteractionRequest:atLocation:forView:];
-[SBSystemNotesContentViewController viewWillAppear:];
-[SBSystemNotesContentViewController setDelegate:];
-[SBSystemNotesContentViewController previousLayoutStateForApplicationTransitionContext:];
-[SBSystemNotesContentViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[SBSystemNotesContentViewController viewDidAppear:];
-[SBSystemNotesContentViewController contentView];
-[SBSystemNotesContentViewController delegate];
-[SBSystemNotesContentViewController sceneHandle:didReceiveAction:];
-[SBSystemNotesContentViewController viewWillLayoutSubviews];
-[SBSystemNotesContentViewController viewDidDisappear:];
-[SBSystemNotesContentViewController preferredContentSize];
-[SBSystemNotesContentViewController pointerInteractionHitTestInsetsForView:];
-[SBSystemNotesContentViewController containerViewControllerDidEndInteraction:targetWindowScene:];
-[SBSystemNotesContentViewController _acquireTraitsParticipantOnWindowSceneIfNecessary:];
-[SBSystemNotesContentViewController _handleThumbnailTapGesture:];
-[SBSystemNotesContentViewController _hitTestTouch:gestureRecognizer:];
-[SBSystemNotesContentViewController _imageFromUserActivity:presentationMode:];
-[SBSystemNotesContentViewController _invalidateTraitsParticipant];
-[SBSystemNotesContentViewController _sbWindowSceneForSceneHandle:];
-[SBSystemNotesContentViewController _sceneFrame];
-[SBSystemNotesContentViewController _sendActionForUpdatedConfiguration:sendCreateIfNecessary:];
-[SBSystemNotesContentViewController _setBlurred:];
-[SBSystemNotesContentViewController _setPreferredSceneContentSize:];
-[SBSystemNotesContentViewController _thumbnailViewForUserActivity:];
-[SBSystemNotesContentViewController _updateForegroundStatus:];
-[SBSystemNotesContentViewController _updateSceneFrameWithCompletion:];
-[SBSystemNotesContentViewController containerViewController:didSettleOnStashState:];
-[SBSystemNotesContentViewController containerViewController:shouldHandleStashingForTransitionContext:];
-[SBSystemNotesContentViewController containerViewControllerDidEndSizeChange:];
-[SBSystemNotesContentViewController containerViewControllerWillBeginSizeChange:behavior:];
-[SBSystemNotesContentViewController initWithSceneHandle:workspace:transientUIInteractionManager:notesInteractionSettings:presentationContext:];
-[SBSystemNotesContentViewController transientUIHandledTouch:withSystemGestureRecognizer:];
-[SBSystemNotesContentViewController updateConfiguration:sendCreateActionIfNecessary:];
```
