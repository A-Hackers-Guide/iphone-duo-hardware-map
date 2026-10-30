# `_UIFeedbackCoreHapticsEngine`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedbackEngine`
- 3 instance variables, 1 properties, 16 instance methods, 10 class methods

## Instance variables

```
@"NSMutableSet" _playersInUse;
@"NSMutableSet" _playersToInvalidate;
@"CHHapticEngine" _coreHapticsEngine;
```

## Properties

```
@property (T@"CHHapticEngine",R,N,V_coreHapticsEngine) coreHapticsEngine;
```

## Class methods

```
+[_UIFeedbackCoreHapticsEngine _internalQueue];
+[_UIFeedbackCoreHapticsEngine sharedEngine];
+[_UIFeedbackCoreHapticsEngine _supportsPlayingIndividualFeedback:];
+[_UIFeedbackCoreHapticsEngine _additionalEngineOptions];
+[_UIFeedbackCoreHapticsEngine _loadHapticEngineClass];
+[_UIFeedbackCoreHapticsEngine _setHapticEngineCreationBlock:];
+[_UIFeedbackCoreHapticsEngine _setHapticPatternClass:];
+[_UIFeedbackCoreHapticsEngine _supportsAbortingDeactivation];
+[_UIFeedbackCoreHapticsEngine _supportsPlayingFeedbackPatternsDirectly];
+[_UIFeedbackCoreHapticsEngine _supportsPlayingIndividualFeedback:allowsIgnoreCapture:];
```

## Instance methods

```
-[_UIFeedbackCoreHapticsEngine _stats_key];
-[_UIFeedbackCoreHapticsEngine _internal_resetCoreHapticsEngine];
-[_UIFeedbackCoreHapticsEngine init];
-[_UIFeedbackCoreHapticsEngine _internal_createCoreHapticsEngine];
-[_UIFeedbackCoreHapticsEngine _internal_startRunningFeedbackPlayerWithCompletion:];
-[_UIFeedbackCoreHapticsEngine _internal_coreHapticsEngineFinishedWithError:completion:];
-[_UIFeedbackCoreHapticsEngine _internal_cooldownUnderlyingPlayerIfPossibleWithCompletion:];
-[_UIFeedbackCoreHapticsEngine coreHapticsEngine];
-[_UIFeedbackCoreHapticsEngine _internal_activateUnderlyingPlayerWithCompletion:];
-[_UIFeedbackCoreHapticsEngine _internal_prewarmUnderlyingPlayerWithCompletion:];
-[_UIFeedbackCoreHapticsEngine _coreHapticsEngineStoppedForReason:];
-[_UIFeedbackCoreHapticsEngine _internal_coreHapticsEngineStoppedForReason:];
-[_UIFeedbackCoreHapticsEngine _internal_dequeueReusableFeedbackPlayerWithCompletionBlock:];
-[_UIFeedbackCoreHapticsEngine _resetCoreHapticsEngine];
-[_UIFeedbackCoreHapticsEngine _internal_teardownUnderlyingPlayerIfPossibleWithCompletion:];
-[_UIFeedbackCoreHapticsEngine _internal_initializeCoreHapticsEngine];
```
