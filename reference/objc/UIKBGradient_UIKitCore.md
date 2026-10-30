# `UIKBGradient`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 10 instance variables, 4 properties, 15 instance methods, 5 class methods

## Instance variables

```
@"NSString" _gradientName;
@"NSString" _flatColorName;
@"NSString" _startColorName;
@"NSString" _endColorName;
@"NSArray" _colors;
@"NSArray" _middleLocations;
d _opacity;
B _horizontal;
B _usesRGBColors;
B _didQueryRGBColors;
```

## Properties

```
@property (Td,N,V_opacity) opacity;
@property (TB,N,V_horizontal) horizontal;
@property (TB,R,N) usesRGBColors;
@property (T@"NSString",R,N) flatColorName;
```

## Class methods

```
+[UIKBGradient gradientWith3Colors:middleLocation:];
+[UIKBGradient gradientWithColors:middleLocations:];
+[UIKBGradient gradientWithFlatColor:];
+[UIKBGradient gradientWithName:];
+[UIKBGradient gradientWithStartColor:endColor:];
```

## Instance methods

```
-[UIKBGradient initWithFlatColor:];
-[UIKBGradient flatColorName];
-[UIKBGradient usesRGBColors];
-[UIKBGradient opacity];
-[UIKBGradient setHorizontal:];
-[UIKBGradient setOpacity:];
-[UIKBGradient initWithColors:middleLocations:];
-[UIKBGradient description];
-[UIKBGradient copyWithZone:];
-[UIKBGradient initWith3Colors:middleLocation:];
-[UIKBGradient CGGradient];
-[UIKBGradient initWithStartColor:endColor:];
-[UIKBGradient isEqual:];
-[UIKBGradient horizontal];
-[UIKBGradient initWithName:];
```
