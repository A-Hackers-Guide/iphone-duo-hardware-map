# `UITableViewHeaderFooterView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UITableViewSubviewReusing`
- 21 instance variables, 42 properties, 159 instance methods, 6 class methods

## Instance variables

```
q _tableViewStyle;
@"UIImage" _backgroundImage;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
q _textAlignment;
d _maxTitleWidth;
@"NSString" _reuseIdentifier;
@"UIView" _backgroundView;
@"_UITableViewHeaderFooterViewLabel" _label;
@"_UITableViewHeaderFooterViewLabel" _detailLabel;
@"UIView" _contentView;
d _leadingMarginWidth;
d _trailingMarginWidth;
@"<_UIContentViewInternal>" _viewForContentConfiguration;
@"_UISystemBackgroundView" _systemBackgroundView;
@? _contentViewConfigurationProvider;
@? _backgroundViewConfigurationProvider;
@"<UITableConstants>" _constants;
@"UITableMetricsAdapter" _metricsAdapter;
{?="isHeader"b1"labelBackgroundColorNeedsUpdate"b1"detailLabelBackgroundColorNeedsUpdate"b1"floating"b1"stripPadding"b1"isTopHeader"b1"didSetSectionHeader"b1"didSetupDefaults"b1"insetsContentViewsToSafeArea"b1"isDisplayed"b1"tableViewHasBeenExplicitlySet"b1"hasCustomBackgroundView"b1"hasCustomBackgroundViewConfigurationProvider"b1"hasCustomBackgroundViewConfiguration"b1"needsConfigurationStateUpdate"b1"hasContentConfiguration"b1"automaticallyUpdatesContentViewConfiguration"b1"automaticallyUpdatesBackgroundViewConfiguration"b1"automaticIntrinsicContentSizeInvalidationEnabled"b1} _headerFooterFlags;
@"<UITable>" _table;
@? _configurationUpdateHandler;
```

## Properties

```
@property (T@"UIViewConfigurationState",N,R) _bridgedConfigurationState;
@property (T{UIEdgeInsets=dddd},R,N,G_effectiveSafeAreaInsets) effectiveSafeAreaInsets;
@property (T@"<UITable>",W,N,V_table) table;
@property (TB,N,S_setAutomaticIntrinsicContentSizeInvalidationEnabled:) _automaticIntrinsicContentSizeInvalidationEnabled;
@property (T@"NSString",C,N,V_reuseIdentifier) reuseIdentifier;
@property (Td,N,G_marginWidth,S_setMarginWidth:) marginWidth;
@property (Td,N,G_rightMarginWidth,S_setRightMarginWidth:) rightMarginWidth;
@property (TB,N,G_insetsContentViewsToSafeArea,S_setInsetsContentViewsToSafeArea:) insetsContentViewsToSafeArea;
@property (TB,N,G_stripPadding,S_setStripPadding:) stripPadding;
@property (TB,N,G_isTopHeader,S_setTopHeader:) topHeader;
@property (T@"<UITableConstants>",&,N,G_constants,S_setConstants:) constants;
@property (T@"UITableMetricsAdapter",&,N,G_metricsAdapter,S_setMetricsAdapter:) metricsAdapter;
@property (T@"UICellConfigurationState",R,N) _configurationState;
@property (TB,N) floating;
@property (Tq,N) tableViewStyle;
@property (T@"UIImage",&,N,V_backgroundImage) backgroundImage;
@property (TB,N) sectionHeader;
@property (T@"UITableView",W,N) tableView;
@property (Tq,N) textAlignment;
@property (T@"NSString",C,N) text;
@property (Td,N,V_maxTitleWidth) maxTitleWidth;
@property (T@"<_UIContentViewConfiguration>",C,N,G_contentViewConfiguration,S_setContentViewConfiguration:) _contentViewConfiguration;
@property (TB,N,G_automaticallyUpdatesContentViewConfiguration,S_setAutomaticallyUpdatesContentViewConfiguration:) _automaticallyUpdatesContentViewConfiguration;
@property (T@?,C,N,G_contentViewConfigurationProvider,S_setContentViewConfigurationProvider:) _contentViewConfigurationProvider;
@property (T@"_UIBackgroundViewConfiguration",C,N,G_backgroundViewConfiguration,S_setBackgroundViewConfiguration:) _backgroundViewConfiguration;
@property (T@?,C,N,G_backgroundViewConfigurationProvider,S_setBackgroundViewConfigurationProvider:) _backgroundViewConfigurationProvider;
@property (TB,N,G_automaticallyUpdatesBackgroundViewConfiguration,S_setAutomaticallyUpdatesBackgroundViewConfiguration:) _automaticallyUpdatesBackgroundViewConfiguration;
@property (TQ,R,N) _viewConfigurationState;
@property (T@"UIViewConfigurationState",R,N) configurationState;
@property (T@?,C,N,V_configurationUpdateHandler) configurationUpdateHandler;
@property (T@"<UIContentConfiguration>",C,N) contentConfiguration;
@property (TB,N) automaticallyUpdatesContentConfiguration;
@property (T@"UIView",R,N,V_contentView) contentView;
@property (T@"UILabel",R,N) textLabel;
@property (T@"UILabel",R,N) detailTextLabel;
@property (T@"UIBackgroundConfiguration",C,N) backgroundConfiguration;
@property (TB,N) automaticallyUpdatesBackgroundConfiguration;
@property (T@"UIView",&,N) backgroundView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UITableViewHeaderFooterView _defaultFontForHeaderFooterView:];
+[UITableViewHeaderFooterView _defaultFontForTableViewStyle:isSectionHeader:];
+[UITableViewHeaderFooterView _defaultPlainHeaderFooterFont];
+[UITableViewHeaderFooterView _defaultTextColorForTableViewStyle:isSectionHeader:];
+[UITableViewHeaderFooterView defaultFooterHeightForStyle:];
+[UITableViewHeaderFooterView defaultHeaderHeightForStyle:];
```

