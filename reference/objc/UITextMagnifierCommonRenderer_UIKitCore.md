# `UITextMagnifierCommonRenderer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 8 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
B m_loaded;
@"NSDictionary" m_images;
@"NSDictionary" m_offsets;
@"CALayer" m_back;
@"CALayer" m_mask;
@"CALayer" m_content;
@"CALayer" m_front;
B _isRegisteredForGeometryChanges;
```

## Instance methods

```
-[UITextMagnifierCommonRenderer update];
-[UITextMagnifierCommonRenderer _geometryChanged:forAncestor:];
-[UITextMagnifierCommonRenderer performOperations:];
-[UITextMagnifierCommonRenderer didMoveToSuperview];
-[UITextMagnifierCommonRenderer backgroundColourIfNecessary];
-[UITextMagnifierCommonRenderer loadImages];
-[UITextMagnifierCommonRenderer magnifier];
-[UITextMagnifierCommonRenderer visualsForMagnifier];
```
