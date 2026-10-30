# `_UIResponderChainFixerUpper`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _deliveryRecords;
@"NSMapTable" _currentDelivery;
```

## Properties

```
@property (T@"NSMapTable",R,N,V_deliveryRecords) deliveryRecords;
@property (T@"NSMapTable",&,N,V_currentDelivery) currentDelivery;
```

## Instance methods

```
-[_UIResponderChainFixerUpper recursiveDescription];
-[_UIResponderChainFixerUpper init];
-[_UIResponderChainFixerUpper description];
-[_UIResponderChainFixerUpper deliveryRecords];
-[_UIResponderChainFixerUpper _nextResponders];
-[_UIResponderChainFixerUpper currentDelivery];
-[_UIResponderChainFixerUpper _callResponder:phase:components:event:];
-[_UIResponderChainFixerUpper _deliverComponents:phase:forEvent:toResponder:];
-[_UIResponderChainFixerUpper _recordDeliveryOfComponents:toResponder:];
-[_UIResponderChainFixerUpper _recursiveDescription:];
-[_UIResponderChainFixerUpper _recursiveDescriptionStep:];
-[_UIResponderChainFixerUpper _removeDeliveryRecordForComponents:];
-[_UIResponderChainFixerUpper _snapshotDeliveryOfComponents:map:block:];
-[_UIResponderChainFixerUpper deliverPressesEvent:toResponder:];
-[_UIResponderChainFixerUpper deliverTouchesEvent:toResponder:];
-[_UIResponderChainFixerUpper forward:phase:withEvent:fromResponder:];
-[_UIResponderChainFixerUpper setCurrentDelivery:];
```
