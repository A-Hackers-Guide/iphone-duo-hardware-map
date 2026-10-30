# `_UIFeedbackBackBoardEngine`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedbackEngine`
- Protocols: `_UIFeedbackPlayer_Internal`
- 2 instance variables, 2 properties, 10 instance methods, 4 class methods

## Instance variables

```
@? _invalidationBlock;
@"NSCountedSet" _suspendedSSIDs;
```

## Properties

```
@property (T@"NSCountedSet",R,N,V_suspendedSSIDs) suspendedSSIDs;
@property (T@?,C,N,V_invalidationBlock) invalidationBlock;
```

## Class methods

```
+[_UIFeedbackBackBoardEngine _internalQueue];
+[_UIFeedbackBackBoardEngine sharedEngine];
+[_UIFeedbackBackBoardEngine _supportsPlayingIndividualFeedback:];
+[_UIFeedbackBackBoardEngine _supportsAbortingDeactivation];
```

## Instance methods

```
-[_UIFeedbackBackBoardEngine _stats_key];
-[_UIFeedbackBackBoardEngine _internal_playFeedbackData:forFeedback:atTime:];
-[_UIFeedbackBackBoardEngine _playFeedback:atTime:];
-[_UIFeedbackBackBoardEngine _stopFeedback:];
-[_UIFeedbackBackBoardEngine suspendedSSIDs];
-[_UIFeedbackBackBoardEngine _internal_stopFeedbackData:forFeedback:];
-[_UIFeedbackBackBoardEngine setInvalidationBlock:];
-[_UIFeedbackBackBoardEngine _updateValueForParameters:withKey:];
-[_UIFeedbackBackBoardEngine _internal_dequeueReusableFeedbackPlayerWithCompletionBlock:];
-[_UIFeedbackBackBoardEngine invalidationBlock];
```
