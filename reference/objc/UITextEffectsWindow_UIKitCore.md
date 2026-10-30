# `UITextEffectsWindow`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIAutoRotatingWindow`
- Protocols: `_UISceneBasedObject`, `_UIVisualStyleStylable`
- 22 instance variables, 23 properties, 109 instance methods, 15 class methods

## Instance variables

```
B _inDealloc;
Q _activeEffectsCount;
B _isFullscreen;
B _isForViewService;
d _defaultWindowLevel;
{CGPoint="x"d"y"d} _hostedViewOrigin;
@"NSDictionary" _perSceneOptions;
@"UIWindowScene" __intendedWindowScene;
Q _activeRemoteViewCount;
Q _windowLevelCount;
[5d] _windowLevelStack;
{CGSize="width"d"height"d} _hostedViewSize;
B _manualHostingOverride;
@"UIEditingOverlayViewController" _editingOverlayViewController;
@"NSLayoutConstraint" _bottomConstraint;
B _sceneIsResizing;
@"_UITextEffectsWindowPlacer" _placer;
@"_UITextEffectsWindowHostManager" _hostManager;
{CGPoint="x"d"y"d} _hostedWindowOffset;
{CGSize="width"d"height"d} _hostedSceneSize;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _hostedSafeInsets;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _hostedViewReference;
```

## Properties

```
@property (T@"UIWindowScene",R) _intendedScene;
@property (T@"NSDictionary",R) _options;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,V_sceneIsResizing) sceneIsResizing;
@property (T@"_UITextEffectsWindowPlacer",R,N,V_placer) placer;
@property (T@"_UITextEffectsWindowHostManager",R,N,V_hostManager) hostManager;
@property (T@"UIEditingOverlayViewController",R,N,V_editingOverlayViewController) editingOverlayViewController;
@property (TI,R) contextID;
@property (TB,R,N,V_isFullscreen) isFullscreen;
@property (TB,R,N,V_isForViewService) isForViewService;
@property (Td,N,V_defaultWindowLevel) defaultWindowLevel;
@property (T{CGSize=dd},R,N) keyboardScreenReferenceSize;
@property (Td,R,N) keyboardWidthForCurrentDevice;
@property (T{CGPoint=dd},N,V_hostedViewOrigin) hostedViewOrigin;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_hostedViewReference) hostedViewReference;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) hostedFrame;
@property (T{CGSize=dd},N,V_hostedViewSize) hostedViewSize;
@property (T{UIEdgeInsets=dddd},N,V_hostedSafeInsets) hostedSafeInsets;
@property (T{CGPoint=dd},N,V_hostedWindowOffset) hostedWindowOffset;
@property (T{CGSize=dd},N,V_hostedSceneSize) hostedSceneSize;
```

## Class methods

```
+[UITextEffectsWindow visualStyleRegistryIdentity];
+[UITextEffectsWindow _isSecure];
+[UITextEffectsWindow _sharedTextEffectsWindowforWindowScene:allowHosted:forViewService:matchesStatusBarOrientationOnAccess:shouldCreateIfNecessary:];
+[UITextEffectsWindow _shouldSoftAssertOnSetScreen];
+[UITextEffectsWindow activeTextEffectsWindowForWindowScene:];
+[UITextEffectsWindow activeTextEffectsWindowForWindowScene:forViewService:];
+[UITextEffectsWindow lowerTextEffectsWindowsForHideNotificationCenter];
+[UITextEffectsWindow raiseTextEffectsWindowsForShowNotificationCenter];
+[UITextEffectsWindow releaseSharedInstances];
+[UITextEffectsWindow setTextEffectsWindowPlacerClass:];
+[UITextEffectsWindow sharedTextEffectsWindow];
+[UITextEffectsWindow sharedTextEffectsWindowAboveStatusBar];
+[UITextEffectsWindow sharedTextEffectsWindowForScreen:];
+[UITextEffectsWindow sharedTextEffectsWindowForWindowScene:];
+[UITextEffectsWindow sharedTextEffectsWindowForWindowScene:forViewService:];
```

## Instance methods

