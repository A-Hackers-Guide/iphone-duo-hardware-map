# `_UIAbstractBSXPCCodingAdapter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`
- 1 instance variables, 5 properties, 6 instance methods, 2 class methods

## Instance variables

```
@ _object;
```

## Properties

```
@property (T@,R,N,V_object) object;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIAbstractBSXPCCodingAdapter supportsBSXPCSecureCoding];
+[_UIAbstractBSXPCCodingAdapter adapterWithObject:];
```

## Instance methods

```
-[_UIAbstractBSXPCCodingAdapter initWithObject:];
-[_UIAbstractBSXPCCodingAdapter encodeWithBSXPCCoder:];
-[_UIAbstractBSXPCCodingAdapter initWithBSXPCCoder:];
-[_UIAbstractBSXPCCodingAdapter object];
-[_UIAbstractBSXPCCodingAdapter initWithBSXPCCoder:clazz:];
-[_UIAbstractBSXPCCodingAdapter initWithBSXPCCoder:collectionOfClass:containingClass:];
```
