# `_UIViewBackingObserver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
@? _observerBlock;
@"NSMutableSet" _additionalObservers;
```

## Properties

```
@property (T@?,C,N,V_observerBlock) observerBlock;
@property (T@"NSMutableSet",&,N,V_additionalObservers) additionalObservers;
```

## Class methods

```
+[_UIViewBackingObserver sharedObserver];
```

## Instance methods

```
-[_UIViewBackingObserver observeValueForKeyPath:ofObject:change:context:];
-[_UIViewBackingObserver additionalObservers];
-[_UIViewBackingObserver observe:forKeyPath:once:];
-[_UIViewBackingObserver additionalBlocks];
-[_UIViewBackingObserver observerBlock];
-[_UIViewBackingObserver setObserverBlock:];
-[_UIViewBackingObserver setAdditionalObservers:];
```
