# `UIKBSplitImageView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 8 instance variables, 1 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _canStretchAsFullWidth;
@"UIImageView" _fullView;
@"UIImageView" _splitLeft;
@"UIImageView" _splitRight;
@"NSString" _currentFilterType;
@"NSArray" _splitConstraints;
@"NSLayoutConstraint" _leftWidthConstraint;
@"NSLayoutConstraint" _rightWidthConstraint;
```

## Properties

```
@property (T@"NSString",&,N,V_currentFilterType) filterType;
```

## Instance methods

```
-[UIKBSplitImageView initWithFrame:canStretchAsFullWidth:];
-[UIKBSplitImageView addExtraFilters:];
-[UIKBSplitImageView insertSubviewAtBottom:];
-[UIKBSplitImageView setImage:cachedWidth:keyplane:];
-[UIKBSplitImageView prepareForDisplay:];
-[UIKBSplitImageView setContentsMultiplyColor:];
-[UIKBSplitImageView setImage:splitLeft:splitRight:keyplane:];
-[UIKBSplitImageView clearImages];
-[UIKBSplitImageView _shouldInheritScreenScaleAsContentScaleFactor];
-[UIKBSplitImageView filterType];
-[UIKBSplitImageView setFilterType:];
```
