# `AVCapturePersonalPhotographerMetadata`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _manualCapture;
f _frameScore;
i _frameID;
I _sessionID;
@"NSString" _detectedContext;
@"AVCapturePersonalPhotographerDuplicateInfo" _duplicateInfo;
```

## Properties

```
@property (TB,R) manualCapture;
@property (Tf,R) frameScore;
@property (Ti,R) frameID;
@property (TI,R) sessionID;
@property (T@"NSString",R) detectedContext;
@property (T@"AVCapturePersonalPhotographerDuplicateInfo",R) duplicateInfo;
```

## Class methods

```
+[AVCapturePersonalPhotographerMetadata supportsSecureCoding];
```

## Instance methods

```
-[AVCapturePersonalPhotographerMetadata sessionID];
-[AVCapturePersonalPhotographerMetadata dealloc];
-[AVCapturePersonalPhotographerMetadata frameID];
-[AVCapturePersonalPhotographerMetadata duplicateInfo];
-[AVCapturePersonalPhotographerMetadata encodeWithCoder:];
-[AVCapturePersonalPhotographerMetadata description];
-[AVCapturePersonalPhotographerMetadata initWithCoder:];
-[AVCapturePersonalPhotographerMetadata detectedContext];
-[AVCapturePersonalPhotographerMetadata frameScore];
-[AVCapturePersonalPhotographerMetadata initWithPersonalPhotographerMetadataDictionary:];
-[AVCapturePersonalPhotographerMetadata manualCapture];
```
