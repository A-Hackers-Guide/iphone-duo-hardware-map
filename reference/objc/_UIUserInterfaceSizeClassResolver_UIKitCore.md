# `_UIUserInterfaceSizeClassResolver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`
- 1 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
resolution;
```

## Properties

```
@property (Tq,N,R) hash;
@property (T@"NSString",N,R) description;
```

## Class methods

```
+[_UIUserInterfaceSizeClassResolver supportsBSXPCSecureCoding];
```

## Instance methods

```
-[_UIUserInterfaceSizeClassResolver init];
-[_UIUserInterfaceSizeClassResolver initWithCompactUserInterfaceSizeClassThreshold:];
-[_UIUserInterfaceSizeClassResolver initWithFixedUserInterfaceSizeClass:];
-[_UIUserInterfaceSizeClassResolver hash];
-[_UIUserInterfaceSizeClassResolver description];
-[_UIUserInterfaceSizeClassResolver encodeWithBSXPCCoder:];
-[_UIUserInterfaceSizeClassResolver initWithRegularUserInterfaceSizeClassThreshold:];
-[_UIUserInterfaceSizeClassResolver initWithBSXPCCoder:];
-[_UIUserInterfaceSizeClassResolver isEqual:];
-[_UIUserInterfaceSizeClassResolver userInterfaceSizeClassForDimension:];
```
