# `UIKBKeyplaneChangeContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 17 instance methods, 2 class methods

## Instance variables

```
B _sizeDidChange;
B _splitWidthsChanged;
B _selfSizingChanged;
B _updateAssistantView;
B _isSecureTextEntry;
B _isDynamicLayout;
B _updatePlacementOnly;
@"UIInputViewSetPlacement" _targetPlacement;
{CGSize="width"d"height"d} _size;
```

## Properties

```
@property (T{CGSize=dd},N,V_size) size;
@property (TB,R,N,V_sizeDidChange) sizeDidChange;
@property (TB,N,V_splitWidthsChanged) splitWidthsChanged;
@property (TB,N,V_selfSizingChanged) selfSizingChanged;
@property (TB,N,V_updateAssistantView) updateAssistantView;
@property (TB,N,V_isSecureTextEntry) isSecureTextEntry;
@property (TB,N,V_isDynamicLayout) isDynamicLayout;
@property (TB,N,V_updatePlacementOnly) updatePlacementOnly;
@property (T@"UIInputViewSetPlacement",&,N,V_targetPlacement) targetPlacement;
```

## Class methods

```
+[UIKBKeyplaneChangeContext keyplaneChangeContext];
+[UIKBKeyplaneChangeContext keyplaneChangeContextWithSize:];
```

## Instance methods

```
-[UIKBKeyplaneChangeContext updateAssistantView];
-[UIKBKeyplaneChangeContext isDynamicLayout];
-[UIKBKeyplaneChangeContext setTargetPlacement:];
-[UIKBKeyplaneChangeContext targetPlacement];
-[UIKBKeyplaneChangeContext setIsDynamicLayout:];
-[UIKBKeyplaneChangeContext updatePlacementOnly];
-[UIKBKeyplaneChangeContext sizeDidChange];
-[UIKBKeyplaneChangeContext size];
-[UIKBKeyplaneChangeContext setUpdatePlacementOnly:];
-[UIKBKeyplaneChangeContext setSelfSizingChanged:];
-[UIKBKeyplaneChangeContext setUpdateAssistantView:];
-[UIKBKeyplaneChangeContext setSplitWidthsChanged:];
-[UIKBKeyplaneChangeContext splitWidthsChanged];
-[UIKBKeyplaneChangeContext isSecureTextEntry];
-[UIKBKeyplaneChangeContext setIsSecureTextEntry:];
-[UIKBKeyplaneChangeContext setSize:];
-[UIKBKeyplaneChangeContext selfSizingChanged];
```
