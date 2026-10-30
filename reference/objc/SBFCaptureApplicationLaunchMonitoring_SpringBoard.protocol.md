# `SBFCaptureApplicationLaunchMonitoring` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `BSInvalidatable`, `BSCancellable`
- 0 instance variables, 2 properties, 5 instance methods, 1 class methods

## Properties

```
@property (T@"FBScene",R,N) scene;
@property (T@"<SBFCaptureApplicationLaunchMonitorDelegate>",R,W,N) delegate;
```

## Class methods

```
+[SBFCaptureApplicationLaunchMonitoring new];
```

## Instance methods

```
-[SBFCaptureApplicationLaunchMonitoring init];
-[SBFCaptureApplicationLaunchMonitoring start];
-[SBFCaptureApplicationLaunchMonitoring scene];
-[SBFCaptureApplicationLaunchMonitoring delegate];
-[SBFCaptureApplicationLaunchMonitoring initWithScene:delegate:];
```
