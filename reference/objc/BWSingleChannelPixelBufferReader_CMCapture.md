# `BWSingleChannelPixelBufferReader`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 8 instance methods, 3 class methods

## Instance variables

```
^{__CVBuffer=} _pixelBuffer;
r* _baseData;
Q _row;
r* _rowData;
Q _width;
Q _height;
```

## Properties

```
@property (TQ,R,N,V_width) width;
@property (TQ,R,N,V_height) height;
@property (TQ,N,V_row) row;
```

## Class methods

```
+[BWSingleChannelPixelBufferReader supportedPixelFormats];
+[BWSingleChannelPixelBufferReader newReaderWithPixelBuffer:];
+[BWSingleChannelPixelBufferReader supportedPixelFormatsAsString];
```

## Instance methods

```
-[BWSingleChannelPixelBufferReader row];
-[BWSingleChannelPixelBufferReader dealloc];
-[BWSingleChannelPixelBufferReader width];
-[BWSingleChannelPixelBufferReader initWithPixelBuffer:];
-[BWSingleChannelPixelBufferReader height];
-[BWSingleChannelPixelBufferReader setRow:];
-[BWSingleChannelPixelBufferReader _internalReadPixelValueAtColumn:];
-[BWSingleChannelPixelBufferReader pixelValueAtColumn:];
```
