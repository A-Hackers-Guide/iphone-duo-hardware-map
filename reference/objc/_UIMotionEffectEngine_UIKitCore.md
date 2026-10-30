# `_UIMotionEffectEngine`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSBacklightStateObserving`, `_UIMotionEffectEventConsumer`
- 24 instance variables, 6 properties, 66 instance methods, 4 class methods

## Instance variables

```
@"_UIAssociationTable" _effectViewAssociationTable;
@"_UILazyMapTable" _sharedAnalyzerSettingsToAnalyzers;
@"NSMapTable" _sharedAnalyzersToEffects;
@"NSMapTable" _suspendedViewsToEffectSets;
@"_UIMotionEffectEventProvider" _eventProvider;
B _hasReceivedAtLeastOneEventSinceStarting;
@"_UIMotionEffectEvent" _pendingEvent;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _pendingEventLock;
@"NSMapTable" _screenStates;
@"NSMapTable" _viewToBodyObserver;
@"NSMapTable" _viewToBodyGroup;
@"NSMapTable" _pendingBodyUpdates;
B _bodyUpdateFlushScheduled;
B _generatingUpdates;
@"NSMutableSet" _suspendReasons;
B _slowUpdatesEnabled;
B _pendingSlowDown;
q _eventProviderStatus;
B _allAnalyzersAreCentered;
B _hasAppliedAtLeastOneUpdateSinceStarting;
B _isPendingReset;
i _thermalNotificationToken;
i _screenDimmingNotificationToken;
q _targetInterfaceOrientation;
```

## Properties

```
@property (Tq,N,S_setTargetInterfaceOrientation:,V_targetInterfaceOrientation) _targetInterfaceOrientation;
@property (T@"NSArray",R,N) suspensionReasons;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIMotionEffectEngine _analyzerClass];
+[_UIMotionEffectEngine _eventProviderClass];
+[_UIMotionEffectEngine _motionEffectsEnabled];
+[_UIMotionEffectEngine _motionEffectsSupported];
```

## Instance methods

```
-[_UIMotionEffectEngine backlight:didCompleteUpdateToState:forEvents:abortedEvents:];
-[_UIMotionEffectEngine _toggleSlowUpdates];
-[_UIMotionEffectEngine _processSynchronizedUpdate];
-[_UIMotionEffectEngine beginSuspendingForReason:];
-[_UIMotionEffectEngine _updateDisplayLinkIntervalForScreenState:];
-[_UIMotionEffectEngine debugDescription];
-[_UIMotionEffectEngine _bodyKeyForBodyID:interfaceAngle:];
-[_UIMotionEffectEngine init];
-[_UIMotionEffectEngine _applyEffectsFromSharedAnalyzer:forScreen:];
-[_UIMotionEffectEngine _removeBodyObserverForView:];
-[_UIMotionEffectEngine _startGeneratingUpdates];
-[_UIMotionEffectEngine _screenStateForDisplayLink:];
-[_UIMotionEffectEngine _hasMotionEffectsForView:];
-[_UIMotionEffectEngine _registerEffect:view:withBodyGroup:];
-[_UIMotionEffectEngine dealloc];
-[_UIMotionEffectEngine _anyActiveEventProvider];
-[_UIMotionEffectEngine _updateEffectsForScreenState:];
-[_UIMotionEffectEngine _setTargetInterfaceOrientation:];
-[_UIMotionEffectEngine _stopGeneratingUpdates];
-[_UIMotionEffectEngine _unregisterAllMotionEffectsForView:];
-[_UIMotionEffectEngine _viewDidMoveFromScreen:toScreen:];
-[_UIMotionEffectEngine _isSuspended];
-[_UIMotionEffectEngine _updateEffectsForSharedProviderOnScreenState:];
-[_UIMotionEffectEngine _handleLatestDeviceMotion:];
-[_UIMotionEffectEngine _startOrStopGeneratingUpdates];
-[_UIMotionEffectEngine _tearDownBodyGroup:];
-[_UIMotionEffectEngine endApplyingMotionEffect:toView:];
-[_UIMotionEffectEngine _updateBacklightState:forScreenState:];
-[_UIMotionEffectEngine endSuspendingMotionEffectsForView:];
-[_UIMotionEffectEngine _screenDidDisconnect:];
-[_UIMotionEffectEngine _motionEffectsAreSuspendedForView:];
-[_UIMotionEffectEngine _viewsForEffect:inBodyGroup:];
-[_UIMotionEffectEngine _createBodyGroupForBodyID:interfaceAngle:key:screenState:];
-[_UIMotionEffectEngine endSuspendingForReason:];
-[_UIMotionEffectEngine _resetMotionAnalysisForScreen:];
-[_UIMotionEffectEngine _currentEventForView:];
-[_UIMotionEffectEngine _attachView:toBodyGroup:];
-[_UIMotionEffectEngine _updateSlowModeForNewEvent:previousEvent:timeSinceLastNewMotionEvent:];
-[_UIMotionEffectEngine _shouldGenerateUpdates];
-[_UIMotionEffectEngine beginSuspendingMotionEffectsForView:];
-[_UIMotionEffectEngine _motionEffect:belongsToView:];
-[_UIMotionEffectEngine _hasEffectsOnScreen:];
-[_UIMotionEffectEngine _wantsSynchronizedUpdates];
-[_UIMotionEffectEngine suspensionReasons];
-[_UIMotionEffectEngine _detachViewFromBodyGroup:];
-[_UIMotionEffectEngine _screenStateForScreen:];
-[_UIMotionEffectEngine _unregisterMotionEffect:fromView:];
-[_UIMotionEffectEngine _flushPendingBodyUpdates];
-[_UIMotionEffectEngine _ensureBodyObserverForView:];
-[_UIMotionEffectEngine updateWithEvent:];
-[_UIMotionEffectEngine _updateEffectsForBodyGroup:screenState:];
-[_UIMotionEffectEngine _applyBodyUpdateForView:bodyID:interfaceAngle:];
-[_UIMotionEffectEngine _applyEffectsFromBodyGroup:analyzer:screen:];
-[_UIMotionEffectEngine _view:didReportBodyID:interfaceAngle:];
-[_UIMotionEffectEngine _screenStateForBacklight:];
-[_UIMotionEffectEngine _motionEffectsForView:];
-[_UIMotionEffectEngine beginApplyingMotionEffect:toView:];
-[_UIMotionEffectEngine _targetInterfaceOrientation];
-[_UIMotionEffectEngine _allBodyGroups];
-[_UIMotionEffectEngine _cleanUpScreenStateIfEmptyForScreen:];
-[_UIMotionEffectEngine updateEventProviderStatus:];
-[_UIMotionEffectEngine _removeScreenStateForScreen:];
-[_UIMotionEffectEngine _unapplyAllEffects];
-[_UIMotionEffectEngine _unregisterEffect:view:fromBodyGroup:];
-[_UIMotionEffectEngine _usesPerScreenProviders];
-[_UIMotionEffectEngine _createScreenStateIfNecessary:];
```
