# `_UISimpleFenceProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIFenceProviding`
- 2 instance variables, 4 properties, 5 instance methods, 1 class methods

## Instance variables

```
B _trackingAny;
B _synchronizing;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISimpleFenceProvider sharedInstance];
```

## Instance methods

```
-[_UISimpleFenceProvider init];
-[_UISimpleFenceProvider synchronizeSystemAnimationFencesWithCleanUpBlock:];
-[_UISimpleFenceProvider isTrackingAnySystemAnimationFence];
-[_UISimpleFenceProvider requestSystemAnimationFence];
-[_UISimpleFenceProvider trackSystemAnimationFence:];
```
