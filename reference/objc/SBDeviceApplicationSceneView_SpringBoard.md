# `SBDeviceApplicationSceneView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBApplicationSceneView`
- Protocols: `SBDeviceApplicationSceneClassicAccessoryViewDelegate`, `PTSettingsKeyObserver`, `SBAppSwitcherPageContentView`
- 24 instance variables, 22 properties, 85 instance methods, 0 class methods

## Instance variables

```
@"<UISceneLayerTarget>" _statusBarLayerTarget;
@"SBSceneHandleBlockObserver" _sceneHandleObserver;
@"UIApplicationSceneClientSettingsDiffInspector" _clientSettingsInspector;
@"UIApplicationSceneSettingsDiffInspector" _sceneSettingsInspector;
@"SBApplicationSceneViewStatusBarDescriptor" _statusBarDescriptor;
@"_UIDirectionalRotationView" _hostCounterRotationView;
@"SBHomeGrabberRotationView" _grabberRotationView;
@"SBFHomeGrabberSettings" _grabberSettings;
B _grabberLivesInCounterRotationView;
@"NSMutableDictionary" _overlayViewsByPriority;
@"SBDeviceApplicationSceneClassicAccessoryView" _classicAccessoryView;
@"SBDeviceApplicationSceneClassicWrapperView" _classicWrapperView;
@"SBDeviceApplicationSceneClassicWrapperView" _liveSnapshotWrapperView;
@"UIView" _wrappedLiveSnapshotView;
B _obscuredByKeyboardOverlay;
@"<BSInvalidatable>" _snapshottingInfoAssertion;
@"UIView<UIScenePresentation>" _currentHostView;
@"NSMutableArray" _multitaskingExclusionRectDebugViews;
@"SBMedusaSettings" _medusaSettings;
@"_UITransitionOverlayView" _transitionOverlayView;
@"SBWallpaperController" _wallpaperController;
B _active;
B _visible;
d _statusBarAlpha;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBDeviceApplicationSceneHandle",R,D,N) sceneHandle;
@property (T@"UIView<SBApplicationSceneBackgroundView>",&,D,N) backgroundView;
@property (TB,N) forcesStatusBarHidden;
@property (T@"SBApplicationSceneViewStatusBarDescriptor",&,N,V_statusBarDescriptor) statusBarDescriptor;
@property (Td,N,V_statusBarAlpha) statusBarAlpha;
@property (T@"SBHomeGrabberView",R,N) homeGrabberView;
@property (TB,N,GisObscuredByKeyboardOverlay) obscuredByKeyboardOverlay;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,N) cornerRadius;
@property (TQ,N) maskedCorners;
@property (T{CACornerRadii={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}},N) cornerRadii;
@property (Tq,N) orientation;
@property (TB,R,N) contentRequiresGroupOpacity;
@property (TB,N,GisActive,V_active) active;
@property (TB,N,GisVisible,V_visible) visible;
```

## Instance methods

