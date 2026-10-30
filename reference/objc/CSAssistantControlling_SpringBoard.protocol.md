# `CSAssistantControlling` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 5 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisSystemAssistantExperienceAvailable) systemAssistantExperienceAvailable;
@property (TB,R,N,GisSystemAssistantExperienceEnabled) systemAssistantExperienceEnabled;
@property (TB,R,N,GisHomeAffordanceDoubleTapGestureEnabled) homeAffordanceDoubleTapGestureEnabled;
```

## Instance methods

```
-[CSAssistantControlling isSystemAssistantExperienceEnabled];
-[CSAssistantControlling removeAssistantControllerObserver:];
-[CSAssistantControlling isHomeAffordanceDoubleTapGestureEnabled];
-[CSAssistantControlling isSystemAssistantExperienceAvailable];
-[CSAssistantControlling addAssistantControllerObserver:];
```
