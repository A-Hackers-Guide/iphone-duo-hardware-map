# `AVCaptureTextureStyle`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 9 instance methods, 3 class methods

## Instance variables

```
@"NSString" _preset;
f _intensity;
f _grain;
Q _hash;
q _version;
```

## Properties

```
@property (T@"NSString",R,N,V_preset) preset;
@property (Tf,R,N,V_intensity) intensity;
@property (Tf,R,N,V_grain) grain;
@property (Tq,R,N,V_version) version;
```

## Class methods

```
+[AVCaptureTextureStyle identityStyle];
+[AVCaptureTextureStyle styleWithPreset:intensity:];
+[AVCaptureTextureStyle styleWithPreset:intensity:grain:];
```

## Instance methods

```
-[AVCaptureTextureStyle intensity];
-[AVCaptureTextureStyle debugDescription];
-[AVCaptureTextureStyle preset];
-[AVCaptureTextureStyle dealloc];
-[AVCaptureTextureStyle version];
-[AVCaptureTextureStyle description];
-[AVCaptureTextureStyle isEqual:];
-[AVCaptureTextureStyle _initWithPreset:intensity:grain:];
-[AVCaptureTextureStyle grain];
```
