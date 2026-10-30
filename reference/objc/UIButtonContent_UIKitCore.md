# `UIButtonContent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCoding`, `NSCopying`
- 10 instance variables, 10 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"NSString" title;
@"NSAttributedString" attributedTitle;
@"UIImage" image;
@"UIImage" background;
@"UIColor" titleColor;
@"UIColor" imageColor;
@"UIColor" shadowColor;
@"NSNumber" drawingStroke;
@"UIImageSymbolConfiguration" preferredSymbolConfiguration;
B isWidthVariant;
```

## Properties

```
@property (T@"NSString",&,N,Vtitle) title;
@property (T@"NSAttributedString",&,N,VattributedTitle) attributedTitle;
@property (T@"UIImage",&,N,Vimage) image;
@property (T@"UIImageSymbolConfiguration",&,N,VpreferredSymbolConfiguration) preferredSymbolConfiguration;
@property (T@"UIImage",&,N,Vbackground) background;
@property (T@"UIColor",&,N,VtitleColor) titleColor;
@property (T@"UIColor",&,N,VimageColor) imageColor;
@property (T@"UIColor",&,N,VshadowColor) shadowColor;
@property (T@"NSNumber",&,N,VdrawingStroke) drawingStroke;
@property (TB,R,D,N) isEmpty;
```

## Instance methods

```
-[UIButtonContent preferredSymbolConfiguration];
-[UIButtonContent drawingStroke];
-[UIButtonContent setBackground:];
-[UIButtonContent titleColor];
-[UIButtonContent imageColor];
-[UIButtonContent setAttributedTitle:];
-[UIButtonContent setPreferredSymbolConfiguration:];
-[UIButtonContent background];
-[UIButtonContent shadowColor];
-[UIButtonContent setDrawingStroke:];
-[UIButtonContent title];
-[UIButtonContent isEmpty];
-[UIButtonContent attributedTitle];
-[UIButtonContent encodeWithCoder:];
-[UIButtonContent setImageColor:];
-[UIButtonContent setTitleColor:];
-[UIButtonContent description];
-[UIButtonContent initWithCoder:];
-[UIButtonContent setTitle:];
-[UIButtonContent setShadowColor:];
-[UIButtonContent image];
-[UIButtonContent copyWithZone:];
-[UIButtonContent updateVariableLengthStringForView:];
-[UIButtonContent setImage:];
```