## Instance methods

```
-[UITableViewHeaderFooterView setUserInteractionEnabled:];
-[UITableViewHeaderFooterView _didUpdateFocusInContext:];
-[UITableViewHeaderFooterView tableView];
-[UITableViewHeaderFooterView setTextAlignment:];
-[UITableViewHeaderFooterView setFloating:];
-[UITableViewHeaderFooterView initWithReuseIdentifier:];
-[UITableViewHeaderFooterView _intrinsicContentSizeInvalidatedForChildView:];
-[UITableViewHeaderFooterView textAlignment];
-[UITableViewHeaderFooterView setTable:];
-[UITableViewHeaderFooterView setBackgroundImage:];
-[UITableViewHeaderFooterView text];
-[UITableViewHeaderFooterView invalidateIntrinsicContentSize];
-[UITableViewHeaderFooterView backgroundImage];
-[UITableViewHeaderFooterView _updateProperties];
-[UITableViewHeaderFooterView table];
-[UITableViewHeaderFooterView textLabel];
-[UITableViewHeaderFooterView _concreteDefaultLayoutMargins];
-[UITableViewHeaderFooterView _bridgedUpdateConfigurationUsingState:];
-[UITableViewHeaderFooterView _constants];
-[UITableViewHeaderFooterView floating];
-[UITableViewHeaderFooterView _updateBackgroundView];
-[UITableViewHeaderFooterView _safeAreaInsetsDidChangeFromOldInsets:];
-[UITableViewHeaderFooterView layoutSubviews];
-[UITableViewHeaderFooterView layoutMarginsDidChange];
-[UITableViewHeaderFooterView setTranslatesAutoresizingMaskIntoConstraints:];
-[UITableViewHeaderFooterView setBackgroundColor:];
-[UITableViewHeaderFooterView sizeThatFits:];
-[UITableViewHeaderFooterView _defaultTextColor];
-[UITableViewHeaderFooterView setTableView:];
-[UITableViewHeaderFooterView setTintColor:];
-[UITableViewHeaderFooterView _setupBackgroundView];
-[UITableViewHeaderFooterView prepareForReuse];
-[UITableViewHeaderFooterView encodeWithCoder:];
-[UITableViewHeaderFooterView contentView];
-[UITableViewHeaderFooterView reuseIdentifier];
-[UITableViewHeaderFooterView setBackgroundConfiguration:];
-[UITableViewHeaderFooterView setFrame:];
-[UITableViewHeaderFooterView backgroundView];
-[UITableViewHeaderFooterView initWithCoder:];
-[UITableViewHeaderFooterView traitCollectionDidChange:];
-[UITableViewHeaderFooterView isTransparentFocusItem];
-[UITableViewHeaderFooterView setText:];
-[UITableViewHeaderFooterView _populateArchivedSubviews:];
-[UITableViewHeaderFooterView backgroundConfiguration];
-[UITableViewHeaderFooterView didMoveToSuperview];
-[UITableViewHeaderFooterView initWithFrame:];
-[UITableViewHeaderFooterView systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:];
-[UITableViewHeaderFooterView setBackgroundView:];
-[UITableViewHeaderFooterView _willUpdateFocusInContext:];
-[UITableViewHeaderFooterView setNeedsUpdateConfiguration];
-[UITableViewHeaderFooterView _viewConfigurationState];
-[UITableViewHeaderFooterView _backgroundRect];
-[UITableViewHeaderFooterView _updateConfigurationUsingState:];
-[UITableViewHeaderFooterView _updateContentAndBackgroundView];
-[UITableViewHeaderFooterView _defaultBackgroundConfiguration];
-[UITableViewHeaderFooterView _insetsToBounds];
-[UITableViewHeaderFooterView _invalidateLabelBackgroundColor];
-[UITableViewHeaderFooterView _label:];
-[UITableViewHeaderFooterView _metricsAdapter];
-[UITableViewHeaderFooterView _setTableViewStyle:updateFrame:];
-[UITableViewHeaderFooterView detailTextLabel];
-[UITableViewHeaderFooterView _applyBackgroundViewConfiguration:withState:];
-[UITableViewHeaderFooterView _applyContentViewConfiguration:withState:usingSPI:];
-[UITableViewHeaderFooterView _automaticIntrinsicContentSizeInvalidationEnabled];
-[UITableViewHeaderFooterView _automaticallyUpdatesBackgroundViewConfiguration];
-[UITableViewHeaderFooterView _automaticallyUpdatesContentViewConfiguration];
-[UITableViewHeaderFooterView _backgroundRectForWidth:];
-[UITableViewHeaderFooterView _backgroundViewConfiguration];
-[UITableViewHeaderFooterView _backgroundViewConfigurationProvider];
-[UITableViewHeaderFooterView _bridgedConfigurationState];
-[UITableViewHeaderFooterView _clearChangeHandlersForOldContentView:];
-[UITableViewHeaderFooterView _configurationState];
-[UITableViewHeaderFooterView _configureDefaultContentViewLayoutMargins];
-[UITableViewHeaderFooterView _contentRect];
-[UITableViewHeaderFooterView _contentRectForWidth:];
-[UITableViewHeaderFooterView _contentViewConfiguration];
-[UITableViewHeaderFooterView _contentViewConfigurationProvider];
-[UITableViewHeaderFooterView _customViewForDefaultBackgroundAppearance];
-[UITableViewHeaderFooterView _detailLabelFrame];
-[UITableViewHeaderFooterView _detailTextSizeForWidth:];
-[UITableViewHeaderFooterView _didUpdateMetrics:];
-[UITableViewHeaderFooterView _effectiveSafeAreaInsets];
-[UITableViewHeaderFooterView _forwardsSystemLayoutFittingSizeToContentView:];
-[UITableViewHeaderFooterView _hostsLayoutEngineAllowsTAMIC_NO];
-[UITableViewHeaderFooterView _insetsContentViewsToSafeArea];
-[UITableViewHeaderFooterView _insetsToContentRect];
-[UITableViewHeaderFooterView _invalidateConfiguration];
-[UITableViewHeaderFooterView _invalidateDetailLabelBackgroundColor];
-[UITableViewHeaderFooterView _isEffectivelyHidden];
-[UITableViewHeaderFooterView _isFloating];
-[UITableViewHeaderFooterView _isSourceListOrMacIdiom];
-[UITableViewHeaderFooterView _isTopHeader];
-[UITableViewHeaderFooterView _labelFrame];
-[UITableViewHeaderFooterView _layoutSystemBackgroundView];
-[UITableViewHeaderFooterView _marginWidth];
-[UITableViewHeaderFooterView _notifyIsDisplaying:];
-[UITableViewHeaderFooterView _performConfigurationStateUpdate];
-[UITableViewHeaderFooterView _prepareForConfigurationStateUpdate];
-[UITableViewHeaderFooterView _resetBackgroundViewConfiguration];
-[UITableViewHeaderFooterView _resetBackgroundViewsAndColor];
-[UITableViewHeaderFooterView _resetContentViews];
-[UITableViewHeaderFooterView _rightMarginWidth];
-[UITableViewHeaderFooterView _setAutomaticIntrinsicContentSizeInvalidationEnabled:];
-[UITableViewHeaderFooterView _setAutomaticallyUpdatesBackgroundViewConfiguration:];
-[UITableViewHeaderFooterView _setAutomaticallyUpdatesContentViewConfiguration:];
-[UITableViewHeaderFooterView _setBackgroundViewConfiguration:];
-[UITableViewHeaderFooterView _setBackgroundViewConfigurationProvider:];
-[UITableViewHeaderFooterView _setConstants:];
-[UITableViewHeaderFooterView _setContentView:insertAtBack:];
-[UITableViewHeaderFooterView _setContentViewConfiguration:];
-[UITableViewHeaderFooterView _setContentViewConfigurationProvider:];
-[UITableViewHeaderFooterView _setInsetsContentViewsToSafeArea:];
-[UITableViewHeaderFooterView _setMarginWidth:];
-[UITableViewHeaderFooterView _setMetricsAdapter:];
-[UITableViewHeaderFooterView _setNeedsConfigurationStateUpdate];
-[UITableViewHeaderFooterView _setRightMarginWidth:];
-[UITableViewHeaderFooterView _setStripPadding:];
-[UITableViewHeaderFooterView _setTopHeader:];
-[UITableViewHeaderFooterView _setupChangeHandlersForNewContentView:];
-[UITableViewHeaderFooterView _setupDefaultsIfNecessary];
-[UITableViewHeaderFooterView _setupLabelAppearance];
-[UITableViewHeaderFooterView _setupLabelForSourceList:];
-[UITableViewHeaderFooterView _sizeThatFits:stripPaddingForAbuttingView:isTopHeader:];
-[UITableViewHeaderFooterView _stripPadding];
-[UITableViewHeaderFooterView _table];
-[UITableViewHeaderFooterView _tableViewDidUpdateMarginWidth];
-[UITableViewHeaderFooterView _textSizeForWidth:];
-[UITableViewHeaderFooterView _tintColorAffectsBackgroundColor];
-[UITableViewHeaderFooterView _updateBackgroundViewConfigurationForState:];
-[UITableViewHeaderFooterView _updateConfigurationWithObservationTracking];
-[UITableViewHeaderFooterView _updateContentViewConfigurationForState:];
-[UITableViewHeaderFooterView _updateDefaultBackgroundAppearance];
-[UITableViewHeaderFooterView _updateDetailLabelBackgroundColor];
-[UITableViewHeaderFooterView _updateDetailLabelBackgroundColorIfNeeded];
-[UITableViewHeaderFooterView _updateViewConfigurationsWithState:];
-[UITableViewHeaderFooterView _updatedContentViewFrameForTargetWidth:];
-[UITableViewHeaderFooterView _useDetailText];
-[UITableViewHeaderFooterView _usingBackgroundConfigurationOrDefaultBackgroundConfiguration];
-[UITableViewHeaderFooterView _usingBackgroundViewConfiguration];
-[UITableViewHeaderFooterView automaticallyUpdatesBackgroundConfiguration];
-[UITableViewHeaderFooterView automaticallyUpdatesContentConfiguration];
-[UITableViewHeaderFooterView configurationState];
-[UITableViewHeaderFooterView configurationUpdateHandler];
-[UITableViewHeaderFooterView contentConfiguration];
-[UITableViewHeaderFooterView defaultBackgroundConfiguration];
-[UITableViewHeaderFooterView defaultContentConfiguration];
-[UITableViewHeaderFooterView maxTitleWidth];
-[UITableViewHeaderFooterView sectionHeader];
-[UITableViewHeaderFooterView setAutomaticallyUpdatesBackgroundConfiguration:];
-[UITableViewHeaderFooterView setAutomaticallyUpdatesContentConfiguration:];
-[UITableViewHeaderFooterView setConfigurationUpdateHandler:];
-[UITableViewHeaderFooterView setContentConfiguration:];
-[UITableViewHeaderFooterView setMaxTitleWidth:];
-[UITableViewHeaderFooterView setNeedsUpdateConstraints];
-[UITableViewHeaderFooterView setReuseIdentifier:];
-[UITableViewHeaderFooterView setSectionHeader:];
-[UITableViewHeaderFooterView setTableViewStyle:];
-[UITableViewHeaderFooterView tableViewStyle];
-[UITableViewHeaderFooterView updateConfigurationUsingState:];
```
