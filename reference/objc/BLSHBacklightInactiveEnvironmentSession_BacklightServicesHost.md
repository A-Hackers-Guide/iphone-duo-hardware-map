# `BLSHBacklightInactiveEnvironmentSession`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightSceneHostEnvironmentObserver`
- 6 instance variables, 6 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"NSHashTable" _environmentObservers;
@"<BLSHBacklightInactiveEnvironmentSessionUpdating>" _updater;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _ended;
@"BLSHBacklightEnvironmentPresentation" _presentation;
```

## Properties

```
@property (T@"<BLSHBacklightInactiveEnvironmentSessionUpdating>",&,N) updater;
@property (T@"BLSHBacklightEnvironmentPresentation",&,N,V_presentation) presentation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHBacklightInactiveEnvironmentSession sessionWithPresentation:];
```

## Instance methods

```
-[BLSHBacklightInactiveEnvironmentSession sessionDidEnd];
-[BLSHBacklightInactiveEnvironmentSession updater];
-[BLSHBacklightInactiveEnvironmentSession hostEnvironment:hostDidSet1HzFlipbook:];
-[BLSHBacklightInactiveEnvironmentSession hostEnvironment:invalidateContentForReason:];
-[BLSHBacklightInactiveEnvironmentSession presentation];
-[BLSHBacklightInactiveEnvironmentSession setPresentation:];
-[BLSHBacklightInactiveEnvironmentSession removeObserver:];
-[BLSHBacklightInactiveEnvironmentSession updaterDidUpdateToPresentation:];
-[BLSHBacklightInactiveEnvironmentSession hostEnvironment:hostDidSetUnrestrictedFramerateUpdates:];
-[BLSHBacklightInactiveEnvironmentSession dealloc];
-[BLSHBacklightInactiveEnvironmentSession setUpdater:];
-[BLSHBacklightInactiveEnvironmentSession hostEnvironment:clientDidUpdateAlwaysOnContentIs1hz:];
-[BLSHBacklightInactiveEnvironmentSession addObserver:];
-[BLSHBacklightInactiveEnvironmentSession initWithPresentation:];
-[BLSHBacklightInactiveEnvironmentSession hostEnvironment:hostDidSetAlwaysOnEnabledForEnvironment:];
-[BLSHBacklightInactiveEnvironmentSession hostEnvironment:hostDidSetHighLuminanceAlwaysOn:];
-[BLSHBacklightInactiveEnvironmentSession hostEnvironment:clientDidUpdateSupportsAlwaysOn:];
-[BLSHBacklightInactiveEnvironmentSession removeEnvironmentsObserver:];
-[BLSHBacklightInactiveEnvironmentSession updaterDidBeginUpdateToBacklightState:];
-[BLSHBacklightInactiveEnvironmentSession hostEnvironment:clientDidUpdateEnabled:];
-[BLSHBacklightInactiveEnvironmentSession addEnvironmentsObserver:];
-[BLSHBacklightInactiveEnvironmentSession hostEnvironment:hostDidSetLiveUpdating:];
-[BLSHBacklightInactiveEnvironmentSession hostEnvironment:hostDidSetCacheFlipbookOnDisplayWake:];
```
