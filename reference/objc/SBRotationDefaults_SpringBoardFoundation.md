# `SBRotationDefaults`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractSpringBoardDefaultDomain`
- 0 instance variables, 5 properties, 3 instance methods, 0 class methods

## Properties

```
@property (T@"NSDictionary",C,D,N) perDisplayLastLockedOrientations;
@property (Tq,D,N) lastLockedOrientation;
@property (TB,R,D,N,GisVideoRotationEnabled) videoRotationEnabled;
@property (TB,R,D,N,GisPostModernRotationForciblyEnabled) postModernRotationForciblyEnabled;
@property (TB,R,D,N,GisLandscapeOverrideEnabled) landscapeOverrideEnabled;
```

## Instance methods

```
-[SBRotationDefaults _bindAndRegisterDefaults];
-[SBRotationDefaults lastLockedOrientationForSurfaceType:];
-[SBRotationDefaults setLastLockedOrientation:forSurfaceType:];
```
