# `_UIResizableImage`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIImage`
- 3 instance variables, 0 properties, 19 instance methods, 1 class methods

## Instance variables

```
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _capInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _subimageInsets;
{?="alwaysStretches"b1"isSubimage"b1} _rImageFlags;
```

## Class methods

```
+[_UIResizableImage supportsSecureCoding];
```

## Instance methods

```
-[_UIResizableImage _suppressesAccessibilityHairlineThickening];
-[_UIResizableImage _configureImage:assumePreconfigured:];
-[_UIResizableImage _contentStretchInPixels];
-[_UIResizableImage _isTiledWhenStretchedToSize:];
-[_UIResizableImage capInsets];
-[_UIResizableImage _setAlwaysStretches:];
-[_UIResizableImage _subimageInsets];
-[_UIResizableImage _setSubimageInsets:];
-[_UIResizableImage _contentRectInPixels];
-[_UIResizableImage _resizableImageWithCapMask:];
-[_UIResizableImage encodeWithCoder:];
-[_UIResizableImage initWithImage:capInsets:];
-[_UIResizableImage initWithCoder:];
-[_UIResizableImage _isResizable];
-[_UIResizableImage resizingMode];
-[_UIResizableImage _setCapInsets:];
-[_UIResizableImage _isSubimage];
-[_UIResizableImage isEqual:];
-[_UIResizableImage _contentRectInPixelsApplyingInsets:emptySizeFallback:];
```
