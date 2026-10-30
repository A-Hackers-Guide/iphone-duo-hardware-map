# `_UIColorPickerColorQueue`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<_UIColorPickerColorQueueDelegate>" _delegate;
@"UIUpdateLink" _updateLink;
@"_UIColorPickerColorQueueContainer" _latestObject;
```

## Properties

```
@property (T@"UIUpdateLink",&,N,V_updateLink) updateLink;
@property (T@"_UIColorPickerColorQueueContainer",&,N,V_latestObject) latestObject;
@property (T@"<_UIColorPickerColorQueueDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[_UIColorPickerColorQueue initWithView:];
-[_UIColorPickerColorQueue setUpdateLink:];
-[_UIColorPickerColorQueue setDelegate:];
-[_UIColorPickerColorQueue delegate];
-[_UIColorPickerColorQueue updateLink];
-[_UIColorPickerColorQueue _forwardToDelegate:];
-[_UIColorPickerColorQueue _pickerDidSelectColor:colorSpace:isVolatile:];
-[_UIColorPickerColorQueue _updateLinkFired];
-[_UIColorPickerColorQueue latestObject];
-[_UIColorPickerColorQueue setLatestObject:];
```
