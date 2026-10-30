# `ULDisplayMonitor_OSX`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULEventMonitor`
- 4 instance variables, 4 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _screenOn;
B _clamshellMode;
B _screenLocked;
@"CUSystemMonitor" _systemMonitor;
```

## Properties

```
@property (T@"CUSystemMonitor",&,N,V_systemMonitor) systemMonitor;
@property (TB,N,V_screenOn) screenOn;
@property (TB,N,V_clamshellMode) clamshellMode;
@property (TB,N,V_screenLocked) screenLocked;
```

## Instance methods

```
-[ULDisplayMonitor_OSX systemMonitor];
-[ULDisplayMonitor_OSX stopMonitoring:];
-[ULDisplayMonitor_OSX setScreenOn:];
-[ULDisplayMonitor_OSX screenLocked];
-[ULDisplayMonitor_OSX screenOn];
-[ULDisplayMonitor_OSX setScreenLocked:];
-[ULDisplayMonitor_OSX clamshellMode];
-[ULDisplayMonitor_OSX latestEventAfterAddingObserverForEventName:];
-[ULDisplayMonitor_OSX startMonitoring:];
-[ULDisplayMonitor_OSX setSystemMonitor:];
-[ULDisplayMonitor_OSX _activateWithCompletion];
-[ULDisplayMonitor_OSX _checkClamshellMode];
-[ULDisplayMonitor_OSX _checkScreenLocked];
-[ULDisplayMonitor_OSX _checkScreenOn];
-[ULDisplayMonitor_OSX _clamshellModeChangedHandler];
-[ULDisplayMonitor_OSX _invalidationHandler];
-[ULDisplayMonitor_OSX _screenLockedChangedHandler];
-[ULDisplayMonitor_OSX _screenOnChangedHandler];
-[ULDisplayMonitor_OSX setClamshellMode:];
```
