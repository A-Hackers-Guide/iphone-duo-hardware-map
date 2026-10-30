# `_UITransformGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `_UITransformEventRespondable`
- 4 instance variables, 8 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"_UIPinchGestureRecognizerDriver" _pinchDriver;
@"_UIRotationGestureRecognizerDriver" _rotationDriver;
@"_UIGestureRecognizerDriver" _composedDriver;
{CGPoint="x"d"y"d} _eventTranslation;
```

## Properties

```
@property (Td,R,N) scale;
@property (Td,R,N) rotation;
@property (T{CGPoint=dd},R,N) translation;
@property (T{CGAffineTransform=dddddd},R,N) transform;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITransformGestureRecognizer translationInView:];
-[_UITransformGestureRecognizer transformInView:];
-[_UITransformGestureRecognizer rotation];
-[_UITransformGestureRecognizer _transformChangedWithEvent:];
-[_UITransformGestureRecognizer _driver];
-[_UITransformGestureRecognizer _isGestureType:];
-[_UITransformGestureRecognizer reset];
-[_UITransformGestureRecognizer transform];
-[_UITransformGestureRecognizer locationInView:];
-[_UITransformGestureRecognizer scale];
-[_UITransformGestureRecognizer _stateUpdatedForDriver:previousState:];
-[_UITransformGestureRecognizer translation];
```
