# `FBSSceneSettingsCore`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSCoreSettingsExtension`
- Protocols: `FBSSceneSettings`
- 0 instance variables, 14 properties, 28 instance methods, 4 class methods

## Properties

```
@property (T@"FBSDisplayConfiguration",C,N) displayConfiguration;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},D,N) frame;
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
@property (T@"BSKeyedSettings",?,&,D,N) propagatedSettings;
@property (T@"<FBSceneClientProcess>",?,&,N) clientProcess;
```

## Class methods

```
+[FBSSceneSettingsCore protocol];
+[FBSSceneSettingsCore propagateSetting:];
+[FBSSceneSettingsCore descriptionOfValue:forSetting:];
+[FBSSceneSettingsCore configureSetting:];
```

## Instance methods

```
-[FBSSceneSettingsCore interfaceOrientation];
-[FBSSceneSettingsCore setForeground:];
-[FBSSceneSettingsCore clientProcess];
-[FBSSceneSettingsCore isClientFuture];
-[FBSSceneSettingsCore displayConfiguration];
-[FBSSceneSettingsCore setDefaultWatchdogBehavior:];
-[FBSSceneSettingsCore setInterfaceOrientation:];
-[FBSSceneSettingsCore setPropagatedSettings:];
-[FBSSceneSettingsCore prefersProcessTaskSuspensionWhileSceneForeground];
-[FBSSceneSettingsCore setClientProcess:];
-[FBSSceneSettingsCore setClientFuture:];
-[FBSSceneSettingsCore level];
-[FBSSceneSettingsCore isForeground];
-[FBSSceneSettingsCore setDisplayConfiguration:];
-[FBSSceneSettingsCore frame:];
-[FBSSceneSettingsCore setLevel:];
-[FBSSceneSettingsCore setJetsamPriority:];
-[FBSSceneSettingsCore isOccluded];
-[FBSSceneSettingsCore defaultWatchdogBehavior];
-[FBSSceneSettingsCore setPrefersProcessTaskSuspensionWhileSceneForeground:];
-[FBSSceneSettingsCore activityMode];
-[FBSSceneSettingsCore jetsamPriority];
-[FBSSceneSettingsCore interruptionPolicy];
-[FBSSceneSettingsCore setActivityMode:];
-[FBSSceneSettingsCore setInterruptionPolicy:];
-[FBSSceneSettingsCore propagatedSettings];
-[FBSSceneSettingsCore setOccluded:];
-[FBSSceneSettingsCore frame];
```
