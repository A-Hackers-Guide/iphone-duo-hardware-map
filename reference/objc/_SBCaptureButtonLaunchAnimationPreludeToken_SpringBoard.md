# `_SBCaptureButtonLaunchAnimationPreludeToken`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHardwareButtonLaunchPreludeAnimationToken`, `BSInvalidatable`
- 3 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<SBCaptureButtonPreludeAnimatingPrivate>" _bezelEffectsCoordinator;
@"BSSimpleAssertion" _underlyingAssertion;
B _valid;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBCaptureButtonLaunchAnimationPreludeToken dealloc];
-[_SBCaptureButtonLaunchAnimationPreludeToken invalidate];
-[_SBCaptureButtonLaunchAnimationPreludeToken cancel];
-[_SBCaptureButtonLaunchAnimationPreludeToken associatedBezelEffectsCoordinator];
-[_SBCaptureButtonLaunchAnimationPreludeToken expandHintingDropletByAddingComponents:shockwave:];
-[_SBCaptureButtonLaunchAnimationPreludeToken initWithPreludeAnimating:invalidationBlock:];
-[_SBCaptureButtonLaunchAnimationPreludeToken isPreludeAnimationToken];
-[_SBCaptureButtonLaunchAnimationPreludeToken preludeAnimationRectPresentationValue];
-[_SBCaptureButtonLaunchAnimationPreludeToken updateShockwaveLightType:];
```
