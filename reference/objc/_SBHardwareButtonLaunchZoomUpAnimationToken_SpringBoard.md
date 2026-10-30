# `_SBHardwareButtonLaunchZoomUpAnimationToken`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHardwareButtonLaunchZoomUpAnimationToken`
- 4 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<SBCaptureButtonPreludeAnimatingPrivate>" _bezelEffectsCoordinator;
@"BSSimpleAssertion" _underlyingAssertion;
d _requestedWindowLevel;
B _valid;
```

## Properties

```
@property (Td,N) requestedDropletWindowLevel;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBHardwareButtonLaunchZoomUpAnimationToken dealloc];
-[_SBHardwareButtonLaunchZoomUpAnimationToken invalidate];
-[_SBHardwareButtonLaunchZoomUpAnimationToken setRequestedDropletWindowLevel:];
-[_SBHardwareButtonLaunchZoomUpAnimationToken animatingDroplet];
-[_SBHardwareButtonLaunchZoomUpAnimationToken animatingDropletContext];
-[_SBHardwareButtonLaunchZoomUpAnimationToken appendZoomUpCompletionBlock:];
-[_SBHardwareButtonLaunchZoomUpAnimationToken associatedBezelEffectsCoordinator];
-[_SBHardwareButtonLaunchZoomUpAnimationToken initWithPreludeAnimating:invalidationBlock:];
-[_SBHardwareButtonLaunchZoomUpAnimationToken isHardwareButtonZoomUpAnimationToken];
-[_SBHardwareButtonLaunchZoomUpAnimationToken preludeAnimationVelocity];
-[_SBHardwareButtonLaunchZoomUpAnimationToken requestedDropletWindowLevel];
```
