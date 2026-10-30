# `BWPhotoDescriptor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 5 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSString" _photoIdentifier;
I _processingFlags;
@"NSDate" _time;
B _timeHasBeenSet;
@"NSTimeZone" _timeZone;
B _timeZoneHasBeenSet;
{?="value"q"timescale"i"flags"I"epoch"q} _presentationTimeStamp;
B _presentationTimeStampHasBeenSet;
```

## Properties

```
@property (T@"NSString",R,N,V_photoIdentifier) photoIdentifier;
@property (TI,R,N,V_processingFlags) processingFlags;
@property (T@"NSDate",&,N) time;
@property (T@"NSTimeZone",&,N) timeZone;
@property (T{?=qiIq},N) presentationTimeStamp;
```

## Class methods

```
+[BWPhotoDescriptor supportsSecureCoding];
```

## Instance methods

```
-[BWPhotoDescriptor setTimeZone:];
-[BWPhotoDescriptor dealloc];
-[BWPhotoDescriptor presentationTimeStamp];
-[BWPhotoDescriptor initWithPhotoIdentifier:processingFlags:time:timeZone:presentationTimeStamp:];
-[BWPhotoDescriptor timeZone];
-[BWPhotoDescriptor encodeWithCoder:];
-[BWPhotoDescriptor photoIdentifier];
-[BWPhotoDescriptor hash];
-[BWPhotoDescriptor processingFlags];
-[BWPhotoDescriptor description];
-[BWPhotoDescriptor initWithCoder:];
-[BWPhotoDescriptor setTime:];
-[BWPhotoDescriptor setPresentationTimeStamp:];
-[BWPhotoDescriptor initWithPhotoIdentifier:processingFlags:];
-[BWPhotoDescriptor isEqual:];
-[BWPhotoDescriptor time];
```
