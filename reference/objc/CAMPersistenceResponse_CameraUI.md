# `CAMPersistenceResponse`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
S _sessionIdentifier;
@"NSString" _persistenceUUID;
@"NSURL" _persistenceURL;
@"NSDate" _creationDate;
@"UIImage" _scrubberImage;
@"CAMCaptureCoordinationInfo" _coordinationInfo;
{CGSize="width"d"height"d} _pixelSize;
```

## Properties

```
@property (T@"NSString",R,C,N,V_persistenceUUID) persistenceUUID;
@property (TS,R,N,V_sessionIdentifier) sessionIdentifier;
@property (T@"NSURL",R,C,N,V_persistenceURL) persistenceURL;
@property (T@"NSDate",R,N,V_creationDate) creationDate;
@property (T@"UIImage",R,C,N,V_scrubberImage) scrubberImage;
@property (T{CGSize=dd},R,N,V_pixelSize) pixelSize;
@property (T@"CAMCaptureCoordinationInfo",R,N,V_coordinationInfo) coordinationInfo;
```

## Instance methods

```
-[CAMPersistenceResponse sessionIdentifier];
-[CAMPersistenceResponse persistenceUUID];
-[CAMPersistenceResponse persistenceURL];
-[CAMPersistenceResponse creationDate];
-[CAMPersistenceResponse pixelSize];
-[CAMPersistenceResponse description];
-[CAMPersistenceResponse coordinationInfo];
-[CAMPersistenceResponse initWithUUID:captureSession:url:creationDate:scrubberImage:pixelSize:coordinationInfo:];
-[CAMPersistenceResponse scrubberImage];
```
