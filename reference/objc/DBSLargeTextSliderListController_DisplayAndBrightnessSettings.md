# `DBSLargeTextSliderListController`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- 9 instance variables, 7 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"PSSpecifier" _sliderGroupSpecifier;
B _viewIsDisappearing;
B _showsExtendedRangeSwitch;
B _usesExtendedRange;
B _showsLargerSizesHelpText;
B _showsResetSliderButton;
@"NSArray" _contentSizeCategories;
q _selectedCategoryIndex;
@"DBSLargeTextController" _largeTextController;
```

## Properties

```
@property (T@"NSArray",C,N,V_contentSizeCategories) contentSizeCategories;
@property (Tq,N,V_selectedCategoryIndex) selectedCategoryIndex;
@property (TB,N,V_showsExtendedRangeSwitch) showsExtendedRangeSwitch;
@property (TB,N,V_usesExtendedRange) usesExtendedRange;
@property (TB,N,V_showsLargerSizesHelpText) showsLargerSizesHelpText;
@property (TB,N,V_showsResetSliderButton) showsResetSliderButton;
@property (T@"DBSLargeTextController",W,N,V_largeTextController) largeTextController;
```

## Instance methods

```
-[DBSLargeTextSliderListController viewWillDisappear:];
-[DBSLargeTextSliderListController viewWillAppear:];
-[DBSLargeTextSliderListController viewDidAppear:];
-[DBSLargeTextSliderListController loadView];
-[DBSLargeTextSliderListController viewSafeAreaInsetsDidChange];
-[DBSLargeTextSliderListController specifiers];
-[DBSLargeTextSliderListController contentSizeCategories];
-[DBSLargeTextSliderListController getDynamicTypeValueForSpecifier:];
-[DBSLargeTextSliderListController initUsingExtendedRange:];
-[DBSLargeTextSliderListController largeTextController];
-[DBSLargeTextSliderListController resetSliderValue];
-[DBSLargeTextSliderListController selectedCategoryIndex];
-[DBSLargeTextSliderListController setContentSizeCategories:];
-[DBSLargeTextSliderListController setDynamicTypeValue:forSpecifier:];
-[DBSLargeTextSliderListController setLargeTextController:];
-[DBSLargeTextSliderListController setSelectedCategoryIndex:];
-[DBSLargeTextSliderListController setShowsExtendedRangeSwitch:];
-[DBSLargeTextSliderListController setShowsLargerSizesHelpText:];
-[DBSLargeTextSliderListController setShowsResetSliderButton:];
-[DBSLargeTextSliderListController setUsesExtendedRange:];
-[DBSLargeTextSliderListController showsExtendedRangeSwitch];
-[DBSLargeTextSliderListController showsLargerSizesHelpText];
-[DBSLargeTextSliderListController showsResetSliderButton];
-[DBSLargeTextSliderListController updateSliderValue];
-[DBSLargeTextSliderListController usesExtendedRange];
```
