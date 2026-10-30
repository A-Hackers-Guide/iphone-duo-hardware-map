# `PFBezierMapping`

- Image: [`/System/Library/PrivateFrameworks/PencilFeedback.framework/PencilFeedback`](../userland/System__Library__PrivateFrameworks__PencilFeedback.framework__PencilFeedback.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _controlPoint1;
{CGPoint="x"d"y"d} _controlPoint2;
{CGPoint="x"d"y"d} _controlPoint3;
```

## Properties

```
@property (T{CGPoint=dd},N,V_controlPoint1) controlPoint1;
@property (T{CGPoint=dd},N,V_controlPoint2) controlPoint2;
@property (T{CGPoint=dd},N,V_controlPoint3) controlPoint3;
```

## Instance methods

```
-[PFBezierMapping controlPoint2];
-[PFBezierMapping controlPoint1];
-[PFBezierMapping map:];
-[PFBezierMapping setControlPoint1:];
-[PFBezierMapping setControlPoint2:];
-[PFBezierMapping controlPoint3];
-[PFBezierMapping initWithControlPoint1:controlPoint2:controlPoint3:];
-[PFBezierMapping quarticBezierWithT:a:b:c:d:e:];
-[PFBezierMapping setControlPoint3:];
-[PFBezierMapping solveTForX:];
```
