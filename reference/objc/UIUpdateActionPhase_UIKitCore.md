# `UIUpdateActionPhase`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 0 instance methods, 12 class methods

## Instance variables

```
i _order;
^{_UIUpdateSequenceItemInternal=} _item;
```

## Class methods

```
+[UIUpdateActionPhase afterUpdateComplete];
+[UIUpdateActionPhase afterEventDispatch];
+[UIUpdateActionPhase afterCADisplayLinkDispatch];
+[UIUpdateActionPhase beforeLowLatencyCATransactionCommit];
+[UIUpdateActionPhase afterUpdateScheduled];
+[UIUpdateActionPhase beforeLowLatencyEventDispatch];
+[UIUpdateActionPhase afterLowLatencyCATransactionCommit];
+[UIUpdateActionPhase beforeCADisplayLinkDispatch];
+[UIUpdateActionPhase beforeCATransactionCommit];
+[UIUpdateActionPhase afterCATransactionCommit];
+[UIUpdateActionPhase beforeEventDispatch];
+[UIUpdateActionPhase afterLowLatencyEventDispatch];
```
