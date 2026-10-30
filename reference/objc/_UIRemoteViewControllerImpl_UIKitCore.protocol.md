# `_UIRemoteViewControllerImpl` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `BSDescriptionStreaming`, `_UIRemoteSheet_Internal`
- 0 instance variables, 9 properties, 52 instance methods, 1 class methods

## Properties

```
@property (T@"_UIRemoteViewController",R,W,N) _owningRemoteViewController;
@property (T@"_UIRemoteViewService",R,N) _remoteViewService;
@property (T@,R,N) _serviceViewControllerProxy;
@property (Ti,R,N) serviceProcessIdentifier;
@property (T{?=[8I]},R,N) serviceAuditToken;
@property (TB,N) serviceViewShouldShareTouchesWithHost;
@property (TB,N) inheritsSecurity;
@property (T@"FBSSceneIdentityToken",R,N) hostedSceneIdentityToken;
@property (T@"NSSet",R,N) _keyboardSceneLayers;
```

## Class methods

```
+[_UIRemoteViewControllerImpl _requestViewController:traitCollection:fromServiceWithBundleIdentifier:service:connectionHandler:newRemoteViewController:remoteViewControllerImpl:];
```

## Instance methods

```
-[_UIRemoteViewControllerImpl preferredStatusBarUpdateAnimation];
-[_UIRemoteViewControllerImpl willTransitionToTraitCollection:withTransitionCoordinator:];
-[_UIRemoteViewControllerImpl preferredUserInterfaceStyle];
-[_UIRemoteViewControllerImpl preferredContentSizeDidChangeForChildContentContainer:];
-[_UIRemoteViewControllerImpl viewIsAppearing:];
-[_UIRemoteViewControllerImpl viewWillDisappear:];
-[_UIRemoteViewControllerImpl _multitaskingDragExclusionRects];
-[_UIRemoteViewControllerImpl supportedInterfaceOrientations];
-[_UIRemoteViewControllerImpl _didResignContentViewControllerOfPopover:];
-[_UIRemoteViewControllerImpl _parentSceneDidUpdateWithDiff:];
-[_UIRemoteViewControllerImpl _remoteViewService];
-[_UIRemoteViewControllerImpl _serviceViewControllerProxy];
-[_UIRemoteViewControllerImpl prefersHomeIndicatorAutoHidden];
-[_UIRemoteViewControllerImpl _intelligenceCollectRemoteContentInVisibleRect:withRemoteContextWrapper:];
-[_UIRemoteViewControllerImpl _preferredStatusBarVisibility];
-[_UIRemoteViewControllerImpl preferredWhitePointAdaptivityStyle];
-[_UIRemoteViewControllerImpl _willBecomeContentViewControllerOfPopover:];
-[_UIRemoteViewControllerImpl _willRotateToInterfaceOrientation:duration:forwardToChildControllers:skipSelf:];
-[_UIRemoteViewControllerImpl preferredScreenEdgesDeferringSystemGestures];
-[_UIRemoteViewControllerImpl __willChangeToIdiom:onScreen:];
-[_UIRemoteViewControllerImpl _preferredStatusBarAxis];
-[_UIRemoteViewControllerImpl setServiceViewShouldShareTouchesWithHost:];
-[_UIRemoteViewControllerImpl _updateTintColor];
-[_UIRemoteViewControllerImpl viewWillAppear:];
-[_UIRemoteViewControllerImpl disconnect];
-[_UIRemoteViewControllerImpl serviceViewShouldShareTouchesWithHost];
-[_UIRemoteViewControllerImpl viewDidMoveToWindow:shouldAppearOrDisappear:];
-[_UIRemoteViewControllerImpl synchronizeAnimationsInActions:];
-[_UIRemoteViewControllerImpl viewDidAppear:];
-[_UIRemoteViewControllerImpl prefersPointerLocked];
-[_UIRemoteViewControllerImpl setInheritsSecurity:];
-[_UIRemoteViewControllerImpl serviceProcessIdentifier];
-[_UIRemoteViewControllerImpl viewWillTransitionToSize:withTransitionCoordinator:];
-[_UIRemoteViewControllerImpl loadView];
-[_UIRemoteViewControllerImpl inheritsSecurity];
-[_UIRemoteViewControllerImpl viewDidDisappear:];
-[_UIRemoteViewControllerImpl __setMediaOverridePID:];
-[_UIRemoteViewControllerImpl _cancelTouchesForCurrentEventInHostedContent];
-[_UIRemoteViewControllerImpl _didReceiveProductivityGestureAction:];
-[_UIRemoteViewControllerImpl preferredStatusBarStyle];
-[_UIRemoteViewControllerImpl _initWithViewServiceBundleIdentifier:owningRemoteViewController:];
-[_UIRemoteViewControllerImpl _movedToParentSceneWithSettings:];
-[_UIRemoteViewControllerImpl _owningRemoteViewController];
-[_UIRemoteViewControllerImpl _setSecurityModeForViewsLayer];
-[_UIRemoteViewControllerImpl _traitCollectionDidChange:];
-[_UIRemoteViewControllerImpl _keyboardSceneLayers];
-[_UIRemoteViewControllerImpl _willAnimateRotationToInterfaceOrientation:duration:forwardToChildControllers:skipSelf:];
-[_UIRemoteViewControllerImpl didMoveToParentViewController:];
-[_UIRemoteViewControllerImpl hostedSceneIdentityToken];
-[_UIRemoteViewControllerImpl _setContentOverlayInsets:andLeftMargin:rightMargin:];
-[_UIRemoteViewControllerImpl serviceAuditToken];
-[_UIRemoteViewControllerImpl _didRotateFromInterfaceOrientation:forwardToChildControllers:skipSelf:];
```
