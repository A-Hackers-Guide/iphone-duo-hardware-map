# `_UITextLoupeView` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 13 instance methods, 0 class methods

## Properties

```
@property (T{CGSize=dd},R,N) preferredSize;
@property (T@"<UICoordinateSpace>",R,N) containerCoordinateSpace;
@property (TB,N) visible;
@property (Td,N) dismissalProgress;
@property (T{CGPoint=dd},N) modelPosition;
@property (T@"UIView<_UITextSelectionWidgetAnimating>",W,N) animatableSelectionWidget;
```

## Instance methods

```
-[_UITextLoupeView visible];
-[_UITextLoupeView setVisible:];
-[_UITextLoupeView setModelPosition:];
-[_UITextLoupeView preferredSize];
-[_UITextLoupeView needsHideLoupe:];
-[_UITextLoupeView setVisible:animated:completion:];
-[_UITextLoupeView animatableSelectionWidget];
-[_UITextLoupeView constrainedModelPositionForPosition:];
-[_UITextLoupeView containerCoordinateSpace];
-[_UITextLoupeView dismissalProgress];
-[_UITextLoupeView modelPosition];
-[_UITextLoupeView setAnimatableSelectionWidget:];
-[_UITextLoupeView setDismissalProgress:];
```
