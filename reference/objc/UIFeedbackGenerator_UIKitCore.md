# `UIFeedbackGenerator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction`
- 17 instance variables, 17 properties, 78 instance methods, 8 class methods

## Instance variables

```
[3q] _styleActivationCount;
[3q] _autoDeactivationCount;
@"NSObject<OS_dispatch_source>" _autoDeactivateTimer;
@"NSMutableDictionary" _preparationTimers;
@? _feedbackWarmingBlock;
d _currentDelay;
@"NSSet" _usedFeedbacks;
B _activated;
B _disabledByView;
@"<UITraitChangeRegistration>" _traitChangeRegistration;
B _usesCustomActivation;
q _activationCount;
q _externalActivationCount;
@"UIView" _view;
@"_UIFeedbackGeneratorGestureRecognizer" _gestureRecognizer;
@"_UIFeedbackGeneratorConfiguration" _configuration;
@"NSSet" _engines;
```

## Properties

```
@property (T@"<UICoordinateSpace>",R,W,N) coordinateSpace;
@property (TB,N,G_isMuted,S_setMuted:) muted;
@property (Tq,N,V_activationCount) activationCount;
@property (Tq,N,V_externalActivationCount) externalActivationCount;
@property (TB,N,V_usesCustomActivation) usesCustomActivation;
@property (T@"UIView",W,N,V_view) view;
@property (T@"_UIFeedbackGeneratorGestureRecognizer",&,N,V_gestureRecognizer) gestureRecognizer;
@property (T@"_UIFeedbackGeneratorConfiguration",&,N,G_configuration,S_setConfiguration:,V_configuration) configuration;
@property (T@"NSSet",R,N,V_engines) engines;
@property (TB,R,N,G_isEnabled) enabled;
@property (Td,R,N,G_autoDeactivationTimeout) autoDeactivationTimeout;
@property (TB,R,N,G_isAutoDeactivated) autoDeactivated;
@property (T@"NSString",R,N) _stats_key;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIFeedbackGenerator _configurationClass];
+[UIFeedbackGenerator _resetAutoDeactivateTimeout];
+[UIFeedbackGenerator _resetPreparationTimeouts];
+[UIFeedbackGenerator _setAutoDeactivateTimeout:];
+[UIFeedbackGenerator _setPreparationTimeout:forStyle:];
+[UIFeedbackGenerator _setRunningTests:];
+[UIFeedbackGenerator behaviorWithConfiguration:coordinateSpace:];
+[UIFeedbackGenerator feedbackGeneratorForView:];
```

## Instance methods

```
-[UIFeedbackGenerator _stats_key];
-[UIFeedbackGenerator initWithConfiguration:view:];
-[UIFeedbackGenerator deactivate];
-[UIFeedbackGenerator coordinateSpace];
-[UIFeedbackGenerator _isEnabled];
-[UIFeedbackGenerator gestureRecognizer];
-[UIFeedbackGenerator activateWithCompletionBlock:];
-[UIFeedbackGenerator init];
-[UIFeedbackGenerator _stopFeedback:];
-[UIFeedbackGenerator initWithView:];
-[UIFeedbackGenerator dealloc];
-[UIFeedbackGenerator _ui_descriptionBuilder];
-[UIFeedbackGenerator setView:];
-[UIFeedbackGenerator initWithConfiguration:];
-[UIFeedbackGenerator _configuration];
-[UIFeedbackGenerator initWithCoordinateSpace:];
-[UIFeedbackGenerator view];
-[UIFeedbackGenerator _deactivated];
-[UIFeedbackGenerator engines];
-[UIFeedbackGenerator _preparationTimeoutForStyle:];
-[UIFeedbackGenerator _playFeedback:];
-[UIFeedbackGenerator prepare];
-[UIFeedbackGenerator willMoveToView:];
-[UIFeedbackGenerator _activated];
-[UIFeedbackGenerator setGestureRecognizer:];
-[UIFeedbackGenerator description];
-[UIFeedbackGenerator isActive];
-[UIFeedbackGenerator _autoDeactivationTimeout];
-[UIFeedbackGenerator didMoveToView:];
-[UIFeedbackGenerator _autoDeactivate];
-[UIFeedbackGenerator _setOutputMode:];
-[UIFeedbackGenerator _stats_prepared];
-[UIFeedbackGenerator activationCount];
-[UIFeedbackGenerator __activateWithStyle:forFeedback:completionBlock:];
-[UIFeedbackGenerator __deactivateWithStyle:];
-[UIFeedbackGenerator _activateWithStyle:completionBlock:];
-[UIFeedbackGenerator _activationCountStatistics];
-[UIFeedbackGenerator _activationDurationStatistics];
-[UIFeedbackGenerator _activationTimeOutCountStatistics];
-[UIFeedbackGenerator _clientDidUpdateGeneratorWithSelector:];
-[UIFeedbackGenerator _deactivateWithStyle:];
-[UIFeedbackGenerator _forceDeactivationForStyle:];
-[UIFeedbackGenerator _isAutoDeactivated];
-[UIFeedbackGenerator _isMuted];
-[UIFeedbackGenerator _outputMode];
-[UIFeedbackGenerator _playCountStatistics];
-[UIFeedbackGenerator _playFeedback:atLocation:];
-[UIFeedbackGenerator _playFeedback:withMinimumIntervalPassed:since:prefersRegularPace:atLocation:];
-[UIFeedbackGenerator _preparationCountStatistics];
-[UIFeedbackGenerator _preparationTimerForStyle:];
-[UIFeedbackGenerator _prepareWithStyle:];
-[UIFeedbackGenerator _resetAutoDeactivationTimeout];
-[UIFeedbackGenerator _scheduleFeedbackWarming];
-[UIFeedbackGenerator _setConfiguration:];
-[UIFeedbackGenerator _setMuted:];
-[UIFeedbackGenerator _setPreparationTimer:forStyle:];
-[UIFeedbackGenerator _setupAutoDeactivateTimer];
-[UIFeedbackGenerator _setupEnginesIfNeededForFeedback:];
-[UIFeedbackGenerator _setupForFeedback:];
-[UIFeedbackGenerator _startFeedbackWarming];
-[UIFeedbackGenerator _statsSuffix];
-[UIFeedbackGenerator _stats_activationDidChangeTo:];
-[UIFeedbackGenerator _stats_activationTimedOut];
-[UIFeedbackGenerator _stats_playedFeedback];
-[UIFeedbackGenerator _stopAutoDeactivateTimer];
-[UIFeedbackGenerator _stopFeedbackWarming];
-[UIFeedbackGenerator _stopPreparationForAllStyles];
-[UIFeedbackGenerator _stopPreparationForStyle:];
-[UIFeedbackGenerator _updateActivationStateForRemovedEngines:addedEngines:prewarmCount:turnOnCount:];
-[UIFeedbackGenerator _updateForViewUserInterfaceIdiom];
-[UIFeedbackGenerator _updatePreparationTimer:withTimeout:];
-[UIFeedbackGenerator externalActivationCount];
-[UIFeedbackGenerator initWithConfiguration:coordinateSpace:];
-[UIFeedbackGenerator performFeedbackWithDelay:insideBlock:];
-[UIFeedbackGenerator setActivationCount:];
-[UIFeedbackGenerator setExternalActivationCount:];
-[UIFeedbackGenerator setUsesCustomActivation:];
-[UIFeedbackGenerator usesCustomActivation];
```
