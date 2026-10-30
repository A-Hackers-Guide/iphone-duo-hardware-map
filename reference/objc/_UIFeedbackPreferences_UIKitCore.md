# `_UIFeedbackPreferences`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _enabledFeedbackTypes;
@"NSDictionary" _defaultFeedbackTypes;
@"NSUserDefaults" _userDefaults;
```

## Properties

```
@property (T@"NSDictionary",R,N,V_defaultFeedbackTypes) defaultFeedbackTypes;
@property (T@"NSUserDefaults",&,N,V_userDefaults) userDefaults;
```

## Class methods

```
+[_UIFeedbackPreferences sharedPreferences];
```

## Instance methods

```
-[_UIFeedbackPreferences userDefaults];
-[_UIFeedbackPreferences observeValueForKeyPath:ofObject:change:context:];
-[_UIFeedbackPreferences _categoryForNullableCategory:];
-[_UIFeedbackPreferences init];
-[_UIFeedbackPreferences enabledFeedbackTypesForCategory:];
-[_UIFeedbackPreferences _invalidate];
-[_UIFeedbackPreferences _setEnabledFeedbackTypes:forCategory:postNotification:];
-[_UIFeedbackPreferences defaultFeedbackTypes];
-[_UIFeedbackPreferences _defaultKeyForCategoryKey:type:];
-[_UIFeedbackPreferences setUserDefaults:];
-[_UIFeedbackPreferences _defaultFeedbackTypesForCategory:];
-[_UIFeedbackPreferences _setEnabledFeedbackTypes:forCategory:];
-[_UIFeedbackPreferences _updateEnabledFeedbackTypes:forKey:type:];
-[_UIFeedbackPreferences _enabledFeedbackTypesForCategory:];
-[_UIFeedbackPreferences _startObservingDefaults];
-[_UIFeedbackPreferences _categoryKeyForCategory:type:];
-[_UIFeedbackPreferences _accessibilityForceTouchChanged:];
```