```
-[SBDeviceApplicationSceneView statusBarAlpha];
-[SBDeviceApplicationSceneView cornerRadii];
-[SBDeviceApplicationSceneView _adjustedOverlayViewPriorities];
-[SBDeviceApplicationSceneView addOverlayView:withPriority:];
-[SBDeviceApplicationSceneView homeGrabberView];
-[SBDeviceApplicationSceneView didMoveToWindow];
-[SBDeviceApplicationSceneView noteFrameInKeyboardReferenceSpaceMayHaveChanged];
-[SBDeviceApplicationSceneView _hidingView:wouldAlsoHideView:];
-[SBDeviceApplicationSceneView _wantsBlackBackground];
-[SBDeviceApplicationSceneView setVisible:];
-[SBDeviceApplicationSceneView sceneContentCoordinateSpace];
-[SBDeviceApplicationSceneView _enumerateOrderedOverlayViewPriorities:];
-[SBDeviceApplicationSceneView contentRequiresGroupOpacity];
-[SBDeviceApplicationSceneView _updateStatusBarVisibilityForHostView];
-[SBDeviceApplicationSceneView isObscuredByKeyboardOverlay];
-[SBDeviceApplicationSceneView _createClassicWrapperViewIfNecessaryForHostView:];
-[SBDeviceApplicationSceneView statusBarDescriptor];
-[SBDeviceApplicationSceneView dealloc];
-[SBDeviceApplicationSceneView _updateEdgeProtectAndAutoHideOnHomeGrabberView];
-[SBDeviceApplicationSceneView sceneHandle:didChangeContentPrefersToDisableClipping:];
-[SBDeviceApplicationSceneView setForcesStatusBarHidden:];
-[SBDeviceApplicationSceneView setCornerRadii:];
-[SBDeviceApplicationSceneView isVisible];
-[SBDeviceApplicationSceneView layoutSubviews];
-[SBDeviceApplicationSceneView _contentFrame];
-[SBDeviceApplicationSceneView maskedCorners];
-[SBDeviceApplicationSceneView _wallpaperStyle];
-[SBDeviceApplicationSceneView _contentContainerEdgeInsets];
-[SBDeviceApplicationSceneView setActive:];
-[SBDeviceApplicationSceneView _crossfadeClipsToBounds];
-[SBDeviceApplicationSceneView _tearDownHostCounterRotationViewIfNecessary];
-[SBDeviceApplicationSceneView setCornerRadius:];
-[SBDeviceApplicationSceneView _createHostCounterRotationViewIfNecessary];
-[SBDeviceApplicationSceneView setBounds:];
-[SBDeviceApplicationSceneView settings:changedValueForKey:];
-[SBDeviceApplicationSceneView setObscuredByKeyboardOverlay:];
-[SBDeviceApplicationSceneView invalidate];
-[SBDeviceApplicationSceneView resolvedHingeEdge];
-[SBDeviceApplicationSceneView setMaskedCorners:];
-[SBDeviceApplicationSceneView setStatusBarAlpha:];
-[SBDeviceApplicationSceneView _sceneHandleDidUpdateSettingsWithDiff:previousSettings:];
-[SBDeviceApplicationSceneView _sceneHandleDidUpdateClientSettings:];
-[SBDeviceApplicationSceneView _useClassicAccessoryView];
-[SBDeviceApplicationSceneView _layoutLiveSnapshotView:];
-[SBDeviceApplicationSceneView _invalidateSceneLiveHostView:];
-[SBDeviceApplicationSceneView enableTransitionOverlay:];
-[SBDeviceApplicationSceneView willRotateFromInterfaceOrientation:toInterfaceOrientation:alongsideContainerView:animated:];
-[SBDeviceApplicationSceneView _didDiscardLiveSnapshotView:];
-[SBDeviceApplicationSceneView _sceneDrivesOwnRotation];
-[SBDeviceApplicationSceneView createHomeGrabberViewIfNecessaryWithSettings:];
-[SBDeviceApplicationSceneView cornerRadius];
-[SBDeviceApplicationSceneView _cleanUpTransitionOverlayView:];
-[SBDeviceApplicationSceneView _updateDragAndDropExclusionDebugViewsIfNecessary];
-[SBDeviceApplicationSceneView forcesStatusBarHidden];
-[SBDeviceApplicationSceneView _layoutLiveHostView:];
-[SBDeviceApplicationSceneView _configureSceneLiveHostView:];
-[SBDeviceApplicationSceneView _contentContainerCornerRadius];
-[SBDeviceApplicationSceneView applicationSceneCompatibilityModeAnimatingChangeTo:];
-[SBDeviceApplicationSceneView _setOrientation:];
-[SBDeviceApplicationSceneView noteApplicationClassicPhoneSceneOrientationPreferenceChangingForUserAction:];
-[SBDeviceApplicationSceneView _configureSceneLiveSnapshotView:];
-[SBDeviceApplicationSceneView description];
-[SBDeviceApplicationSceneView tearDownHomeGrabberView];
-[SBDeviceApplicationSceneView _transitionViewForHostView];
-[SBDeviceApplicationSceneView _transitionViewForLiveSnapshotView:];
-[SBDeviceApplicationSceneView _refresh];
-[SBDeviceApplicationSceneView _representsTranslucentContent];
-[SBDeviceApplicationSceneView teardownClassicAccessoryViewIfNecessary];
-[SBDeviceApplicationSceneView _windowManagementStyleDidChange:];
-[SBDeviceApplicationSceneView deviceApplicationSceneView];
-[SBDeviceApplicationSceneView isActive];
-[SBDeviceApplicationSceneView sceneHandle:didChangePreferredHingeEdge:];
-[SBDeviceApplicationSceneView compatibilityContentContainerForOrientation:];
-[SBDeviceApplicationSceneView setStatusBarDescriptor:];
-[SBDeviceApplicationSceneView prepareForContentRotation];
-[SBDeviceApplicationSceneView _shouldAnimatePropertyWithKey:];
-[SBDeviceApplicationSceneView sceneHandle:didChangeFillingCompatibilityReservedStrip:];
-[SBDeviceApplicationSceneView _compatibilityReservedStripForOrientation:];
-[SBDeviceApplicationSceneView setBackgroundView:];
-[SBDeviceApplicationSceneView createClassicAccessoryViewIfNecessary];
-[SBDeviceApplicationSceneView _useClassicWrapperView];
-[SBDeviceApplicationSceneView initWithSceneHandle:referenceSize:contentOrientation:containerOrientation:hostRequester:];
-[SBDeviceApplicationSceneView _configureSceneSnapshot:];
-[SBDeviceApplicationSceneView _contentPrefersToDisableClipping];
-[SBDeviceApplicationSceneView removeOverlayView:withPriority:];
```
