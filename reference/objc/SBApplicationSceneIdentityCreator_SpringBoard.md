# `SBApplicationSceneIdentityCreator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBApplicationSceneIdentityCreating`
- 1 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
```

## Properties

```
@property (T@"SBApplicationController",R,N,V_applicationController) applicationController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBApplicationSceneIdentityCreator newSceneIdentityForApplication:];
-[SBApplicationSceneIdentityCreator applicationController];
-[SBApplicationSceneIdentityCreator initWithApplicationController:];
-[SBApplicationSceneIdentityCreator newSceneIdentityForApplication:supportsMultiwindow:];
-[SBApplicationSceneIdentityCreator newSceneIdentityForBundleIdentifier:uniqueIdentifier:];
-[SBApplicationSceneIdentityCreator newSceneIdentityForBundleIdentifier:];
-[SBApplicationSceneIdentityCreator newSceneIdentityForBundleIdentifier:supportsMultiwindow:];
-[SBApplicationSceneIdentityCreator _sceneIdentifierForBundleIdentifier:uniqueIdentifier:];
```
