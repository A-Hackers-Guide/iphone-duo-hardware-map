# `_UIFloatingMotionConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 2 properties, 6 instance methods, 5 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _rotation;
{CGPoint="x"d"y"d} _translation;
```

## Properties

```
@property (T{CGPoint=dd},R,N,V_rotation) rotation;
@property (T{CGPoint=dd},R,N,V_translation) translation;
```

## Class methods

```
+[_UIFloatingMotionConfiguration configurationWithLargeTranslationOnAxis:];
+[_UIFloatingMotionConfiguration configurationWithRotation:];
+[_UIFloatingMotionConfiguration configurationWithRotationOnAxis:];
+[_UIFloatingMotionConfiguration configurationWithTranslation:];
+[_UIFloatingMotionConfiguration configurationWithTranslationOnAxis:];
```

## Instance methods

```
-[_UIFloatingMotionConfiguration rotation];
-[_UIFloatingMotionConfiguration hash];
-[_UIFloatingMotionConfiguration copyWithZone:];
-[_UIFloatingMotionConfiguration isEqual:];
-[_UIFloatingMotionConfiguration translation];
-[_UIFloatingMotionConfiguration _initWithTranslation:rotation:];
```
