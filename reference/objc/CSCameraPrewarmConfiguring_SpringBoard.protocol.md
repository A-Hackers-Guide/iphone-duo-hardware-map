# `CSCameraPrewarmConfiguring` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 6 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) prewarmCameraHardware;
@property (TB,R,N) prewarmForCaptureLaunch;
@property (TB,R,N) backgroundLaunch;
@property (Tq,R,N) backgroundLaunchTarget;
@property (T@"NSString",R,C,N) applicationBundleIdentifier;
@property (T@"NSString",R,C,N) prewarmingBundleIdentifier;
```

## Instance methods

```
-[CSCameraPrewarmConfiguring backgroundLaunch];
-[CSCameraPrewarmConfiguring applicationBundleIdentifier];
-[CSCameraPrewarmConfiguring prewarmForCaptureLaunch];
-[CSCameraPrewarmConfiguring backgroundLaunchTarget];
-[CSCameraPrewarmConfiguring prewarmCameraHardware];
-[CSCameraPrewarmConfiguring prewarmingBundleIdentifier];
```
