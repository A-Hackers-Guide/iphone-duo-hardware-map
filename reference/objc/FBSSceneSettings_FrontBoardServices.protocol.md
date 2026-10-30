# `FBSSceneSettings` (protocol)

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 14 properties, 28 instance methods, 0 class methods

## Properties

```
@property (T@"FBSDisplayConfiguration",C,N) displayConfiguration;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) frame;
@property (Td,N) level;
@property (Tq,N) interfaceOrientation;
@property (TB,N,GisForeground) foreground;
@property (Tq,N) interruptionPolicy;
@property (TB,N,GisOccluded) occluded;
@property (TB,N,GisClientFuture) clientFuture;
@property (TS,N) jetsamPriority;
@property (Tc,?,N) activityMode;
@property (Tq,?,N) defaultWatchdogBehavior;
@property (TB,?,N) prefersProcessTaskSuspensionWhileSceneForeground;
@property (T@"BSKeyedSettings",?,&,N) propagatedSettings;
@property (T@"<FBSceneClientProcess>",?,&,N) clientProcess;
```

## Instance methods

```
-[FBSSceneSettings interfaceOrientation];
-[FBSSceneSettings setForeground:];
-[FBSSceneSettings isClientFuture];
-[FBSSceneSettings displayConfiguration];
-[FBSSceneSettings setInterfaceOrientation:];
-[FBSSceneSettings setClientFuture:];
-[FBSSceneSettings level];
-[FBSSceneSettings isForeground];
-[FBSSceneSettings setDisplayConfiguration:];
-[FBSSceneSettings setLevel:];
-[FBSSceneSettings setJetsamPriority:];
-[FBSSceneSettings isOccluded];
-[FBSSceneSettings setFrame:];
-[FBSSceneSettings jetsamPriority];
-[FBSSceneSettings interruptionPolicy];
-[FBSSceneSettings setInterruptionPolicy:];
-[FBSSceneSettings setOccluded:];
-[FBSSceneSettings frame];
-[FBSSceneSettings clientProcess];
-[FBSSceneSettings setDefaultWatchdogBehavior:];
-[FBSSceneSettings setPropagatedSettings:];
-[FBSSceneSettings prefersProcessTaskSuspensionWhileSceneForeground];
-[FBSSceneSettings setClientProcess:];
-[FBSSceneSettings defaultWatchdogBehavior];
-[FBSSceneSettings setPrefersProcessTaskSuspensionWhileSceneForeground:];
-[FBSSceneSettings activityMode];
-[FBSSceneSettings setActivityMode:];
-[FBSSceneSettings propagatedSettings];
```
