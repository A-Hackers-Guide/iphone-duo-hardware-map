# `FBSSceneSettings`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSettings`
- Protocols: `FBSSceneSettings`, `NSCopying`, `NSMutableCopying`
- 1 instance variables, 17 properties, 14 instance methods, 8 class methods

## Instance variables

```
@"NSSet" _ignoreOcclusionReasons;
```

## Properties

```
@property (TB,D,N,GisOccluded) occluded;
@property (TB,D,N,GisClientFuture) clientFuture;
@property (T@"<FBSceneClientProcess>",&,D,N) clientProcess;
@property (TB,R,N,GisBackgrounded) backgrounded;
@property (Tc,R,N) jetsamMode;
@property (T@"FBSDisplayIdentity",R,C,N) displayIdentity;
@property (T@"FBSDisplayConfiguration",R,C,D,N) displayConfiguration;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,D,N) frame;
@property (Td,R,D,N) level;
@property (Tq,R,D,N) interfaceOrientation;
@property (TB,R,D,N,GisForeground) foreground;
@property (Tq,R,D,N) interruptionPolicy;
@property (TS,R,D,N) jetsamPriority;
@property (Tc,?,N) activityMode;
@property (Tq,?,N) defaultWatchdogBehavior;
@property (TB,?,N) prefersProcessTaskSuspensionWhileSceneForeground;
@property (T@"BSKeyedSettings",?,&,N) propagatedSettings;
```

## Class methods

```
+[FBSSceneSettings _baseClass];
+[FBSSceneSettings settings];
+[FBSSceneSettings subclassExtension];
+[FBSSceneSettings mutableSubclass];
+[FBSSceneSettings _settingsExtensionsForSceneExtension:];
+[FBSSceneSettings immutableSubclass];
+[FBSSceneSettings _mutableClass];
+[FBSSceneSettings _diffClass];
```

## Instance methods

```
-[FBSSceneSettings isBackgrounded];
-[FBSSceneSettings bounds];
-[FBSSceneSettings displayIdentity];
-[FBSSceneSettings initWithSettings:];
-[FBSSceneSettings transientLocalSettings];
-[FBSSceneSettings _appendToDescriptionBuilder:];
-[FBSSceneSettings _hasAdditionalDescription];
-[FBSSceneSettings _isEmptyForCoding:];
-[FBSSceneSettings _isEqualToSettings:];
-[FBSSceneSettings _propagatedSettings];
-[FBSSceneSettings ignoreOcclusionReasons];
-[FBSSceneSettings isIgnoringOcclusions];
-[FBSSceneSettings jetsamMode];
-[FBSSceneSettings setJetsamMode:];
```
