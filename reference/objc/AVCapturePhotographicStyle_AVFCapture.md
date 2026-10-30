# `AVCapturePhotographicStyle`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 7 instance methods, 3 class methods

## Instance variables

```
@"AVCaptureSmartStyle" _smartStyle;
@"AVCaptureTextureStyle" _textureStyle;
```

## Properties

```
@property (T@"AVCaptureSmartStyle",R,&,N,V_smartStyle) smartStyle;
@property (T@"AVCaptureTextureStyle",R,&,N,V_textureStyle) textureStyle;
```

## Class methods

```
+[AVCapturePhotographicStyle identityStyle];
+[AVCapturePhotographicStyle styleWithSmartStyle:];
+[AVCapturePhotographicStyle styleWithSmartStyle:textureStyle:];
```

## Instance methods

```
-[AVCapturePhotographicStyle debugDescription];
-[AVCapturePhotographicStyle textureStyle];
-[AVCapturePhotographicStyle smartStyle];
-[AVCapturePhotographicStyle dealloc];
-[AVCapturePhotographicStyle description];
-[AVCapturePhotographicStyle isEqual:];
-[AVCapturePhotographicStyle _initWithSmartStyle:textureStyle:];
```
