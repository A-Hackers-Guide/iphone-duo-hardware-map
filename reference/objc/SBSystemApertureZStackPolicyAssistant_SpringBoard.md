# `SBSystemApertureZStackPolicyAssistant`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDeviceApplicationSceneHandleObserver`, `SBHomeGrabberViewObserver`
- 7 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"<SBSystemApertureZStackPolicyAssistantDelegate>" _delegate;
@"<SBSystemApertureZStackPolicyAssistantWindowSceneProviding>" _windowSceneProvider;
@"SBFZStackParticipant" _participant;
@"NSArray" _foregroundPairs;
B _suppressSystemApertureForSystemChromeSuppression;
@"NSSet" _associatedBundleIdentifiersToSuppressInSystemAperture;
@"NSSet" _associatedSceneIdentifiersToSuppressInSystemAperture;
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
-[SBSystemApertureZStackPolicyAssistant sceneHandle:didUpdateClientSettings:];
-[SBSystemApertureZStackPolicyAssistant homeGrabberViewDidUpdateHidden:];
```
