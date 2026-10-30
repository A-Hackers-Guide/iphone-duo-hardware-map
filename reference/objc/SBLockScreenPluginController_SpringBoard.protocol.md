# `SBLockScreenPluginController` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `SBPluginBundleController`, `SBUIOptionalLegibility`
- 0 instance variables, 5 properties, 11 instance methods, 0 class methods

## Properties

```
@property (T@"<SBLockScreenPluginAgent>",W,N) pluginAgent;
@property (Tq,R,N) pluginPriority;
@property (T@"UIViewController<SBLockScreenPluginViewController>",R,N) pluginViewController;
@property (T@"<SBLockScreenPluginAppearance>",R,N) pluginAppearance;
@property (T@"SBLockScreenPluginAction",?,R,&,N) pluginUnlockAction;
```

## Instance methods

```
-[SBLockScreenPluginController pluginViewController];
-[SBLockScreenPluginController setPluginAgent:];
-[SBLockScreenPluginController pluginAgent];
-[SBLockScreenPluginController pluginAppearance];
-[SBLockScreenPluginController pluginPriority];
-[SBLockScreenPluginController updateForPresentation:];
-[SBLockScreenPluginController pluginDidDeactivateWithContext:];
-[SBLockScreenPluginController hidesLockScreenComplications];
-[SBLockScreenPluginController pluginHandleEvent:];
-[SBLockScreenPluginController pluginUnlockAction];
-[SBLockScreenPluginController pluginWillActivateWithContext:];
```
