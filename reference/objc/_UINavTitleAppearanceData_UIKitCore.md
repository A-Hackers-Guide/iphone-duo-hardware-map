# `_UINavTitleAppearanceData`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIBarAppearanceData`
- 12 instance variables, 11 properties, 23 instance methods, 2 class methods

## Instance variables

```
@"NSDictionary" _titleTextAttributes;
@"NSDictionary" _largeTitleTextAttributes;
{UIOffset="horizontal"d"vertical"d} _titlePositionAdjustment;
@"_UINavigationBarTitleFontProvider" _titleFontProvider;
q _titleFontProviderIdiom;
B _titleControlHidden;
@"NSDictionary" _titleTextWithSubtitleAttributes;
@"NSDictionary" _largeTitleTextWithSubtitleAttributes;
@"NSDictionary" _inlineLargeTitleTextWithVerticalBarAttributes;
@"NSDictionary" _subtitleTextAttributes;
@"NSDictionary" _largeSubtitleTextAttributes;
@"NSObject" __largeSubtitleTextAttributesForSwift;
```

## Properties

```
@property (T@"NSDictionary",C,N) titleTextAttributes;
@property (T@"NSDictionary",R,C,N) titleTextWithSubtitleAttributes;
@property (T@"NSDictionary",C,N) subtitleTextAttributes;
@property (T{UIOffset=dd},N) titlePositionAdjustment;
@property (T@"NSDictionary",C,N) largeTitleTextAttributes;
@property (T@"NSDictionary",R,C,N) largeTitleTextWithSubtitleAttributes;
@property (T@"NSDictionary",R,C,N) inlineLargeTitleTextWithVerticalBarAttributes;
@property (T@"NSDictionary",C,N) largeSubtitleTextAttributes;
@property (TB,N) titleControlHidden;
@property (T@"NSObject",R,N) _subtitleTextAttributesForSwift;
@property (T@"NSObject",C,N,V__largeSubtitleTextAttributesForSwift) _largeSubtitleTextAttributesForSwift;
```

## Class methods

```
+[_UINavTitleAppearanceData decodeFromCoder:prefix:];
+[_UINavTitleAppearanceData standardTitleDataForIdiom:];
```

## Instance methods

```
-[_UINavTitleAppearanceData describeInto:];
-[_UINavTitleAppearanceData hashInto:];
-[_UINavTitleAppearanceData setSubtitleTextAttributes:];
-[_UINavTitleAppearanceData titleControlHidden];
-[_UINavTitleAppearanceData encodeToCoder:prefix:];
-[_UINavTitleAppearanceData setTitlePositionAdjustment:];
-[_UINavTitleAppearanceData largeSubtitleTextAttributes];
-[_UINavTitleAppearanceData titleTextWithSubtitleAttributes];
-[_UINavTitleAppearanceData largeTitleTextAttributes];
-[_UINavTitleAppearanceData set_largeSubtitleTextAttributesForSwift:];
-[_UINavTitleAppearanceData _subtitleTextAttributesForSwift];
-[_UINavTitleAppearanceData _largeSubtitleTextAttributesForSwift];
-[_UINavTitleAppearanceData setLargeSubtitleTextAttributes:];
-[_UINavTitleAppearanceData setTitleControlHidden:];
-[_UINavTitleAppearanceData subtitleTextAttributes];
-[_UINavTitleAppearanceData largeTitleTextWithSubtitleAttributes];
-[_UINavTitleAppearanceData setTitleTextAttributes:];
-[_UINavTitleAppearanceData titleTextAttributes];
-[_UINavTitleAppearanceData checkEqualTo:];
-[_UINavTitleAppearanceData setLargeTitleTextAttributes:];
-[_UINavTitleAppearanceData replicate];
-[_UINavTitleAppearanceData inlineLargeTitleTextWithVerticalBarAttributes];
-[_UINavTitleAppearanceData titlePositionAdjustment];
```
