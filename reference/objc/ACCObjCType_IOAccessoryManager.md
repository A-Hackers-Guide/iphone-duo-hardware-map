# `ACCObjCType`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`](../userland/System__Library__CoreAccessories__PlugIns__Transports__IOAccessoryManager.transport__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
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
+[ACCObjCType typeForValue:];
+[ACCObjCType typeForEncoding:];
```

## Instance methods

```
-[ACCObjCType className];
-[ACCObjCType encoding];
-[ACCObjCType flags];
-[ACCObjCType code];
-[ACCObjCType isObject];
-[ACCObjCType isNumber];
-[ACCObjCType size];
-[ACCObjCType name];
-[ACCObjCType isIntegerNumber];
-[ACCObjCType getBytes:forObject:];
-[ACCObjCType initWithCode:encoding:name:className:size:flags:];
-[ACCObjCType isFloatingPointNumber];
-[ACCObjCType objectWithBytes:];
```
