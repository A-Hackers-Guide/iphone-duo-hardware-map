# `_UIFocusSearchInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _treatFocusableItemAsLeaf;
B _forceFocusToLeaveContainer;
@? _evaluator;
```

## Properties

```
@property (T@?,C,N,V_evaluator) evaluator;
@property (TB,N,V_treatFocusableItemAsLeaf) treatFocusableItemAsLeaf;
@property (TB,N,V_forceFocusToLeaveContainer) forceFocusToLeaveContainer;
```

## Class methods

```
+[_UIFocusSearchInfo defaultInfo];
```

## Instance methods

```
-[_UIFocusSearchInfo evaluator];
-[_UIFocusSearchInfo forceFocusToLeaveContainer];
-[_UIFocusSearchInfo initWithFocusEvaluator:];
-[_UIFocusSearchInfo setEvaluator:];
-[_UIFocusSearchInfo setForceFocusToLeaveContainer:];
-[_UIFocusSearchInfo setTreatFocusableItemAsLeaf:];
-[_UIFocusSearchInfo shouldIncludeFocusItem:];
-[_UIFocusSearchInfo treatFocusableItemAsLeaf];
```
