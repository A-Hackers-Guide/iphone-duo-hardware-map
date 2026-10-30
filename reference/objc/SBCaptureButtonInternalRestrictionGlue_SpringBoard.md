# `SBCaptureButtonInternalRestrictionGlue`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 2 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"SBCaptureButtonRestrictionCoordinator" _coordinator;
@"<BSInvalidatable>" _captureButtonInhibitionAssertion;
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
-[SBCaptureButtonInternalRestrictionGlue dealloc];
-[SBCaptureButtonInternalRestrictionGlue invalidate];
-[SBCaptureButtonInternalRestrictionGlue initWithCoordinator:];
-[SBCaptureButtonInternalRestrictionGlue acquireRestriction:];
-[SBCaptureButtonInternalRestrictionGlue relinquishRestriction];
```
