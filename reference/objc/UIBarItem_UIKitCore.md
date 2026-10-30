# `UIBarItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCoding`, `UIAppearance`
- 5 instance variables, 19 properties, 20 instance methods, 8 class methods

## Instance variables

```
B _hasCustomizableInstanceAppearanceModifications;
B _shouldArchiveUIAppearanceTags;
@"UIImage" _largeContentSizeImage;
q _tag;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _largeContentSizeImageInsets;
```

## Properties

```
@property (TB,N,S_setHasCustomizableInstanceAppearanceModifications:,V_hasCustomizableInstanceAppearanceModifications) _hasCustomizableInstanceAppearanceModifications;
@property (TB,N,S_setShouldArchiveUIAppearanceTags:,V_shouldArchiveUIAppearanceTags) _shouldArchiveUIAppearanceTags;
@property (T@"NSString",R,C,N) resolvedTitle;
@property (TB,R,N) selected;
@property (TB,R,N) hasTitle;
@property (TB,R,N) hasImage;
@property (TB,D,N,GisEnabled) enabled;
@property (T@"NSString",C,D,N) title;
@property (T@"UIImage",&,D,N) image;
@property (T@"UIImage",&,D,N) landscapeImagePhone;
@property (T@"UIImage",&,N,V_largeContentSizeImage) largeContentSizeImage;
@property (T{UIEdgeInsets=dddd},D,N) imageInsets;
@property (T{UIEdgeInsets=dddd},D,N) landscapeImagePhoneInsets;
@property (T{UIEdgeInsets=dddd},N,V_largeContentSizeImageInsets) largeContentSizeImageInsets;
@property (Tq,N,V_tag) tag;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIBarItem appearance];
+[UIBarItem appearanceForTraitCollection:whenContainedInInstancesOfClasses:];
+[UIBarItem _appearanceBlindViewClasses];
+[UIBarItem _appearanceWhenContainedIn:];
+[UIBarItem appearanceForTraitCollection:];
+[UIBarItem appearanceForTraitCollection:whenContainedIn:];
+[UIBarItem appearanceWhenContainedIn:];
+[UIBarItem appearanceWhenContainedInInstancesOfClasses:];
```

## Instance methods

```
-[UIBarItem setLargeContentSizeImage:];
-[UIBarItem resolvedTitle];
-[UIBarItem hasImage];
-[UIBarItem init];
-[UIBarItem setTag:];
-[UIBarItem largeContentSizeImageInsets];
-[UIBarItem setTitleTextAttributes:forState:];
-[UIBarItem titleTextAttributesForState:];
-[UIBarItem encodeWithCoder:];
-[UIBarItem tag];
-[UIBarItem largeContentSizeImage];
-[UIBarItem initWithCoder:];
-[UIBarItem selected];
-[UIBarItem hasTitle];
-[UIBarItem setLargeContentSizeImageInsets:];
-[UIBarItem _attributedTitleForState:withDefaultAttributes:];
-[UIBarItem _hasCustomizableInstanceAppearanceModifications];
-[UIBarItem _setHasCustomizableInstanceAppearanceModifications:];
-[UIBarItem _setShouldArchiveUIAppearanceTags:];
-[UIBarItem _shouldArchiveUIAppearanceTags];
```
