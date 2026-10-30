# `CATintedImage`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 2 properties, 12 instance methods, 5 class methods

## Instance variables

```
^{CGImage=} _image;
^{CGColor=} _tint;
I _copy_flags;
```

## Properties

```
@property (T^{CGImage=},&,V_image) image;
@property (T^{CGColor=},&,V_tint) tint;
```

## Class methods

```
+[CATintedImage supportsSecureCoding];
+[CATintedImage tintedImageWithCGImage:tint:copyFlags:];
+[CATintedImage tintedImageWithCGImage:tint:];
+[CATintedImage CAMLParserStartElement:];
+[CATintedImage tintedImageWithCABackingStore:];
```

## Instance methods

```
-[CATintedImage CAMLTypeForKey:];
-[CATintedImage CAMLParser:setValue:forKey:];
-[CATintedImage dealloc];
-[CATintedImage CA_copyRenderValue];
-[CATintedImage tint];
-[CATintedImage setTint:];
-[CATintedImage encodeWithCAMLWriter:];
-[CATintedImage encodeWithCoder:];
-[CATintedImage initWithCoder:];
-[CATintedImage image];
-[CATintedImage CA_prepareRenderValue];
-[CATintedImage setImage:];
```
