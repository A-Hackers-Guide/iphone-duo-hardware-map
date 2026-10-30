# `UIDebuggingIvar`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 8 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
@"NSString" _typeDescription;
@ _value;
@"NSObject" _object;
^{objc_ivar=} _objcIvar;
r* _typeEncoding;
```

## Properties

```
@property (T@"NSObject",N,V_object) object;
@property (T^{objc_ivar=},N,V_objcIvar) objcIvar;
@property (T@"NSString",C,N,V_name) name;
@property (T@"NSString",C,N,V_typeDescription) typeDescription;
@property (Tr*,N,V_typeEncoding) typeEncoding;
@property (T@,N,V_value) value;
@property (T@"NSString",R,N) valueDescription;
@property (TB,R,N) isObject;
```

## Class methods

```
+[UIDebuggingIvar ivarWithObjcIvar:forObject:];
```

## Instance methods

```
-[UIDebuggingIvar dealloc];
-[UIDebuggingIvar value];
-[UIDebuggingIvar setObject:];
-[UIDebuggingIvar isObject];
-[UIDebuggingIvar setValue:];
-[UIDebuggingIvar typeDescription];
-[UIDebuggingIvar setName:];
-[UIDebuggingIvar object];
-[UIDebuggingIvar name];
-[UIDebuggingIvar objcIvar];
-[UIDebuggingIvar setObjcIvar:];
-[UIDebuggingIvar setTypeDescription:];
-[UIDebuggingIvar setTypeEncoding:];
-[UIDebuggingIvar typeEncoding];
-[UIDebuggingIvar valueDescription];
```
