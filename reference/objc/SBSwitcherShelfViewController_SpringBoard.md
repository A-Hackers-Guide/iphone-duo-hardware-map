# `SBSwitcherShelfViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFTouchPassThroughViewController`
- Protocols: `SBSwitcherContentViewControllerDelegate`, `SBSwitcherContentViewControllerDataSource`, `SBShelfLiveContentOverlayCoordinatorDelegate`, `SBAssistantObserver`, `SBTransientUIIndirectPanToDismissParticipant`, `SBTransientUITapToDismissParticipant`, `SBAttentionAwarenessClientDelegate`, `SBLayoutStateTransitionObserver`
- 19 instance variables, 18 properties, 74 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"SBFluidSwitcherViewController" _contentViewController;
@"SBShelfLiveContentOverlayCoordinator" _liveContentOverlayCoordinator;
@"SBShelfRootSwitcherModifier" _rootModifier;
@"SBFluidSwitcherPersonality" _personality;
@"SBAttentionAwarenessClient" _idleTouchAwarenessClient;
@"NSArray" _appLayouts;
{CGSize="width"d"height"d} _halfHalfSize;
q _activePresentationAndDismissalAnimations;
B _presented;
@"SBSwitcherShelf" _shelf;
@"<SBSwitcherShelfViewControllerDataSource>" _dataSource;
@"<SBSwitcherShelfViewControllerDelegate>" _delegate;
Q _contentOptions;
@"NSSet" _ignoredDisplayItems;
q _contentOrientation;
@"SBPortalView" _homeAffordancePortalView;
Q _animationStyle;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _presentationTargetFrame;
```

## Properties

```
@property (T@"SBSwitcherShelfView",&,D,N) view;
@property (T@"SBSwitcherShelf",R,N,V_shelf) shelf;
@property (T@"<SBSwitcherShelfViewControllerDataSource>",R,W,N,V_dataSource) dataSource;
@property (T@"<SBSwitcherShelfViewControllerDelegate>",R,W,N,V_delegate) delegate;
@property (T@"NSArray",R,C,N,V_appLayouts) appLayouts;
@property (TQ,N,V_contentOptions) contentOptions;
@property (T@"NSSet",C,N,V_ignoredDisplayItems) ignoredDisplayItems;
@property (T@"NSSet",&,N) focusedDisplayItems;
@property (Tq,N,V_contentOrientation) contentOrientation;
@property (T@"SBPortalView",&,N,V_homeAffordancePortalView) homeAffordancePortalView;
@property (TB,R,N,V_presented) presented;
@property (TB,R,N,GisPresentingOrDismissing) presentingOrDismissing;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_presentationTargetFrame) presentationTargetFrame;
@property (TQ,R,N,V_animationStyle) animationStyle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSwitcherShelfViewController _windowScene];
-[SBSwitcherShelfViewController layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:];
-[SBSwitcherShelfViewController clientDidResetForUserAttention:withEvent:];
-[SBSwitcherShelfViewController layoutStateTransitionCoordinator:transitionWillEndWithTransitionContext:];
-[SBSwitcherShelfViewController windowSceneForSwitcherContentController:];
-[SBSwitcherShelfViewController switcherInterfaceOrientationForSwitcherContentController:];
-[SBSwitcherShelfViewController client:attentionLostTimeoutDidExpire:forConfigurationGeneration:withAssociatedObject:];
-[SBSwitcherShelfViewController switcherContentController:frameForFloatingAppLayoutInInterfaceOrientation:floatingConfiguration:];
-[SBSwitcherShelfViewController appLayouts];
-[SBSwitcherShelfViewController switcherContentController:frameForCenterItemWithConfiguration:interfaceOrientation:];
-[SBSwitcherShelfViewController switcherContentController:frameForItemWithRole:inMainAppLayout:interfaceOrientation:];
-[SBSwitcherShelfViewController viewWillDisappear:];
-[SBSwitcherShelfViewController switcherContentController:requestNewWindowForBundleIdentifier:];
-[SBSwitcherShelfViewController switcherContentController:performTransitionWithRequest:gestureInitiated:];
-[SBSwitcherShelfViewController contentOrientation];
-[SBSwitcherShelfViewController dealloc];
-[SBSwitcherShelfViewController activeInterfaceOrientationForSwitcherContentController:];
-[SBSwitcherShelfViewController displayItemLayoutAttributesProvider];
-[SBSwitcherShelfViewController setContentOrientation:];
-[SBSwitcherShelfViewController appLayoutsForSwitcherContentController:];
-[SBSwitcherShelfViewController animationStyle];
-[SBSwitcherShelfViewController viewDidLoad];
-[SBSwitcherShelfViewController viewDidLayoutSubviews];
-[SBSwitcherShelfViewController windowManagementContextForSwitcherContentController:];
-[SBSwitcherShelfViewController contentOptions];
-[SBSwitcherShelfViewController switcherContentController:transitionEventForContext:identifier:phase:animated:];
-[SBSwitcherShelfViewController nextDisplayItemInteractionTimeForSwitcherContentController:];
-[SBSwitcherShelfViewController viewWillAppear:];
-[SBSwitcherShelfViewController switcherContentController:deletedDisplayItem:inAppLayout:forReason:];
-[SBSwitcherShelfViewController layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBSwitcherShelfViewController dataSource];
-[SBSwitcherShelfViewController loadView];
-[SBSwitcherShelfViewController _dockHeightWillChange:];
-[SBSwitcherShelfViewController delegate];
-[SBSwitcherShelfViewController viewWillLayoutSubviews];
-[SBSwitcherShelfViewController switcherContentController:supportsTitleItemsForAppLayout:];
-[SBSwitcherShelfViewController assistantWillAppear:windowScene:];
-[SBSwitcherShelfViewController isPresentingOrDismissing];
-[SBSwitcherShelfViewController presented];
-[SBSwitcherShelfViewController setContentOptions:];
-[SBSwitcherShelfViewController performTransitionWithContext:animated:completion:];
-[SBSwitcherShelfViewController beginHidingAppLayout:forReason:];
-[SBSwitcherShelfViewController _appLayouts];
-[SBSwitcherShelfViewController _dismissShelfIfNeededWithLocation:window:];
-[SBSwitcherShelfViewController _frameForCenterItemWithConfiguration:interfaceOrientation:];
-[SBSwitcherShelfViewController _frameForFloatingAppLayoutInInterfaceOrientation:floatingConfiguration:];
-[SBSwitcherShelfViewController _frameForItemWithRole:inMainAppLayout:interfaceOrientation:];
-[SBSwitcherShelfViewController _performNewWindowRequestForBundleIdentifier:];
-[SBSwitcherShelfViewController _performSwitcherTransitionRequest:];
-[SBSwitcherShelfViewController _rebuildCachedAppLayouts];
-[SBSwitcherShelfViewController _transitionEventForContext:identifier:phase:animated:];
-[SBSwitcherShelfViewController dismissShelfForAccessibilityTransition];
-[SBSwitcherShelfViewController dismissShelfForShelfTransition];
-[SBSwitcherShelfViewController dismissShelfWithTransitionSource:];
-[SBSwitcherShelfViewController focusedDisplayItems];
-[SBSwitcherShelfViewController homeAffordancePortalView];
-[SBSwitcherShelfViewController ignoredDisplayItems];
-[SBSwitcherShelfViewController initWithShelf:dataSource:delegate:applicationController:pictureInPictureCoordinator:];
-[SBSwitcherShelfViewController itemCornerRadiusForAppLayout:];
-[SBSwitcherShelfViewController itemFrameForAppLayout:];
-[SBSwitcherShelfViewController itemScaleForAppLayout:];
-[SBSwitcherShelfViewController performKeyboardShortcutAction:];
-[SBSwitcherShelfViewController presentationTargetFrame];
-[SBSwitcherShelfViewController setFocusedDisplayItems:];
-[SBSwitcherShelfViewController setHomeAffordancePortalView:];
-[SBSwitcherShelfViewController setIgnoredDisplayItems:];
-[SBSwitcherShelfViewController setPresented:withTargetFrame:style:completion:];
-[SBSwitcherShelfViewController shelf];
-[SBSwitcherShelfViewController shelfLiveContentOverlayCoordinator:liveViewForAppLayout:];
-[SBSwitcherShelfViewController shelfLiveContentOverlayCoordinatorAppLayouts:];
-[SBSwitcherShelfViewController shelfLiveContentOverlayCoordinatorSnapshotCache:];
-[SBSwitcherShelfViewController switcherContentController:setContentOrientation:];
-[SBSwitcherShelfViewController transientUI:wasIndirectPannedToDismissFromGestureRecognizer:];
-[SBSwitcherShelfViewController transientUIHandledTouch:withSystemGestureRecognizer:];
```
