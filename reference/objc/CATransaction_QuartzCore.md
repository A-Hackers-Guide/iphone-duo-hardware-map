# `CATransaction`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 73 class methods

## Class methods

```
+[CATransaction setAnimationTimingFunction:];
+[CATransaction setBoolValue:forKey:];
+[CATransaction setBeginTime:];
+[CATransaction setAnimationDuration:];
+[CATransaction commit];
+[CATransaction setCompletionBlock:];
+[CATransaction completionBlock];
+[CATransaction begin];
+[CATransaction synchronize];
+[CATransaction setDisableActions:];
+[CATransaction animationDuration];
+[CATransaction flush];
+[CATransaction batch];
+[CATransaction setLowLatency:];
+[CATransaction disableActions];
+[CATransaction animator];
+[CATransaction lowLatency];
+[CATransaction setValue:forKey:];
+[CATransaction valueForKey:];
+[CATransaction currentPhase];
+[CATransaction animationTimingFunction];
+[CATransaction activate];
+[CATransaction boolValueForKey:];
+[CATransaction lock];
+[CATransaction unlock];
+[CATransaction currentState];
+[CATransaction beginTime];
+[CATransaction batchWithDefaultServerObserver:];
+[CATransaction emptyLowLatency];
+[CATransaction forceCommitTime];
+[CATransaction registerBoolKey];
+[CATransaction setEarliestAutomaticCommitTime:];
+[CATransaction _implicitAnimationForLayer:keyPath:];
+[CATransaction activateBackground:];
+[CATransaction addCommitHandler:forPhase:];
+[CATransaction animatesFromModelValues];
+[CATransaction assertInactive];
+[CATransaction batchAsynchronously];
+[CATransaction commitTime];
+[CATransaction committingContexts];
+[CATransaction defaultDisableRunLoopObserverCommits];
+[CATransaction disableImplicitTransactionMainThreadAssert];
+[CATransaction disableRunLoopObserverCommits];
+[CATransaction disableSignPosts];
+[CATransaction earliestAutomaticCommitTime];
+[CATransaction enableUpdateCycleSupport];
+[CATransaction finishFrameWithToken:];
+[CATransaction flushAsRunLoopObserver];
+[CATransaction frameStallSkipRequest];
+[CATransaction generateSeed];
+[CATransaction inputTime];
+[CATransaction popAnimator];
+[CATransaction pushAnimator:];
+[CATransaction remoteInputMachTime];
+[CATransaction setAnimatesFromModelValues:];
+[CATransaction setCommitHandler:];
+[CATransaction setCommitTime:];
+[CATransaction setCommittingContexts:];
+[CATransaction setDefaultDisableRunLoopObserverCommits:];
+[CATransaction setDisableImplicitTransactionMainThreadAssert:];
+[CATransaction setDisableRunLoopObserverCommits:];
+[CATransaction setDisableSignPosts:];
+[CATransaction setEmptyLowLatency:];
+[CATransaction setForceCommitTime:];
+[CATransaction setFrameInputTime:withToken:];
+[CATransaction setFrameStallSkipRequest:];
+[CATransaction setImplicitTransactionDidBeginHandler:];
+[CATransaction setInputTime:];
+[CATransaction setPresentationHandler:queue:];
+[CATransaction setRemoteInputMachTime:];
+[CATransaction setUpdateDeadline:];
+[CATransaction startFrameWithReason:beginTime:commitDeadline:];
+[CATransaction updateDeadline];
```
