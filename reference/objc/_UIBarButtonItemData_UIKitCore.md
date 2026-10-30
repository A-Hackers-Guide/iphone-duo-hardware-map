# `_UIBarButtonItemData`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIBarAppearanceData`
- Protocols: `_UIBarButtonItemDataFallback`
- 14 instance variables, 17 properties, 44 instance methods, 3 class methods

## Instance variables

```
[4@"NSDictionary"] _titleTextAttributes;
[4@"UIImage"] _backgroundImage;
[4{UIOffset="horizontal"d"vertical"d}] _titlePositionAdjustment;
[4{UIOffset="horizontal"d"vertical"d}] _backgroundImagePositionAdjustment;
@"UIImageSymbolConfiguration" _imageSymbolConfiguration;
@"UIImageSymbolConfiguration" _compactImageSymbolConfiguration;
@"UIImage" _backIndicatorImage;
@"UIImage" _backIndicatorTransitionMaskImage;
@"UIImageSymbolConfiguration" _backIndicatorSymbolConfiguration;
@"UIImageSymbolConfiguration" _compactBackIndicatorSymbolConfiguration;
@"<_UIBarButtonItemDataFallback>" _fallback;
[4{?="hasUserFont"b1"hasUserColor"b1"hasUserTitlePosition"b1"hasUserBackgroundImage"b1"hasUserBackgroundImagePosition"b1}] _stateFlags;
{?="isBackButtonData"b1} _dataFlags;
q _style;
```

## Properties

```
@property (Tq,R,N,V_style) style;
@property (TB,R,N) isBackButtonData;
@property (T@"<_UIBarButtonItemDataFallback>",R,N) fallback;
@property (T@"UIImageSymbolConfiguration",R,N) imageSymbolConfiguration;
@property (T@"UIImageSymbolConfiguration",R,N) compactImageSymbolConfiguration;
@property (T@"UIImage",R,N) backIndicatorImage;
@property (T@"UIImage",R,N) backIndicatorTransitionMaskImage;
@property (T@"UIImage",R,N) compactBackIndicatorImage;
@property (T@"UIImage",R,N) compactBackIndicatorTransitionMaskImage;
@property (T@"UIImageSymbolConfiguration",R,N) backIndicatorSymbolConfiguration;
@property (T@"UIImageSymbolConfiguration",R,N) backIndicatorTransitionMaskSymbolConfiguration;
@property (T@"UIImageSymbolConfiguration",R,N) compactBackIndicatorSymbolConfiguration;
@property (T@"UIImageSymbolConfiguration",R,N) compactBackIndicatorTransitionMaskSymbolConfiguration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIBarButtonItemData standardBackButtonData];
+[_UIBarButtonItemData standardItemDataForStyle:];
+[_UIBarButtonItemData decodeFromCoder:prefix:];
```

## Instance methods

```
-[_UIBarButtonItemData describeInto:];
-[_UIBarButtonItemData imageSymbolConfiguration];
-[_UIBarButtonItemData hashInto:];
-[_UIBarButtonItemData fallback];
-[_UIBarButtonItemData _decodeTitleTextAttributesFromCoder:prefix:];
-[_UIBarButtonItemData dataWithNewFallback:];
-[_UIBarButtonItemData compactBackIndicatorTransitionMaskSymbolConfiguration];
-[_UIBarButtonItemData encodeToCoder:prefix:];
-[_UIBarButtonItemData fontForState:style:];
-[_UIBarButtonItemData backIndicatorTransitionMaskSymbolConfiguration];
-[_UIBarButtonItemData _decodeBackgroundPositionAdjustmentsFromCoder:prefix:];
-[_UIBarButtonItemData backIndicatorTextStyleForSymbolConfiguration];
-[_UIBarButtonItemData titlePositionAdjustmentForState:style:];
-[_UIBarButtonItemData backgroundImagePositionAdjustmentForState:];
-[_UIBarButtonItemData titlePositionAdjustmentForState:];
-[_UIBarButtonItemData initWithStyle:];
-[_UIBarButtonItemData backgroundImagePositionAdjustmentForState:style:];
-[_UIBarButtonItemData style];
-[_UIBarButtonItemData compactBackIndicatorImage];
-[_UIBarButtonItemData setTitleTextAttributes:forState:];
-[_UIBarButtonItemData copyAsBackButtonDataWithIndicatorsAndFallbackFrom:];
-[_UIBarButtonItemData compactBackIndicatorTransitionMaskImage];
-[_UIBarButtonItemData backgroundImageForState:];
-[_UIBarButtonItemData _fallbackColorForState:];
-[_UIBarButtonItemData setBackIndicatorImage:transitionMaskImage:];
-[_UIBarButtonItemData titleTextAttributesForState:];
-[_UIBarButtonItemData _decodeBackgroundImagesFromCoder:prefix:];
-[_UIBarButtonItemData textStyleForSymbolConfiguration];
-[_UIBarButtonItemData _decodeTitlePositionAdjustmentsFromCoder:prefix:];
-[_UIBarButtonItemData compactBackIndicatorSymbolConfiguration];
-[_UIBarButtonItemData backgroundImageForState:style:];
-[_UIBarButtonItemData backIndicatorTransitionMaskImage];
-[_UIBarButtonItemData colorForState:style:];
-[_UIBarButtonItemData backIndicatorSymbolConfiguration];
-[_UIBarButtonItemData setTitlePositionAdjustment:forState:];
-[_UIBarButtonItemData compactImageSymbolConfiguration];
-[_UIBarButtonItemData _fallbackFontForState:];
-[_UIBarButtonItemData checkEqualTo:];
-[_UIBarButtonItemData isBackButtonData];
-[_UIBarButtonItemData backIndicatorImage];
-[_UIBarButtonItemData resetBackIndicatorImages];
-[_UIBarButtonItemData setBackgroundImagePositionAdjustment:forState:];
-[_UIBarButtonItemData replicate];
-[_UIBarButtonItemData setBackgroundImage:forState:];
```
