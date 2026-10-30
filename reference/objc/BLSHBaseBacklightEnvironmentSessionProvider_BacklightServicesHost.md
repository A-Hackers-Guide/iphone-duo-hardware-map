# `BLSHBaseBacklightEnvironmentSessionProvider`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightInactiveEnvironmentSessionObserving`, `BLSHBacklightEnvironmentSessionProviding`, `BLSHPresentationSetting`
- 6 instance variables, 7 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"BLSHBacklightInactiveEnvironmentSession" _lock_activeSession;
@"BLSHBacklightEnvironmentPresentation" _lock_presentation;
@? _lock_setPresentationCompletion;
@"NSString" _displayLoggingName;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BLSDisplay>" _display;
```

## Properties

```
@property (T@"<BLSDisplay>",R,N,V_display) display;
@property (T@"BLSHBacklightInactiveEnvironmentSession",R,N) activeSession;
@property (T@"BLSHBacklightEnvironmentPresentation",R,N) presentation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHBaseBacklightEnvironmentSessionProvider didEndInactiveEnvironmentSession:];
-[BLSHBaseBacklightEnvironmentSessionProvider display];
-[BLSHBaseBacklightEnvironmentSessionProvider presentation];
-[BLSHBaseBacklightEnvironmentSessionProvider initForDisplay:];
-[BLSHBaseBacklightEnvironmentSessionProvider init];
-[BLSHBaseBacklightEnvironmentSessionProvider createInactiveEnvironmentSession];
-[BLSHBaseBacklightEnvironmentSessionProvider createInactiveEnvironmentSessionForDisplay:];
-[BLSHBaseBacklightEnvironmentSessionProvider inactiveEnvironmentSession:didUpdateToPresentation:];
-[BLSHBaseBacklightEnvironmentSessionProvider activeSession];
-[BLSHBaseBacklightEnvironmentSessionProvider setPresentation:withCompletion:];
-[BLSHBaseBacklightEnvironmentSessionProvider presentationEntrySupportsAlwaysOn:];
-[BLSHBaseBacklightEnvironmentSessionProvider setPresentation:completion:];
-[BLSHBaseBacklightEnvironmentSessionProvider setPresentationWithFBScenes:flipbookContext:completion:];
```
