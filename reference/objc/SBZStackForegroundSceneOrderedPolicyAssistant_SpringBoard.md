# `SBZStackForegroundSceneOrderedPolicyAssistant`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneObserver`, `SBSceneHandleObserver`
- 5 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _foregroundScenes;
@"NSArray" _observedSceneSettingSelectors;
@"<SBZStackForegroundScenePolicyAssistantDelegate>" _delegate;
@"SBFZStackParticipant" _zStackParticipant;
@"FBSSceneClientSettingsDiffInspector" _sceneClientSettingsDiffInspector;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBZStackForegroundSceneOrderedPolicyAssistant sceneHandle:didUpdateClientSettings:];
-[SBZStackForegroundSceneOrderedPolicyAssistant initWithDelegate:];
-[SBZStackForegroundSceneOrderedPolicyAssistant _didUpdateClientSettings:];
-[SBZStackForegroundSceneOrderedPolicyAssistant initWithParticipant:];
-[SBZStackForegroundSceneOrderedPolicyAssistant dealloc];
-[SBZStackForegroundSceneOrderedPolicyAssistant resolveProposedPoliciesForForegroundScenes:];
-[SBZStackForegroundSceneOrderedPolicyAssistant observedSceneSettings];
-[SBZStackForegroundSceneOrderedPolicyAssistant scene:didUpdateClientSettings:];
-[SBZStackForegroundSceneOrderedPolicyAssistant _foregroundScenes];
-[SBZStackForegroundSceneOrderedPolicyAssistant _invokePropertyResolution];
-[SBZStackForegroundSceneOrderedPolicyAssistant setForegroundScenes:];
```
