# `SBDashBoardCameraPrewarmConfiguration`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSCameraPrewarmConfiguring`
- 5 instance variables, 10 properties, 7 instance methods, 0 class methods

## Instance variables

```
B _prewarmCameraHardware;
B _prewarmForCaptureLaunch;
q _backgroundLaunchTarget;
@"NSString" _applicationBundleIdentifier;
@"NSString" _prewarmingBundleIdentifier;
```

## Properties

```
@property (TB,R,N,V_prewarmCameraHardware) prewarmCameraHardware;
@property (TB,R,N,V_prewarmForCaptureLaunch) prewarmForCaptureLaunch;
@property (TB,R,N) backgroundLaunch;
@property (Tq,R,N,V_backgroundLaunchTarget) backgroundLaunchTarget;
@property (T@"NSString",R,C,N,V_applicationBundleIdentifier) applicationBundleIdentifier;
@property (T@"NSString",R,C,N,V_prewarmingBundleIdentifier) prewarmingBundleIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDashBoardCameraPrewarmConfiguration backgroundLaunch];
-[SBDashBoardCameraPrewarmConfiguration applicationBundleIdentifier];
-[SBDashBoardCameraPrewarmConfiguration prewarmForCaptureLaunch];
-[SBDashBoardCameraPrewarmConfiguration backgroundLaunchTarget];
-[SBDashBoardCameraPrewarmConfiguration initWithPrewarmCameraHardware:prewarmForCaptureLaunch:backgroundLaunchTarget:applicationBundleIdentifier:prewarmingBundleIdentifier:];
-[SBDashBoardCameraPrewarmConfiguration prewarmCameraHardware];
-[SBDashBoardCameraPrewarmConfiguration prewarmingBundleIdentifier];
```
