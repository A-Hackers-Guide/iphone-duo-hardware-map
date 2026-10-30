# `SBTopAffordanceViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBAffordancePresenceControllerDelegate`, `SWKWindowControlsViewControllerDelegate`, `SBDeviceApplicationSceneHandleObserver`, `SBTransientUITapToDismissParticipant`, `SBTransientUIIndirectPanToDismissParticipant`, `SBTopAffordanceControlling`, `SBWindowControlsControlling`
- 14 instance variables, 9 properties, 47 instance methods, 0 class methods

## Instance variables

```
@"SBAffordancePresenceController" _affordancePresenceController;
q _optionsMask;
q _interfaceOrientation;
@"SWKWindowControlsViewController" _windowControlsViewController;
{CGSize="width"d"height"d} _windowControlsInitialSize;
{CGPoint="x"d"y"d} _effectiveWindowControlsLayoutMargin;
@"SBDeviceApplicationSceneHandle" _sceneHandle;
@"BSSpringAnimationSettings" _styleSettings;
B _hidden;
{SBWindowControlsLayout="style"q"underlapsStatusBar"B"margin"{CGPoint="x"d"y"d}} _windowControlsLayout;
B _highlighted;
B _autoHides;
q _activeAppearance;
@"<SBTopAffordanceViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBTopAffordanceViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisHighlighted,V_highlighted) highlighted;
@property (TB,R,N,GisExpanded) expanded;
@property (TB,N,V_autoHides) autoHides;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,N,V_activeAppearance) activeAppearance;
```

## Instance methods

```
-[SBTopAffordanceViewController dismissAnimated:];
-[SBTopAffordanceViewController sceneHandle:clientConnectedForScene:];
-[SBTopAffordanceViewController setHidden:];
-[SBTopAffordanceViewController isExpanded];
-[SBTopAffordanceViewController autoHides];
-[SBTopAffordanceViewController isHighlighted];
-[SBTopAffordanceViewController sceneHandle:didUpdateSettingsWithDiff:previousSettings:];
-[SBTopAffordanceViewController dealloc];
-[SBTopAffordanceViewController activeAppearance];
-[SBTopAffordanceViewController viewDidLoad];
-[SBTopAffordanceViewController shouldAutorotate];
-[SBTopAffordanceViewController updateWindowControlsLayout:];
-[SBTopAffordanceViewController updateTopAffordanceContextMenuWithOptions:selectedActionType:layout:hidden:interfaceOrientation:];
-[SBTopAffordanceViewController setDelegate:];
-[SBTopAffordanceViewController isHidden];
-[SBTopAffordanceViewController setHighlighted:];
-[SBTopAffordanceViewController setOverrideUserInterfaceStyle:];
-[SBTopAffordanceViewController loadView];
-[SBTopAffordanceViewController delegate];
-[SBTopAffordanceViewController viewWillLayoutSubviews];
-[SBTopAffordanceViewController windowControlsView];
-[SBTopAffordanceViewController traitCollectionDidChange:];
-[SBTopAffordanceViewController setAutoHides:];
-[SBTopAffordanceViewController affordancePresenceController:didChangeToPresence:];
-[SBTopAffordanceViewController setActiveAppearance:];
-[SBTopAffordanceViewController _safeAreaEdgeInsetsForSettings:];
-[SBTopAffordanceViewController _dismissIfNeededWithLocation:window:];
-[SBTopAffordanceViewController _lockScreenUIDidLock:];
-[SBTopAffordanceViewController _setWindowControlsLayout:];
-[SBTopAffordanceViewController _updateStyleForOverrideUserInterfaceStyle];
-[SBTopAffordanceViewController _updateWindowControlsLayoutAnimated:previousLayout:];
-[SBTopAffordanceViewController _updateWindowControlsViewFrame];
-[SBTopAffordanceViewController _updateWindowControlsViewFrameHidden:];
-[SBTopAffordanceViewController _windowControlsAccessibilityIdentifier];
-[SBTopAffordanceViewController initWithDeviceApplicationSceneHandle:];
-[SBTopAffordanceViewController setHidden:forReason:animated:];
-[SBTopAffordanceViewController transientUI:wasIndirectPannedToDismissFromGestureRecognizer:];
-[SBTopAffordanceViewController transientUIHandledTouch:withSystemGestureRecognizer:];
-[SBTopAffordanceViewController updateWindowControlsAdaptiveStyle:adaptive:];
-[SBTopAffordanceViewController windowControlsViewController:didRequestAction:];
-[SBTopAffordanceViewController windowControlsViewController:didRequestArrangeWithConfiguration:];
-[SBTopAffordanceViewController windowControlsViewController:didRequestMoveToDisplay:];
-[SBTopAffordanceViewController windowControlsViewController:didRequestSlideOverAction:];
-[SBTopAffordanceViewController windowControlsViewController:didRequestTileToPosition:];
-[SBTopAffordanceViewController windowControlsViewControllerDidRequestAddAnotherWindow:];
-[SBTopAffordanceViewController windowControlsViewControllerWillCollapse:];
-[SBTopAffordanceViewController windowControlsViewControllerWillExpand:];
```
