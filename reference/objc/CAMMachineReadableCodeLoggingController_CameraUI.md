# `CAMMachineReadableCodeLoggingController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
B __seenMachineReadableObjectOfAcceptableSize;
B __seenMachineReadableObjectOfUnacceptableSize;
B __seenMachineReadableObjectInNonActiveState;
```

## Properties

```
@property (TB,N,S_setSeenMachineReadableObjectOfAcceptableSize:,V__seenMachineReadableObjectOfAcceptableSize) _seenMachineReadableObjectOfAcceptableSize;
@property (TB,N,S_setSeenMachineReadableObjectOfUnacceptableSize:,V__seenMachineReadableObjectOfUnacceptableSize) _seenMachineReadableObjectOfUnacceptableSize;
@property (TB,N,S_setSeenMachineReadableObjectInNonActiveState:,V__seenMachineReadableObjectInNonActiveState) _seenMachineReadableObjectInNonActiveState;
```

## Instance methods

```
-[CAMMachineReadableCodeLoggingController init];
-[CAMMachineReadableCodeLoggingController _seenMachineReadableObjectInNonActiveState];
-[CAMMachineReadableCodeLoggingController _seenMachineReadableObjectOfAcceptableSize];
-[CAMMachineReadableCodeLoggingController _seenMachineReadableObjectOfUnacceptableSize];
-[CAMMachineReadableCodeLoggingController _setSeenMachineReadableObjectInNonActiveState:];
-[CAMMachineReadableCodeLoggingController _setSeenMachineReadableObjectOfAcceptableSize:];
-[CAMMachineReadableCodeLoggingController _setSeenMachineReadableObjectOfUnacceptableSize:];
-[CAMMachineReadableCodeLoggingController logMachineReadableCodeResult:isOfSignificantSize:];
-[CAMMachineReadableCodeLoggingController logMachineReadableCodeResultDuringInactiveAppState];
-[CAMMachineReadableCodeLoggingController resetLoggingState];
```
