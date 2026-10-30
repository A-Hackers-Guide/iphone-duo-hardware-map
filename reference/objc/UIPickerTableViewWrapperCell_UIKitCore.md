# `UIPickerTableViewWrapperCell`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPickerTableViewCell`
- 4 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"UIView" _wrappedView;
@"UIView" _wrappedViewContainer;
{CGSize="width"d"height"d} _wrappedViewSize;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _wrappedViewInsets;
```

## Properties

```
@property (T@"UIView",&,N) wrappedView;
@property (T{UIEdgeInsets=dddd},N,V_wrappedViewInsets) wrappedViewInsets;
```

## Instance methods

```
-[UIPickerTableViewWrapperCell _anyDateLabel];
-[UIPickerTableViewWrapperCell _updateWrappedView];
-[UIPickerTableViewWrapperCell resizeSubviewsWithOldSize:];
-[UIPickerTableViewWrapperCell _setIsCenterCell:shouldModifyAlphaOfView:];
-[UIPickerTableViewWrapperCell setWrappedViewInsets:];
-[UIPickerTableViewWrapperCell wrappedView];
-[UIPickerTableViewWrapperCell setWrappedView:];
-[UIPickerTableViewWrapperCell prepareForReuse];
-[UIPickerTableViewWrapperCell wrappedViewInsets];
-[UIPickerTableViewWrapperCell _updateWrappedViewFrame];
-[UIPickerTableViewWrapperCell initWithStyle:reuseIdentifier:];
```
