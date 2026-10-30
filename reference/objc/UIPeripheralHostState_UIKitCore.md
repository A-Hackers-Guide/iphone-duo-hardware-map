# `UIPeripheralHostState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
{UIPeripheralAnimationGeometry="outPosition"{CGPoint="x"d"y"d}"inPosition"{CGPoint="x"d"y"d}"bounds"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"transform"{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d}"targetFrameHeightDelta"d} _geometry;
@"NSDictionary" _screenGeometry;
B _inPositionIsDestination;
```

## Properties

```
@property (T{UIPeripheralAnimationGeometry={CGPoint=dd}{CGPoint=dd}{CGRect={CGPoint=dd}{CGSize=dd}}{CGAffineTransform=dddddd}d},N,V_geometry) geometry;
@property (T@"NSDictionary",&,N,V_screenGeometry) screenGeometry;
@property (TB,N,V_inPositionIsDestination) inPositionIsDestination;
```

## Class methods

```
+[UIPeripheralHostState stateWithGeometry:inPositionIsDestination:];
```

## Instance methods

```
-[UIPeripheralHostState dealloc];
-[UIPeripheralHostState geometry];
-[UIPeripheralHostState setGeometry:];
-[UIPeripheralHostState inPositionIsDestination];
-[UIPeripheralHostState screenGeometry];
-[UIPeripheralHostState setInPositionIsDestination:];
-[UIPeripheralHostState setScreenGeometry:];
```
