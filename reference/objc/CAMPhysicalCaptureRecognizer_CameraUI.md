# `CAMPhysicalCaptureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 5 instance variables, 5 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _suspended;
@"NSSet" _activeButtons;
q _lastActiveButton;
@"NSArray" _desiredButtons;
q _pressType;
```

## Properties

```
@property (Tq,N,V_pressType) pressType;
@property (Tq,N,V_lastActiveButton) lastActiveButton;
@property (T@"NSSet",C,N,V_activeButtons) activeButtons;
@property (T@"NSArray",C,N,V_desiredButtons) desiredButtons;
@property (TB,N,GisSuspended,V_suspended) suspended;
```

## Instance methods

```
-[CAMPhysicalCaptureRecognizer setSuspended:];
-[CAMPhysicalCaptureRecognizer isSuspended];
-[CAMPhysicalCaptureRecognizer pressesCancelled:withEvent:];
-[CAMPhysicalCaptureRecognizer pressesEnded:withEvent:];
-[CAMPhysicalCaptureRecognizer reset];
-[CAMPhysicalCaptureRecognizer touchesBegan:withEvent:];
-[CAMPhysicalCaptureRecognizer initWithTarget:action:];
-[CAMPhysicalCaptureRecognizer setPressType:];
-[CAMPhysicalCaptureRecognizer pressesBegan:withEvent:];
-[CAMPhysicalCaptureRecognizer setEnabled:];
-[CAMPhysicalCaptureRecognizer pressType];
-[CAMPhysicalCaptureRecognizer _captureButtonForPressType:];
-[CAMPhysicalCaptureRecognizer _updateApplicationButtonStatus];
-[CAMPhysicalCaptureRecognizer activeButtons];
-[CAMPhysicalCaptureRecognizer desiredButtons];
-[CAMPhysicalCaptureRecognizer lastActiveButton];
-[CAMPhysicalCaptureRecognizer setActiveButtons:];
-[CAMPhysicalCaptureRecognizer setDesiredButtons:];
-[CAMPhysicalCaptureRecognizer setLastActiveButton:];
```
