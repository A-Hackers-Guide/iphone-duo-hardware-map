# `SBCaptureApplicationLaunchAssertionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 4 instance variables, 7 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _observerQueue;
@"NSMutableDictionary" _launchAssertionsPerBundleIdentifier;
@"NSMutableDictionary" _assertionTimersByBundleIdentifier;
@"NSHashTable" _observers;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V_launchAssertionsPerBundleIdentifier) launchAssertionsPerBundleIdentifier;
@property (T@"NSMutableDictionary",R,N,V_assertionTimersByBundleIdentifier) assertionTimersByBundleIdentifier;
@property (T@"NSHashTable",R,N,V_observers) observers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBCaptureApplicationLaunchAssertionManager sharedInstance];
```

## Instance methods

```
-[SBCaptureApplicationLaunchAssertionManager _queue_removeObserver:];
-[SBCaptureApplicationLaunchAssertionManager debugDescription];
-[SBCaptureApplicationLaunchAssertionManager succinctDescriptionBuilder];
-[SBCaptureApplicationLaunchAssertionManager removeObserver:];
-[SBCaptureApplicationLaunchAssertionManager init];
-[SBCaptureApplicationLaunchAssertionManager dealloc];
-[SBCaptureApplicationLaunchAssertionManager descriptionWithMultilinePrefix:];
-[SBCaptureApplicationLaunchAssertionManager succinctDescription];
-[SBCaptureApplicationLaunchAssertionManager addObserver:];
-[SBCaptureApplicationLaunchAssertionManager description];
-[SBCaptureApplicationLaunchAssertionManager observers];
-[SBCaptureApplicationLaunchAssertionManager _queue_addObserver:];
-[SBCaptureApplicationLaunchAssertionManager descriptionBuilderWithMultilinePrefix:];
-[SBCaptureApplicationLaunchAssertionManager _clearAssertionTimerForBundleIdentifier:];
-[SBCaptureApplicationLaunchAssertionManager _notifyObserversAssertionDidUpdateForBundleIdentifier:];
-[SBCaptureApplicationLaunchAssertionManager _startAssertionTimerForBundleIdentifier:];
-[SBCaptureApplicationLaunchAssertionManager acquireCaptureApplicationLaunchAssertionForBundleIdentifier:reason:];
-[SBCaptureApplicationLaunchAssertionManager assertionForBundleIdentifier:];
-[SBCaptureApplicationLaunchAssertionManager assertionTimersByBundleIdentifier];
-[SBCaptureApplicationLaunchAssertionManager launchAssertionsPerBundleIdentifier];
```
