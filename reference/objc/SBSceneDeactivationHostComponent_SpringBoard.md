# `SBSceneDeactivationHostComponent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `FBSceneComponent`
- 2 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"FBScene" _fbScene;
@"UIApplicationSceneDeactivationManager" _deactivationManager;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSceneDeactivationHostComponent sceneWillActivate:];
-[SBSceneDeactivationHostComponent sceneWillDeactivate:withContext:];
-[SBSceneDeactivationHostComponent setScene:];
-[SBSceneDeactivationHostComponent scene:willUpdateSettings:];
-[SBSceneDeactivationHostComponent invalidate];
```
