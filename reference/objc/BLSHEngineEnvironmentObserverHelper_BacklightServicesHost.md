# `BLSHEngineEnvironmentObserverHelper`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightInactiveEnvironmentSessionObserving`, `BLSHDateSpecifierModelObserving`
- 6 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<BLSHBacklightSceneHostEnvironmentObserver>" _engine;
@"BLSHDateSpecifierModel" _lock_presentationDatesModel;
@"NSMutableSet" _lock_modelEnvironments;
@"BLSHBacklightInactiveEnvironmentSession" _lock_inactiveSession;
@"BLSHBacklightEnvironmentPresentation" _lock_presentation;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Properties

```
@property (T@"BLSHBacklightInactiveEnvironmentSession",&,N) inactiveSession;
@property (T@"BLSHDateSpecifierModel",&,N) presentationDatesModel;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHEngineEnvironmentObserverHelper initWithEngine:];
-[BLSHEngineEnvironmentObserverHelper didEndInactiveEnvironmentSession:];
-[BLSHEngineEnvironmentObserverHelper inactiveSession];
-[BLSHEngineEnvironmentObserverHelper inactiveEnvironmentSession:didUpdateToPresentation:];
-[BLSHEngineEnvironmentObserverHelper setInactiveSession:];
-[BLSHEngineEnvironmentObserverHelper dateSpecifierModel:didAddEnvironment:];
-[BLSHEngineEnvironmentObserverHelper dateSpecifierModel:didRemoveEnvironment:];
-[BLSHEngineEnvironmentObserverHelper didUpdateToPresentation:];
-[BLSHEngineEnvironmentObserverHelper presentationDatesModel];
-[BLSHEngineEnvironmentObserverHelper setPresentationDatesModel:];
```
