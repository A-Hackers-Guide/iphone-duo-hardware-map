# `CAMOverlayService`

- Image: [`/System/Library/PrivateFrameworks/CameraOverlayServices.framework/CameraOverlayServices`](../userland/System__Library__PrivateFrameworks__CameraOverlayServices.framework__CameraOverlayServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"CAMOverlayServiceConnection" __activeConnection;
```

## Properties

```
@property (T@"CAMOverlayServiceConnection",&,N,S_setActiveConnection:,V__activeConnection) _activeConnection;
```

## Class methods

```
+[CAMOverlayService sharedService];
+[CAMOverlayService version];
```

## Instance methods

```
-[CAMOverlayService _init];
-[CAMOverlayService _activeConnection];
-[CAMOverlayService createConnectionWithClient:queue:];
-[CAMOverlayService _setActiveConnection:];
-[CAMOverlayService createConnectionWithClient:];
```
