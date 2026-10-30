# `SBActivitySystemApertureSceneHandle`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ACUISSystemApertureSceneHandleDelegate`, `BSInvalidatable`
- 5 instance variables, 10 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _isForAlertTarget;
@"ACUISSystemApertureSceneHandle" _sceneHandle;
@"SBWindowScene" _activeWindowScene;
Q _activeLayoutDirection;
@"<SBActivitySystemApertureSceneHandleDelegate>" _delegate;
```

## Properties

```
@property (TB,R,N,V_isForAlertTarget) isForAlertTarget;
@property (T@"FBScene",R,N) scene;
@property (T@"ACActivityDescriptor",R,N) descriptor;
@property (T@"<SBActivitySystemApertureSceneHandleDelegate>",W,N,V_delegate) delegate;
@property (T@"SBWindowScene",W,N,V_activeWindowScene) activeWindowScene;
@property (TQ,N,V_activeLayoutDirection) activeLayoutDirection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBActivitySystemApertureSceneHandle descriptor];
-[SBActivitySystemApertureSceneHandle activeWindowScene];
-[SBActivitySystemApertureSceneHandle setActiveWindowScene:];
-[SBActivitySystemApertureSceneHandle invalidate];
-[SBActivitySystemApertureSceneHandle setDelegate:];
-[SBActivitySystemApertureSceneHandle activeLayoutDirection];
-[SBActivitySystemApertureSceneHandle scene];
-[SBActivitySystemApertureSceneHandle delegate];
-[SBActivitySystemApertureSceneHandle activitySystemApertureSceneHandle:requestsLaunchWithAction:];
-[SBActivitySystemApertureSceneHandle activitySystemApertureSceneHandle:updatedContentPayloadID:];
-[SBActivitySystemApertureSceneHandle _createSceneHandleWithDescriptor:];
-[SBActivitySystemApertureSceneHandle _updateMetricsForWindowScene:];
-[SBActivitySystemApertureSceneHandle initWithDescriptor:configuringForAlertTarget:];
-[SBActivitySystemApertureSceneHandle initWithDescriptor:configuringForAlertTarget:windowScene:];
-[SBActivitySystemApertureSceneHandle isForAlertTarget];
-[SBActivitySystemApertureSceneHandle setActiveLayoutDirection:];
-[SBActivitySystemApertureSceneHandle setActiveWindowScene:activeLayoutDirection:];
```
