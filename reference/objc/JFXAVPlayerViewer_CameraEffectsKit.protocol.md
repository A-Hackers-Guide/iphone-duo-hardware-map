# `JFXAVPlayerViewer` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T@"AVPlayer",&,N) player;
@property (T@"NSString",C,N) videoGravity;
@property (T{CGSize=dd},R,N) displaySize;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) videoBounds;
@property (TB,R,N,GisReadyForDisplay) readyForDisplay;
@property (TB,N) showAVControls;
```

## Instance methods

```
-[JFXAVPlayerViewer player];
-[JFXAVPlayerViewer isReadyForDisplay];
-[JFXAVPlayerViewer videoBounds];
-[JFXAVPlayerViewer setPlayer:];
-[JFXAVPlayerViewer videoGravity];
-[JFXAVPlayerViewer setVideoGravity:];
-[JFXAVPlayerViewer displaySize];
-[JFXAVPlayerViewer configureDisplayAttributesForColorSpace:];
-[JFXAVPlayerViewer setShowAVControls:];
-[JFXAVPlayerViewer showAVControls];
```
