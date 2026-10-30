# `_UIFocusLinearMovementSequence`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 2 class methods

## Instance variables

```
B _looping;
B _restrictEnteringSequence;
@"NSArray" _items;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_items) items;
@property (TB,R,N,GisLooping,V_looping) looping;
@property (TB,R,N,GrestrictsEnteringSequence,V_restrictEnteringSequence) restrictEnteringSequence;
```

## Class methods

```
+[_UIFocusLinearMovementSequence sequenceWithItems:loops:];
+[_UIFocusLinearMovementSequence sequenceWithItems:loops:restrictEnteringSequence:];
```

## Instance methods

```
-[_UIFocusLinearMovementSequence init];
-[_UIFocusLinearMovementSequence items];
-[_UIFocusLinearMovementSequence isLooping];
-[_UIFocusLinearMovementSequence initWithItems:loops:];
-[_UIFocusLinearMovementSequence initWithItems:loops:restrictEnteringSequence:];
-[_UIFocusLinearMovementSequence restrictsEnteringSequence];
```
