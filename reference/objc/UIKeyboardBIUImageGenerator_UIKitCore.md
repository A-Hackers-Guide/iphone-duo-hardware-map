# `UIKeyboardBIUImageGenerator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _useButtonShapes;
@"UIImage" _biuBoldImage;
@"UIImage" _biuItalicImage;
@"UIImage" _biuUnderlineImage;
@"NSMutableDictionary" _imageCache;
@"UIColor" _tintColor;
@"UIColor" _normalColor;
```

## Properties

```
@property (T@"UIColor",&,N,V_tintColor) tintColor;
@property (T@"UIColor",&,N,V_normalColor) normalColor;
```

## Instance methods

```
-[UIKeyboardBIUImageGenerator init];
-[UIKeyboardBIUImageGenerator setTintColor:];
-[UIKeyboardBIUImageGenerator tintColor];
-[UIKeyboardBIUImageGenerator _invalidateCache];
-[UIKeyboardBIUImageGenerator BIUImageForBold:italic:underline:];
-[UIKeyboardBIUImageGenerator setNormalColor:];
-[UIKeyboardBIUImageGenerator _accessibilitySettingsChanged:];
-[UIKeyboardBIUImageGenerator _drawBIUAtSize:bold:italic:underline:];
-[UIKeyboardBIUImageGenerator normalColor];
```
