# `AVCapturePersonalPhotographerSessionResults`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 16 instance methods, 1 class methods

## Instance variables

```
q _photoSettingsUniqueID;
@"NSMutableArray" _capturedSettingsIDs;
@"NSMutableDictionary" _timestampsBySettingsID;
@"NSMutableArray" _systemRecommendedPhotosToSaveBySettingsID;
@"NSMutableArray" _systemRecommendedPhotosToDeleteBySettingsID;
```

## Properties

```
@property (Tq,R,V_photoSettingsUniqueID) photoSettingsUniqueID;
@property (T@"NSArray",R) systemRecommendedPhotosToSaveBySettingsID;
@property (T@"NSArray",R) systemRecommendedPhotosToDeleteBySettingsID;
@property (T@"NSArray",R) systemRecommendedPhotosToSaveByTimestamp;
@property (T@"NSArray",R) systemRecommendedPhotosToDeleteByTimestamp;
```

## Class methods

```
+[AVCapturePersonalPhotographerSessionResults initialize];
```

## Instance methods

```
-[AVCapturePersonalPhotographerSessionResults debugDescription];
-[AVCapturePersonalPhotographerSessionResults dealloc];
-[AVCapturePersonalPhotographerSessionResults description];
-[AVCapturePersonalPhotographerSessionResults _isPhotoRegisteredWithSettingsIDNumber:];
-[AVCapturePersonalPhotographerSessionResults _timestampsForSettingsIDs:];
-[AVCapturePersonalPhotographerSessionResults initWithPhotoSettingsUniqueID:];
-[AVCapturePersonalPhotographerSessionResults isPhotoRegisteredForDeletionWithSettingsID:];
-[AVCapturePersonalPhotographerSessionResults isPhotoRegisteredWithSettingsID:];
-[AVCapturePersonalPhotographerSessionResults photoSettingsUniqueID];
-[AVCapturePersonalPhotographerSessionResults registerPhotoSettingsIDForDeletion:];
-[AVCapturePersonalPhotographerSessionResults registerPhotoTimestamp:forSettingsID:];
-[AVCapturePersonalPhotographerSessionResults registerPhotoWithSettingsID:];
-[AVCapturePersonalPhotographerSessionResults systemRecommendedPhotosToDeleteBySettingsID];
-[AVCapturePersonalPhotographerSessionResults systemRecommendedPhotosToDeleteByTimestamp];
-[AVCapturePersonalPhotographerSessionResults systemRecommendedPhotosToSaveBySettingsID];
-[AVCapturePersonalPhotographerSessionResults systemRecommendedPhotosToSaveByTimestamp];
```
