# `_UICursorAccessoryView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIVisualEffectView`
- Protocols: `UIGestureRecognizerDelegate`
- 10 instance variables, 8 properties, 27 instance methods, 7 class methods

## Instance variables

```
@"UIView" _activeHighlightBackgroundView;
@"NSMutableOrderedSet" _displayedIdentifiers;
@"NSMutableDictionary" _itemViewsByIdentifier;
@"NSMutableArray" _dividerViews;
@"UITapGestureRecognizer" _accessoryItemTapGestureRecognizer;
B _visionShouldColorSelection;
@"UIView" _containerView;
@"UIColor" _tintColor;
@"<_UICursorAccessoryItemDataSource>" _dataSource;
@"NSArray" _accessoryIdentifiers;
```

## Properties

```
@property (T@"<_UICursorAccessoryItemDataSource>",W,N,V_dataSource) dataSource;
@property (T@"NSArray",&,N,V_accessoryIdentifiers) accessoryIdentifiers;
@property (Td,R,N) activeAccessoryXOffset;
@property (T@"UIColor",&,N) tintColor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UICursorAccessoryView largeItemSize];
+[_UICursorAccessoryView glyphWidth];
+[_UICursorAccessoryView defaultItemSize];
+[_UICursorAccessoryView glyphHeight];
+[_UICursorAccessoryView glassSubvariantName];
+[_UICursorAccessoryView baseFontSize];
+[_UICursorAccessoryView grayscaleLuminance:];
```

## Instance methods

```
-[_UICursorAccessoryView initWithDataSource:];
-[_UICursorAccessoryView activeAccessoryXOffset];
-[_UICursorAccessoryView setAccessoryIdentifiers:animated:];
-[_UICursorAccessoryView _layoutDisplayedAccessoryItemViews];
-[_UICursorAccessoryView _updateBackgroundEffects:];
-[_UICursorAccessoryView layoutSubviews];
-[_UICursorAccessoryView setDataSource:];
-[_UICursorAccessoryView accessoryIdentifiers];
-[_UICursorAccessoryView sizeThatFits:];
-[_UICursorAccessoryView setTintColor:];
-[_UICursorAccessoryView setAccessoryIdentifiers:];
-[_UICursorAccessoryView dataSource];
-[_UICursorAccessoryView _layoutHighlightView];
-[_UICursorAccessoryView _applyCornerMaskToSelf];
-[_UICursorAccessoryView _cleanupRemovedItemViews];
-[_UICursorAccessoryView gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[_UICursorAccessoryView tintColor];
-[_UICursorAccessoryView _reloadAccessoryItemViews];
-[_UICursorAccessoryView _scheduleRemovedItemViewCleanup];
-[_UICursorAccessoryView tintColorAdjusted:];
-[_UICursorAccessoryView _allItemViewsActive];
-[_UICursorAccessoryView _layoutContainerView];
-[_UICursorAccessoryView _displayedItemViewAtIndex:];
-[_UICursorAccessoryView _needsContainerGlass];
-[_UICursorAccessoryView _ensureNumberOfReusableViews:inArray:ofClass:];
-[_UICursorAccessoryView _unionRectActiveItems];
-[_UICursorAccessoryView _didRecognizeAccessoryTapGestureRecognizer:];
```
