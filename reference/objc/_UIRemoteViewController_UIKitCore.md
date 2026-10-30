# `_UIRemoteViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `_UIRemoteSheet_Internal`, `BSDescriptionStreaming`, `_UIEventDeferringRuleOwning`, `_UIRemoteSheet`
- 4 instance variables, 17 properties, 84 instance methods, 9 class methods

## Instance variables

```
@"<_UIRemoteViewControllerImpl>" _impl;
{?="usesSceneHostingImplementation"b1} _flags;
B __appProtectionLocked;
@"NSString" _serviceBundleIdentifier;
```

## Properties

```
@property (T@"NSSet",R,N) _keyboardSceneLayers;
@property (TB,R,N,G_isAppProtectionLocked,V__appProtectionLocked) _appProtectionLocked;
@property (T@"_UIRemoteViewControllerAppProtectionMetrics",R) _appProtectionMetrics;
@property (T@"NSString",R,N) _extensionBundleIdentifierForAppProtection;
@property (T@"NSString",R,N,V_serviceBundleIdentifier) serviceBundleIdentifier;
@property (Ti,R,N) serviceProcessIdentifier;
@property (T{?=[8I]},R,N) serviceAuditToken;
@property (TB,N,S_setShouldUpdateRemoteTextEffectsWindow:) _shouldUpdateRemoteTextEffectsWindow;
@property (TB,N) serviceViewShouldShareTouchesWithHost;
@property (TB,N,S_setViewClipsToBounds:) _viewClipsToBounds;
@property (T@"<_UIRemoteSheet_Internal>",?,R,N) _containedRemoteSheet;
@property (TB,?,R,N) _remoteSheetAllowsConnection;
@property (T@"_UISheetPresentationControllerConfiguration",&,N,S_setSheetConfiguration:) _sheetConfiguration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIRemoteViewController exportedInterface];
+[_UIRemoteViewController __shouldHostRemoteTextEffectsWindow];
+[_UIRemoteViewController _shouldForwardViewWillTransitionToSize];
+[_UIRemoteViewController _shouldSendLegacyMethodsFromViewWillTransitionToSize];
+[_UIRemoteViewController requestViewController:fromServiceWithBundleIdentifier:connectionHandler:];
+[_UIRemoteViewController requestViewControllerWithService:connectionHandler:];
+[_UIRemoteViewController requestViewControllerWithService:traitCollection:connectionHandler:];
+[_UIRemoteViewController serviceViewControllerInterface];
+[_UIRemoteViewController shouldPropagateAppearanceCustomizations];
```

## Instance methods

