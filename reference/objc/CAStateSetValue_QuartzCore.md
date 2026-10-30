# `CAStateSetValue`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAStateElement`
- 2 instance variables, 2 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSString" _keyPath;
@ _value;
```

## Properties

```
@property (T@"NSString",C,N,V_keyPath) keyPath;
@property (T@,&,N) value;
```

## Class methods

```
+[CAStateSetValue supportsSecureCoding];
```

## Instance methods

```
-[CAStateSetValue keyPath];
-[CAStateSetValue setKeyPath:];
-[CAStateSetValue CAMLTypeForKey:];
-[CAStateSetValue debugDescription];
-[CAStateSetValue dealloc];
-[CAStateSetValue value];
-[CAStateSetValue matches:];
-[CAStateSetValue apply:];
-[CAStateSetValue setValue:];
-[CAStateSetValue encodeWithCAMLWriter:];
-[CAStateSetValue CAMLTypeSupportedForKey:];
-[CAStateSetValue encodeWithCoder:];
-[CAStateSetValue initWithCoder:];
-[CAStateSetValue foreachLayer:];
-[CAStateSetValue copyWithZone:];
```
