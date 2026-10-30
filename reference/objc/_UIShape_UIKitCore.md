# `_UIShape`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 11 properties, 15 instance methods, 4 class methods

## Instance variables

```
@"UIBezierPath" _path;
d _cornerRadius;
@"NSString" _cornerCurve;
Q _cornerMask;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rect;
{CACornerRadii="minXMaxY"{CGSize="width"d"height"d}"maxXMaxY"{CGSize="width"d"height"d}"maxXMinY"{CGSize="width"d"height"d}"minXMinY"{CGSize="width"d"height"d}} _cornerRadii;
```

## Properties

```
@property (T@"UIBezierPath",R,N,V_path) path;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_rect) rect;
@property (Td,R,N,V_cornerRadius) cornerRadius;
@property (T@"NSString",R,N,V_cornerCurve) cornerCurve;
@property (TQ,R,N,V_cornerMask) cornerMask;
@property (T{CACornerRadii={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}},R,N,V_cornerRadii) cornerRadii;
@property (T{CGSize=dd},R,N) size;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (TB,R,N) isRect;
@property (T@"UIBezierPath",R,N) outline;
@property (T@"_UIShape",R,N) zeroOriginShape;
```

## Class methods

```
+[_UIShape shapeWithPath:];
+[_UIShape shapeWithRoundedRect:cornerRadii:cornerCurve:];
+[_UIShape shapeWithRoundedRect:cornerRadius:cornerCurve:];
+[_UIShape shapeWithRoundedRect:cornerRadius:cornerCurve:cornerMask:];
```

## Instance methods

```
-[_UIShape cornerRadii];
-[_UIShape size];
-[_UIShape zeroOriginShape];
-[_UIShape rect];
-[_UIShape cornerRadius];
-[_UIShape bounds];
-[_UIShape description];
-[_UIShape copyWithZone:];
-[_UIShape cornerCurve];
-[_UIShape isEqual:];
-[_UIShape cornerMask];
-[_UIShape outline];
-[_UIShape isRect];
-[_UIShape shapeConvertedFromCoordinateSpace:toCoordinateSpace:];
-[_UIShape path];
```