```
-[UITextEffectsWindow _options];
-[UITextEffectsWindow didAddSubview:];
-[UITextEffectsWindow rootViewController];
-[UITextEffectsWindow addSubview:];
-[UITextEffectsWindow _extendsScreenSceneLifetime];
-[UITextEffectsWindow handleStatusBarChangeFromHeight:toHeight:];
-[UITextEffectsWindow isFullscreen];
-[UITextEffectsWindow dealloc];
-[UITextEffectsWindow convertRect:toCoordinateSpace:];
-[UITextEffectsWindow keyboardScreenReferenceSize];
-[UITextEffectsWindow layoutSubviews];
-[UITextEffectsWindow _shouldAutorotateToInterfaceOrientation:];
-[UITextEffectsWindow convertRect:fromCoordinateSpace:];
-[UITextEffectsWindow _matchingOptions:];
-[UITextEffectsWindow _intendedScene];
-[UITextEffectsWindow _inputWindowController];
-[UITextEffectsWindow setFrame:];
-[UITextEffectsWindow _configureContextOptions:];
-[UITextEffectsWindow updateEditingOverlayContainer];
-[UITextEffectsWindow _initWithScene:options:];
-[UITextEffectsWindow _didRemoveSubview:];
-[UITextEffectsWindow _canActAsKeyWindowForScreen:];
-[UITextEffectsWindow actualSceneBounds];
-[UITextEffectsWindow contextID];
-[UITextEffectsWindow initWithFrame:];
-[UITextEffectsWindow isInternalWindow];
-[UITextEffectsWindow sendSubviewToBack:];
-[UITextEffectsWindow bringSubviewToFront:];
-[UITextEffectsWindow resetTransform];
-[UITextEffectsWindow _isFullscreen];
-[UITextEffectsWindow actualSceneFrameForOrientation:];
-[UITextEffectsWindow delayHideWindow];
-[UITextEffectsWindow becomeKeyWindow];
-[UITextEffectsWindow hostedSceneSize];
-[UITextEffectsWindow sceneIsResizing];
-[UITextEffectsWindow _automaticContainerBackgroundIsGlass];
-[UITextEffectsWindow _canAffectStatusBarAppearance];
-[UITextEffectsWindow _commonInitWithOptions:];
-[UITextEffectsWindow _commonTextEffectsInit];
-[UITextEffectsWindow _createSystemGestureGateGestureRecognizerIfNeeded];
-[UITextEffectsWindow _didSnapshot];
-[UITextEffectsWindow _forHostedProcessConvertPoint:forWindow:wasFromWindow:];
-[UITextEffectsWindow _forHostedProcessConvertRect:forWindow:wasFromWindow:];
-[UITextEffectsWindow _initBasicWithScene:options:];
-[UITextEffectsWindow _initWithFrame:attached:];
-[UITextEffectsWindow _initWithFrame:debugName:windowScene:];
-[UITextEffectsWindow _internalInterfaceOrientation];
-[UITextEffectsWindow _isExternallyPlaced];
-[UITextEffectsWindow _isRemoteKeyboardWindow];
-[UITextEffectsWindow _isTextEffectsWindow];
-[UITextEffectsWindow _matchDeviceOrientation];
-[UITextEffectsWindow _restoreWindowLevel];
-[UITextEffectsWindow _sceneBounds];
-[UITextEffectsWindow _sceneBoundsDidChange];
-[UITextEffectsWindow _sceneReferenceBounds];
-[UITextEffectsWindow _setWindowLevel:];
-[UITextEffectsWindow _shouldInstallRootPresentationController];
-[UITextEffectsWindow _shouldResizeWithScene];
-[UITextEffectsWindow _shouldTextEffectsWindowBeHostedForView:];
-[UITextEffectsWindow _sortSubviewsOfView:];
-[UITextEffectsWindow _updateRootViewConstraintsForInterfaceOrientationAndStatusBarHeight];
-[UITextEffectsWindow _updateTransformLayer];
-[UITextEffectsWindow _usableSceneBounds];
-[UITextEffectsWindow _willSnapshot];
-[UITextEffectsWindow _windowOwnsInterfaceOrientationTransform];
-[UITextEffectsWindow aboveStatusBarWindow];
-[UITextEffectsWindow actualSceneBoundsForLandscape:];
-[UITextEffectsWindow actualSceneFrame];
-[UITextEffectsWindow actualSceneOrientation];
-[UITextEffectsWindow addBottomPadding:];
-[UITextEffectsWindow convertPoint:fromView:];
-[UITextEffectsWindow convertPoint:fromWindow:];
-[UITextEffectsWindow convertPoint:toView:];
-[UITextEffectsWindow convertPoint:toWindow:];
-[UITextEffectsWindow convertRect:fromView:];
-[UITextEffectsWindow convertRect:fromWindow:];
-[UITextEffectsWindow convertRect:toView:];
-[UITextEffectsWindow convertRect:toWindow:];
-[UITextEffectsWindow defaultWindowLevel];
-[UITextEffectsWindow editingOverlayContainerView];
-[UITextEffectsWindow editingOverlayViewController];
-[UITextEffectsWindow enableRemoteHosting];
-[UITextEffectsWindow hostManager];
-[UITextEffectsWindow hostedFrame];
-[UITextEffectsWindow hostedSafeInsets];
-[UITextEffectsWindow hostedViewOrigin];
-[UITextEffectsWindow hostedViewReference];
-[UITextEffectsWindow hostedViewSize];
-[UITextEffectsWindow hostedWindowOffset];
-[UITextEffectsWindow isForViewService];
-[UITextEffectsWindow isTrackingKeyboard];
-[UITextEffectsWindow keyboardWidthForCurrentDevice];
-[UITextEffectsWindow layoutViewsForTrackedGuides];
-[UITextEffectsWindow placeOwningWindowRelativeToResponder:];
-[UITextEffectsWindow placer];
-[UITextEffectsWindow setDefaultWindowLevel:];
-[UITextEffectsWindow setEnableRemoteHosting:];
-[UITextEffectsWindow setHostedSafeInsets:];
-[UITextEffectsWindow setHostedSceneSize:];
-[UITextEffectsWindow setHostedViewOrigin:];
-[UITextEffectsWindow setHostedViewReference:];
-[UITextEffectsWindow setHostedViewSize:];
-[UITextEffectsWindow setHostedWindowOffset:];
-[UITextEffectsWindow slideOverWindowVerticalOffset];
-[UITextEffectsWindow sortSubviews];
-[UITextEffectsWindow updateForOrientation:];
-[UITextEffectsWindow updateForOrientation:forceResetTransform:];
-[UITextEffectsWindow updateLastRemoteView:forView:inContainer:];
-[UITextEffectsWindow updateSubviewOrdering];
```
