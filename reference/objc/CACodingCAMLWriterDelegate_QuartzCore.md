# `CACodingCAMLWriterDelegate`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMLWriterDelegate`
- 5 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSString" _resourceDir;
i _serial;
@"NSString" _imageFormat;
@"NSDictionary" _imageEncodeOptions;
B _skipHiddenLayers;
```

## Properties

```
@property (T@"NSString",C,V_imageFormat) imageFormat;
@property (T@"NSDictionary",C,V_imageEncodeOptions) imageEncodeOptions;
@property (TB,V_skipHiddenLayers) skipHiddenLayers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CACodingCAMLWriterDelegate dealloc];
-[CACodingCAMLWriterDelegate CAMLWriter:URLForResource:];
-[CACodingCAMLWriterDelegate CAMLWriter:typeForObject:];
-[CACodingCAMLWriterDelegate setImageFormat:];
-[CACodingCAMLWriterDelegate CAMLWriter:shouldEncodeObject:];
-[CACodingCAMLWriterDelegate imageEncodeOptions];
-[CACodingCAMLWriterDelegate imageFormat];
-[CACodingCAMLWriterDelegate initWithResourceDir:];
-[CACodingCAMLWriterDelegate setImageEncodeOptions:];
-[CACodingCAMLWriterDelegate setSkipHiddenLayers:];
-[CACodingCAMLWriterDelegate skipHiddenLayers];
```
