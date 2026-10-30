# `_UIFocusDisplayLinkScrollAnimator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 1 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"UIScreen" _screen;
@"_UIFocusEngineScrollableContainerOffsets" _singleScrollableContainerEntry;
@"NSMapTable" _scrollableContainers;
@"CADisplayLink" _displayLink;
@"NSTimer" _timer;
d _lastHeartbeatTime;
d _defaultConvergenceRate;
```

## Properties

```
@property (Td,N) defaultConvergenceRate;
```

## Instance methods

```
-[_UIFocusDisplayLinkScrollAnimator initWithScreen:];
-[_UIFocusDisplayLinkScrollAnimator observeValueForKeyPath:ofObject:change:context:];
-[_UIFocusDisplayLinkScrollAnimator dealloc];
-[_UIFocusDisplayLinkScrollAnimator isAnimatingScrollableContainer:];
-[_UIFocusDisplayLinkScrollAnimator _applyAccelerationLimitToAcceleration:currentOffset:targetOffset:];
-[_UIFocusDisplayLinkScrollAnimator _canCreateDisplayLink];
-[_UIFocusDisplayLinkScrollAnimator _commonHeartbeat];
-[_UIFocusDisplayLinkScrollAnimator _commonHeartbeat:];
-[_UIFocusDisplayLinkScrollAnimator _createEntryForEnvironmentScrollableContainer:];
-[_UIFocusDisplayLinkScrollAnimator _displayLinkHeartbeat:];
-[_UIFocusDisplayLinkScrollAnimator _entryForEnvironmentScrollableContainer:createIfNeeded:];
-[_UIFocusDisplayLinkScrollAnimator _entryForScrollableContainer:];
-[_UIFocusDisplayLinkScrollAnimator _hyperJumpContentOffsetIfNecessaryForEntry:currentOffset:];
-[_UIFocusDisplayLinkScrollAnimator _processEntry:timeDelta:completed:cancelled:];
-[_UIFocusDisplayLinkScrollAnimator _removeEntry:];
-[_UIFocusDisplayLinkScrollAnimator _shouldPushAndPopRunLoopModes];
-[_UIFocusDisplayLinkScrollAnimator _switchToTimerScrolling];
-[_UIFocusDisplayLinkScrollAnimator _timerHeartbeat:];
-[_UIFocusDisplayLinkScrollAnimator _updateHeartbeatConfiguration];
-[_UIFocusDisplayLinkScrollAnimator adjustTargetContentOffsetForScrollableContainer:byDelta:];
-[_UIFocusDisplayLinkScrollAnimator cancelScrollingForScrollableContainer:];
-[_UIFocusDisplayLinkScrollAnimator currentVelocityForScrollableContainer:];
-[_UIFocusDisplayLinkScrollAnimator defaultConvergenceRate];
-[_UIFocusDisplayLinkScrollAnimator setDefaultConvergenceRate:];
-[_UIFocusDisplayLinkScrollAnimator setTargetContentOffset:forEnvironmentScrollableContainer:convergenceRate:completion:];
-[_UIFocusDisplayLinkScrollAnimator targetContentOffsetForScrollableContainer:];
-[_UIFocusDisplayLinkScrollAnimator velocityToScrollFromOffset:toOffset:];
```
