# `_UISlotView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 8 instance variables, 3 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSString" _localization;
@? _slotStyleResolver;
@? _slotAnyContentProvider;
@"<_UISlotViewContentDelegate>" _contentDelegate;
@"UISSlotStyle" _currentSlotStyle;
{CGSize="width"d"height"d} _intrinsicContentSize;
@"<UISSlotAnyContent>" _slotContent;
Q _currentGeneration;
```

## Properties

```
@property (T@?,C,N,S_setSlotAnyContentProvider:) _slotAnyContentProvider;
@property (T@?,C,N,S_setSlotStyleResolver:) _slotStyleResolver;
@property (T@"<_UISlotViewContentDelegate>",W,N,S_setContentDelegate:) _contentDelegate;
```

## Class methods

```
+[_UISlotView accessInstanceVariablesDirectly];
```

## Instance methods

```
-[_UISlotView intrinsicContentSize];
-[_UISlotView displayLayer:];
-[_UISlotView _contentDelegate];
-[_UISlotView init];
-[_UISlotView _updateContent];
-[_UISlotView _setSlotAnyContentProvider:];
-[_UISlotView dealloc];
-[_UISlotView tintColorDidChange];
-[_UISlotView _setSlotStyleResolver:];
-[_UISlotView _slotStyleDidChange:];
-[_UISlotView traitCollectionDidChange:];
-[_UISlotView _slotStyleResolver];
-[_UISlotView _slotAnyContentProvider];
-[_UISlotView _setContentDelegate:];
-[_UISlotView _overlayView:centerInView:];
```
