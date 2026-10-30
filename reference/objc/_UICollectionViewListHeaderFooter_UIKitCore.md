# `_UICollectionViewListHeaderFooter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionReusableView`
- 8 instance variables, 10 properties, 46 instance methods, 1 class methods

## Instance variables

```
{?="style"b3"needsConfigurationStateUpdate"b1"hasCustomBackgroundColor"b1"hasCustomBackgroundViewConfigurationProvider"b1"hasCustomBackgroundViewConfiguration"b1"automaticallyUpdatesBackgroundViewConfiguration"b1"automaticallyUpdatesContentViewConfiguration"b1} _headerFooterFlags;
# _contentViewConfigurationClass;
@? _contentViewConfigurationProvider;
@"_UISystemBackgroundView" _systemBackgroundView;
@? _backgroundViewConfigurationProvider;
@"UIView" _contentView;
@"<UITableConstants>" _constants;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _contentViewInsets;
```

## Properties

```
@property (T@"UIView",&,N,V_contentView) contentView;
@property (T{UIEdgeInsets=dddd},R,N,G_contentViewInsets,V_contentViewInsets) contentViewInsets;
@property (T@"<UITableConstants>",R,N,G_constants,V_constants) constants;
@property (T@"<_UIContentViewConfiguration>",C,N,G_contentViewConfiguration,S_setContentViewConfiguration:) _contentViewConfiguration;
@property (TB,N,G_automaticallyUpdatesContentViewConfiguration,S_setAutomaticallyUpdatesContentViewConfiguration:) _automaticallyUpdatesContentViewConfiguration;
@property (T@?,C,N,G_contentViewConfigurationProvider,S_setContentViewConfigurationProvider:) _contentViewConfigurationProvider;
@property (T@"_UIBackgroundViewConfiguration",C,N,G_backgroundViewConfiguration,S_setBackgroundViewConfiguration:) _backgroundViewConfiguration;
@property (TB,N,G_automaticallyUpdatesBackgroundViewConfiguration,S_setAutomaticallyUpdatesBackgroundViewConfiguration:) _automaticallyUpdatesBackgroundViewConfiguration;
@property (T@?,C,N,G_backgroundViewConfigurationProvider,S_setBackgroundViewConfigurationProvider:) _backgroundViewConfigurationProvider;
@property (TQ,R,N) _viewConfigurationState;
```

## Class methods

```
+[_UICollectionViewListHeaderFooter _contentViewClass];
```

## Instance methods

```
-[_UICollectionViewListHeaderFooter setUserInteractionEnabled:];
-[_UICollectionViewListHeaderFooter _didUpdateFocusInContext:];
-[_UICollectionViewListHeaderFooter setContentView:];
-[_UICollectionViewListHeaderFooter _constants];
-[_UICollectionViewListHeaderFooter layoutSubviews];
-[_UICollectionViewListHeaderFooter setSemanticContentAttribute:];
-[_UICollectionViewListHeaderFooter setBackgroundColor:];
-[_UICollectionViewListHeaderFooter sizeThatFits:];
-[_UICollectionViewListHeaderFooter prepareForReuse];
-[_UICollectionViewListHeaderFooter encodeWithCoder:];
-[_UICollectionViewListHeaderFooter _layoutContentView];
-[_UICollectionViewListHeaderFooter contentView];
-[_UICollectionViewListHeaderFooter initWithCoder:];
-[_UICollectionViewListHeaderFooter traitCollectionDidChange:];
-[_UICollectionViewListHeaderFooter _populateArchivedSubviews:];
-[_UICollectionViewListHeaderFooter initWithFrame:];
-[_UICollectionViewListHeaderFooter systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:];
-[_UICollectionViewListHeaderFooter _viewConfigurationState];
-[_UICollectionViewListHeaderFooter _applyBackgroundViewConfiguration:];
-[_UICollectionViewListHeaderFooter _automaticallyUpdatesBackgroundViewConfiguration];
-[_UICollectionViewListHeaderFooter _automaticallyUpdatesContentViewConfiguration];
-[_UICollectionViewListHeaderFooter _backgroundViewConfiguration];
-[_UICollectionViewListHeaderFooter _backgroundViewConfigurationProvider];
-[_UICollectionViewListHeaderFooter _contentTargetSizeForTargetSize:withHorizontalFittingPriority:verticalFittingPriority:forUseWithSizeThatFits:];
-[_UICollectionViewListHeaderFooter _contentViewConfiguration];
-[_UICollectionViewListHeaderFooter _contentViewConfigurationProvider];
-[_UICollectionViewListHeaderFooter _contentViewInsets];
-[_UICollectionViewListHeaderFooter _defaultBackgroundViewConfigurationProvider];
-[_UICollectionViewListHeaderFooter _layoutSystemBackgroundView];
-[_UICollectionViewListHeaderFooter _performConfigurationStateUpdate];
-[_UICollectionViewListHeaderFooter _resetBackgroundColor];
-[_UICollectionViewListHeaderFooter _resetBackgroundViewConfiguration];
-[_UICollectionViewListHeaderFooter _setAutomaticallyUpdatesBackgroundViewConfiguration:];
-[_UICollectionViewListHeaderFooter _setAutomaticallyUpdatesContentViewConfiguration:];
-[_UICollectionViewListHeaderFooter _setBackgroundViewConfiguration:];
-[_UICollectionViewListHeaderFooter _setBackgroundViewConfigurationProvider:];
-[_UICollectionViewListHeaderFooter _setContentViewConfiguration:];
-[_UICollectionViewListHeaderFooter _setContentViewConfigurationProvider:];
-[_UICollectionViewListHeaderFooter _setLayoutAttributes:];
-[_UICollectionViewListHeaderFooter _setNeedsConfigurationStateUpdate];
-[_UICollectionViewListHeaderFooter _styleFromLayoutAttributes:];
-[_UICollectionViewListHeaderFooter _updateBackgroundViewConfigurationForState:];
-[_UICollectionViewListHeaderFooter _updateConstants];
-[_UICollectionViewListHeaderFooter _updateContentViewConfigurationForState:];
-[_UICollectionViewListHeaderFooter _updateDefaultBackgroundAppearance];
-[_UICollectionViewListHeaderFooter _updateViewConfigurationsWithState:];
```
