# `BKUIPearlEnrollAudioManager`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"BKUIPearlAudioSession" _audioSession;
@"BKUIPearlEnrollControllerPreloadedState" _preloadedState;
@"<BKUIPearlAudioStateDelegate>" _stateDelegate;
@"CHHapticEngine" _hapticsEngine;
```

## Properties

```
@property (T@"CHHapticEngine",&,N,V_hapticsEngine) hapticsEngine;
@property (T@"BKUIPearlEnrollControllerPreloadedState",&,N,V_preloadedState) preloadedState;
@property (T@"<BKUIPearlAudioStateDelegate>",W,N,V_stateDelegate) stateDelegate;
```

## Instance methods

```
-[BKUIPearlEnrollAudioManager dealloc];
-[BKUIPearlEnrollAudioManager setStateDelegate:];
-[BKUIPearlEnrollAudioManager stateDelegate];
-[BKUIPearlEnrollAudioManager cleanupHaptics];
-[BKUIPearlEnrollAudioManager cleanupHapticsAndSound];
-[BKUIPearlEnrollAudioManager cleanupSound];
-[BKUIPearlEnrollAudioManager createEngine];
-[BKUIPearlEnrollAudioManager fadeCurrentSound:completion:];
-[BKUIPearlEnrollAudioManager hapticEventWithEventType:withDelay:];
-[BKUIPearlEnrollAudioManager hapticsEngine];
-[BKUIPearlEnrollAudioManager playHaptic:withDelay:];
-[BKUIPearlEnrollAudioManager playHapticWithEvents:];
-[BKUIPearlEnrollAudioManager preloadedState];
-[BKUIPearlEnrollAudioManager setHapticsEngine:];
-[BKUIPearlEnrollAudioManager setPreloadedState:];
-[BKUIPearlEnrollAudioManager setUpHaptics];
-[BKUIPearlEnrollAudioManager setupSound];
-[BKUIPearlEnrollAudioManager triggerSoundHapticForTransitionToState:fromState:];
-[BKUIPearlEnrollAudioManager triggerSoundHapticForTransitionToSubstate:fromSubstate:];
```
