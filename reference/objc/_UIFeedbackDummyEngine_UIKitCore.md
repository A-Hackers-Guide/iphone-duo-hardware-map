# `_UIFeedbackDummyEngine`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedbackEngine`
- Protocols: `_UIFeedbackPlayer_Internal`
- 1 instance variables, 1 properties, 10 instance methods, 2 class methods

## Instance variables

```
@? _invalidationBlock;
```

## Properties

```
@property (T@?,C,N,V_invalidationBlock) invalidationBlock;
```

## Class methods

```
+[_UIFeedbackDummyEngine sharedEngine];
+[_UIFeedbackDummyEngine _supportsPlayingIndividualFeedback:];
```

## Instance methods

```
-[_UIFeedbackDummyEngine _stats_key];
-[_UIFeedbackDummyEngine _internal_playFeedbackData:forFeedback:atTime:];
-[_UIFeedbackDummyEngine _playFeedback:atTime:];
-[_UIFeedbackDummyEngine _stopFeedback:];
-[_UIFeedbackDummyEngine _internal_activateUnderlyingPlayerWithCompletion:];
-[_UIFeedbackDummyEngine _internal_stopFeedbackData:forFeedback:];
-[_UIFeedbackDummyEngine setInvalidationBlock:];
-[_UIFeedbackDummyEngine _updateValueForParameters:withKey:];
-[_UIFeedbackDummyEngine _internal_dequeueReusableFeedbackPlayerWithCompletionBlock:];
-[_UIFeedbackDummyEngine invalidationBlock];
```
