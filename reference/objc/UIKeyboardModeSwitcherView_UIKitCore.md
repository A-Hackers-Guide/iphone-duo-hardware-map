# `UIKeyboardModeSwitcherView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIGestureRecognizerDelegate`, `UIContextMenuInteractionDelegate`
- 5 instance variables, 9 properties, 28 instance methods, 2 class methods

## Instance variables

```
@"<_UIAnimatedKeyboardElement>" _animatedKeyboardElement;
@"UITapGestureRecognizer" _tapGestureRecognizer;
@"UIContextMenuInteraction" _contextMenuInteraction;
@"UIView" _contextMenuTargettedPreview;
@"UIImageView" _ellipsisImageView;
```

## Properties

```
@property (T@"UITapGestureRecognizer",&,N,V_tapGestureRecognizer) tapGestureRecognizer;
@property (T@"UIContextMenuInteraction",&,N,V_contextMenuInteraction) contextMenuInteraction;
@property (T@"UIView",&,N,V_contextMenuTargettedPreview) contextMenuTargettedPreview;
@property (T@"UIImageView",&,N,V_ellipsisImageView) ellipsisImageView;
@property (T@"<_UIAnimatedKeyboardElement>",W,N,V_animatedKeyboardElement) animatedKeyboardElement;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKeyboardModeSwitcherView _shouldShowSplitForSmallLayoutClassWithActiveLayout:];
+[UIKeyboardModeSwitcherView shouldShowSplitForSmallLayoutClassWithActiveLayout];
```

## Instance methods

```
-[UIKeyboardModeSwitcherView tapGestureRecognizer];
-[UIKeyboardModeSwitcherView contextMenuInteraction:willEndForConfiguration:animator:];
-[UIKeyboardModeSwitcherView contextMenuInteraction:configurationForMenuAtLocation:];
-[UIKeyboardModeSwitcherView _handleTap:];
-[UIKeyboardModeSwitcherView contextMenuInteraction:willDisplayMenuForConfiguration:animator:];
-[UIKeyboardModeSwitcherView setContextMenuInteraction:];
-[UIKeyboardModeSwitcherView contextMenuInteraction];
-[UIKeyboardModeSwitcherView gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UIKeyboardModeSwitcherView traitCollectionDidChange:];
-[UIKeyboardModeSwitcherView setTapGestureRecognizer:];
-[UIKeyboardModeSwitcherView initWithRenderConfig:];
-[UIKeyboardModeSwitcherView _updateBackgroundColor];
-[UIKeyboardModeSwitcherView pointInside:withEvent:];
-[UIKeyboardModeSwitcherView _contextMenuInteraction:styleForMenuWithConfiguration:];
-[UIKeyboardModeSwitcherView setContextMenuTargettedPreview:];
-[UIKeyboardModeSwitcherView _actionsForKeyboardPositions];
-[UIKeyboardModeSwitcherView _actionsForMediumKeyboardPositions];
-[UIKeyboardModeSwitcherView _actionsForSmallKeyboardPositions];
-[UIKeyboardModeSwitcherView _addDotViewAtPoint:];
-[UIKeyboardModeSwitcherView _addEllipsisImageView];
-[UIKeyboardModeSwitcherView _glyphColorForTraitCollection:];
-[UIKeyboardModeSwitcherView _updateEllipsisImageView];
-[UIKeyboardModeSwitcherView animatedKeyboardElement];
-[UIKeyboardModeSwitcherView contextMenuTargettedPreview];
-[UIKeyboardModeSwitcherView ellipsisImageView];
-[UIKeyboardModeSwitcherView setAnimatedKeyboardElement:];
-[UIKeyboardModeSwitcherView setEllipsisImageView:];
-[UIKeyboardModeSwitcherView supplementalVisibleFramesInView:];
```
