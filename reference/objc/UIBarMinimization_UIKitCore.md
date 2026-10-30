# `UIBarMinimization`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`, `NSCoding`
- 2 instance variables, 5 properties, 13 instance methods, 1 class methods

## Instance variables

```
backing;
mutationHandler;
```

## Properties

```
@property (Tq,N) minimizationBehavior;
@property (Tq,N) safeAreaAdjustment;
@property (Tq,N) restorationBehavior;
@property (Tq,N,R) hash;
@property (T@"NSString",N,R) description;
```

## Class methods

```
+[UIBarMinimization supportsSecureCoding];
```

## Instance methods

```
-[UIBarMinimization init];
-[UIBarMinimization encodeWithCoder:];
-[UIBarMinimization hash];
-[UIBarMinimization description];
-[UIBarMinimization initWithCoder:];
-[UIBarMinimization copyWithZone:];
-[UIBarMinimization isEqual:];
-[UIBarMinimization minimizationBehavior];
-[UIBarMinimization restorationBehavior];
-[UIBarMinimization safeAreaAdjustment];
-[UIBarMinimization setMinimizationBehavior:];
-[UIBarMinimization setRestorationBehavior:];
-[UIBarMinimization setSafeAreaAdjustment:];
```
