# `CLEEDUploadServiceConfig`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
q _numInFlightUploads;
q _maxUploadFileSizeMB;
q _maxUploadQuotaMB;
```

## Properties

```
@property (Tq,R,N,V_numInFlightUploads) numInFlightUploads;
@property (Tq,R,N,V_maxUploadFileSizeMB) maxUploadFileSizeMB;
@property (Tq,R,N,V_maxUploadQuotaMB) maxUploadQuotaMB;
```

## Class methods

```
+[CLEEDUploadServiceConfig supportsSecureCoding];
```

## Instance methods

```
-[CLEEDUploadServiceConfig dealloc];
-[CLEEDUploadServiceConfig encodeWithCoder:];
-[CLEEDUploadServiceConfig description];
-[CLEEDUploadServiceConfig initWithCoder:];
-[CLEEDUploadServiceConfig initWithNumInflightUploads:maxUploadFileSizeMB:maxUploadQuotaMB:];
-[CLEEDUploadServiceConfig maxUploadFileSizeMB];
-[CLEEDUploadServiceConfig maxUploadQuotaMB];
-[CLEEDUploadServiceConfig numInFlightUploads];
```
