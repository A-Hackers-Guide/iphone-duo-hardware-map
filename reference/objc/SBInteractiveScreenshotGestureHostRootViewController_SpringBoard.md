# `SBInteractiveScreenshotGestureHostRootViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFTouchPassThroughViewController`
- Protocols: `BSInvalidatable`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
I _hostingContextID;
i _hostingPid;
@"_UILayerHostView" _layerHostView;
@"UIScreen" _screen;
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
-[SBInteractiveScreenshotGestureHostRootViewController initWithScreen:];
-[SBInteractiveScreenshotGestureHostRootViewController supportedInterfaceOrientations];
-[SBInteractiveScreenshotGestureHostRootViewController viewDidLoad];
-[SBInteractiveScreenshotGestureHostRootViewController invalidate];
-[SBInteractiveScreenshotGestureHostRootViewController _canShowWhileLocked];
-[SBInteractiveScreenshotGestureHostRootViewController _reloadLayerHostView];
-[SBInteractiveScreenshotGestureHostRootViewController setHostingContextID:pid:];
```