```
-[_UIRemoteViewController _setViewClipsToBounds:];
-[_UIRemoteViewController preferredStatusBarUpdateAnimation];
-[_UIRemoteViewController _setSheetConfiguration:];
-[_UIRemoteViewController _extensionBundleIdentifierForAppProtection];
-[_UIRemoteViewController interfaceElementCategory];
-[_UIRemoteViewController willTransitionToTraitCollection:withTransitionCoordinator:];
-[_UIRemoteViewController _sheetConfiguration];
-[_UIRemoteViewController preferredUserInterfaceStyle];
-[_UIRemoteViewController preferredContentSizeDidChangeForChildContentContainer:];
-[_UIRemoteViewController debugDescription];
-[_UIRemoteViewController serviceBundleIdentifier];
-[_UIRemoteViewController viewIsAppearing:];
-[_UIRemoteViewController viewWillDisappear:];
-[_UIRemoteViewController _multitaskingDragExclusionRects];
-[_UIRemoteViewController supportedInterfaceOrientations];
-[_UIRemoteViewController _allowsShielding];
-[_UIRemoteViewController viewServiceDidTerminateWithError:];
-[_UIRemoteViewController _didResignContentViewControllerOfPopover:];
-[_UIRemoteViewController _parentSceneDidUpdateWithDiff:];
-[_UIRemoteViewController prefersHomeIndicatorAutoHidden];
-[_UIRemoteViewController _viewClipsToBounds];
-[_UIRemoteViewController _intelligenceCollectRemoteContentInVisibleRect:withRemoteContextWrapper:];
-[_UIRemoteViewController _preferredStatusBarVisibility];
-[_UIRemoteViewController _containedRemoteSheet];
-[_UIRemoteViewController preferredWhitePointAdaptivityStyle];
-[_UIRemoteViewController _willBecomeContentViewControllerOfPopover:];
-[_UIRemoteViewController _willRotateToInterfaceOrientation:duration:forwardToChildControllers:skipSelf:];
-[_UIRemoteViewController preferredScreenEdgesDeferringSystemGestures];
-[_UIRemoteViewController __willChangeToIdiom:onScreen:];
-[_UIRemoteViewController _preferredStatusBarAxis];
-[_UIRemoteViewController setServiceViewShouldShareTouchesWithHost:];
-[_UIRemoteViewController succinctDescription];
-[_UIRemoteViewController _updateTintColor];
-[_UIRemoteViewController viewWillAppear:];
-[_UIRemoteViewController disconnect];
-[_UIRemoteViewController serviceViewShouldShareTouchesWithHost];
-[_UIRemoteViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[_UIRemoteViewController synchronizeAnimationsInActions:];
-[_UIRemoteViewController viewDidAppear:];
-[_UIRemoteViewController prefersPointerLocked];
-[_UIRemoteViewController setInheritsSecurity:];
-[_UIRemoteViewController serviceProcessIdentifier];
-[_UIRemoteViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[_UIRemoteViewController loadView];
-[_UIRemoteViewController inheritsSecurity];
-[_UIRemoteViewController _shouldRemoteViewControllerFenceOriginChanges];
-[_UIRemoteViewController description];
-[_UIRemoteViewController viewDidDisappear:];
-[_UIRemoteViewController appendDescriptionToStream:];
-[_UIRemoteViewController __setMediaOverridePID:];
-[_UIRemoteViewController _cancelTouchesForCurrentEventInHostedContent];
-[_UIRemoteViewController _didReceiveProductivityGestureAction:];
-[_UIRemoteViewController preferredStatusBarStyle];
-[_UIRemoteViewController _movedToParentSceneWithSettings:];
-[_UIRemoteViewController _setSecurityModeForViewsLayer];
-[_UIRemoteViewController _traitCollectionDidChange:];
-[_UIRemoteViewController _keyboardSceneLayers];
-[_UIRemoteViewController _willAnimateRotationToInterfaceOrientation:duration:forwardToChildControllers:skipSelf:];
-[_UIRemoteViewController didMoveToParentViewController:];
-[_UIRemoteViewController canBecomeFirstResponder];
-[_UIRemoteViewController hostedSceneIdentityToken];
-[_UIRemoteViewController _setContentOverlayInsets:andLeftMargin:rightMargin:];
-[_UIRemoteViewController serviceAuditToken];
-[_UIRemoteViewController _didRotateFromInterfaceOrientation:forwardToChildControllers:skipSelf:];
-[_UIRemoteViewController _ignoreAppSupportedOrientations];
-[_UIRemoteViewController _serviceAccessibilityServerPort];
-[_UIRemoteViewController __isKindOfUIRemoteViewController];
-[_UIRemoteViewController __shouldRemoteViewControllerFenceGeometryChange:forAncestor:];
-[_UIRemoteViewController __shouldRemoteViewControllerFenceOperations];
-[_UIRemoteViewController _allowsKeyboardFocus];
-[_UIRemoteViewController _appProtectionMetrics];
-[_UIRemoteViewController _initWithServiceBundleIdentifier:service:];
-[_UIRemoteViewController _initializeAccessibilityPortInformation];
-[_UIRemoteViewController _isAppProtectionLocked];
-[_UIRemoteViewController _isHostingRemoteContent];
-[_UIRemoteViewController _preferredStatusBarAxisDidChange];
-[_UIRemoteViewController _remoteKeyboardRemoteView];
-[_UIRemoteViewController _setShouldUpdateRemoteTextEffectsWindow:];
-[_UIRemoteViewController _shouldUpdateRemoteTextEffectsWindow];
-[_UIRemoteViewController _sizeTrackingView];
-[_UIRemoteViewController intrinsicContentSizeForServiceSize:];
-[_UIRemoteViewController serviceViewControllerProxy];
-[_UIRemoteViewController serviceViewControllerProxyWithErrorHandler:];
-[_UIRemoteViewController viewDidInvalidateIntrinsicContentSize];
```
