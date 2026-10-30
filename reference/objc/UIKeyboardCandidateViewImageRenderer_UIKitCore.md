# `UIKeyboardCandidateViewImageRenderer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"UIView" _viewForTraitCollection;
@"NSCache" _imageCache;
```

## Properties

```
@property (T@"NSCache",&,N,V_imageCache) imageCache;
@property (T@"UIView",W,N,V_viewForTraitCollection) viewForTraitCollection;
```

## Class methods

```
+[UIKeyboardCandidateViewImageRenderer sharedImageRenderer];
```

## Instance methods

```
-[UIKeyboardCandidateViewImageRenderer setImageCache:];
-[UIKeyboardCandidateViewImageRenderer init];
-[UIKeyboardCandidateViewImageRenderer imageCache];
-[UIKeyboardCandidateViewImageRenderer separatorImageWithColor:height:];
-[UIKeyboardCandidateViewImageRenderer drawGradientImage:startPoint:endPoint:applyScale:];
-[UIKeyboardCandidateViewImageRenderer edgeMaskImageForRightSide:];
-[UIKeyboardCandidateViewImageRenderer extensionMaskImage];
-[UIKeyboardCandidateViewImageRenderer handwritingCellBackgroundImageForDarkKeyboard:highlighted:];
-[UIKeyboardCandidateViewImageRenderer highlightedBarCellBackgroundImageWithColor:insets:];
-[UIKeyboardCandidateViewImageRenderer pocketShadowImageForDarkKeyboard:fadesToBottom:drawShadow:topPadding:bottomPadding:height:];
-[UIKeyboardCandidateViewImageRenderer setViewForTraitCollection:];
-[UIKeyboardCandidateViewImageRenderer viewForTraitCollection];
```
