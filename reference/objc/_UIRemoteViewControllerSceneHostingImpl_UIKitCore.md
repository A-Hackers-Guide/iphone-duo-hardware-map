# `_UIRemoteViewControllerSceneHostingImpl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneHostingControllerDelegate`, `_UIViewServiceHostSessionDelegate`, `_UIViewServiceHostSceneComponentDelegate`, `_UIRemoteViewControllerImpl`
- 10 instance variables, 17 properties, 69 instance methods, 1 class methods

## Instance variables

```
@"_UISceneHostingController" _sceneHostingController;
@"_UIViewServiceHostSceneComponent" _hostComponent;
@"_UIViewServiceHostSession" _session;
@"NSString" _requestedViewControllerClassName;
@? _connectionHandler;
@"_UIRemoteViewController" _strongSelf;
@"NSXPCConnection" _auxiliaryConnection;
{?="hasConfiguredAppProtection"b1} _flags;
@"_UIRemoteViewController" _owningRemoteViewController;
@"_UIRemoteViewService" _service;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_UIRemoteViewController",R,W,N,V_owningRemoteViewController) _owningRemoteViewController;
@property (T@"_UIRemoteViewService",R,N,V_service) _remoteViewService;
@property (T@,R,N) _serviceViewControllerProxy;
@property (Ti,R,N) serviceProcessIdentifier;
@property (T{?=[8I]},R,N) serviceAuditToken;
@property (TB,N) serviceViewShouldShareTouchesWithHost;
@property (TB,N) inheritsSecurity;
@property (T@"FBSSceneIdentityToken",R,N) hostedSceneIdentityToken;
@property (T@"NSSet",R,N) _keyboardSceneLayers;
@property (T@"<_UIRemoteSheet_Internal>",?,R,N) _containedRemoteSheet;
@property (TB,?,R,N) _remoteSheetAllowsConnection;
@property (T@"_UISheetPresentationControllerConfiguration",&,N,S_setSheetConfiguration:) _sheetConfiguration;
@property (TB,N,S_setViewClipsToBounds:) _viewClipsToBounds;
```

## Class methods

```
+[_UIRemoteViewControllerSceneHostingImpl _requestViewController:traitCollection:fromServiceWithBundleIdentifier:service:connectionHandler:newRemoteViewController:remoteViewControllerImpl:];
```

## Instance methods

