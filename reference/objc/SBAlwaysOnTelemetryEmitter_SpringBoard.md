# `SBAlwaysOnTelemetryEmitter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSBacklightStateObserving`, `BLSHBacklightHostTelemetryDelegate`, `SBBacklightEnvironmentSessionProviderObserver`, `BLSHAssertionServiceObserving`, `BLSHFlipbookTelemetry`
- 13 instance variables, 5 properties, 28 instance methods, 1 class methods

## Instance variables

```
@"SBBacklightEnvironmentSessionProvider" _backlightEnvironmentSessionProvider;
@"NSHashTable" _backlights;
@"SBAlwaysOnDefaults" _alwaysOnDefaults;
@"<BSDefaultObserver>" _alwaysOnDefaultsObserverToken;
@"NSObject<OS_dispatch_queue>" _metricsQueue;
@"SBAlwaysOnTelemetryMetrics" _mq_metrics;
@"NSTimer" _mq_deferredLoggingTimer;
@"NSSet" _mq_currentPresentationBundleIdentifiers;
@"NSObject<OS_dispatch_queue>" _powerlogSendQueue;
@"NSObject<OS_dispatch_queue>" _biomeWriterQueue;
@"BMDisplayAlwaysOn" _lastBiomeEvent;
@"NSDictionary" _lastAlwaysOnEnabledPayload;
@"SBAlwaysOnPolicyCoordinator" _alwaysOnPolicyCoordinator;
```

## Properties

```
@property (T@"SBAlwaysOnPolicyCoordinator",W,N,V_alwaysOnPolicyCoordinator) alwaysOnPolicyCoordinator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBAlwaysOnTelemetryEmitter new];
```

## Instance methods

```
-[SBAlwaysOnTelemetryEmitter service:didAcquireAssertion:];
-[SBAlwaysOnTelemetryEmitter alwaysOnPolicyCoordinator];
-[SBAlwaysOnTelemetryEmitter backlightTelemetrySource:willUpdateDisplayForState:forEvent:];
-[SBAlwaysOnTelemetryEmitter init];
-[SBAlwaysOnTelemetryEmitter _significantTimeChange:];
-[SBAlwaysOnTelemetryEmitter dealloc];
-[SBAlwaysOnTelemetryEmitter backlightEnvironmentSessionsProvider:didUpdatePresentationWithBundleIdentifiers:];
-[SBAlwaysOnTelemetryEmitter backlightTelemetrySource:didUpdateDisplayForState:forEvent:];
-[SBAlwaysOnTelemetryEmitter logTelemetryForRenderSession:];
-[SBAlwaysOnTelemetryEmitter backlightTelemetrySource:didAcquireSystemActivityWithError:isActive:details:forEvent:];
-[SBAlwaysOnTelemetryEmitter initWithBacklightEnvironmentSessionProvider:];
-[SBAlwaysOnTelemetryEmitter completeIntializationAfterBLSStartup];
-[SBAlwaysOnTelemetryEmitter backlightTelemetrySource:hadExistingSystemActivityForEvent:];
-[SBAlwaysOnTelemetryEmitter backlightTelemetrySource:didUpdateVisualContentsToBeginTransitionToState:forEvent:];
-[SBAlwaysOnTelemetryEmitter logTelemetryForRequestDates:];
-[SBAlwaysOnTelemetryEmitter setAlwaysOnPolicyCoordinator:];
-[SBAlwaysOnTelemetryEmitter backlightTelemetrySource:willTransitionToState:forEvent:];
-[SBAlwaysOnTelemetryEmitter logTelemetryForInvalidation:];
-[SBAlwaysOnTelemetryEmitter backlightTelemetrySource:didCompleteUpdateToState:forEvent:];
-[SBAlwaysOnTelemetryEmitter resolveTelemetryBacklightState];
-[SBAlwaysOnTelemetryEmitter addBacklight:];
-[SBAlwaysOnTelemetryEmitter backlight:didChangeAlwaysOnEnabled:];
-[SBAlwaysOnTelemetryEmitter service:didCancelAssertion:withError:];
-[SBAlwaysOnTelemetryEmitter backlightTelemetrySource:didCompleteUpdateToFlipbookState:forEvent:];
-[SBAlwaysOnTelemetryEmitter service:didResumeAssertion:];
-[SBAlwaysOnTelemetryEmitter service:didPauseAssertion:];
-[SBAlwaysOnTelemetryEmitter removeBacklight:];
-[SBAlwaysOnTelemetryEmitter copyiOSSpecificFieldsAndResetMetrics];
```
