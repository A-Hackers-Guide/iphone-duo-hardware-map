# `SBHostProxyClientComponent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `SBContinuitySessionScreenRecordingObserver`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"BSServiceConnectionEndpointInjector" _openAppInstanceInjector;
@"SBSceneRenderingEnvironmentParticipant" _sceneRenderingEnvironmentParticipant;
@"FBSDisplayConfiguration" _initialDisplayConfiguration;
```

## Properties

```
@property (T@"FBSDisplayConfiguration",R,C,N,V_initialDisplayConfiguration) initialDisplayConfiguration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBHostProxyClientComponent scene:didUpdateSettings:];
-[SBHostProxyClientComponent setScene:];
-[SBHostProxyClientComponent invalidate];
-[SBHostProxyClientComponent _windowManagementStyleDidChange:];
-[SBHostProxyClientComponent sceneWillInvalidate:];
-[SBHostProxyClientComponent _updateDisplayConfiguration:];
-[SBHostProxyClientComponent _didUpdateUserInterfaceStyle:withAnimationSettings:fence:];
-[SBHostProxyClientComponent _setSceneRenderingEnvironmentParticipant:];
-[SBHostProxyClientComponent _updateDisplayConfiguration:fence:];
-[SBHostProxyClientComponent continuitySessionDidUpdateScreenRecordingState:];
-[SBHostProxyClientComponent continuityUserInterfaceStyleProvider:didUpdateUserInterfaceStyle:withAnimationSettings:fence:];
-[SBHostProxyClientComponent initialDisplayConfiguration];
```
