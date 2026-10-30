# `CSIBitmapWrapper`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 25 instance variables, 17 properties, 45 instance methods, 0 class methods

## Instance variables

```
^{CGContext=} _bitmapContext;
@"NSData" _pixelData;
I _pixelFormat;
I _width;
I _height;
Q _rowbytes;
B _allowsMultiPassEncoding;
B _allowsOptimalRowbytesPacking;
B _allowsCompactCompression;
B _allowsPaletteImageCompression;
B _allowsHevcCompression;
B _allowsDeepmapImageCompression;
B _allowsDeepmap2ImageCompression;
B _flipped;
^{CGImage=} _sourceImage;
^{CGImage=} _destImage;
q _texturePixelFormat;
I _imageAlpha;
d _compressionQuality;
q _compressionType;
Q _colorSpaceID;
q _textureInterpretation;
i _exifOrientation;
q _targetPlatform;
@"NSString" _name;
```

## Properties

```
@property (TI,N,V_pixelFormat) pixelFormat;
@property (TB,V_allowsMultiPassEncoding) allowsMultiPassEncoding;
@property (TB,V_allowsOptimalRowbytesPacking) allowsOptimalRowbytesPacking;
@property (TB) allowsCompactCompression;
@property (TB,V_allowsPaletteImageCompression) allowsPaletteImageCompression;
@property (TB,V_allowsHevcCompression) allowsHevcCompression;
@property (TB,V_allowsDeepmapImageCompression) allowsDeepmapImageCompression;
@property (TB,V_allowsDeepmap2ImageCompression) allowsDeepmap2ImageCompression;
@property (TB,N,V_flipped) flipped;
@property (Td,N,V_compressionQuality) compressionQuality;
@property (Tq,V_targetPlatform) targetPlatform;
@property (Tq,V_compressionType) compressionType;
@property (TQ,N,V_colorSpaceID) colorSpaceID;
@property (Tq,N,V_textureInterpretation) textureInterpretation;
@property (Ti,N,V_exifOrientation) exifOrientation;
@property (T@"NSString",N,V_name) name;
@property (TQ,N) rowbytes;
```

## Instance methods

```
-[CSIBitmapWrapper compressionQuality];
-[CSIBitmapWrapper targetPlatform];
-[CSIBitmapWrapper compressionType];
-[CSIBitmapWrapper setAllowsPaletteImageCompression:];
-[CSIBitmapWrapper setCompressionQuality:];
-[CSIBitmapWrapper setColorSpaceID:];
-[CSIBitmapWrapper setCompressionType:];
-[CSIBitmapWrapper setTargetPlatform:];
-[CSIBitmapWrapper colorSpaceID];
-[CSIBitmapWrapper allowsDeepmapImageCompression];
-[CSIBitmapWrapper allowsDeepmap2ImageCompression];
-[CSIBitmapWrapper setPixelData:];
-[CSIBitmapWrapper textureInterpretation];
-[CSIBitmapWrapper setAllowsCompactCompression:];
-[CSIBitmapWrapper setFlipped:];
-[CSIBitmapWrapper sourceAlphaInfo];
-[CSIBitmapWrapper exifOrientation];
-[CSIBitmapWrapper allowsHevcCompression];
-[CSIBitmapWrapper dealloc];
-[CSIBitmapWrapper initWithCGImage:width:height:texturePixelFormat:];
-[CSIBitmapWrapper allowsMultiPassEncoding];
-[CSIBitmapWrapper rowbytes];
-[CSIBitmapWrapper setSourceAlphaInfo:];
-[CSIBitmapWrapper allowsPaletteImageCompression];
-[CSIBitmapWrapper setRowbytes:];
-[CSIBitmapWrapper compressedData:usedEncoding:andRowChunkSize:];
-[CSIBitmapWrapper setAllowsOptimalRowbytesPacking:];
-[CSIBitmapWrapper pixelData];
-[CSIBitmapWrapper allowsCompactCompression];
-[CSIBitmapWrapper setTextureInterpretation:];
-[CSIBitmapWrapper setAllowsDeepmap2ImageCompression:];
-[CSIBitmapWrapper setAllowsMultiPassEncoding:];
-[CSIBitmapWrapper bitmapContext];
-[CSIBitmapWrapper setName:];
-[CSIBitmapWrapper setAllowsHevcCompression:];
-[CSIBitmapWrapper setExifOrientation:];
-[CSIBitmapWrapper allowsOptimalRowbytesPacking];
-[CSIBitmapWrapper pixelFormat];
-[CSIBitmapWrapper flipped];
-[CSIBitmapWrapper initWithPixelWidth:pixelHeight:];
-[CSIBitmapWrapper width];
-[CSIBitmapWrapper setPixelFormat:];
-[CSIBitmapWrapper name];
-[CSIBitmapWrapper height];
-[CSIBitmapWrapper setAllowsDeepmapImageCompression:];
```
