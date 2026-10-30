# `UIContentSizeCategoryPreference`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 12 instance methods, 10 class methods

## Instance variables

```
@"NSString" _preferredContentSizeCategory;
@"NSString" _preferredContentSizeCategoryCarPlay;
```

## Properties

```
@property (T@"NSString",C,N,V_preferredContentSizeCategory) preferredContentSizeCategory;
@property (T@"NSString",C,N,V_preferredContentSizeCategoryCarPlay) preferredContentSizeCategoryCarPlay;
```

## Class methods

```
+[UIContentSizeCategoryPreference resetSystemPreferenceOverride];
+[UIContentSizeCategoryPreference asyncOverrideSystemWithPreference:];
+[UIContentSizeCategoryPreference overrideSystemWithPreference:];
+[UIContentSizeCategoryPreference asyncResetSystemPreferenceOverride];
+[UIContentSizeCategoryPreference _resetSystemPreferenceOverride];
+[UIContentSizeCategoryPreference _populateUserDefaultsContentSizeCategory:carPlay:];
+[UIContentSizeCategoryPreference overrideSystemWithPreference:forBlock:];
+[UIContentSizeCategoryPreference _overrideSystemPreferenceToContentSizeCategory:];
+[UIContentSizeCategoryPreference _overrideSystemPreferenceToContentSizeCategory:forBlock:];
+[UIContentSizeCategoryPreference system];
```

## Instance methods

```
-[UIContentSizeCategoryPreference preferredContentSizeCategory];
-[UIContentSizeCategoryPreference init];
-[UIContentSizeCategoryPreference setPreferredContentSizeCategory:];
-[UIContentSizeCategoryPreference setPreferredContentSizeCategoryCarPlay:];
-[UIContentSizeCategoryPreference initWithContentSizeCategory:carPlay:];
-[UIContentSizeCategoryPreference initWithRawUserDefaults];
-[UIContentSizeCategoryPreference hash];
-[UIContentSizeCategoryPreference description];
-[UIContentSizeCategoryPreference preferredContentSizeCategoryCarPlay];
-[UIContentSizeCategoryPreference initWithContentSizeCategory:];
-[UIContentSizeCategoryPreference isEqual:];
-[UIContentSizeCategoryPreference checkForChanges];
```
