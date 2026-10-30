# `AVExternalStorageDevice`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 15 instance methods, 2 class methods

## Instance variables

```
^{OpaqueFigExternalStorageDeviceManager=} _externalStorageDeviceManager;
^{__CFString=} _figExternalStorageDeviceUUID;
^{__CFArray=} _nextAvailableURLArray;
^{__CFString=} _displayName;
^{__CFURL=} _baseURL;
^{__CFString=} _uniqueIdentifier;
i _writingSpeed;
```

## Properties

```
@property (T@"NSString",R,N) displayName;
@property (Tq,R,N) freeSize;
@property (Tq,R,N) totalSize;
@property (TB,R,N,GisConnected) connected;
@property (T@"NSUUID",R,N) uuid;
@property (T@"NSSet",R,N) reasonsNotRecommendedForCaptureUse;
@property (TB,R,N,GisNotRecommendedForCaptureUse) notRecommendedForCaptureUse;
```

## Class methods

```
+[AVExternalStorageDevice authorizationStatus];
+[AVExternalStorageDevice requestAccessWithCompletionHandler:];
```

## Instance methods

```
-[AVExternalStorageDevice isConnected];
-[AVExternalStorageDevice baseURL];
-[AVExternalStorageDevice uuid];
-[AVExternalStorageDevice displayName];
-[AVExternalStorageDevice dealloc];
-[AVExternalStorageDevice _uniqueIdentifier];
-[AVExternalStorageDevice totalSize];
-[AVExternalStorageDevice figExternalStorageDeviceUUID];
-[AVExternalStorageDevice freeSize];
-[AVExternalStorageDevice initWithExternalStorageDeviceManager:figExternalStorageDeviceUUID:];
-[AVExternalStorageDevice isNotRecommendedForCaptureUse];
-[AVExternalStorageDevice nextAvailableURLsWithPathExtensions:error:];
-[AVExternalStorageDevice reasonsNotRecommendedForCaptureUse];
-[AVExternalStorageDevice updateExternalStorageDeviceManager:andFigExternalStorageDeviceUUID:];
-[AVExternalStorageDevice writingSpeed];
```
