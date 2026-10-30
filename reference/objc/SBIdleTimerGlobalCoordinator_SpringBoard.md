# `SBIdleTimerGlobalCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBIdleTimerObserving`, `SBIdleTimerGlobalStateMonitorObserving`, `PTSettingsKeyObserver`, `SBIdleTimerCoordinating`
- 20 instance variables, 9 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"SBIdleTimerDescriptorFactory" _idleTimerDescriptorFactory;
@"SBIdleTimerGlobalStateMonitor" _globalStateMonitor;
@"SBIdleTimerProxy" _idleTimerProxy;
@"SBIdleTimerProxy" _enabledIdleTimerProxy;
@"SBIdleTimerDescriptor" _enabledIdleTimerDescriptor;
B _idleTimerSourceEnabled;
@"SBIdleTimerCoordinatorHelper" _idleTimerCoordinatorHelper;
@"<BSInvalidatable>" _disableAutoDimAssertion;
@"FBSDisplayLayoutMonitor" _layoutMonitor;
B _started;
@"<SBIdleTimerResetSource>" _lastResetSource;
@"SBIdleTimerTelemetryEmitter" _idleTimerTelemetryEmitter;
@"NSString" _currentDisablingClientBundleIdentifier;
@"<BSInvalidatable>" _stateCaptureAssertion;
@"PTTestRecipe" _clientDisableAssertionsTestRecipe;
@"PTTestRecipe" _internalDisableAssertionsTestRecipe;
@"SBIdleTimerSettings" _idleTimerPrototypeSettings;
@"<SBIdleTimerGlobalCoordinatorDelegate>" _delegate;
@"<SBIdleTimerProviding>" _idleTimerProvider;
@"NSMutableDictionary" _idleTimerDisableAssertions;
```

## Properties

```
@property (T@"<SBIdleTimer>",R,N) idleTimer;
@property (T@"<SBIdleTimerProviding>",W,N,G_idleTimerProvider,S_setIdleTimerProvider:,V_idleTimerProvider) idleTimerProvider;
@property (T@"NSMutableDictionary",&,N,G_idleTimerDisableAssertions,S_setIdleTimerDisableAssertions:,V_idleTimerDisableAssertions) idleTimerDisableAssertions;
@property (T@"<SBIdleTimerGlobalCoordinatorDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisIdleTimerDisabled) idleTimerDisabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBIdleTimerGlobalCoordinator idleTimer];
-[SBIdleTimerGlobalCoordinator _addStateCaptureHandlers];
-[SBIdleTimerGlobalCoordinator idleTimerProvider:didProposeBehavior:forReason:];
-[SBIdleTimerGlobalCoordinator _stateCaptureDescription];
-[SBIdleTimerGlobalCoordinator resetIdleTimerIfNonConsecutiveSource:forReason:];
-[SBIdleTimerGlobalCoordinator idleTimerDidRefresh:];
-[SBIdleTimerGlobalCoordinator _updateIdleTimerForReason:];
-[SBIdleTimerGlobalCoordinator _idleTimerDisableAssertions];
-[SBIdleTimerGlobalCoordinator dealloc];
-[SBIdleTimerGlobalCoordinator acquireIdleTimerDisableAssertionForReason:];
-[SBIdleTimerGlobalCoordinator start];
-[SBIdleTimerGlobalCoordinator settings:changedValueForKey:];
-[SBIdleTimerGlobalCoordinator initWithGlobalStateMonitor:];
-[SBIdleTimerGlobalCoordinator _activeIdleTimerProvider];
-[SBIdleTimerGlobalCoordinator _updateGlobalStateDisableAssertions];
-[SBIdleTimerGlobalCoordinator _updateIdleTimerForProvider:behavior:descriptor:forReason:];
-[SBIdleTimerGlobalCoordinator _setIdleTimerDisableAssertions:];
-[SBIdleTimerGlobalCoordinator _logEffectiveLockTimeout];
-[SBIdleTimerGlobalCoordinator _registerTestRecipes];
-[SBIdleTimerGlobalCoordinator isIdleTimerDisabled];
-[SBIdleTimerGlobalCoordinator setDelegate:];
-[SBIdleTimerGlobalCoordinator _applyActiveIdleTimerDescriptorForReason:];
-[SBIdleTimerGlobalCoordinator _idleTimerPrefsChanged];
-[SBIdleTimerGlobalCoordinator idleTimerDidResetForUserAttention:];
-[SBIdleTimerGlobalCoordinator _updateIdleTimerForProvider:behavior:forReason:];
-[SBIdleTimerGlobalCoordinator _registerClientDisableAssertionsTestRecipe];
-[SBIdleTimerGlobalCoordinator _setIdleTimerSourceEnabled:forReason:];
-[SBIdleTimerGlobalCoordinator _setIdleTimerProvider:];
-[SBIdleTimerGlobalCoordinator idleTimerGlobalStateMonitor:changedForReason:];
-[SBIdleTimerGlobalCoordinator delegate];
-[SBIdleTimerGlobalCoordinator layoutMonitor:didUpdateDisplayLayout:withContext:];
-[SBIdleTimerGlobalCoordinator resetIdleTimerForReason:];
-[SBIdleTimerGlobalCoordinator _unregisterTestRecipes];
-[SBIdleTimerGlobalCoordinator resetIdleTimerIfCurrentIdealDurationAtLeast:forReason:];
-[SBIdleTimerGlobalCoordinator _idleTimerProvider];
-[SBIdleTimerGlobalCoordinator _logTelemetryForIdleTimerUpdatedFromTimer:toTimer:withReason:];
-[SBIdleTimerGlobalCoordinator _hasIdleTimerDisableAssertions];
-[SBIdleTimerGlobalCoordinator _registerInternalDisableAssertionsTestRecipe];
-[SBIdleTimerGlobalCoordinator _setIdleTimerWithDescriptor:forReason:];
-[SBIdleTimerGlobalCoordinator _areIdleTimerDisableAssertionsPrevented];
```
