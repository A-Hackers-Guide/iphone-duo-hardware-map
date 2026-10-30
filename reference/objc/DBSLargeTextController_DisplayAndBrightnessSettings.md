# `DBSLargeTextController`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- 6 instance variables, 3 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"DBSLargeTextSliderListController" _sliderListController;
@"DBSLargeTextSliderListController" _extendedRangeSliderListController;
B _usesExtendedRange;
B _showsResetSliderButton;
B _showsExtendedRangeSwitch;
B _savesCategoryNameOnlyOnSliderEvent;
```

## Properties

```
@property (TB,N,V_showsResetSliderButton) showsResetSliderButton;
@property (TB,N,V_savesCategoryNameOnlyOnSliderEvent) savesCategoryNameOnlyOnSliderEvent;
@property (TB,N,V_showsExtendedRangeSwitch) showsExtendedRangeSwitch;
```

## Instance methods

```
-[DBSLargeTextController init];
-[DBSLargeTextController dealloc];
-[DBSLargeTextController viewDidLayoutSubviews];
-[DBSLargeTextController loadView];
-[DBSLargeTextController sizeCategoryDidChange:];
-[DBSLargeTextController specifiers];
-[DBSLargeTextController addAccessibilitySettingsButtonToSpecifiers:];
-[DBSLargeTextController jumpToAccessibilitySettings:];
-[DBSLargeTextController readPreferredContentSizeCategoryName];
-[DBSLargeTextController readUsesExtendedRange];
-[DBSLargeTextController resetContentSizeCategoryName];
-[DBSLargeTextController savePreferredContentSizeCategoryName:];
-[DBSLargeTextController saveUsesExtendedRange:];
-[DBSLargeTextController savesCategoryNameOnlyOnSliderEvent];
-[DBSLargeTextController setSavesCategoryNameOnlyOnSliderEvent:];
-[DBSLargeTextController setShowsExtendedRangeSwitch:];
-[DBSLargeTextController setShowsResetSliderButton:];
-[DBSLargeTextController setUsesExtendedRange:forSpecifier:];
-[DBSLargeTextController showsExtendedRangeSwitch];
-[DBSLargeTextController showsResetSliderButton];
-[DBSLargeTextController updateSlider];
-[DBSLargeTextController updateSlidersForNewUsesExtendedRangeValue:];
-[DBSLargeTextController usesExtendedRangeForSpecifier:];
```
