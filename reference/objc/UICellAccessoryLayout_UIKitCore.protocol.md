# `UICellAccessoryLayout` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"UICellAccessoryManager",W,N) manager;
@property (Td,N) safeAreaInset;
@property (TQ,N) edge;
@property (T@?,C,N) standardLayoutWidthProvider;
@property (T@?,C,N) disclosureLayoutWidthProvider;
```

## Instance methods

```
-[UICellAccessoryLayout setEdge:];
-[UICellAccessoryLayout edge];
-[UICellAccessoryLayout setManager:];
-[UICellAccessoryLayout setDisclosureLayoutWidthProvider:];
-[UICellAccessoryLayout prepareLayoutForAccessories:previousAccessories:configurationIdentifier:animated:];
-[UICellAccessoryLayout endLayout];
-[UICellAccessoryLayout initialFrameForAccessory:];
-[UICellAccessoryLayout manager];
-[UICellAccessoryLayout finalFrameForAccessory:];
-[UICellAccessoryLayout initialAlphaForAccessory:];
-[UICellAccessoryLayout setStandardLayoutWidthProvider:];
-[UICellAccessoryLayout finalAlphaForAccessory:];
-[UICellAccessoryLayout disclosureLayoutWidthProvider];
-[UICellAccessoryLayout setSafeAreaInset:];
-[UICellAccessoryLayout standardLayoutWidthProvider];
-[UICellAccessoryLayout safeAreaInset];
```
