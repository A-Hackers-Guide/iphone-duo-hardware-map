# `ULDisplayMonitor`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULEventMonitor`
- 4 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _displayOn;
B _screenLocked;
@"FBSDisplayLayoutMonitor" _displayLayoutMinitor;
@"NSString" _appInFocus;
```

## Properties

```
@property (T@"FBSDisplayLayoutMonitor",&,N,V_displayLayoutMinitor) displayLayoutMinitor;
@property (T@"NSString",&,N,V_appInFocus) appInFocus;
@property (TB,N,V_displayOn) displayOn;
@property (TB,N,V_screenLocked) screenLocked;
```

## Instance methods

```
-[ULDisplayMonitor stopMonitoring:];
-[ULDisplayMonitor appInFocus];
-[ULDisplayMonitor setDisplayOn:];
-[ULDisplayMonitor displayOn];
-[ULDisplayMonitor _checkAppInFocusFromLayout:];
-[ULDisplayMonitor _didUpdateDisplayLayout:];
-[ULDisplayMonitor screenLocked];
-[ULDisplayMonitor setScreenLocked:];
-[ULDisplayMonitor latestEventAfterAddingObserverForEventName:];
-[ULDisplayMonitor setAppInFocus:];
-[ULDisplayMonitor setDisplayLayoutMinitor:];
-[ULDisplayMonitor _checkDisplayOnFromLayout:];
-[ULDisplayMonitor startMonitoring:];
-[ULDisplayMonitor _checkScreenLockedFromLayout:];
-[ULDisplayMonitor displayLayoutMinitor];
```
