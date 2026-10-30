# `SBFDisplayContentModeResolutionPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 3 properties, 13 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,C,N) name;
@property (TB,R,N) swapsContentMode;
@property (TB,R,N) isUserInitiated;
```

## Instance methods

```
-[SBFDisplayContentModeResolutionPolicy debugDescription];
-[SBFDisplayContentModeResolutionPolicy isUserInitiated];
-[SBFDisplayContentModeResolutionPolicy description];
-[SBFDisplayContentModeResolutionPolicy name];
-[SBFDisplayContentModeResolutionPolicy isInteractiveForDisplayProxy:devicePose:];
-[SBFDisplayContentModeResolutionPolicy notePolicyDidActivate];
-[SBFDisplayContentModeResolutionPolicy notePolicyDidDeactivate];
-[SBFDisplayContentModeResolutionPolicy noteResolvedPrevailingPolicy:];
-[SBFDisplayContentModeResolutionPolicy preferredPrimarySurfaceTypeForDevicePose:];
-[SBFDisplayContentModeResolutionPolicy resolvedModeForDisplayProxy:devicePose:];
-[SBFDisplayContentModeResolutionPolicy shouldBeActiveForDevicePose:prevailingPolicy:candidatePolicy:];
-[SBFDisplayContentModeResolutionPolicy swapsContentMode];
-[SBFDisplayContentModeResolutionPolicy targetModeForDisplayProxy:devicePose:];
```
