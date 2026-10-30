# `_UIResponderIntegrityProtection`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _deliveryStack;
@"NSMapTable" _pressBeganRecords;
```

## Class methods

```
+[_UIResponderIntegrityProtection rip];
```

## Instance methods

```
-[_UIResponderIntegrityProtection init];
-[_UIResponderIntegrityProtection finishedDeliveringPresses];
-[_UIResponderIntegrityProtection responder:class:receivedPresses:inPhase:withEvent:];
-[_UIResponderIntegrityProtection startDeliveringPresses:inPhase:withEvent:];
```
