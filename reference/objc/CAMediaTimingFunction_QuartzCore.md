# `CAMediaTimingFunction`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 0 properties, 13 instance methods, 4 class methods

## Instance variables

```
^{CAMediaTimingFunctionPrivate=[2f][2f]} _priv;
```

## Class methods

```
+[CAMediaTimingFunction supportsSecureCoding];
+[CAMediaTimingFunction CAMLParserEndElement:content:];
+[CAMediaTimingFunction functionWithControlPoints::::];
+[CAMediaTimingFunction functionWithName:];
```

## Instance methods

```
-[CAMediaTimingFunction _getPoints:];
-[CAMediaTimingFunction dealloc];
-[CAMediaTimingFunction _solveForInput:];
-[CAMediaTimingFunction CA_copyRenderValue];
-[CAMediaTimingFunction CA_copyNumericValue:];
-[CAMediaTimingFunction encodeWithCAMLWriter:];
-[CAMediaTimingFunction encodeWithCoder:];
-[CAMediaTimingFunction description];
-[CAMediaTimingFunction initWithCoder:];
-[CAMediaTimingFunction CA_numericValueCount];
-[CAMediaTimingFunction CAMLType];
-[CAMediaTimingFunction getControlPointAtIndex:values:];
-[CAMediaTimingFunction initWithControlPoints::::];
```
