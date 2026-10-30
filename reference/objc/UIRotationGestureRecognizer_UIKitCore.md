# `UIRotationGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 1 instance variables, 2 properties, 11 instance methods, 3 class methods

## Instance variables

```
@"_UIRotationGestureRecognizerDriver" _driver;
```

## Properties

```
@property (Td,N) rotation;
@property (Td,R,N) velocity;
```

## Class methods

```
+[UIRotationGestureRecognizer supportsSecureCoding];
+[UIRotationGestureRecognizer _supportsDefaultTouchTypes];
+[UIRotationGestureRecognizer _supportsDefaultPressTypes];
```

## Instance methods

```
-[UIRotationGestureRecognizer _preRecognitionWeight];
-[UIRotationGestureRecognizer rotation];
-[UIRotationGestureRecognizer _setPostRecognitionWeight:];
-[UIRotationGestureRecognizer anchorPoint];
-[UIRotationGestureRecognizer _driver];
-[UIRotationGestureRecognizer _isGestureType:];
-[UIRotationGestureRecognizer _postRecognitionWeight];
-[UIRotationGestureRecognizer velocity];
-[UIRotationGestureRecognizer locationInView:];
-[UIRotationGestureRecognizer setRotation:];
-[UIRotationGestureRecognizer _setPreRecognitionWeight:];
```
