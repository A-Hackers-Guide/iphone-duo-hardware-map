# `CAValueFunction`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 1 properties, 11 instance methods, 3 class methods

## Instance variables

```
@"NSString" _string;
^v _impl;
```

## Properties

```
@property (T@"NSString",R) name;
```

## Class methods

```
+[CAValueFunction supportsSecureCoding];
+[CAValueFunction CAMLParserStartElement:];
+[CAValueFunction functionWithName:];
```

## Instance methods

```
-[CAValueFunction _initWithName:];
-[CAValueFunction dealloc];
-[CAValueFunction CA_copyRenderValue];
-[CAValueFunction encodeWithCAMLWriter:];
-[CAValueFunction encodeWithCoder:];
-[CAValueFunction initWithCoder:];
-[CAValueFunction inputCount];
-[CAValueFunction name];
-[CAValueFunction apply:result:];
-[CAValueFunction apply:result:parameterFunction:context:];
-[CAValueFunction outputCount];
```
