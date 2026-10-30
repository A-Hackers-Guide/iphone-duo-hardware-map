# `SBDeviceApplicationSceneClassicWrapperView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `SBFDevicePoseProviderObserver`, `PTSettingsKeyObserver`
- 18 instance variables, 13 properties, 50 instance methods, 2 class methods

## Instance variables

```
@"_SBDeviceApplicationSceneClassicHostPositioningView" _positioningView;
@"SBAppSwitcherDefaults" _appSwitcherDefaults;
@"<BSDefaultObserver>" _appSwitcherDefaultsObserver;
@"SBSwitcherWindowingSettings" _windowingSettings;
B _canRasterize;
@"<BSInvalidatable>" _classicLetterboxRegistration;
{?="horizontal"q"vertical"q} _contentAlignments;
B _contentAlignmentsAreUserChosen;
{CGSize="width"d"height"d} _lastLaidOutFullScreenContentSize;
{?="reservedEdge"Q"extent"d"contentAlignmentEdge"Q} _reservedStrip;
B _hasLaidOutScene;
{?="sceneReferenceFrame"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"sceneInterfaceOrientation"q"orientation"q"hingeEdge"Q"reservedStrip"{?="reservedEdge"Q"extent"d"contentAlignmentEdge"Q}"screenRegionBounds"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}} _lastLayoutInputs;
Q _lastHalfHingeEdge;
B _suppressLayoutUpdatesForStartOfClassicPhoneAppRotation;
B _preparingForUserDrivenClassicRotation;
@"SBDeviceApplicationSceneHandle" _sceneHandle;
q _orientation;
q _startingOrientationForClassicPhoneAppRotation;
```

## Properties

```
@property (T@"SBDeviceApplicationSceneHandle",R,N,V_sceneHandle) sceneHandle;
@property (T@"NSArray",R,N) contentViews;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) contentFrame;
@property (Tq,N,V_orientation) orientation;
@property (TB,R,N) wantsBlackBackground;
@property (TB,N,V_suppressLayoutUpdatesForStartOfClassicPhoneAppRotation) suppressLayoutUpdatesForStartOfClassicPhoneAppRotation;
@property (TB,N,V_preparingForUserDrivenClassicRotation) preparingForUserDrivenClassicRotation;
@property (Tq,N,V_startingOrientationForClassicPhoneAppRotation) startingOrientationForClassicPhoneAppRotation;
@property (TB,R,N) allowsContentAlignmentAdjustment;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBDeviceApplicationSceneClassicWrapperView shouldUseWrapperViewForSceneHandle:];
+[SBDeviceApplicationSceneClassicWrapperView wrapperForSnapshotOfSceneHandle:liveWrapper:];
```

## Instance methods

