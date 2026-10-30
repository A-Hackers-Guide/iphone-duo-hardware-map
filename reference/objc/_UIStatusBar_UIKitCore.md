# `_UIStatusBar`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIGestureRecognizerDelegate`, `UIAccessibilityHUDGestureDelegate`, `UIPointerInteractionDelegate`
- 28 instance variables, 39 properties, 134 instance methods, 7 class methods

## Instance variables

```
@"<_UIStatusBarVisualProvider>" _visualProvider;
{?="needsLayoutUpdateForPartFrames"b1"visualProviderClassScalesWithScreenNativeScale"b1"visualProviderClassImplementsReferenceScreenScale"b1"visualProviderClassRequiresIterativeOverflow"b1"visualProviderImplementsModeUpdatedFromMode"b1"visualProviderImplementsOrientationUpdatedFromOrientation"b1"visualProviderImplementsAvoidanceFrameUpdatedFromFrame"b1"visualProviderImplementsStyleUpdatedFromStyle"b1"visualProviderImplementsWillUpdateWithData"b1"visualProviderImplementsDataUpdated"b1"visualProviderImplementsCanFixupDisplayItemAttributes"b1"visualProviderImplementsSizeUpdatedFromSize"b1"visualProviderImplementsRegionWillSetDisplayItems"b1"visualProviderImplementsStatusBarRegionsUpdated"b1"visualProviderImplementsActionableHighlightedInitialPress"b1"visualProviderImplementsDisplayItemIdentifiersForPartWithIdentifier"b1"visualProviderImplementsRegionIdentifiersForPartWithIdentifier"b1"visualProviderImplementsStatusBarEnabledPartsUpdated"b1"visualProviderImplementsItemCreated"b1"updatingStates"b1"forcingIterativeOverflow"b1} _statusBarFlags;
@"UIScreen" _targetScreen;
@"NSDictionary" _visualProviderInfo;
q _style;
@"UIColor" _foregroundColor;
q _mode;
q _orientation;
@"_UIStatusBarData" _currentData;
@"UIGestureRecognizer" _actionGestureRecognizer;
@"NSArray" _enabledPartIdentifiers;
@"NSArray" _disabledPartIdentifiers;
@"NSMutableDictionary" _items;
@"NSMutableDictionary" _displayItemStates;
@? _updateCompletionHandler;
@"UIView" _foregroundView;
@"<_UIStatusBarActionable>" _targetActionable;
@"UIPointerInteraction" _pointerInteraction;
@"<_UIStatusBarActionable>" _hoveredActionable;
@"UIAccessibilityHUDGestureManager" _accessibilityHUDGestureManager;
# _visualProviderClass;
@"NSDictionary" _regions;
@"_UIStatusBarDataAggregator" _dataAggregator;
@"_UIStatusBarData" _currentAggregatedData;
@"_UIStatusBarStyleAttributes" _styleAttributes;
@"_UIStatusBarAction" _action;
@? _regionActionValidationBlock;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _avoidanceFrame;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_items) items;
@property (T@"NSMutableDictionary",&,N,V_displayItemStates) displayItemStates;
@property (T@?,C,N,V_updateCompletionHandler) updateCompletionHandler;
@property (T@"UIView",&,N,V_foregroundView) foregroundView;
@property (T@"<_UIStatusBarActionable>",W,N,V_targetActionable) targetActionable;
@property (T@"UIPointerInteraction",&,N,V_pointerInteraction) pointerInteraction;
@property (T@"<_UIStatusBarActionable>",W,N,V_hoveredActionable) hoveredActionable;
@property (T@"UIAccessibilityHUDGestureManager",&,N,V_accessibilityHUDGestureManager) accessibilityHUDGestureManager;
@property (T@"NSString",&,N,G_visualProviderClassName,S_setVisualProviderClassName:) visualProviderClassName;
@property (T#,&,N,G_visualProviderClass,S_setVisualProviderClass:,V_visualProviderClass) visualProviderClass;
@property (T@"<_UIStatusBarVisualProvider>",R,N) visualProvider;
@property (T@"NSDictionary",R,N,V_regions) regions;
@property (T@"_UIStatusBarDataAggregator",R,N,V_dataAggregator) dataAggregator;
@property (T@"_UIStatusBarData",R,N,V_currentAggregatedData) currentAggregatedData;
@property (T@"UIView",R,N) containerView;
@property (TI,R,N) animationContextId;
@property (TB,R,N,GareAnimationsEnabled) animationsEnabled;
@property (T@"_UIStatusBarStyleAttributes",&,N,V_styleAttributes) styleAttributes;
@property (T@"_UIStatusBarAction",&,N,V_action) action;
@property (T@"UIScreen",R,N,G_effectiveTargetScreen) effectiveTargetScreen;
@property (T@?,C,N,V_regionActionValidationBlock) regionActionValidationBlock;
@property (T{CGAffineTransform=dddddd},R,N,G_effectiveScaleTransform) effectiveScaleTransform;
@property (T@"UIScreen",&,N,V_targetScreen) targetScreen;
@property (T@"NSDictionary",&,N,V_visualProviderInfo) visualProviderInfo;
@property (Tq,N,V_style) style;
@property (T@"UIColor",C,N,V_foregroundColor) foregroundColor;
@property (Tq,N,V_mode) mode;
@property (Tq,N,V_orientation) orientation;
@property (T@"_UIStatusBarData",R,N,V_currentData) currentData;
@property (T@"NSSet",R,N) dependentDataEntryKeys;
@property (T@"_UIStatusBarData",C,N) overlayData;
@property (T@"UIGestureRecognizer",R,N,V_actionGestureRecognizer) actionGestureRecognizer;
@property (T@"NSArray",C,N,V_enabledPartIdentifiers) enabledPartIdentifiers;
@property (T@"NSArray",C,N,V_disabledPartIdentifiers) disabledPartIdentifiers;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_avoidanceFrame) avoidanceFrame;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIStatusBar intrinsicContentSizeForTargetScreen:orientation:onLockScreen:isAzulBLinked:];
+[_UIStatusBar registerSensorActivityIndicator:forScreen:];
+[_UIStatusBar sensorActivityIndicatorPartIdentifier];
+[_UIStatusBar intrinsicContentSizeForTargetScreen:orientation:onLockScreen:];
+[_UIStatusBar _effectiveScaleForVisualProviderClass:targetScreen:];
+[_UIStatusBar sensorActivityIndicatorForScreen:];
+[_UIStatusBar stringForStatusBarStyle:];
```

