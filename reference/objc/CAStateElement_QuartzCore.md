# `CAStateElement`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 3 properties, 18 instance methods, 2 class methods

## Instance variables

```
@"CALayer" _target;
@"CAStateElement" _source;
```

## Properties

```
@property (T@"CALayer",W,N,V_target) target;
@property (T@"CAStateElement",&,N,V_source) source;
@property (T@"NSString",R,C,N) keyPath;
```

## Class methods

```
+[CAStateElement supportsSecureCoding];
+[CAStateElement CAMLParserStartElement:];
```

## Instance methods

```
-[CAStateElement save];
-[CAStateElement keyPath];
-[CAStateElement CAMLTypeForKey:];
-[CAStateElement CAMLParser:setValue:forKey:];
-[CAStateElement dealloc];
-[CAStateElement matches:];
-[CAStateElement setSource:];
-[CAStateElement apply:];
-[CAStateElement encodeWithCAMLWriter:];
-[CAStateElement setTarget:];
-[CAStateElement CAMLTypeSupportedForKey:];
-[CAStateElement encodeWithCoder:];
-[CAStateElement initWithCoder:];
-[CAStateElement foreachLayer:];
-[CAStateElement target];
-[CAStateElement copyWithZone:];
-[CAStateElement source];
-[CAStateElement targetName];
```
