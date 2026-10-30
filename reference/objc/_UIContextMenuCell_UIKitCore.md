# `_UIContextMenuCell`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewCell`
- 3 instance variables, 4 properties, 22 instance methods, 3 class methods

## Instance variables

```
B __highlightBackgroundViewNeedsUpdate;
B __selectedBackgroundViewNeedsUpdate;
@"UIShape" __backgroundShape;
```

## Properties

```
@property (T@"UIShape",C,N,V__backgroundShape) _backgroundShape;
@property (TB,N,V__highlightBackgroundViewNeedsUpdate) _highlightBackgroundViewNeedsUpdate;
@property (TB,N,V__selectedBackgroundViewNeedsUpdate) _selectedBackgroundViewNeedsUpdate;
@property (T@"_UIContextMenuCellContentView",R,N) actionView;
```

## Class methods

```
+[_UIContextMenuCell _contentViewClass];
+[_UIContextMenuCell _isInternalCell];
+[_UIContextMenuCell _wantsLegacyMenuGesture];
```

## Instance methods

```
-[_UIContextMenuCell _setTypeSelectState:];
-[_UIContextMenuCell setSelected:];
-[_UIContextMenuCell _highlightBackgroundViewNeedsUpdate];
-[_UIContextMenuCell setDirectionalLayoutMargins:];
-[_UIContextMenuCell _backgroundShape];
-[_UIContextMenuCell actionView];
-[_UIContextMenuCell didUpdateFocusInContext:withAnimationCoordinator:];
-[_UIContextMenuCell _configureFocusedFloatingContentView:];
-[_UIContextMenuCell _selectedBackgroundViewNeedsUpdate];
-[_UIContextMenuCell set_backgroundShape:];
-[_UIContextMenuCell layoutSubviews];
-[_UIContextMenuCell _updateStateWithAnimationCoordinator:animated:];
-[_UIContextMenuCell _allowsHorizontalFocusMovement];
-[_UIContextMenuCell setHighlighted:];
-[_UIContextMenuCell focusItemDeferralMode];
-[_UIContextMenuCell set_selectedBackgroundViewNeedsUpdate:];
-[_UIContextMenuCell prepareForReuse];
-[_UIContextMenuCell _configureBackgroundView:withContentShape:selected:];
-[_UIContextMenuCell _wantsKeyCommandsWhenDeferred];
-[_UIContextMenuCell set_highlightBackgroundViewNeedsUpdate:];
-[_UIContextMenuCell initWithFrame:];
-[_UIContextMenuCell setHighlighted:forHover:];
```
