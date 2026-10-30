# `_UIContentSizeCategoryPreferenceSystem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIContentSizeCategoryPreference`
- 4 instance variables, 1 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _observingNotification;
B _didCheckForPreferredContentSizeCategoryOverride;
B _applicationOverridesPreferredContentSizeCategory;
@"UIContentSizeCategoryPreference" _overridePreferences;
```

## Properties

```
@property (T@"UIContentSizeCategoryPreference",&,N,V_overridePreferences) overridePreferences;
```

## Instance methods

```
-[_UIContentSizeCategoryPreferenceSystem _updateContentSizeCategory:carPlay:postingNotification:];
-[_UIContentSizeCategoryPreferenceSystem setOverridePreferences:];
-[_UIContentSizeCategoryPreferenceSystem dealloc];
-[_UIContentSizeCategoryPreferenceSystem _endObservingPreferredContentSizeChangedNotification];
-[_UIContentSizeCategoryPreferenceSystem setPreferredContentSizeCategory:];
-[_UIContentSizeCategoryPreferenceSystem _postContentSizeCategoryDidChangeNotification];
-[_UIContentSizeCategoryPreferenceSystem _beginObservingPreferredContentSizeChangedNotification];
-[_UIContentSizeCategoryPreferenceSystem _postContentSizeCategoryDidChangeNotificationForCarPlay:];
-[_UIContentSizeCategoryPreferenceSystem overridePreferences];
-[_UIContentSizeCategoryPreferenceSystem description];
-[_UIContentSizeCategoryPreferenceSystem initAsSystem];
-[_UIContentSizeCategoryPreferenceSystem _postCarPlayContentSizeCategoryDidChangeNotification];
-[_UIContentSizeCategoryPreferenceSystem _updateContentSizeCategoriesFromUserDefaultsPostingNotification:];
-[_UIContentSizeCategoryPreferenceSystem checkForChanges];
-[_UIContentSizeCategoryPreferenceSystem _readAndObservePreferences];
```
