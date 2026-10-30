# `SBApplicationActivationHelper`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 6 instance methods, 5 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
```

## Properties

```
@property (T@"SBApplicationController",R,N,V_applicationController) applicationController;
```

## Class methods

```
+[SBApplicationActivationHelper initialize];
+[SBApplicationActivationHelper applicationIconRepresentingBundleIdentifier:inIconModel:applicationController:];
+[SBApplicationActivationHelper applicationRepresentingApplication:applicationController:];
+[SBApplicationActivationHelper applicationSupportsMultitaskingShelf:applicationController:];
+[SBApplicationActivationHelper applicationToActivateForApplication:applicationController:];
```

## Instance methods

```
-[SBApplicationActivationHelper applicationController];
-[SBApplicationActivationHelper initWithApplicationController:];
-[SBApplicationActivationHelper _activateWorkspaceEntity:fromIcon:location:validator:];
-[SBApplicationActivationHelper activateApplication:fromIcon:location:activationSettings:actions:];
-[SBApplicationActivationHelper transitionSourceForIcon:iconLocation:];
-[SBApplicationActivationHelper workflowClientFromWebClip:appToLaunch:];
```
