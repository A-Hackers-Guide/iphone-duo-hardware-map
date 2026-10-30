# `MLKey`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
@"NSString" _scope;
```

## Properties

```
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSString",R,N,V_scope) scope;
```

## Class methods

```
+[MLKey supportsSecureCoding];
```

## Instance methods

```
-[MLKey scope];
-[MLKey initWithKeyName:];
-[MLKey encodeWithCoder:];
-[MLKey hash];
-[MLKey description];
-[MLKey initWithCoder:];
-[MLKey copyWithZone:];
-[MLKey isEqual:];
-[MLKey name];
-[MLKey deletingPrefixingScope:];
-[MLKey hasGlobalScope];
-[MLKey hasSameNameAsKey:];
-[MLKey initWithKeyName:scope:];
-[MLKey scopedTo:];
```
