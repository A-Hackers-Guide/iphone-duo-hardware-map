# `UIShape`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIShapeProvider`, `NSCopying`
- 1 instance variables, 2 properties, 12 instance methods, 12 class methods

## Instance variables

```
value;
```

## Properties

```
@property (T@"NSString",N,R) description;
@property (T@"NSString",N,R) debugDescription;
```

## Class methods

```
+[UIShape shapeWithProvider:];
+[UIShape shapeWithBezierPath:];
+[UIShape _contentShape];
+[UIShape capsuleShape];
+[UIShape circleShape];
+[UIShape fixedRectShapeWithRect:];
+[UIShape fixedRectShapeWithRect:cornerRadius:];
+[UIShape fixedRectShapeWithRect:cornerRadius:cornerCurve:maskedCorners:];
+[UIShape rectShape];
+[UIShape rectShapeWithCornerRadius:];
+[UIShape rectShapeWithCornerRadius:cornerCurve:];
+[UIShape rectShapeWithCornerRadius:cornerCurve:maskedCorners:];
```

## Instance methods

```
-[UIShape resolvedShapeInContext:];
-[UIShape debugDescription];
-[UIShape init];
-[UIShape _resolvedShapeInRect:];
-[UIShape shapeWithProvider:];
-[UIShape _resolvedShapeInView:];
-[UIShape description];
-[UIShape copyWithZone:];
-[UIShape isEqual:];
-[UIShape shapeByApplyingInset:];
-[UIShape shapeByApplyingInsets:];
-[UIShape shapeWithBezierPath:];
```
