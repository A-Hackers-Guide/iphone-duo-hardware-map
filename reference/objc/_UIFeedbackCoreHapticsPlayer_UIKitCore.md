# `_UIFeedbackCoreHapticsPlayer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFeedbackPlayer_Internal`
- 4 instance variables, 3 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _internalQueue;
@? _invalidationBlock;
@"_UIFeedbackCoreHapticsEngine" _hapticEngine;
@"<CHHapticPatternPlayer>" _coreHapticsPlayer;
```

## Properties

```
@property (T@"_UIFeedbackCoreHapticsEngine",W,N,V_hapticEngine) hapticEngine;
@property (T@"<CHHapticPatternPlayer>",&,N,V_coreHapticsPlayer) coreHapticsPlayer;
@property (T@?,C,N,V_invalidationBlock) invalidationBlock;
```

## Instance methods

```
-[_UIFeedbackCoreHapticsPlayer initWithEngine:];
-[_UIFeedbackCoreHapticsPlayer _internal_createFixedParameterForParameters:withKey:forEventType:];
-[_UIFeedbackCoreHapticsPlayer _internal_playFeedbackData:forFeedback:atTime:];
-[_UIFeedbackCoreHapticsPlayer hapticEngine];
-[_UIFeedbackCoreHapticsPlayer _playFeedback:atTime:];
-[_UIFeedbackCoreHapticsPlayer _stopFeedback:];
-[_UIFeedbackCoreHapticsPlayer _internal_createEventsForLegacyFeedbackData:];
-[_UIFeedbackCoreHapticsPlayer coreHapticsPlayer];
-[_UIFeedbackCoreHapticsPlayer _internal_createEventsForTransientHapticData:];
-[_UIFeedbackCoreHapticsPlayer setHapticEngine:];
-[_UIFeedbackCoreHapticsPlayer _internal_updateValueForParameters:withKey:];
-[_UIFeedbackCoreHapticsPlayer _internal_createPatternForFeedbackData:feedback:engine:];
-[_UIFeedbackCoreHapticsPlayer _internal_createPlayerWithPattern:];
-[_UIFeedbackCoreHapticsPlayer setCoreHapticsPlayer:];
-[_UIFeedbackCoreHapticsPlayer _internal_stopFeedbackData:forFeedback:];
-[_UIFeedbackCoreHapticsPlayer setInvalidationBlock:];
-[_UIFeedbackCoreHapticsPlayer _internal_createEventsForFileFeedbackData:engine:parameters:parameterCurves:];
-[_UIFeedbackCoreHapticsPlayer _updateValueForParameters:withKey:];
-[_UIFeedbackCoreHapticsPlayer _internal_immediateParametersForFeedbackData:];
-[_UIFeedbackCoreHapticsPlayer invalidationBlock];
-[_UIFeedbackCoreHapticsPlayer _internal_createEventsForFeedbackData:engine:parameters:parameterCurves:];
-[_UIFeedbackCoreHapticsPlayer _internal_createEventsForLibraryFeedbackData:engine:parameters:parameterCurves:];
```
