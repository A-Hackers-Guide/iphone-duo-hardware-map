# `AVCapturePersonalPhotographerDuplicateInfo`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
{?="value"q"timescale"i"flags"I"epoch"q} _originalPresentationTimestamp;
{?="value"q"timescale"i"flags"I"epoch"q} _replacedPhotoTimestamp;
q _settingsID;
```

## Properties

```
@property (T{?=qiIq},R) originalPresentationTimestamp;
@property (T{?=qiIq},R) replacedPhotoTimestamp;
@property (Tq,R) settingsID;
```

## Class methods

```
+[AVCapturePersonalPhotographerDuplicateInfo supportsSecureCoding];
```

## Instance methods

```
-[AVCapturePersonalPhotographerDuplicateInfo settingsID];
-[AVCapturePersonalPhotographerDuplicateInfo encodeWithCoder:];
-[AVCapturePersonalPhotographerDuplicateInfo description];
-[AVCapturePersonalPhotographerDuplicateInfo initWithCoder:];
-[AVCapturePersonalPhotographerDuplicateInfo initWithDuplicateInfoDictionary:];
-[AVCapturePersonalPhotographerDuplicateInfo originalPresentationTimestamp];
-[AVCapturePersonalPhotographerDuplicateInfo replacedPhotoTimestamp];
```
