# `_UINavigationItemProxy`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UINavigationItemChangeObserver`
- 2 instance variables, 4 properties, 34 instance methods, 1 class methods

## Instance variables

```
@"UINavigationItem" _destinationNavigationItem;
@"UINavigationItem" _sourceNavigationItem;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UINavigationItemProxy transferPropertiesFromItem:toDestinationItem:];
```

## Instance methods

```
-[_UINavigationItemProxy navigationItemUpdatedNavigationBarVisibility:];
-[_UINavigationItemProxy navigationItemUpdatedCanvasView:];
-[_UINavigationItemProxy navigationItemUpdatedSearchController:oldSearchController:];
-[_UINavigationItemProxy navigationItemUpdatedToolbarAvoidsKeyboard:];
-[_UINavigationItemProxy navigationItem:appearance:categoriesChanged:];
-[_UINavigationItemProxy navigationItemUpdatedLargeTitleContent:];
-[_UINavigationItemProxy navigationItemUpdatedBackButtonContent:animated:];
-[_UINavigationItemProxy navigationItemUpdatedSearchBarPlacementAllowsToolbarIntegration:];
-[_UINavigationItemProxy navigationItemUpdatedNavigationBarSafeAreaAdjustment:];
-[_UINavigationItemProxy navigationItemUpdatedScrollEdgeProgress:];
-[_UINavigationItemProxy navigationItemUpdatedRightBarButtonItems:animated:];
-[_UINavigationItemProxy navigationItemUpdatedTitleContent:animated:];
-[_UINavigationItemProxy navigationItemUpdatedMinimumContentMargins:];
-[_UINavigationItemProxy navigationItemUpdatedPromptContent:];
-[_UINavigationItemProxy navigationItemUpdatedCenterBarButtonItems:animated:];
-[_UINavigationItemProxy navigationItemUpdatedSearchBarPlacementAllowsExternalIntegration:];
-[_UINavigationItemProxy navigationItemIsTopItem:];
-[_UINavigationItemProxy presentationSourceForContent:navigationItem:];
-[_UINavigationItemProxy shouldSearchControllerDeferPresentationTransitionForNavigationItem:];
-[_UINavigationItemProxy navigationItemUpdatedLeftBarButtonItems:animated:];
-[_UINavigationItemProxy navigationItemUpdatedAdditionalOverflowItems:];
-[_UINavigationItemProxy navigationItemUpdatedBarCompressionBehavior:];
-[_UINavigationItemProxy navigationItemUpdatedBackgroundAppearance:];
-[_UINavigationItemProxy navigationItemUpdatedLargeTitleDisplayMode:];
-[_UINavigationItemProxy navigationItemSearchControllerReadyForDeferredAutomaticShowsScopeBar:];
-[_UINavigationItemProxy navigationItem:updatedPalettePart:oldPalette:];
-[_UINavigationItemProxy navigationItemUpdatedBottomPalette:oldPalette:];
-[_UINavigationItemProxy navigationItemUpdatedContentLayout:animated:];
-[_UINavigationItemProxy navigationItemIsBackItem:];
-[_UINavigationItemProxy navigationItemUpdatedMinimizeBehavior:];
-[_UINavigationItemProxy reloadDestinationItemFromSource];
-[_UINavigationItemProxy initWithDestinationNavigationItem:sourceNavigationItem:];
-[_UINavigationItemProxy navigationItemUpdatedAllowsInteractivePopWhenBackButtonHidden:];
-[_UINavigationItemProxy navigationItemUpdatedAllowsInteractivePopWhenNavigationBarHidden:];
```
