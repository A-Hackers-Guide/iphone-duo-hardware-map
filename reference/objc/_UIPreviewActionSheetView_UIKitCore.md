# `_UIPreviewActionSheetView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIGestureRecognizerDelegate`, `UIScrollViewDelegate`
- 6 instance variables, 10 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"<_UIPreviewActionSheetViewDelegate>" _delegate;
@? _completionHandler;
@"NSArray" _actions;
@"NSString" _title;
@"UILongPressGestureRecognizer" _captureTouchesRecognizer;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _contentInsets;
```

## Properties

```
@property (T@"NSArray",&,N,V_actions) actions;
@property (T@"NSString",&,N,V_title) title;
@property (T@"UILongPressGestureRecognizer",&,N,V_captureTouchesRecognizer) captureTouchesRecognizer;
@property (T{UIEdgeInsets=dddd},N,V_contentInsets) contentInsets;
@property (T@"<_UIPreviewActionSheetViewDelegate>",W,N,V_delegate) delegate;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPreviewActionSheetView setCompletionHandler:];
-[_UIPreviewActionSheetView completionHandler];
-[_UIPreviewActionSheetView setContentInsets:];
-[_UIPreviewActionSheetView setActions:];
-[_UIPreviewActionSheetView actions];
-[_UIPreviewActionSheetView setDelegate:];
-[_UIPreviewActionSheetView title];
-[_UIPreviewActionSheetView delegate];
-[_UIPreviewActionSheetView contentInsets];
-[_UIPreviewActionSheetView initWithCoder:];
-[_UIPreviewActionSheetView setTitle:];
-[_UIPreviewActionSheetView initWithFrame:];
-[_UIPreviewActionSheetView _performActionForPreviewAction:interfaceAction:];
-[_UIPreviewActionSheetView _setupViewHierarchy];
-[_UIPreviewActionSheetView captureTouchesRecognizer];
-[_UIPreviewActionSheetView initWithFrame:title:items:contentInsets:];
-[_UIPreviewActionSheetView setCaptureTouchesRecognizer:];
```
