# `SBLaunchImageOverridesContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSString" _sceneID;
@"SBActivationSettings" _settings;
B _ignoreSnapshots;
@"NSString" _launchImageName;
@"NSURL" _url;
```

## Properties

```
@property (T@"NSString",R,C,N,V_sceneID) sceneID;
@property (T@"SBActivationSettings",R,N,V_settings) activationSettings;
@property (TB,R,N,V_ignoreSnapshots) ignoreSnapshots;
@property (T@"NSString",R,C,N,V_launchImageName) launchImageName;
@property (T@"NSURL",R,C,N,V_url) url;
```

## Instance methods

```
-[SBLaunchImageOverridesContext sceneID];
-[SBLaunchImageOverridesContext launchImageName];
-[SBLaunchImageOverridesContext url];
-[SBLaunchImageOverridesContext ignoreSnapshots];
-[SBLaunchImageOverridesContext activationSettings];
-[SBLaunchImageOverridesContext initWithSceneID:activationSettings:];
```
