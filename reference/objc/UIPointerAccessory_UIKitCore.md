# `UIPointerAccessory`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 10 instance methods, 2 class methods

## Instance variables

```
B _isArrowAccessory;
B _orientationMatchesAngle;
@"UIPointerShape" _shape;
{?="offset"d"angle"d} _position;
```

## Properties

```
@property (T@"UIPointerShape",C,N,V_shape) shape;
@property (T{?=dd},N,V_position) position;
@property (TB,R,N,V_isArrowAccessory) _isArrowAccessory;
@property (TB,N,V_orientationMatchesAngle) orientationMatchesAngle;
```

## Class methods

```
+[UIPointerAccessory accessoryWithShape:position:];
+[UIPointerAccessory arrowAccessoryWithPosition:];
```

## Instance methods

```
-[UIPointerAccessory setShape:];
-[UIPointerAccessory position];
-[UIPointerAccessory shape];
-[UIPointerAccessory hash];
-[UIPointerAccessory setPosition:];
-[UIPointerAccessory copyWithZone:];
-[UIPointerAccessory isEqual:];
-[UIPointerAccessory _isArrowAccessory];
-[UIPointerAccessory orientationMatchesAngle];
-[UIPointerAccessory setOrientationMatchesAngle:];
```
