# `CAMFocusLockWithLensPositionCommand`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureCommand`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
f __lensPosition;
@? __completionBlock;
```

## Properties

```
@property (Tf,N,S_setLensPosition:,V__lensPosition) _lensPosition;
@property (T@?,C,N,S_setCompletionBlock:,V__completionBlock) _completionBlock;
```

## Class methods

```
+[CAMFocusLockWithLensPositionCommand currentLensPositionSentinel];
```

## Instance methods

```
-[CAMFocusLockWithLensPositionCommand _completionBlock];
-[CAMFocusLockWithLensPositionCommand executeWithContext:];
-[CAMFocusLockWithLensPositionCommand copyWithZone:];
-[CAMFocusLockWithLensPositionCommand _setCompletionBlock:];
-[CAMFocusLockWithLensPositionCommand _lensPosition];
-[CAMFocusLockWithLensPositionCommand _setLensPosition:];
-[CAMFocusLockWithLensPositionCommand initWithLensPosition:completionBlock:];
```
