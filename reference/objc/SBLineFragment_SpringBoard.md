# `SBLineFragment`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
Q _index;
d _lineWidth;
{_NSRange="location"Q"length"Q} _range;
```

## Properties

```
@property (TQ,N,V_index) index;
@property (T{_NSRange=QQ},N,V_range) range;
@property (Td,N,V_lineWidth) lineWidth;
```

## Class methods

```
+[SBLineFragment fragmentWithIndex:length:lineWidth:];
```

## Instance methods

```
-[SBLineFragment lineWidth];
-[SBLineFragment setLineWidth:];
-[SBLineFragment range];
-[SBLineFragment index];
-[SBLineFragment setRange:];
-[SBLineFragment setIndex:];
-[SBLineFragment description];
```
