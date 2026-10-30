# `_UIContextMenuLayoutArbiter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"UIView" _containerView;
Q _currentLayout;
@"_UIContextMenuLayoutArbiterInput" _currentInput;
@"_UIIntrusionDebugOverlay" _debugOverlay;
{?="attachment"Q"alignment"Q"attachmentOffset"d"alignmentOffset"d"gravity"q} _menuAnchor;
```

## Properties

```
@property (T@"UIView",W,N,V_containerView) containerView;
@property (TQ,N,V_currentLayout) currentLayout;
@property (T@"_UIContextMenuLayoutArbiterInput",&,N,V_currentInput) currentInput;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) contentBounds;
@property (T{?=QQddq},R,N,V_menuAnchor) menuAnchor;
@property (T@"_UIIntrusionDebugOverlay",&,N,V_debugOverlay) debugOverlay;
```

## Instance methods

```
-[_UIContextMenuLayoutArbiter contentBounds];
-[_UIContextMenuLayoutArbiter setContainerView:];
-[_UIContextMenuLayoutArbiter setDebugOverlay:];
-[_UIContextMenuLayoutArbiter contentSpacing];
-[_UIContextMenuLayoutArbiter sourceWindowBounds];
-[_UIContextMenuLayoutArbiter setCurrentLayout:];
-[_UIContextMenuLayoutArbiter _computedPreviewBoundsForContentBounds:presentedScale:sourceWindowBounds:];
-[_UIContextMenuLayoutArbiter computedLayoutWithInput:];
-[_UIContextMenuLayoutArbiter currentLayout];
-[_UIContextMenuLayoutArbiter _computedMenuBoundsForContentBounds:predictedPreviewFrame:];
-[_UIContextMenuLayoutArbiter contentBoundsForConstrainingPreview];
-[_UIContextMenuLayoutArbiter menuAnchor];
-[_UIContextMenuLayoutArbiter containerView];
-[_UIContextMenuLayoutArbiter currentInput];
-[_UIContextMenuLayoutArbiter _drawContentBoundsDebugUI:];
-[_UIContextMenuLayoutArbiter initWithContainerView:layout:];
-[_UIContextMenuLayoutArbiter _positionPlatterFrame:andActionViewFrame:inBounds:aboutSourcePoint:];
-[_UIContextMenuLayoutArbiter _defaultAttachmentEdge];
-[_UIContextMenuLayoutArbiter _accessoryPositionsForBaseLayout:];
-[_UIContextMenuLayoutArbiter _automaticAlignmentAndOffset:forAttachment:sourcePoint:];
-[_UIContextMenuLayoutArbiter _computedMenuAnchorPointForMenuFrame:previewFrame:];
-[_UIContextMenuLayoutArbiter setCurrentInput:];
-[_UIContextMenuLayoutArbiter debugOverlay];
```
