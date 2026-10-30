# `SBDeviceApplicationSceneStatusBarBreadcrumbProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDeviceApplicationSceneHandleObserver`
- 5 instance variables, 7 properties, 24 instance methods, 5 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"SiriBreadcrumbSource" _siriSource;
@"SBBreadcrumbActionContext" _currentBreadcrumbActionContext;
@"SBDeviceApplicationSceneHandle" _sceneHandle;
@"NSHashTable" _observers;
```

## Properties

```
@property (TB,R,N) hasBreadcrumb;
@property (TB,R,N) hasAssistantBreadcrumb;
@property (T@"NSString",R,C,N) breadcrumbTitle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBDeviceApplicationSceneStatusBarBreadcrumbProvider _breadcrumbBundleIdForActivatingSceneEntity:withTransitionContext:];
+[SBDeviceApplicationSceneStatusBarBreadcrumbProvider _breadcrumbSceneIdForAppWithBundleID:activatingSceneEntity:withTransitionContext:];
+[SBDeviceApplicationSceneStatusBarBreadcrumbProvider _breadcrumbTitleForAppWithBundleID:sceneHandle:activatingSceneEntity:withTransitionContext:applicationController:];
+[SBDeviceApplicationSceneStatusBarBreadcrumbProvider _destinationContextsForActivatingSceneEntity:withTransitionContext:applicationController:];
+[SBDeviceApplicationSceneStatusBarBreadcrumbProvider _shouldAddBreadcrumbToActivatingSceneEntity:sceneHandle:withTransitionContext:applicationController:];
```

## Instance methods

```
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider sceneHandle:didChangeEffectiveForegroundness:];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider initWithSceneHandle:applicationController:];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider _installedApplicationsDidChange:];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider succinctDescriptionBuilder];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider removeObserver:];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider _openStrategyForAppLinkState:];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider captureContextForActivatingSceneEntity:withTransitionContext:];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider descriptionWithMultilinePrefix:];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider _setCurrentBreadcrumbActionContext:];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider _showTransientOverlayInPlaceForWindowScene:];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider hasBreadcrumb];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider succinctDescription];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider addObserver:];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider prepareForReuse];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider _presentAssistantFromBreadcrumb];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider hasAssistantBreadcrumb];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider _handleBreadcrumbAction];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider noteDidUpdateDisplayProperties];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider _activateBreadcrumbApplication:withSceneIdentifier:sceneIdentityProvider:displayConfiguration:];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider activateBreadcrumbIfPossible];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider _presentSpotlightFromBreadcrumbInWindowScene:];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider _breadcrumbNavigationActionContextForActivatingSceneEntity:withTransitionContext:];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider breadcrumbTitle];
-[SBDeviceApplicationSceneStatusBarBreadcrumbProvider descriptionBuilderWithMultilinePrefix:];
```