```
-[_UIRemoteViewControllerSceneHostingImpl _setViewClipsToBounds:];
-[_UIRemoteViewControllerSceneHostingImpl preferredStatusBarUpdateAnimation];
-[_UIRemoteViewControllerSceneHostingImpl _setSheetConfiguration:];
-[_UIRemoteViewControllerSceneHostingImpl willTransitionToTraitCollection:withTransitionCoordinator:];
-[_UIRemoteViewControllerSceneHostingImpl _sheetConfiguration];
-[_UIRemoteViewControllerSceneHostingImpl preferredUserInterfaceStyle];
-[_UIRemoteViewControllerSceneHostingImpl preferredContentSizeDidChangeForChildContentContainer:];
-[_UIRemoteViewControllerSceneHostingImpl _remoteSheetAllowsConnection];
-[_UIRemoteViewControllerSceneHostingImpl debugDescription];
-[_UIRemoteViewControllerSceneHostingImpl viewIsAppearing:];
-[_UIRemoteViewControllerSceneHostingImpl viewWillDisappear:];
-[_UIRemoteViewControllerSceneHostingImpl _multitaskingDragExclusionRects];
-[_UIRemoteViewControllerSceneHostingImpl supportedInterfaceOrientations];
-[_UIRemoteViewControllerSceneHostingImpl dealloc];
-[_UIRemoteViewControllerSceneHostingImpl _didResignContentViewControllerOfPopover:];
-[_UIRemoteViewControllerSceneHostingImpl _parentSceneDidUpdateWithDiff:];
-[_UIRemoteViewControllerSceneHostingImpl _remoteViewService];
-[_UIRemoteViewControllerSceneHostingImpl _serviceViewControllerProxy];
-[_UIRemoteViewControllerSceneHostingImpl prefersHomeIndicatorAutoHidden];
-[_UIRemoteViewControllerSceneHostingImpl _viewClipsToBounds];
-[_UIRemoteViewControllerSceneHostingImpl _intelligenceCollectRemoteContentInVisibleRect:withRemoteContextWrapper:];
-[_UIRemoteViewControllerSceneHostingImpl _viewServiceHostSessionDidConnectToClient:];
-[_UIRemoteViewControllerSceneHostingImpl _preferredStatusBarVisibility];
-[_UIRemoteViewControllerSceneHostingImpl _containedRemoteSheet];
-[_UIRemoteViewControllerSceneHostingImpl preferredWhitePointAdaptivityStyle];
-[_UIRemoteViewControllerSceneHostingImpl _willBecomeContentViewControllerOfPopover:];
-[_UIRemoteViewControllerSceneHostingImpl _willRotateToInterfaceOrientation:duration:forwardToChildControllers:skipSelf:];
-[_UIRemoteViewControllerSceneHostingImpl preferredScreenEdgesDeferringSystemGestures];
-[_UIRemoteViewControllerSceneHostingImpl __willChangeToIdiom:onScreen:];
-[_UIRemoteViewControllerSceneHostingImpl _preferredStatusBarAxis];
-[_UIRemoteViewControllerSceneHostingImpl sceneDidInvalidateWithError:];
-[_UIRemoteViewControllerSceneHostingImpl setServiceViewShouldShareTouchesWithHost:];
-[_UIRemoteViewControllerSceneHostingImpl succinctDescription];
-[_UIRemoteViewControllerSceneHostingImpl _updateTintColor];
-[_UIRemoteViewControllerSceneHostingImpl viewWillAppear:];
-[_UIRemoteViewControllerSceneHostingImpl disconnect];
-[_UIRemoteViewControllerSceneHostingImpl serviceViewShouldShareTouchesWithHost];
-[_UIRemoteViewControllerSceneHostingImpl supportedInterfaceOrientationsDidUpdate];
-[_UIRemoteViewControllerSceneHostingImpl viewDidMoveToWindow:shouldAppearOrDisappear:];
-[_UIRemoteViewControllerSceneHostingImpl synchronizeAnimationsInActions:];
-[_UIRemoteViewControllerSceneHostingImpl viewDidAppear:];
-[_UIRemoteViewControllerSceneHostingImpl prefersPointerLocked];
-[_UIRemoteViewControllerSceneHostingImpl setInheritsSecurity:];
-[_UIRemoteViewControllerSceneHostingImpl serviceProcessIdentifier];
-[_UIRemoteViewControllerSceneHostingImpl viewWillTransitionToSize:withTransitionCoordinator:];
-[_UIRemoteViewControllerSceneHostingImpl loadView];
-[_UIRemoteViewControllerSceneHostingImpl inheritsSecurity];
-[_UIRemoteViewControllerSceneHostingImpl description];
-[_UIRemoteViewControllerSceneHostingImpl viewDidDisappear:];
-[_UIRemoteViewControllerSceneHostingImpl appendDescriptionToStream:];
-[_UIRemoteViewControllerSceneHostingImpl __setMediaOverridePID:];
-[_UIRemoteViewControllerSceneHostingImpl _cancelTouchesForCurrentEventInHostedContent];
-[_UIRemoteViewControllerSceneHostingImpl _didReceiveProductivityGestureAction:];
-[_UIRemoteViewControllerSceneHostingImpl preferredStatusBarStyle];
-[_UIRemoteViewControllerSceneHostingImpl _initWithViewServiceBundleIdentifier:owningRemoteViewController:];
-[_UIRemoteViewControllerSceneHostingImpl _movedToParentSceneWithSettings:];
-[_UIRemoteViewControllerSceneHostingImpl _owningRemoteViewController];
-[_UIRemoteViewControllerSceneHostingImpl _setSecurityModeForViewsLayer];
-[_UIRemoteViewControllerSceneHostingImpl _traitCollectionDidChange:];
-[_UIRemoteViewControllerSceneHostingImpl _keyboardSceneLayers];
-[_UIRemoteViewControllerSceneHostingImpl _viewServiceHostSessionDidInvalidate:withError:];
-[_UIRemoteViewControllerSceneHostingImpl _willAnimateRotationToInterfaceOrientation:duration:forwardToChildControllers:skipSelf:];
-[_UIRemoteViewControllerSceneHostingImpl didMoveToParentViewController:];
-[_UIRemoteViewControllerSceneHostingImpl hostedSceneIdentityToken];
-[_UIRemoteViewControllerSceneHostingImpl _setContentOverlayInsets:andLeftMargin:rightMargin:];
-[_UIRemoteViewControllerSceneHostingImpl serviceAuditToken];
-[_UIRemoteViewControllerSceneHostingImpl _didRotateFromInterfaceOrientation:forwardToChildControllers:skipSelf:];
-[_UIRemoteViewControllerSceneHostingImpl statusBarAxisDidUpdate];
-[_UIRemoteViewControllerSceneHostingImpl viewServiceClientIsReady];
```
