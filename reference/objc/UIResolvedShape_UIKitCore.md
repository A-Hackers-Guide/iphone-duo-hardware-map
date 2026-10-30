# `UIResolvedShape`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
value;
cachedShape;
```

## Properties

```
@property (T@"UIBezierPath",N,R) path;
@property (T@"UIShape",N,R) shape;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,R) boundingRect;
@property (T@"NSString",N,R) description;
@property (T@"NSString",N,R) debugDescription;
```

## Instance methods

```
-[UIResolvedShape boundingRect];
-[UIResolvedShape debugDescription];
-[UIResolvedShape shape];
-[UIResolvedShape init];
-[UIResolvedShape description];
-[UIResolvedShape copyWithZone:];
-[UIResolvedShape shapeByApplyingInset:];
-[UIResolvedShape shapeByApplyingInsets:];
-[UIResolvedShape path];
-[UIResolvedShape _shapeByClippingToShape:];
-[UIResolvedShape _shapeByConvertingFromSpace:toSpace:];
```
