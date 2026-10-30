# `LACMechanismTree`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 10 instance methods, 2 class methods

## Instance variables

```
? children;
B isAnd;
q value;
```

## Properties

```
@property (T@"NSArray",N,R) children;
@property (TB,N,R,VisAnd) isAnd;
@property (Tq,N,R,Vvalue) value;
@property (T@"NSString",N,R) description;
```

## Class methods

```
+[LACMechanismTree mechanismTreeFromError:];
+[LACMechanismTree mechanismTreeFromSerializedTree:];
```

## Instance methods

```
-[LACMechanismTree init];
-[LACMechanismTree value];
-[LACMechanismTree initWithValue:];
-[LACMechanismTree children];
-[LACMechanismTree description];
-[LACMechanismTree initWithChildren:isAndNode:];
-[LACMechanismTree isAnd];
-[LACMechanismTree isSatisfiableWithValue:];
-[LACMechanismTree isValue:replaceableByValue:];
-[LACMechanismTree isValueRequired:];
```