```
-[SBDeviceApplicationSceneClassicWrapperView setOrientation:];
-[SBDeviceApplicationSceneClassicWrapperView contentViews];
-[SBDeviceApplicationSceneClassicWrapperView sceneHandle];
-[SBDeviceApplicationSceneClassicWrapperView contentFrame];
-[SBDeviceApplicationSceneClassicWrapperView orientation];
-[SBDeviceApplicationSceneClassicWrapperView removeContentView:];
-[SBDeviceApplicationSceneClassicWrapperView dealloc];
-[SBDeviceApplicationSceneClassicWrapperView initWithSceneHandle:];
-[SBDeviceApplicationSceneClassicWrapperView layoutSubviews];
-[SBDeviceApplicationSceneClassicWrapperView addContentView:];
-[SBDeviceApplicationSceneClassicWrapperView settings:changedValueForKey:];
-[SBDeviceApplicationSceneClassicWrapperView poseProvider:didUpdateFromPose:toPose:];
-[SBDeviceApplicationSceneClassicWrapperView _isDisplaySized];
-[SBDeviceApplicationSceneClassicWrapperView _isHingeOpeningTowardsFullyOpen];
-[SBDeviceApplicationSceneClassicWrapperView _fullScreenSize];
-[SBDeviceApplicationSceneClassicWrapperView _isClassicContentRepositionable];
-[SBDeviceApplicationSceneClassicWrapperView _animateContentAlignmentChange];
-[SBDeviceApplicationSceneClassicWrapperView _clearRegisteredClassicLetterboxInnerFrame];
-[SBDeviceApplicationSceneClassicWrapperView _contentAreaBounds];
-[SBDeviceApplicationSceneClassicWrapperView _contentCenterForAlignments:vertical:];
-[SBDeviceApplicationSceneClassicWrapperView _cornerRadiiForContentFrame:inContentArea:reservedStrip:];
-[SBDeviceApplicationSceneClassicWrapperView _currentOrLastHingeEdgeInHalf:];
-[SBDeviceApplicationSceneClassicWrapperView _effectiveSceneBounds];
-[SBDeviceApplicationSceneClassicWrapperView _isFlexibleWindowingEnabled];
-[SBDeviceApplicationSceneClassicWrapperView _isProbablyScreenSized];
-[SBDeviceApplicationSceneClassicWrapperView _layoutForScreenRegionBounds:reservedStrip:sceneBounds:requiresClassicTreatment:classicAppScaled:stretchesToFill:];
-[SBDeviceApplicationSceneClassicWrapperView _recordLayoutInputs:];
-[SBDeviceApplicationSceneClassicWrapperView _registerClassicLetterboxInnerFrame:forSceneIdentifier:];
-[SBDeviceApplicationSceneClassicWrapperView _reservedStripForHingeEdge:];
-[SBDeviceApplicationSceneClassicWrapperView _reservedStripForLayoutWithHingeEdge:];
-[SBDeviceApplicationSceneClassicWrapperView _sceneInterfaceOrientation];
-[SBDeviceApplicationSceneClassicWrapperView _sceneReferenceFrame];
-[SBDeviceApplicationSceneClassicWrapperView _sceneSizeDiffersBetweenFullScreenAndHalfWithHingeEdge:];
-[SBDeviceApplicationSceneClassicWrapperView _screenRegionBoundsForLayoutWithHingeEdge:];
-[SBDeviceApplicationSceneClassicWrapperView _shouldInterpolateBetweenHalfWithHingeEdge:];
-[SBDeviceApplicationSceneClassicWrapperView _shouldRasterizePositioningLayer];
-[SBDeviceApplicationSceneClassicWrapperView _statusBarOcclusionRect];
-[SBDeviceApplicationSceneClassicWrapperView _updateClassicLetterboxRegions];
-[SBDeviceApplicationSceneClassicWrapperView _windowingModeChanged];
-[SBDeviceApplicationSceneClassicWrapperView allowsContentAlignmentAdjustment];
-[SBDeviceApplicationSceneClassicWrapperView classicContentCoordinateSpace];
-[SBDeviceApplicationSceneClassicWrapperView preparingForUserDrivenClassicRotation];
-[SBDeviceApplicationSceneClassicWrapperView resetContentAlignmentAnimated:];
-[SBDeviceApplicationSceneClassicWrapperView setPreparingForUserDrivenClassicRotation:];
-[SBDeviceApplicationSceneClassicWrapperView setStartingOrientationForClassicPhoneAppRotation:];
-[SBDeviceApplicationSceneClassicWrapperView setSuppressLayoutUpdatesForStartOfClassicPhoneAppRotation:];
-[SBDeviceApplicationSceneClassicWrapperView startingOrientationForClassicPhoneAppRotation];
-[SBDeviceApplicationSceneClassicWrapperView stepContentAlignmentAlongAxis:towardsTrailing:];
-[SBDeviceApplicationSceneClassicWrapperView suppressLayoutUpdatesForStartOfClassicPhoneAppRotation];
-[SBDeviceApplicationSceneClassicWrapperView wantsBlackBackground];
```
