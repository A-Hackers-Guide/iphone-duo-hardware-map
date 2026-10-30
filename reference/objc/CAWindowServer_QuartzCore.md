# `CAWindowServer`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 6 properties, 29 instance methods, 6 class methods

## Instance variables

```
^{CAWindowServerImpl=^{__CFArray}I@?} _impl;
B _mirroringEnabled;
@"CAWindowServerDisplayExternalSyncManager" _displayExternalSyncManager;
```

## Properties

```
@property (T@"NSArray",R) displays;
@property (TB,GisMirroringEnabled,V_mirroringEnabled) mirroringEnabled;
@property (TI) rendererFlags;
@property (TB,GisSecure) secure;
@property (T@"CAWindowServerDisplayExternalSyncManager",R,N,V_displayExternalSyncManager) displayExternalSyncManager;
@property (T@?) slotDeletionCallback;
```

## Class methods

```
+[CAWindowServer server];
+[CAWindowServer context];
+[CAWindowServer serverIfRunning];
+[CAWindowServer contextWithOptions:];
+[CAWindowServer serverWithOptions:];
+[CAWindowServer stopServer];
```

## Instance methods

```
-[CAWindowServer taskNamePortOfContextId:];
-[CAWindowServer isMirroringEnabled];
-[CAWindowServer isSecure];
-[CAWindowServer rendererFlags];
-[CAWindowServer setSecure:];
-[CAWindowServer clientPortOfContextId:];
-[CAWindowServer init];
-[CAWindowServer contextIdHostingContextId:];
-[CAWindowServer dealloc];
-[CAWindowServer setMirroringEnabled:];
-[CAWindowServer _init];
-[CAWindowServer displays];
-[CAWindowServer description];
-[CAWindowServer _detectDisplays];
-[CAWindowServer addDisplay:];
-[CAWindowServer displayExternalSyncManager];
-[CAWindowServer displayWithDisplayId:];
-[CAWindowServer displayWithName:];
-[CAWindowServer displayWithUniqueId:];
-[CAWindowServer enableOutOfProcessDisplayObservation];
-[CAWindowServer insecureProcessIds];
-[CAWindowServer isSlotValid:];
-[CAWindowServer removeAllDisplays];
-[CAWindowServer removeDisplay:];
-[CAWindowServer secureModeViolations];
-[CAWindowServer setRendererFlags:];
-[CAWindowServer setSlotDeletionCallback:];
-[CAWindowServer slotDeletionCallback];
-[CAWindowServer updateBandWidthInfoForAllDisplays];
```
