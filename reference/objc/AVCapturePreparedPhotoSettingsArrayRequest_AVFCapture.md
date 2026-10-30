# `AVCapturePreparedPhotoSettingsArrayRequest`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
Q _requestID;
@"NSArray" _photoSettingsArray;
@? _completionHandler;
B _completed;
```

## Properties

```
@property (TQ,R) requestID;
@property (T@"NSArray",R) photoSettingsArray;
@property (T@?,R,V_completionHandler) completionHandler;
@property (TB,N,GisCompleted,V_completed) completed;
```

## Class methods

```
+[AVCapturePreparedPhotoSettingsArrayRequest preparedPhotoSettingsArrayRequestWithArray:completionHandler:];
```

## Instance methods

```
-[AVCapturePreparedPhotoSettingsArrayRequest setCompleted:];
-[AVCapturePreparedPhotoSettingsArrayRequest completionHandler];
-[AVCapturePreparedPhotoSettingsArrayRequest requestID];
-[AVCapturePreparedPhotoSettingsArrayRequest isCompleted];
-[AVCapturePreparedPhotoSettingsArrayRequest dealloc];
-[AVCapturePreparedPhotoSettingsArrayRequest _initWithArray:completionHandler:];
-[AVCapturePreparedPhotoSettingsArrayRequest _setRequestID:];
-[AVCapturePreparedPhotoSettingsArrayRequest photoSettingsArray];
```
