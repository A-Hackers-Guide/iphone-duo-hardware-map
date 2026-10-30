# `_UIFeedbackSystemSoundEngine`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedbackEngine`
- Protocols: `_UIFeedbackPlayer_Internal`
- 3 instance variables, 3 properties, 17 instance methods, 3 class methods

## Instance variables

```
@? _invalidationBlock;
@"NSCountedSet" _warmSSIDs;
@"NSCountedSet" _suspendedSSIDs;
```

## Properties

```
@property (T@"NSCountedSet",R,N,V_suspendedSSIDs) suspendedSSIDs;
@property (T@"NSCountedSet",R,N,V_warmSSIDs) warmSSIDs;
@property (T@?,C,N,V_invalidationBlock) invalidationBlock;
```

## Class methods

```
+[_UIFeedbackSystemSoundEngine _internalQueue];
+[_UIFeedbackSystemSoundEngine sharedEngine];
+[_UIFeedbackSystemSoundEngine _supportsPlayingIndividualFeedback:];
```

## Instance methods

```
-[_UIFeedbackSystemSoundEngine _stats_key];
-[_UIFeedbackSystemSoundEngine _internal_playFeedbackData:forFeedback:atTime:];
-[_UIFeedbackSystemSoundEngine _playFeedback:atTime:];
-[_UIFeedbackSystemSoundEngine _internal_prepareSystemSoundID:forBeingActive:];
-[_UIFeedbackSystemSoundEngine _internal_playFeedbackDataNow:forFeedback:withOptions:];
-[_UIFeedbackSystemSoundEngine _stopFeedback:];
-[_UIFeedbackSystemSoundEngine _internal_startWarmingFeedbacks:];
-[_UIFeedbackSystemSoundEngine _internal_performForEachSSIDsInFeedbacks:block:];
-[_UIFeedbackSystemSoundEngine suspendedSSIDs];
-[_UIFeedbackSystemSoundEngine _internal_updateSuspension];
-[_UIFeedbackSystemSoundEngine _internal_stopFeedbackData:forFeedback:];
-[_UIFeedbackSystemSoundEngine setInvalidationBlock:];
-[_UIFeedbackSystemSoundEngine _updateValueForParameters:withKey:];
-[_UIFeedbackSystemSoundEngine _internal_dequeueReusableFeedbackPlayerWithCompletionBlock:];
-[_UIFeedbackSystemSoundEngine _internal_stopWarmingFeedbacks:];
-[_UIFeedbackSystemSoundEngine invalidationBlock];
-[_UIFeedbackSystemSoundEngine warmSSIDs];
```
