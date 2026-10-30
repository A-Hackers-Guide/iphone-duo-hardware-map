# `_UICompanionSceneInterestClientComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `BSDescriptionStreaming`, `_UISceneAccessoryRegistryDelegate`, `_UISceneAccessoryContainerClientObserver`, `_UISceneAccessoryInterestClient`, `_UICompanionSceneInterestClient`, `FBSSceneObserver`
- 5 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _needsAccessoryRegistrationEvaluation;
@"<BSInvalidatable>" _stateCaptureToken;
@"_UISceneAccessoryRegistry" _accessoryRegistry;
@"_UIWindowSceneTraitOverrideHandle" _traitHandle;
@"NSHashTable" _companionContainerScenes;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",C,N) interestedAttributes;
```

## Instance methods

```
-[_UICompanionSceneInterestClientComponent debugDescription];
-[_UICompanionSceneInterestClientComponent setScene:];
-[_UICompanionSceneInterestClientComponent dealloc];
-[_UICompanionSceneInterestClientComponent _handleSceneWillConnectNotification:];
-[_UICompanionSceneInterestClientComponent succinctDescription];
-[_UICompanionSceneInterestClientComponent invalidate];
-[_UICompanionSceneInterestClientComponent _handleSceneDidDisconnectNotification:];
-[_UICompanionSceneInterestClientComponent interestedAttributes];
-[_UICompanionSceneInterestClientComponent description];
-[_UICompanionSceneInterestClientComponent _scene:didUpdateAvailableAttributes:];
-[_UICompanionSceneInterestClientComponent appendDescriptionToStream:];
-[_UICompanionSceneInterestClientComponent collectedSceneRegistrationsDidChangeForRegistry:];
-[_UICompanionSceneInterestClientComponent setInterestedAttributes:];
```
