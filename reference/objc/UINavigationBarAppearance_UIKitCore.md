# `UINavigationBarAppearance`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIBarAppearance`
- Protocols: `_UIBarButtonItemAppearanceChangeObserver`
- 8 instance variables, 20 properties, 48 instance methods, 1 class methods

## Instance variables

```
@"_UINavTitleAppearanceData" _barTitleData;
@"UIBarButtonItemAppearance" _buttonAppearance;
@"UIBarButtonItemAppearance" _prominentButtonAppearance;
@"UIBarButtonItemAppearance" _backButtonAppearance;
@"_UINavigationBarVisualProvider" _visualProvider;
q __backgroundVisibility;
d __backgroundVisibilityOnScrollDistance;
@"NSDictionary" __subtitleTextAttributes;
```

## Properties

```
@property (T@"_UINavigationBarVisualProvider",R,N,V_visualProvider) visualProvider;
@property (Tq,N,V__backgroundVisibility) _backgroundVisibility;
@property (Td,N,V__backgroundVisibilityOnScrollDistance) _backgroundVisibilityOnScrollDistance;
@property (TB,N,S_setTitleControlHidden:) _titleControlHidden;
@property (T@"NSDictionary",C,N,S_setSubtitleTextAttributes:,V__subtitleTextAttributes) _subtitleTextAttributes;
@property (T@"NSDictionary",C,N) titleTextAttributes;
@property (T{UIOffset=dd},N) titlePositionAdjustment;
@property (T@"NSDictionary",C,N) subtitleTextAttributes;
@property (T@"NSDictionary",C,N) largeTitleTextAttributes;
@property (T@"NSDictionary",C,N) largeSubtitleTextAttributes;
@property (T@"UIBarButtonItemAppearance",C,N,V_buttonAppearance) buttonAppearance;
@property (T@"UIBarButtonItemAppearance",C,N,V_prominentButtonAppearance) prominentButtonAppearance;
@property (T@"UIBarButtonItemAppearance",C,N,V_backButtonAppearance) backButtonAppearance;
@property (T@"UIImage",R,N) backIndicatorImage;
@property (T@"UIImage",R,N) backIndicatorTransitionMaskImage;
@property (T@"UIBarButtonItemAppearance",C,N) doneButtonAppearance;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UINavigationBarAppearance supportsSecureCoding];
```

## Instance methods

```
-[UINavigationBarAppearance _defaultBackgroundData];
-[UINavigationBarAppearance visualProvider];
-[UINavigationBarAppearance setSubtitleTextAttributes:];
-[UINavigationBarAppearance _setSubtitleTextAttributes:];
-[UINavigationBarAppearance prominentButtonAppearance];
-[UINavigationBarAppearance setButtonAppearance:];
-[UINavigationBarAppearance setTitlePositionAdjustment:];
-[UINavigationBarAppearance largeSubtitleTextAttributes];
-[UINavigationBarAppearance _backButtonAppearance];
-[UINavigationBarAppearance setBackButtonAppearance:];
-[UINavigationBarAppearance _checkEqualTo:];
-[UINavigationBarAppearance _prominentButtonAppearance];
-[UINavigationBarAppearance largeTitleTextAttributes];
-[UINavigationBarAppearance _barTitleData];
-[UINavigationBarAppearance set_backgroundVisibility:];
-[UINavigationBarAppearance _describeInto:];
-[UINavigationBarAppearance setLargeSubtitleTextAttributes:];
-[UINavigationBarAppearance _decodeFromCoder:];
-[UINavigationBarAppearance _setupDefaults];
-[UINavigationBarAppearance set_backgroundVisibilityOnScrollDistance:];
-[UINavigationBarAppearance setProminentButtonAppearance:];
-[UINavigationBarAppearance _plainButtonAppearanceData];
-[UINavigationBarAppearance setBackIndicatorImage:transitionMaskImage:];
-[UINavigationBarAppearance _setTitleControlHidden:];
-[UINavigationBarAppearance _backgroundVisibility];
-[UINavigationBarAppearance encodeWithCoder:];
-[UINavigationBarAppearance subtitleTextAttributes];
-[UINavigationBarAppearance buttonAppearance];
-[UINavigationBarAppearance backIndicatorTransitionMaskImage];
-[UINavigationBarAppearance backButtonAppearance];
-[UINavigationBarAppearance _subtitleTextAttributes];
-[UINavigationBarAppearance doneButtonAppearance];
-[UINavigationBarAppearance setTitleTextAttributes:];
-[UINavigationBarAppearance _plainButtonAppearance];
-[UINavigationBarAppearance titleTextAttributes];
-[UINavigationBarAppearance _backButtonAppearanceData];
-[UINavigationBarAppearance setLargeTitleTextAttributes:];
-[UINavigationBarAppearance backIndicatorImage];
-[UINavigationBarAppearance _prominentButtonAppearanceData];
-[UINavigationBarAppearance _titleControlHidden];
-[UINavigationBarAppearance _completeInit];
-[UINavigationBarAppearance _barButtonItemDataChanged:];
-[UINavigationBarAppearance _hashInto:];
-[UINavigationBarAppearance titlePositionAdjustment];
-[UINavigationBarAppearance _barButtonItemAppearanceChangedItemData:toItemData:fromItemData:];
-[UINavigationBarAppearance _copyFromAppearance:];
-[UINavigationBarAppearance _backgroundVisibilityOnScrollDistance];
-[UINavigationBarAppearance setDoneButtonAppearance:];
```
