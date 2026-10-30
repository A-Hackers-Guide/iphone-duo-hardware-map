# `CFXMediaSettings`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `JFXMediaSettingsProvider`
- 5 instance variables, 10 properties, 13 instance methods, 1 class methods

## Instance variables

```
i _timeScale;
i _frameRate;
@"NSObject<OS_dispatch_queue>" _queue;
{CGSize="width"d"height"d} _frameSize;
{CGSize="width"d"height"d} _renderSize;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (Ti,N,V_timeScale) timeScale;
@property (Ti,N,V_frameRate) frameRate;
@property (T{CGSize=dd},N,V_frameSize) frameSize;
@property (T{CGSize=dd},N,V_renderSize) renderSize;
@property (T{CGSize=dd},N) compositionSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CFXMediaSettings sharedInstance];
```

## Instance methods

```
-[CFXMediaSettings timeScale];
-[CFXMediaSettings renderSize];
-[CFXMediaSettings setTimeScale:];
-[CFXMediaSettings init];
-[CFXMediaSettings queue];
-[CFXMediaSettings frameSize];
-[CFXMediaSettings setFrameRate:];
-[CFXMediaSettings setQueue:];
-[CFXMediaSettings frameRate];
-[CFXMediaSettings setFrameSize:];
-[CFXMediaSettings setRenderSize:];
-[CFXMediaSettings compositionSize];
-[CFXMediaSettings setCompositionSize:];
```
