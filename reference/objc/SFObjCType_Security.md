# `SFObjCType`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 10 properties, 13 instance methods, 2 class methods

## Instance variables

```
q _code;
@"NSString" _encoding;
@"NSString" _name;
@"NSString" _className;
Q _size;
Q _flags;
```

## Properties

```
@property (Tq,R,N,V_code) code;
@property (T@"NSString",R,N,V_encoding) encoding;
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSString",R,N,V_className) className;
@property (TQ,R,N,V_size) size;
@property (TQ,R,N,V_flags) flags;
@property (TB,R,N,GisNumber) number;
@property (TB,R,N,GisIntegerNumber) integerNumber;
@property (TB,R,N,GisFloatingPointNumber) floatingPointNumber;
@property (TB,R,N,GisObject) object;
```

## Class methods

```
+[SFObjCType typeForValue:];
+[SFObjCType typeForEncoding:];
```

## Instance methods

```
-[SFObjCType className];
-[SFObjCType encoding];
-[SFObjCType flags];
-[SFObjCType code];
-[SFObjCType isObject];
-[SFObjCType isNumber];
-[SFObjCType size];
-[SFObjCType name];
-[SFObjCType isIntegerNumber];
-[SFObjCType getBytes:forObject:];
-[SFObjCType initWithCode:encoding:name:className:size:flags:];
-[SFObjCType isFloatingPointNumber];
-[SFObjCType objectWithBytes:];
```
