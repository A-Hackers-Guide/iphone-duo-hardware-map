# `_UIContextMenuHeaderView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionReusableView`
- 14 instance variables, 12 properties, 41 instance methods, 0 class methods

## Instance variables

```
B _needsConstraintRebuild;
B _isDisplayingTitleAndAccessory;
B _isMenuTitle;
Q _separatorStyle;
@"NSString" _title;
@"UIAction" _accessoryAction;
@"UIView" _contentView;
@"UIView" _bgView;
@"UILabel" _titleLabel;
@"UIView" _separator;
@"UIButton" _accessoryButton;
@"UIView" _titleWithAccessoryContainer;
@"NSArray" _titleWithAccessoryContainerConstraints;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _unscaledLayoutMargins;
```

## Properties

```
@property (T@"UIView",&,N,V_bgView) bgView;
@property (T@"UILabel",&,N,V_titleLabel) titleLabel;
@property (T@"UIView",&,N,V_separator) separator;
@property (T@"UIButton",&,N,V_accessoryButton) accessoryButton;
@property (T@"UIView",&,N,V_titleWithAccessoryContainer) titleWithAccessoryContainer;
@property (T@"NSArray",&,N,V_titleWithAccessoryContainerConstraints) titleWithAccessoryContainerConstraints;
@property (TQ,N,V_separatorStyle) separatorStyle;
@property (T@"NSString",C,N,V_title) title;
@property (T@"UIAction",R,N,V_accessoryAction) accessoryAction;
@property (T@"UIView",&,N,V_contentView) contentView;
@property (TB,N,V_isMenuTitle) isMenuTitle;
@property (T{NSDirectionalEdgeInsets=dddd},N,V_unscaledLayoutMargins) unscaledLayoutMargins;
```

## Instance methods

```
-[_UIContextMenuHeaderView separator];
-[_UIContextMenuHeaderView setSeparator:];
-[_UIContextMenuHeaderView setContentView:];
-[_UIContextMenuHeaderView accessoryButton];
-[_UIContextMenuHeaderView setSeparatorStyle:];
-[_UIContextMenuHeaderView setTitleLabel:];
-[_UIContextMenuHeaderView _separatorHeight];
-[_UIContextMenuHeaderView titleLabel];
-[_UIContextMenuHeaderView setAccessoryButton:];
-[_UIContextMenuHeaderView _updateBackgroundView];
-[_UIContextMenuHeaderView _titleFont];
-[_UIContextMenuHeaderView title];
-[_UIContextMenuHeaderView accessoryAction];
-[_UIContextMenuHeaderView contentView];
-[_UIContextMenuHeaderView updateConstraints];
-[_UIContextMenuHeaderView setTitle:];
-[_UIContextMenuHeaderView initWithFrame:];
-[_UIContextMenuHeaderView separatorStyle];
-[_UIContextMenuHeaderView setBackgroundMaterialGroupName:];
-[_UIContextMenuHeaderView setTitleWithAccessoryContainer:];
-[_UIContextMenuHeaderView setIsMenuTitle:];
-[_UIContextMenuHeaderView _clearTitleWithAccessoryContainerConstraints];
-[_UIContextMenuHeaderView _createAccessoryButton];
-[_UIContextMenuHeaderView _createTitleLabelIfNecessary];
-[_UIContextMenuHeaderView _createTitleWithAccessoryContainerConstraints];
-[_UIContextMenuHeaderView _isDisplayingTitleLabel];
-[_UIContextMenuHeaderView _labelRenderingMode];
-[_UIContextMenuHeaderView _setNeedsConstraintRebuild];
-[_UIContextMenuHeaderView _titleLabelFilterForCurrentTraits];
-[_UIContextMenuHeaderView _titleLabelNumberOfLines];
-[_UIContextMenuHeaderView _updateCompositingFilterForCurrentState];
-[_UIContextMenuHeaderView _updateLayoutMargins];
-[_UIContextMenuHeaderView bgView];
-[_UIContextMenuHeaderView isMenuTitle];
-[_UIContextMenuHeaderView setBgView:];
-[_UIContextMenuHeaderView setTitle:accessoryAction:];
-[_UIContextMenuHeaderView setTitleWithAccessoryContainerConstraints:];
-[_UIContextMenuHeaderView setUnscaledLayoutMargins:];
-[_UIContextMenuHeaderView titleWithAccessoryContainer];
-[_UIContextMenuHeaderView titleWithAccessoryContainerConstraints];
-[_UIContextMenuHeaderView unscaledLayoutMargins];
```
