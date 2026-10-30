# `JFXMediaItem`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 8 properties, 28 instance methods, 1 class methods

## Instance variables

```
i _durationAt30fps;
q _mediaType;
q _mediaState;
q _mediaLoadState;
q _interfaceOrientationForDisplay;
@"<JFXMediaItemDelegate>" _delegate;
```

## Properties

```
@property (Tq,N,V_mediaType) mediaType;
@property (Tq,N,V_mediaState) mediaState;
@property (Tq,N,V_mediaLoadState) mediaLoadState;
@property (Ti,N,V_durationAt30fps) durationAt30fps;
@property (Tq,N,V_interfaceOrientationForDisplay) interfaceOrientationForDisplay;
@property (T@"PVColorSpace",R,N) colorSpace;
@property (Ti,R,N) playableMediaContentMode;
@property (T@"<JFXMediaItemDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[JFXMediaItem supportsSecureCoding];
```

## Instance methods

```
-[JFXMediaItem info];
-[JFXMediaItem init];
-[JFXMediaItem dealloc];
-[JFXMediaItem setMediaState:];
-[JFXMediaItem colorSpace];
-[JFXMediaItem setMediaType:];
-[JFXMediaItem setDelegate:];
-[JFXMediaItem delegate];
-[JFXMediaItem hash];
-[JFXMediaItem description];
-[JFXMediaItem copyWithZone:];
-[JFXMediaItem mediaType];
-[JFXMediaItem isEqual:];
-[JFXMediaItem mediaState];
-[JFXMediaItem durationAt30fps];
-[JFXMediaItem canBeAddedToSequence];
-[JFXMediaItem canHaveFilter];
-[JFXMediaItem canSaveToCameraRoll];
-[JFXMediaItem hasAudibleCharacteristic];
-[JFXMediaItem hasPhotoCharacteristic];
-[JFXMediaItem hasVisualCharacteristic];
-[JFXMediaItem initWithInfo:delegate:];
-[JFXMediaItem interfaceOrientationForDisplay];
-[JFXMediaItem mediaLoadState];
-[JFXMediaItem playableMediaContentMode];
-[JFXMediaItem setDurationAt30fps:];
-[JFXMediaItem setInterfaceOrientationForDisplay:];
-[JFXMediaItem setMediaLoadState:];
```
