# `EspressoDataFrameImageAttachment`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EspressoDataFrameAttachment`
- 2 instance variables, 1 properties, 4 instance methods, 1 class methods

## Instance variables

```
{vImage_Buffer="data"^v"height"Q"width"Q"rowBytes"Q} buffer;
i _nChannels;
```

## Properties

```
@property (Ti,V_nChannels) nChannels;
```

## Class methods

```
+[EspressoDataFrameImageAttachment createCVPixelBufferFromvImage:withPixelFormat:];
```

## Instance methods

```
-[EspressoDataFrameImageAttachment copyAsImageGrayscaleOrBGRA];
-[EspressoDataFrameImageAttachment loadFromDict:frameStorage:];
-[EspressoDataFrameImageAttachment nChannels];
-[EspressoDataFrameImageAttachment setNChannels:];
```
