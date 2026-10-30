# `SBAssistantIslandActivityElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemApertureContextProviding`, `SBSystemApertureSuppressible`, `SBSystemApertureGestureCustomizing`, `SBSystemApertureElement`, `SAActivityBehavior`
- 8 instance variables, 21 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"SBAssistantIslandActivityElementViewProvider" _viewProvider;
@"<SAAutomaticallyInvalidatable>" _alertingAssertion;
@"NSHashTable" _observers;
@"<SAElementHosting>" _elementHost;
@"<SAActivityHosting>" _activityHost;
@"<SBSystemAperturePlatformElementHosting>" _platformElementHost;
@"<SBSystemApertureGestureHandling>" _gestureHandler;
@"NSString" _stageSceneIdentifier;
```

## Properties

```
@property (TB,R,N,GisAlerting) alerting;
@property (T@"NSString",C,N,V_stageSceneIdentifier) stageSceneIdentifier;
@property (TB,?,R,N,GisAffiliatedWithSessionMonitor) affiliatedWithSessionMonitor;
@property (T@"UIColor",?,R,N) keyColor;
@property (T@"FBScene",?,R,N) scene;
@property (TB,?,R,N) preventsSwipeToHide;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) preferredAvoidanceRect;
@property (Td,?,R,N) preferredAvoidanceCornerRadius;
@property (TB,?,R,N) inhibitsIndicatorMitosis;
@property (Td,?,R,N) preferredSystemClipPadding;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,?,N,GisSuppressed) suppressed;
@property (T@"<SBSystemApertureGestureHandling>",W,N,V_gestureHandler) gestureHandler;
@property (T@"<SBSystemAperturePlatformElementHosting>",?,W,N,V_platformElementHost) platformElementHost;
@property (T@"<SAElementHosting>",?,W,N,V_elementHost) elementHost;
@property (T@"NSString",R,C,N) clientIdentifier;
@property (T@"NSString",R,C,N) elementIdentifier;
@property (T@"<SAActivityHosting>",?,W,N,V_activityHost) activityHost;
```

## Instance methods

```
-[SBAssistantIslandActivityElement _notifyObservers];
-[SBAssistantIslandActivityElement setGestureHandler:];
-[SBAssistantIslandActivityElement inhibitsIndicatorMitosis];
-[SBAssistantIslandActivityElement preferredAvoidanceCornerRadius];
-[SBAssistantIslandActivityElement isAlerting];
-[SBAssistantIslandActivityElement clientIdentifier];
-[SBAssistantIslandActivityElement elementIdentifier];
-[SBAssistantIslandActivityElement removeObserver:];
-[SBAssistantIslandActivityElement init];
-[SBAssistantIslandActivityElement shouldSuppressElementWhilePresentingSceneWithIdentifier:];
-[SBAssistantIslandActivityElement viewProvider];
-[SBAssistantIslandActivityElement preferredAvoidanceRect];
-[SBAssistantIslandActivityElement setPlatformElementHost:];
-[SBAssistantIslandActivityElement addObserver:];
-[SBAssistantIslandActivityElement activityHost];
-[SBAssistantIslandActivityElement elementHost];
-[SBAssistantIslandActivityElement gestureHandler];
-[SBAssistantIslandActivityElement hasActivityBehavior];
-[SBAssistantIslandActivityElement setActivityHost:];
-[SBAssistantIslandActivityElement setElementHost:];
-[SBAssistantIslandActivityElement platformElementHost];
-[SBAssistantIslandActivityElement dropAlertingAssertion];
-[SBAssistantIslandActivityElement elementDescription];
-[SBAssistantIslandActivityElement inhibitSystemLongPressGesture];
-[SBAssistantIslandActivityElement inhibitSystemPanGesture];
-[SBAssistantIslandActivityElement preventsSwipeToHide];
-[SBAssistantIslandActivityElement setStageSceneIdentifier:];
-[SBAssistantIslandActivityElement stageSceneIdentifier];
-[SBAssistantIslandActivityElement takeAlertingAssertion];
```
