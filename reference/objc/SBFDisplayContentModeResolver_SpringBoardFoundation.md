# `SBFDisplayContentModeResolver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `SBFDevicePoseProviderObserver`, `BSInvalidatable`
- 14 instance variables, 6 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"SBFDisplayContentModeTransitionCoordinator" _currentTransitionCoordinator;
@"NSArray" _policies;
@"SBFResolvedDisplayContentMode" _resolution;
@"SBFYoinkDisplayContentModeResolutionPolicy" _yoinkPolicy;
@"SBFForceCoverDisplayOnlyDisplayContentModeResolutionPolicy" _forceCoverDisplayOnlyPolicy;
@"SBFDevicePoseProvider" _devicePoseProvider;
@"NSMutableDictionary" _displayProxies;
B _isReadyToResolve;
B _isInvalidated;
Q _delegateCalloutDepth;
@"SBFDevicePoseDefaults" _devicePoseDefaults;
q _preferredTransitionStyle;
@"<BSInvalidatable>" _stateCaptureHandle;
@"<SBFDisplayContentModeResolverDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBFDisplayContentModeResolverDelegate>",W,N,V_delegate) delegate;
@property (T@"SBFDisplayContentModeTransitionContext",R,N) currentTransitionContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFDisplayContentModeResolver debugDescription];
-[SBFDisplayContentModeResolver dealloc];
-[SBFDisplayContentModeResolver succinctDescription];
-[SBFDisplayContentModeResolver poseProvider:didUpdateFromPose:toPose:];
-[SBFDisplayContentModeResolver invalidate];
-[SBFDisplayContentModeResolver setDelegate:];
-[SBFDisplayContentModeResolver delegate];
-[SBFDisplayContentModeResolver description];
-[SBFDisplayContentModeResolver appendDescriptionToStream:];
-[SBFDisplayContentModeResolver _continuousFoldEffectProgress];
-[SBFDisplayContentModeResolver _devicePose];
-[SBFDisplayContentModeResolver _identifierForWindowScene:];
-[SBFDisplayContentModeResolver _mechanicalHingeAngleDegrees];
-[SBFDisplayContentModeResolver _proxyForWindowScene:];
-[SBFDisplayContentModeResolver _resolvedModeForDisplay:];
-[SBFDisplayContentModeResolver _shouldAcceptDisplayConfiguration:];
-[SBFDisplayContentModeResolver _startResolvingContentModeOfDisplay:];
-[SBFDisplayContentModeResolver _startTransitionWithDisplays:];
-[SBFDisplayContentModeResolver _startTransitionWithDisplaysIfNeeded:newResolution:oldResolution:];
-[SBFDisplayContentModeResolver _stopResolvingContentModeOfDisplay:];
-[SBFDisplayContentModeResolver _surfaceTypeForWindowScene:];
-[SBFDisplayContentModeResolver _targetModeForDisplay:];
-[SBFDisplayContentModeResolver _updateCurrentTransitionIfNeeded];
-[SBFDisplayContentModeResolver _updateDisplayContentModesWithContext:continuationHandler:];
-[SBFDisplayContentModeResolver _updateResolvedContentModesForDisplays];
-[SBFDisplayContentModeResolver acquireForceCoverDisplayOnlyEnabledAssertionWithReason:];
-[SBFDisplayContentModeResolver acquireForcePrimaryContentAssertionForWindowScene:reason:invalidationHandler:];
-[SBFDisplayContentModeResolver acquireYoinkActivationAssertionForWindowScene:reason:invalidationHandler:];
-[SBFDisplayContentModeResolver appliedContentModeOfDisplayForWindowScene:];
-[SBFDisplayContentModeResolver currentTransitionContext];
-[SBFDisplayContentModeResolver initWithDevicePoseProvider:];
-[SBFDisplayContentModeResolver isAppliedDisplayContentModeUserInitiatedForWindowScene:];
-[SBFDisplayContentModeResolver startResolvingContentModeOfDisplayForWindowScene:];
-[SBFDisplayContentModeResolver stopResolvingContentModeOfDisplayForWindowScene:];
```