## Instance methods

```
-[_UIStatusBar alphaForPartWithIdentifier:];
-[_UIStatusBar frameForPartWithIdentifier:];
-[_UIStatusBar setOffset:forPartWithIdentifier:];
-[_UIStatusBar setForegroundColor:];
-[_UIStatusBar setOrientation:];
-[_UIStatusBar setEnabledPartIdentifiers:];
-[_UIStatusBar _traitCollectionForChildEnvironment:];
-[_UIStatusBar disabledPartIdentifiers];
-[_UIStatusBar frameForDisplayItemWithIdentifier:];
-[_UIStatusBar resetVisualProvider];
-[_UIStatusBar _forceLayoutEngineSolutionInRationalEdges];
-[_UIStatusBar visualProvider];
-[_UIStatusBar setPointerInteraction:];
-[_UIStatusBar updateWithData:];
-[_UIStatusBar statusBarGesture:];
-[_UIStatusBar regions];
-[_UIStatusBar _accessibilityHUDGestureManager:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIStatusBar _rearrangeOverflowedItems];
-[_UIStatusBar _updateActionGestureRecognizerAllowableTouchTypesIfNeeded];
-[_UIStatusBar _actionablesForPartWithIdentifier:includeInternalItems:onlyVisible:];
-[_UIStatusBar intrinsicContentSize];
-[_UIStatusBar _accessibilityHUDGestureManager:HUDItemForPoint:];
-[_UIStatusBar _accessibilityHUDGestureManager:gestureLiftedAtPoint:];
-[_UIStatusBar setStyle:forPartWithIdentifier:];
-[_UIStatusBar _accessibilityHUDGestureManager:showHUDItem:];
-[_UIStatusBar foregroundView];
-[_UIStatusBar _gestureRecognizer:pressInsideActionable:];
-[_UIStatusBar _prepareVisualProviderIfNeeded];
-[_UIStatusBar setUpdateCompletionHandler:];
-[_UIStatusBar pointerInteraction:styleForRegion:];
-[_UIStatusBar _updateWithData:completionHandler:];
-[_UIStatusBar setItems:];
-[_UIStatusBar displayItemIdentifiersInRegionsWithIdentifiers:];
-[_UIStatusBar pointerInteraction:willEnterRegion:animator:];
-[_UIStatusBar pointerInteraction:willExitRegion:animator:];
-[_UIStatusBar actionForPartWithIdentifier:];
-[_UIStatusBar resizeSubviewsWithOldSize:];
-[_UIStatusBar setDisplayItemStates:];
-[_UIStatusBar orientation];
-[_UIStatusBar setAction:forPartWithIdentifier:];
-[_UIStatusBar currentData];
-[_UIStatusBar accessibilityHUDGestureManager];
-[_UIStatusBar displayItemStates];
-[_UIStatusBar overlayData];
-[_UIStatusBar setOverlayData:];
-[_UIStatusBar styleAttributesForStyle:];
-[_UIStatusBar _effectiveTargetScreen];
-[_UIStatusBar _frameForActionable:];
-[_UIStatusBar layoutSubviews];
-[_UIStatusBar visualProviderInfo];
-[_UIStatusBar _pressFrameForActionable:];
-[_UIStatusBar setAction:];
-[_UIStatusBar action];
-[_UIStatusBar initWithStyle:];
-[_UIStatusBar displayItemWithIdentifier:];
-[_UIStatusBar _itemWithIdentifier:createIfNeeded:];
-[_UIStatusBar items];
-[_UIStatusBar style];
-[_UIStatusBar setAlpha:forPartWithIdentifier:];
-[_UIStatusBar itemsDependingOnKeys:];
-[_UIStatusBar currentAggregatedData];
-[_UIStatusBar setMode:];
-[_UIStatusBar setStyle:];
-[_UIStatusBar regionWithIdentifier:];
-[_UIStatusBar setSemanticContentAttribute:];
-[_UIStatusBar _performAnimations:];
-[_UIStatusBar _updateWithAggregatedData:];
-[_UIStatusBar containerView];
-[_UIStatusBar _updateDisplayedItemsWithData:styleAttributes:extraAnimations:];
-[_UIStatusBar setStyleAttributes:];
-[_UIStatusBar frameForPartWithIdentifier:includeInternalItems:];
-[_UIStatusBar setHoveredActionable:];
-[_UIStatusBar gestureRecognizerShouldBegin:];
-[_UIStatusBar styleAttributes];
-[_UIStatusBar setVisualProviderInfo:];
-[_UIStatusBar offsetForPartWithIdentifier:];
-[_UIStatusBar setTargetScreen:];
-[_UIStatusBar setAvoidanceFrame:animationSettings:options:];
-[_UIStatusBar _statusBarWindowForAccessibilityHUD];
-[_UIStatusBar animationContextId];
-[_UIStatusBar updateForcingIterativeOverflow];
-[_UIStatusBar _fixupDisplayItemAttributes];
-[_UIStatusBar itemIdentifiersInRegionsWithIdentifiers:];
-[_UIStatusBar pointerInteraction];
-[_UIStatusBar avoidanceFrame];
-[_UIStatusBar _performWithInheritedAnimation:];
-[_UIStatusBar _visualProviderClassName];
-[_UIStatusBar _accessibilityHUDGestureManager:shouldTerminateHUDGestureForOtherGestureRecognizer:];
-[_UIStatusBar regionActionValidationBlock];
-[_UIStatusBar mode];
-[_UIStatusBar pointerInteraction:regionForRequest:defaultRegion:];
-[_UIStatusBar _regionsForPartWithIdentifier:includeInternalItems:];
-[_UIStatusBar styleForPartWithIdentifier:];
-[_UIStatusBar updateWithAnimations:];
-[_UIStatusBar actionGestureRecognizer];
-[_UIStatusBar setForegroundView:];
-[_UIStatusBar dataAggregator];
-[_UIStatusBar description];
-[_UIStatusBar _delayUpdatesWithKeys:fromAnimation:];
-[_UIStatusBar _extendedHoverFrameForActionable:];
-[_UIStatusBar itemWithIdentifier:];
-[_UIStatusBar setDisabledPartIdentifiers:];
-[_UIStatusBar updateConstraints];
-[_UIStatusBar traitCollectionDidChange:];
-[_UIStatusBar _gestureRecognizer:touchInsideActionable:];
-[_UIStatusBar _accessibilityHUDGestureManager:shouldBeginAtPoint:];
-[_UIStatusBar targetScreen];
-[_UIStatusBar setAccessibilityHUDGestureManager:];
-[_UIStatusBar setTargetActionable:];
-[_UIStatusBar _setVisualProviderClass:];
-[_UIStatusBar _setVisualProviderClassName:];
-[_UIStatusBar _cursorLocation:isInsideHoverableActionable:];
-[_UIStatusBar foregroundColor];
-[_UIStatusBar _updateRegionItems];
-[_UIStatusBar _prepareAnimations:];
-[_UIStatusBar _visualProviderClass];
-[_UIStatusBar _cursorLocation:isInsideActionable:];
-[_UIStatusBar targetActionable];
-[_UIStatusBar _dismissAccessibilityHUDForGestureManager:];
-[_UIStatusBar hoveredActionable];
-[_UIStatusBar _updateStyleAttributes];
-[_UIStatusBar _effectiveStyleFromStyle:];
-[_UIStatusBar updateCompletionHandler];
-[_UIStatusBar dataEntryKeysForItemsWithIdentifiers:];
-[_UIStatusBar setAvoidanceFrame:];
-[_UIStatusBar dependentDataEntryKeys];
-[_UIStatusBar _gestureRecognizer:isInsideActionable:];
-[_UIStatusBar areAnimationsEnabled];
-[_UIStatusBar _effectiveScaleTransform];
-[_UIStatusBar enabledPartIdentifiers];
-[_UIStatusBar _frameForActionable:actionInsets:];
-[_UIStatusBar setRegionActionValidationBlock:];
-[_UIStatusBar stateForDisplayItemWithIdentifier:];
-[_UIStatusBar _accessibilityHUDGestureManager:canCancelGestureRecognizer:];
```
